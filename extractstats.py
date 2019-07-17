import pyodbc
import impala.dbapi

conn = impala.dbapi.connect(host = cfg['impala.prod.avvo.com'], port = cfg['21000'], 
                            database = 'src', use_ssl = True,
                            user = cfg['hsejiane'], password = cfg['xxx'],
                            auth_mechanism = 'PLAIN')

cur=conn.cursor()
print(cur.execute('show database in src;'))
