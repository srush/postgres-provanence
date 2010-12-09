import psycopg2
import cherrypy
#import webbrowser
import os
import simplejson
import sys
import StringIO

from pygraphviz import *
from itertools import *
#MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")


# origin_tableid        | oid       | not null
#  dest_tableid          | oid       | not null
#  num_primary_keys      | integer   | not null
#  command_id            | integer   | not null
#  primary_keys          | integer[] | 
#  num_dest_primary_keys | integer   | 
#  dest_primary_keys     | integer[] | 

colors = ["red", "green", "blue", "purple", "brown", "orange"]

class AjaxApp(object):
    def get_generic(self, conn, table_name, prim_atts, prim_vals):
      cur4 = conn.cursor()
      query= """ SELECT * FROM %s WHERE """%(table_name) + \
          " AND ".join([" %s = %s "%(a,b) for (a,b) in izip(prim_atts, prim_vals)  ] )
      print query
      cur4.execute(query)
      return cur4


    def get_table_id(self, conn, table_name):
      cur_init = conn.cursor() 
      cur_init.execute("""
                   SELECT ca.relfilenode  
                   FROM pg_class as ca 
                   WHERE ca.relname = '%s' ;"""%(table_name))
      table_id = cur_init.fetchone()[0]

      cur_init.close()
      return table_id

    def display_generic(self, out, table, key, cur):
      
      res = cur.fetchone()
      print >>out, "<a href='?tablename=%s&primary_key=%s'>"%(table,key)
      print >>out, "<table style='margin: 15px; padding:3px; border :3px solid; '>"
      print >>out, "<tr><th style =' ' colspan=2><div style='padding:5px; font:20px; border:2px solid %s;'>%s</div></th></tr>"%(colors[table.__hash__()%len(colors)], table)
      
      for des, col in izip(cur.description, res):
        print >>out, "<tr>"
        print >>out, "<td style='text-align:right;'><b>" + str(des[0]) + "</b></td>"
        colstr = str(col)
        if len(colstr)>100: 
          colstr = colstr[0:100] + "..."
        print >>out, "<td style='padding-left:5px;'>" + colstr + "</td> "
        print >> out, "</tr>"
      print >>out, "</td></table></a>"

