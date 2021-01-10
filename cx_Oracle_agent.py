import cx_Oracle

username = "system"
password = "Oradoc_db1"

#faz a conecção à BD usando username, password, connectionString e o tipo de enconding
conn_pdb1 = cx_Oracle.connect(username, password, "//127.0.0.1/orclpdb1.localdomain", encoding="UTF-8")

#cursor responsável por executar as queries
cur_pdb1 = conn_pdb1.cursor()

#faz a conecção à BD usando username, password, connectionString e o tipo de enconding
#conn_pdb2 = cx_Oracle.connect(username, password, "//127.0.0.1/tp.localdomain", encoding="UTF-8")

#cursor responsável por executar as queries
#cur_pdb2 = conn_pdb2.cursor()

#execução da query que obtem a informação para a tabela "Database_Instance"
res = cur_pdb1.execute("SELECT DBID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME FROM DBA_HIST_DATABASE_INSTANCE WHERE STARTUP_TIME = (SELECT MAX(STARTUP_TIME) FROM DBA_HIST_DATABASE_INSTANCE)")

#define os "headers" do resultado da query
columns = [col[0] for col in res.description] 

#Manipula o tipo/estrutura dos resultados da query
res.rowfactory = lambda *args: dict(zip(columns, args))

#Vai buscar o array de resultados da query (já tratados), fetchone() seria suficiente neste caso visto os resultados só terem uma row
print(res.fetchone()) 
