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
        int4                     num_primary_keys;
        int4                     command_id;
        int4			primary_keys[INDEX_MAX_KEYS];	
        int4                     num_dest_primary_keys;
        int4			dest_primary_keys[INDEX_MAX_KEYS];	
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
#define Natts_pg_prov				7
#define Anum_pg_prov_origin_tableid		1
#define Anum_pg_prov_dest_tableid		2
#define Anum_pg_prov_num_primary_keys		3
#define Anum_pg_prov_com_id  		4
#define Anum_pg_prov_primary_keys		5
#define Anum_pg_prov_num_dest_primary_keys		6
#define Anum_pg_prov_dest_primary_keys		7

#endif   /* PG_PROV_H */
