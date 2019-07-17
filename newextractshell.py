from impala.dbapi import connect


# Set up a new impala connection
conn = connect(host='impala.prod.avvo.com', port=21050, auth_mechanism='GSSAPI',
               kerberos_service_name='impala',
               use_ssl=False, ca_cert=None,
               ldap_user=None, ldap_password=None)
cursor = conn.cursor()

# Fetch all tables list from impala
# We add 'src' (database name) to each table name in order to 
# give impala proper full table name
cursor.execute("SHOW TABLES in {database_name}".format(database_name='src'))
tables = [x for x in map(lambda x: "src.{table}".format(table=x[0]), cursor.fetchall())]

# Check if all tables/partitions has incremental stats
# True - all partitions/table has incremental stats
# False - at least one partitions/table has no incremental stats
tables_incremental_stats = {}
for table in tables:
    cursor.execute("SHOW TABLE STATS {table_name}".format(table_name=table))
    inc_stats = [s for s in map(lambda x: x[7], cursor.fetchall())]
    tables_incremental_stats[table] = False if any(st == 'false' for st in inc_stats) else True 

# Now do whatever you want with tables_incremental_stats