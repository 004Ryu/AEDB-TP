import cx_Oracle

'''def f_insert_sql(table):
    res_insert_sql = "INSERT INTO %s \
                                   values (%s, %s)")
    return insert_sql
'''
def main():
    username = "system"
    password = "Oradoc_db1"

    #User2 , user criado para fazer inserts
    username2 = "TRABALHOPDB"
    pasword2  = "trab"
    #faz a conecção à BD usando username, password, connectionString e o tipo de enconding
    conn_pdb1 = cx_Oracle.connect(username, password, "//127.0.0.1/orclpdb1.localdomain", encoding="UTF-8")

    #cursor responsável por executar as queries
    cur_pdb1 = conn_pdb1.cursor()


    #Query1
    sql1 = "SELECT DB_ID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME, NUMBER_THREADS \
                            FROM DATABASE_INSTANCE                                                                           \
                            WHERE STARTUP_TIME = (SELECT MAX(STARTUP_TIME) FROM DATABASE_INSTANCE)"
    #sql_insert = f_insert_sql("DATABASE_INSTANCE")

    #Query2
    sql2 = "SELECT USER_ID, USERNAME, ACCOUNT_STATUS, EXPIRY_DATE, DEFAULT_TABLESPACE, TEMPORARY_TABLESPACE, CREATED, \
            COMMON, LAST_LOGIN, TIMESTAMP, PROFILE_ID \
            FROM USERS \
            INNER JOIN PROFILES P \
            ON USERS.PROFILE_ID = P.PROFILE_ID \
            WHERE TIMESTAMP = SYSDATE AND LAST_LOGIN = SYSDATE"
    #sql_insert = f_insert_sql("TABELA")

    #Query3
    sql3 = "SELECT USER_ID, ROLE_ID\
            FROM USERS_HAS_ROLES UR\
            INNER JOIN USERS U \
            ON UR.USER_ID = U.USER_ID \
            INNER JOIN ROLES R \
            ON UR.ROLE_ID = R.ROLE_ID"

    #Query4
    sql4 = "SELECT DATAFILE_ID, DATAFILE_NAME, DIRECTORY, TOTAL_SPACE, AUTOEXTENSIBLE, FREE_SPACE, STATUS, TIMESTAMP, TABLESPACE_ID, \
            DB_ID FROM DATAFILES \
            INNER JOIN TABLESPACES T \
            ON DATAFILES.TABLESPACE_ID = T.TABLESPACE_ID \
            WHERE TIMESTAMP = SYSDATE"

    #sql_insert = f_insert_sql("TABELA")
    
    #Query5
    sql5 = "SELECT TABLESPACE_ID, TABLESPACE_NAME, STATUS, TYPE, SEGMENT_SPACE_MANAGEMENT, TIMESTAMP, DB_ID \
        FROM TABLESPACES \
        INNER JOIN DATABASE_INSTANCE DBI ON TABLESPACES.DB_ID = DBI.DB_ID \
        WHERE TIMESTAMP = SYSDATE"

    #Query6
    sql6 = "SELECT CPU_ID, DB_ID, SQL_ID, EXECUTIONS_DELTA. BUFFER_GETS_DELTA, DISK_READS_DELTA, IOWAIT_DELTA, APWAIT_DELTA, \
            CPU_TIME_DELTA, ELAPSED_TIME_DELTA, TIMESTAMP \
            FROM CPU \
            INNER JOIN DATABASE_INSTANCE DBI ON CPU.DB_ID = CPU.DB_ID \
            WHERE TIMESTAMP = SYSDATE"

    #Query7
    sql7 = "SELECT MEMORY_ID, FIXED_SIZE, VARIABLE_SIZE, DATABASE_BUFFERS, REDO_BUFFERS, TIMESTAMP, DB_ID \
            FROM MEMORY \
            INNER JOIN DATABASE_INSTANCE DBI \
            ON MEMORY.DB_ID = DBI_DB_ID \
            WHERE TIMESTAMP = SYSDATE"

    #Query8
    sql8 = "SELECT SESSION_ID, SAMPLE_TIME, SQL_ID, SQL_OP_NAME, SQL_PLAN_OPERATION, WAIT_CLASS, WAIT_TIME, \
            SESSION_TYPE, SESSION_STATE, TIME_WAITED, TIMESTAMP, USER_ID \
            FROM SESSIONS S \
            INNER JOIN USERS U \
            ON U.USER_ID = S.USER_ID \
            WHERE TIMESTAMP = SYSDATE"
    
    #Query9
    sql9 = "SELECT ROLE_ID, ROLE_NAME, AUTHENTICATION_TYPE, COMMON, TIMESTAMP \
            FROM ROLES \
            WHERE TIMESTAMP = SYSDATE"

    #EXECUTE QUERY
    res = cur_pdb1.execute(sql1)

    #define os "headers" do resultado da query
    columns = [col[0] for col in res.description] 

    #Manipula o tipo/estrutura dos resultados da query
    res.rowfactory = lambda *args: dict(zip(columns, args))

    #Vai buscar o array de resultados da query (já tratados), fetchone() seria suficiente neste caso visto os resultados só terem uma row
    res = res.fetchall() 

    #Faz a conexão *a BD para fazer os Inserts 
    conn_pdb2 = cx_Oracle.connect(username2, password2, "//127.0.0.1/TrabalhoPDB.localdomain", encoding="UTF-8")

     #cursor responsável por executar as queries
    cur_pdb2 = conn_pdb2.cursor()

    #Insert Queries
    i_sql1 = "INSERT INTO DATABASE_INSTANCE (field, field) values (%s, %s)"

    i_sql2 = ""

    i_sql3 = ""

    while(1):
        for row in res:

            #Query de Insert
            cur_pdb2.execute(i_sql1, )
            #Commit changes to db
            conn_pdb2.commit()

    cur_pdb2.close()
    conn_pdb2.close()
    
    cur_pdb1.close()
    conn_pdb1.close()

if __name__ == 'main':
    main()