#ifndef PG_PROV_H
#define PG_PROV_H

#include "catalog/genbki.h"

/* ----------------
 *		pg_prov definition.  cpp turns this into
 *		typedef struct FormData_pg_prov
 * ----------------
 */
#define ProvRelationId  87563

CATALOG(pg_prov,87563) BKI_WITHOUT_OIDS
{
	Oid			origin_tableid;	
	Oid			dest_tableid;	
        
} FormData_pg_prov;


/* ----------------
 *		Form_pg_statistic corresponds to a pointer to a tuple with
 *		the format of pg_statistic relation.
 * ----------------
 */
typedef FormData_pg_prov *Form_pg_prov;

/* ----------------
 *		compiler constants for pg_statistic
 * ----------------
 */
#define Natts_pg_prov				2
#define Anum_pg_prov_origin_tableid		1
#define Anum_pg_prov_dest_tableid		2


#endif   /* PG_PROV_H */
