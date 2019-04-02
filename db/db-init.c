//quick program to initialize the database

#include "stdio.h"
#include "sqlite3.h"

static int callback()
{
	return 0;
}

int init_sounds(sqlite3 *db, char *sql, int *rc, char *zErrMsg);
int init_configuration(sqlite3 *db, char *sql, int *rc, char *zErrMsg);

int main()
{
	sqlite3 *db;
	char *zErrMsg = 0;
	int rc;
	char *sql;

	rc = sqlite3_open("test.db", &db);

	if(rc)
	{
		fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
		return 0;
	}
	else
	{
		fprintf(stderr, "opened database successfully\n");
	}


	init_sounds(db, sql, &rc, zErrMsg);
	init_configuration(db, sql, &rc, zErrMsg);

	if(rc != SQLITE_OK)
	{
		printf("ERROR\n");
	}
	else
	{
		printf("RET OK\n");
	}


	sqlite3_close(db);
}


int init_sounds(sqlite3 *db, char *sql, int *rc, char *zErrMsg)
{
	sql = "CREATE TABLE SOUNDS(" \
	       "TIME INT PRIMARY KEY NOT NULL," \
	       "FREQUENCY INT NOT NULL," \
	       "DIRECTION INT NOT NULL," \
	       "AMPLITUDE INT NOT NULL);";

	*rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);
}


int init_configuration(sqlite3 *db, char *sql, int *rc, char *zErrMsg)
{
	sql = "CREATE TABLE CONFIGURATION(" \
	       "ID INT PRIMARY KEY NOT NULL," \
	       "TARGET_FREQUENCIES TEXT NOT NULL," \
	       "ERROR_THRESHOLD INT NOT NULL," \
	       "ANGLE_OFFSET INT NOT NULL," \
	       "HISTORY INT NOT NULL," \
	       "ACTIVE_MICS TEXT NOT NULL);";

	*rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);
}
