/* A Bison parser, made by GNU Bison 1.875.  */

/* Skeleton parser for Yacc-like parsing with Bison,
   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002 Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place - Suite 330,
   Boston, MA 02111-1307, USA.  */

/* As a special exception, when this file is copied by Bison into a
   Bison output file, you may use that output file without restriction.
   This special exception was added by the Free Software Foundation
   in version 1.24 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENT = 258,
     FCONST = 259,
     SCONST = 260,
     BCONST = 261,
     XCONST = 262,
     Op = 263,
     ICONST = 264,
     PARAM = 265,
     TYPECAST = 266,
     DOT_DOT = 267,
     COLON_EQUALS = 268,
     T_WORD = 269,
     T_CWORD = 270,
     T_DATUM = 271,
     LESS_LESS = 272,
     GREATER_GREATER = 273,
     K_ABSOLUTE = 274,
     K_ALIAS = 275,
     K_ALL = 276,
     K_BACKWARD = 277,
     K_BEGIN = 278,
     K_BY = 279,
     K_CASE = 280,
     K_CLOSE = 281,
     K_CONSTANT = 282,
     K_CONTINUE = 283,
     K_CURSOR = 284,
     K_DEBUG = 285,
     K_DECLARE = 286,
     K_DEFAULT = 287,
     K_DETAIL = 288,
     K_DIAGNOSTICS = 289,
     K_DUMP = 290,
     K_ELSE = 291,
     K_ELSIF = 292,
     K_END = 293,
     K_ERRCODE = 294,
     K_ERROR = 295,
     K_EXCEPTION = 296,
     K_EXECUTE = 297,
     K_EXIT = 298,
     K_FETCH = 299,
     K_FIRST = 300,
     K_FOR = 301,
     K_FORWARD = 302,
     K_FROM = 303,
     K_GET = 304,
     K_HINT = 305,
     K_IF = 306,
     K_IN = 307,
     K_INFO = 308,
     K_INSERT = 309,
     K_INTO = 310,
     K_IS = 311,
     K_LAST = 312,
     K_LOG = 313,
     K_LOOP = 314,
     K_MESSAGE = 315,
     K_MOVE = 316,
     K_NEXT = 317,
     K_NO = 318,
     K_NOT = 319,
     K_NOTICE = 320,
     K_NULL = 321,
     K_OPEN = 322,
     K_OPTION = 323,
     K_OR = 324,
     K_PERFORM = 325,
     K_PRIOR = 326,
     K_QUERY = 327,
     K_RAISE = 328,
     K_RELATIVE = 329,
     K_RESULT_OID = 330,
     K_RETURN = 331,
     K_REVERSE = 332,
     K_ROWTYPE = 333,
     K_ROW_COUNT = 334,
     K_SCROLL = 335,
     K_SQLSTATE = 336,
     K_STRICT = 337,
     K_THEN = 338,
     K_TO = 339,
     K_TYPE = 340,
     K_USE_COLUMN = 341,
     K_USE_VARIABLE = 342,
     K_USING = 343,
     K_VARIABLE_CONFLICT = 344,
     K_WARNING = 345,
     K_WHEN = 346,
     K_WHILE = 347
   };
#endif
#define IDENT 258
#define FCONST 259
#define SCONST 260
#define BCONST 261
#define XCONST 262
#define Op 263
#define ICONST 264
#define PARAM 265
#define TYPECAST 266
#define DOT_DOT 267
#define COLON_EQUALS 268
#define T_WORD 269
#define T_CWORD 270
#define T_DATUM 271
#define LESS_LESS 272
#define GREATER_GREATER 273
#define K_ABSOLUTE 274
#define K_ALIAS 275
#define K_ALL 276
#define K_BACKWARD 277
#define K_BEGIN 278
#define K_BY 279
#define K_CASE 280
#define K_CLOSE 281
#define K_CONSTANT 282
#define K_CONTINUE 283
#define K_CURSOR 284
#define K_DEBUG 285
#define K_DECLARE 286
#define K_DEFAULT 287
#define K_DETAIL 288
#define K_DIAGNOSTICS 289
#define K_DUMP 290
#define K_ELSE 291
#define K_ELSIF 292
#define K_END 293
#define K_ERRCODE 294
#define K_ERROR 295
#define K_EXCEPTION 296
#define K_EXECUTE 297
#define K_EXIT 298
#define K_FETCH 299
#define K_FIRST 300
#define K_FOR 301
#define K_FORWARD 302
#define K_FROM 303
#define K_GET 304
#define K_HINT 305
#define K_IF 306
#define K_IN 307
#define K_INFO 308
#define K_INSERT 309
#define K_INTO 310
#define K_IS 311
#define K_LAST 312
#define K_LOG 313
#define K_LOOP 314
#define K_MESSAGE 315
#define K_MOVE 316
#define K_NEXT 317
#define K_NO 318
#define K_NOT 319
#define K_NOTICE 320
#define K_NULL 321
#define K_OPEN 322
#define K_OPTION 323
#define K_OR 324
#define K_PERFORM 325
#define K_PRIOR 326
#define K_QUERY 327
#define K_RAISE 328
#define K_RELATIVE 329
#define K_RESULT_OID 330
#define K_RETURN 331
#define K_REVERSE 332
#define K_ROWTYPE 333
#define K_ROW_COUNT 334
#define K_SCROLL 335
#define K_SQLSTATE 336
#define K_STRICT 337
#define K_THEN 338
#define K_TO 339
#define K_TYPE 340
#define K_USE_COLUMN 341
#define K_USE_VARIABLE 342
#define K_USING 343
#define K_VARIABLE_CONFLICT 344
#define K_WARNING 345
#define K_WHEN 346
#define K_WHILE 347




#if ! defined (YYSTYPE) && ! defined (YYSTYPE_IS_DECLARED)
#line 114 "gram.y"
typedef union YYSTYPE {
		core_YYSTYPE			core_yystype;
		/* these fields must match core_YYSTYPE: */
		int						ival;
		char					*str;
		const char				*keyword;

		PLword					word;
		PLcword					cword;
		PLwdatum				wdatum;
		bool					boolean;
		struct
		{
			char *name;
			int  lineno;
		}						varname;
		struct
		{
			char *name;
			int  lineno;
			PLpgSQL_datum   *scalar;
			PLpgSQL_rec     *rec;
			PLpgSQL_row     *row;
		}						forvariable;
		struct
		{
			char *label;
			int  n_initvars;
			int  *initvarnos;
		}						declhdr;
		struct
		{
			List *stmts;
			char *end_label;
			int   end_label_location;
		}						loop_body;
		List					*list;
		PLpgSQL_type			*dtype;
		PLpgSQL_datum			*datum;
		PLpgSQL_var				*var;
		PLpgSQL_expr			*expr;
		PLpgSQL_stmt			*stmt;
		PLpgSQL_condition		*condition;
		PLpgSQL_exception		*exception;
		PLpgSQL_exception_block	*exception_block;
		PLpgSQL_nsitem			*nsitem;
		PLpgSQL_diag_item		*diagitem;
		PLpgSQL_stmt_fetch		*fetch;
		PLpgSQL_case_when		*casewhen;
} YYSTYPE;
/* Line 1204 of yacc.c.  */
#line 271 "pl_gram.h"
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE plpgsql_yylval;

#if ! defined (YYLTYPE) && ! defined (YYLTYPE_IS_DECLARED)
typedef struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
} YYLTYPE;
# define yyltype YYLTYPE /* obsolescent; will be withdrawn */
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif

extern YYLTYPE plpgsql_yylloc;


