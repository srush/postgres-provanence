#ifndef PG_PROV_H
#define PG_PROV_H

#include "catalog/genbki.h"

/* ----------------
 *		pg_statistic definition.  cpp turns this into
 *		typedef struct FormData_pg_statistic
 * ----------------
 */
#define StatisticRelationId  87563

CATALOG(pg_prov,87563) BKI_WITHOUT_OIDS
{
	/* These fields form the unique key for the entry: */
	Oid			tableid;		/* relation containing table */
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
#define Natts_pg_prov				1
#define Anum_pg_prov_tableid		1


#endif   /* PG_PROV_H */
