import psycopg2
import cherrypy
#import webbrowser
import os
import simplejson
import sys
import StringIO
from itertools import *
#MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")


# origin_tableid        | oid       | not null
#  dest_tableid          | oid       | not null
#  num_primary_keys      | integer   | not null
#  command_id            | integer   | not null
#  primary_keys          | integer[] | 
#  num_dest_primary_keys | integer   | 
#  dest_primary_keys     | integer[] | 




class AjaxApp(object):
    def get_generic(self, conn, table_name, prim_atts, prim_vals):
      cur4 = conn.cursor()
      query= """ SELECT * FROM %s WHERE """%(table_name) + \
          " AND ".join([" %s = %s "%(a,b) for (a,b) in izip(prim_atts, prim_vals)  ] )
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

    def display_generic(self, out, cur):
      
      res = cur.fetchone()
      print >>out, "<table style='margin: 15px; border :1 solid;'>"
      for des, col in izip(cur.description, res) :
        print >>out, "<tr>"
        print >>out, "<td>" + str(des[0]) + "</td>"
        print >>out, "<td>" + str(col) + "</td> "
        print >> out, "</tr>"
      print >>out, "</table>"

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
    def index(self, tablename=None, primary_key=None, backward=True):


      
      
      out = StringIO.StringIO()


      print >>out, "<form method='GET'> "
      print >>out, "Table: <input type='text' name='tablename'> "
      print >>out, "Primary Key: <input type='text' name='primary_key'> "
      print >>out, "Backward: <input type='checkbox' value='true' checked='true' name='backward'> "
      print >>out, "<input type='Submit' value='View'> "
      
      print >>out, "</form> "

      
      conn = psycopg2.connect("host=localhost user=postgres")


      tableid = self.get_table_id(conn, tablename);
      

      print >>out, """<table> <thead> 
                          <tr><th>Dest</th>
                              <th>Primary Key</th>
    <th>Table ID</th>
                                 </tr></thead><tr>"""
          
      print >>out, "<td>"+ str(tablename)+"</td>"
      print >>out, "<td>"+ str(primary_key)+"</td>"
      print >>out, "<td>"+ str(tableid)+"</td>"
      print >>out, "</tr></table>"


      initial_prim = self.get_primary_atts(conn, tableid)
      self.display_generic(out, self.get_generic(conn, tablename, initial_prim, primary_key))

      


      
      cur = conn.cursor()      
      query = """
                   SELECT pg_prov.primary_keys, pg_prov.dest_primary_keys, pg_prov.origin_tableid, pg_prov.dest_tableid, ca.relname, cb.relname  
                   FROM pg_prov, pg_class as ca, pg_class as cb 
                   WHERE ca.relfilenode = pg_prov.origin_tableid 
                         and cb.relfilenode = pg_prov.dest_tableid """
      if backward:
        query += "and pg_prov.dest_tableid = %s and pg_prov.dest_primary_keys = ARRAY[%s];"%(tableid, primary_key)
      else:
        query += """and pg_prov.origin_tableid = %s and pg_prov.primary_keys = ARRAY[%s];"""%(tableid, primary_key) 
      
      cur.execute(query)
      for row  in cur:
        (o_prim, d_prim, o_id, d_id, o_rel, d_rel) = row
        
        prim_atts = self.get_primary_atts(conn, o_id)
        cur4 = self.get_generic(conn, o_rel, prim_atts, o_prim)
        self.display_generic(out, cur4)
        cur4.close()
      
      cur.close()
      conn.close()
      return out.getvalue()# open(os.path.join(MEDIA_DIR, u'index.html'))

    @cherrypy.expose
    def submit(self, name):
      cherrypy.response.headers['Content-Type'] = 'application/json'
      return simplejson.dumps(dict(title="Hello, %s" % name))

#config = {'/media':
#                {'tools.staticdir.on': True,
#                 'tools.staticdir.dir': MEDIA_DIR,
#                }
#        }

#def open_page():
    #ebbrowser.open("http://127.0.0.1:8080/")
#cherrypy.engine.subscribe('start', open_page)
#cherrypy.tree.mount(AjaxApp(), '/')
cherrypy.quickstart(AjaxApp())