#       print >>out, """<td> <form method ='GET'> <input type='submit' name ='backward' value='Backward'> <input type='hidden' name='tablename' value='%s'>
# <br>
# <input type='hidden' name='primary_key' value='%s' ><input type='submit' name='forw' value='Forward'> </form></td>"""%(table, key)
      print >>out, "</tr>"

    def get_primary_atts(self, conn, o_id):
      prim_atts = []
      cur2 = conn.cursor()
      cur2.execute("""
                   SELECT indisprimary,indkey FROM pg_index  
                   WHERE indrelid = %s;"""%(o_id))

      for (isprimary, keys) in cur2:
        if not isprimary:
          continue
          #print >>out, isprimary, keys  
        for key in keys:
          cur3 = conn.cursor()
          cur3.execute("""
                   SELECT attname FROM pg_attribute  
                   WHERE attrelid =%s and attnum=%s;"""%(o_id, key))
          prim_atts.append(cur3.fetchone()[0])
          cur3.close()
          
      cur2.close()
      return prim_atts

      
    @cherrypy.expose
    def index(self, tablename=None, primary_key=None):


      
      
      out = StringIO.StringIO()

      print >>out, "<div style='font:arial'><center>"
      print >>out, "<form method='GET'> "
      print >>out, "Table: <input type='text' name='tablename'> "
      print >>out, "Primary Key: <input type='text' name='primary_key'> "
      print >>out, "<input type='Submit' value='View'> "
      
      print >>out, "</form> "

      
      if not tablename:
        return out.getvalue()

      conn = psycopg2.connect("host=localhost user=postgres")


      tableid = self.get_table_id(conn, tablename);
      

    #   print >>out, """<table> <thead> 
    #                       <tr><th>Dest</th>
    #                           <th>Primary Key</th>
    # <th>Table ID</th>
    #                              </tr></thead><tr>"""
          
    #   print >>out, "<td>"+ str(tablename)+"</td>"
    #   print >>out, "<td>"+ str(primary_key)+"</td>"
    #   print >>out, "<td>"+ str(tableid)+"</td>"
    #   print >>out, "</tr></table>"


      initial_prim = self.get_primary_atts(conn, tableid)

      print initial_prim, primary_key
      self.display_generic(out, tablename, primary_key, 
                           self.get_generic(conn, tablename, initial_prim, [primary_key]))

      


      #print >>out, "<table><tr><th> Table</th><th> Tuple</th><th>Action</th></th>"
      print >>out, "<div style='width:800px'>"
      for backward in [True, False]:
        if backward:
          print >>out, "<div style='width:300px; float: left;'>"
          print >>out, "<center><div> Backward</div></center>"
        else:

          print >>out, "<div style='width:300px; float: right;'>"
          print >>out, "<center><div> Forward</div></center>"
        cur = conn.cursor()      
        query = """
                   SELECT pg_prov.primary_keys, pg_prov.dest_primary_keys, pg_prov.origin_tableid, pg_prov.dest_tableid, ca.relname, cb.relname  
                   FROM pg_prov, pg_class as ca, pg_class as cb 
                   WHERE ca.relfilenode = pg_prov.origin_tableid 
                         and cb.relfilenode = pg_prov.dest_tableid """
        if backward:
          query += "and pg_prov.dest_tableid = %s and pg_prov.dest_primary_keys = ARRAY[%s];"%(tableid, primary_key)
          fetch = lambda row: (row[0], row[2], row[4])

        else:
          query += """and pg_prov.origin_tableid = %s and pg_prov.primary_keys = ARRAY[%s];"""%(tableid, primary_key) 
          fetch = lambda row: (row[1], row[3], row[5])
        print query
        cur.execute(query)
        for row  in cur:
          #(o_prim, d_prim, o_id, d_id, o_rel, d_rel) = row
          #print >>out, row
          (o_prim, o_id, o_name) = fetch(row)
          prim_atts = self.get_primary_atts(conn, o_id)
          cur4 = self.get_generic(conn, o_name, prim_atts, o_prim)
          self.display_generic(out, o_name, o_prim[0], cur4)
          cur4.close()
        #print >>out, "</table>"
        cur.close()
        
        print >>out, "</div>"
      print >>out, "</div>"
      print >>out, "</center></div>"        
      conn.close()
      return out.getvalue()# open(os.path.join(MEDIA_DIR, u'index.html'))

    @cherrypy.expose
    def draw(self):      
      out = StringIO.StringIO()
      conn = psycopg2.connect("host=localhost user=postgres")
      cur = conn.cursor()      
      query = """
                   SELECT pg_prov.primary_keys, pg_prov.dest_primary_keys, pg_prov.origin_tableid, pg_prov.dest_tableid, ca.relname, cb.relname  
                   FROM pg_prov, pg_class as ca, pg_class as cb 
                   WHERE ca.relfilenode = pg_prov.origin_tableid 
                         and cb.relfilenode = pg_prov.dest_tableid"""
      
      cur.execute(query)
      G=AGraph(strict=False,directed=True)
      G.graph_attr['rankdir']='LR'

      i =0

      for row  in cur:
        print >>out, row
        (o_prim, d_prim, o_id, d_id, o_rel, d_rel) = row
        
        
        G.add_edge(o_rel + ":" +str(o_prim), 
                   d_rel + ":" +str(d_prim))
        
        node1 = G.get_node(o_rel + ":" +str(o_prim))
        node1.attr["color"] = colors[o_rel.__hash__()%len(colors)]
        node2 = G.get_node(d_rel + ":" +str(d_prim))
        node2.attr["color"] = colors[d_rel.__hash__()%len(colors)] 
        i+=1
        if i > 500: break
      G.draw("canviz-read-only/db.xdot", prog="dot")
      G.draw("canviz-read-only/db.ps", prog="dot")
      cur.close()
      conn.close()
      raise cherrypy.HTTPRedirect("canviz/db.html", 301)
      return out.getvalue()

    @cherrypy.expose
    def submit(self, name):
      cherrypy.response.headers['Content-Type'] = 'application/json'
      return simplejson.dumps(dict(title="Hello, %s" % name))

config = {'global':
            {'tools.staticdir.root': '/home/srush/Projects/db/js_frontend/'},
          '/canviz':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir':'canviz-read-only/'
                }
          ,'/canviz/prototype':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir':'canviz-read-only/prototype/'
                }
          ,'/canviz/path':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir':'canviz-read-only/path/'
                }
          ,'/canviz/graphs':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir':'canviz-read-only/graphs/'
                }          
          ,'/canviz/graphs/images':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir':'canviz-read-only/graphs/images'
                }          

        }

#def open_page():
    #ebbrowser.open("http://127.0.0.1:8080/")
#cherrypy.engine.subscribe('start', open_page)
#cherrypy.tree.mount(AjaxApp(), '/', config=config)
cherrypy.quickstart(AjaxApp(), '/', config)
