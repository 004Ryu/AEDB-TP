import cx_Oracle
from time import time, sleep

# Falta:
#       Testar se os inserts funcionam, se sim falta completar o resto deles mas é simples
#       Fazer logging das operações
#       Se possível tentar optimizar o processo de insert

def main():
        username = "system"
        password = "Oradoc_db1"

        #User2 , user criado para fazer inserts
        username2 = "TRABALHOPDB"
        password2  = "trab"
        #faz a conecção à BD usando username, password, connectionString e o tipo de enconding
        conn_pdb1 = cx_Oracle.connect(username, password, "//127.0.0.1/orclpdb1.localdomain", encoding="UTF-8")

        #cursor responsável por executar as queries
        cur_pdb1 = conn_pdb1.cursor()

        #Faz a conexão *a BD para fazer os Inserts 
        conn_pdb2 = cx_Oracle.connect(username2, password2, "//127.0.0.1/TrabalhoPDB.localdomain", encoding="UTF-8")

        #cursor responsável por executar as queries
        cur_pdb2 = conn_pdb2.cursor()

        #Query1 
        # (select info da trabalhoPDB)
        sql1 = "SELECT DB_ID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME, NUMBER_THREADS \
                                FROM DATABASE_INSTANCE                                                                           \
                                WHERE STARTUP_TIME = (SELECT MAX(STARTUP_TIME) FROM DATABASE_INSTANCE)"
        # (select info da orclpdb1 )
        sql1_2 = "SELECT DBID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME \
        FROM DBA_HIST_DATABASE_INSTANCE WHERE STARTUP_TIME = (SELECT MAX(STARTUP_TIME) FROM DBA_HIST_DATABASE_INSTANCE)"
        

        #Query2
        # (select info da trabalhoPDB)
        sql2 = "SELECT USER_ID, USERNAME, ACCOUNT_STATUS, EXPIRY_DATE, DEFAULT_TABLESPACE, TEMPORARY_TABLESPACE, CREATED, \
                COMMON, LAST_LOGIN, TIMESTAMP, PROFILE_ID \
                FROM USERS \
                INNER JOIN PROFILES P \
                ON USERS.PROFILE_ID = P.PROFILE_ID \
                WHERE TIMESTAMP = SYSDATE AND LAST_LOGIN = SYSDATE"
        
        # (select info da orclpdb1 )
        sql2_2 = "SELECT USERNAME, USER_ID, ACCOUNT_STATUS, \
                        EXPIRY_DATE, DEFAULT_TABLESPACE, TEMPORARY_TABLESPACE \
                        CREATED, PROFILE, COMMON, LAST_LOGIN, SYSDATE \
                        FROM DBA_USERS"

        #Query3
        # (select info da trabalhoPDB)
        sql3 = "SELECT USER_ID, ROLE_ID\
                FROM USERS_HAS_ROLES UR\
                INNER JOIN USERS U \
                ON UR.USER_ID = U.USER_ID \
                INNER JOIN ROLES R \
                ON UR.ROLE_ID = R.ROLE_ID"

        #Query4
        # (select info da trabalhoPDB)
        sql4 = "SELECT DATAFILE_ID, DATAFILE_NAME, DIRECTORY, TOTAL_SPACE, AUTOEXTENSIBLE, FREE_SPACE, STATUS, TIMESTAMP, TABLESPACE_ID, \
                DB_ID FROM DATAFILES \
                INNER JOIN TABLESPACES T \
                ON DATAFILES.TABLESPACE_ID = T.TABLESPACE_ID \
                WHERE TIMESTAMP = SYSDATE"
        
        # (select info da orclpdb1 )
        sql4_2 = "SELECT a.FILE_NAME, a.FILE_ID, a.TABLESPACE_NAME, a.BYTES,\
                        a.AUTOEXTENSIBLE, b.FREE_BYTES, a.ONLINE_STATUS, SYSTIMESTAMP\
                        FROM dba_data_files a, \
                        (SELECT file_id, SUM(bytes) free_bytes \
                        FROM dba_free_space b GROUP BY file_id) b \
                        WHERE a.file_id=b.file_id"
        
        #Query5
        # (select info da trabalhoPDB)
        sql5 = "SELECT TABLESPACE_ID, TABLESPACE_NAME, STATUS, TYPE, SEGMENT_SPACE_MANAGEMENT, TIMESTAMP, DB_ID \
                FROM TABLESPACES \
                INNER JOIN DATABASE_INSTANCE DBI ON TABLESPACES.DB_ID = DBI.DB_ID \
                WHERE TIMESTAMP = SYSDATE"

        # (select info da orclpdb1 )
        sql5_2 = "SELECT TABLESPACE_NAME, STATUS, CONTENTS, SEGMENT_SPACE_MANAGEMENT, \
                        SYSTIMESTAMP \
                        FROM DBA_TABLESPACES"
        #Query6
        # (select info da trabalhoPDB)
        sql6 = "SELECT CPU_ID, DB_ID, SQL_ID, EXECUTIONS_DELTA. BUFFER_GETS_DELTA, DISK_READS_DELTA, IOWAIT_DELTA, APWAIT_DELTA, \
                CPU_TIME_DELTA, ELAPSED_TIME_DELTA, TIMESTAMP \
                FROM CPU \
                INNER JOIN DATABASE_INSTANCE DBI ON CPU.DB_ID = CPU.DB_ID \
                WHERE TIMESTAMP = SYSDATE"

        # (select info da orclpdb1 )
        sql6_2 = " SELECT DBID, SQL_ID, EXECUTIONS_DELTA, DISK_READS_DELTA, BUFFER_GETS_DELTA, CPU_TIME_DELTA, ELAPSED_TIME_DELTA, \
                IOWAIT_DELTA, APWAIT_DELTA, SYSTIMESTAMP \
                FROM DBA_HIST_SQLSTAT"

        #Query7
        # (select info da trabalhoPDB)
        sql7 = "SELECT MEMORY_ID, FIXED_SIZE, VARIABLE_SIZE, DATABASE_BUFFERS, REDO_BUFFERS, TIMESTAMP, DB_ID \
                FROM MEMORY \
                INNER JOIN DATABASE_INSTANCE DBI \
                ON MEMORY.DB_ID = DBI_DB_ID \
                WHERE TIMESTAMP = SYSDATE"

        # (select info da orclpdb1 )
        sql7_2 = "SELECT * FROM V$SGA"

        #Query8
        # (select info da trabalhoPDB)
        sql8 = "SELECT SESSION_ID, SAMPLE_TIME, SQL_ID, SQL_OP_NAME, SQL_PLAN_OPERATION, WAIT_CLASS, WAIT_TIME, \
                SESSION_TYPE, SESSION_STATE, TIME_WAITED, TIMESTAMP, USER_ID \
                FROM SESSIONS S \
                INNER JOIN USERS U \
                ON U.USER_ID = S.USER_ID \
                WHERE TIMESTAMP = SYSDATE"
        
        # (select info da orclpdb1 )
        sql8_2 = "select\
                substr(a.spid,1,9) pid,\
                substr(b.sid,1,5) sid,\
                substr(b.serial#,1,5) ser#,\
                substr(b.machine,1,6) box,\
                substr(b.username,1,10) username,\
                substr(b.osuser,1,8) os_user,\
                substr(b.program,1,30) program\
                        from v$session b, v$process a\
                        where\
                        b.paddr = a.addr\
                        and type='USER'"
        #Query9
        # (select info da trabalhoPDB)
        sql9 = "SELECT ROLE_ID, ROLE_NAME, AUTHENTICATION_TYPE, COMMON, TIMESTAMP \
                FROM ROLES \
                WHERE TIMESTAMP = SYSDATE"

        # (select info da orclpdb1 )
        sql9_2 = "SELECT ROLE, ROLE_ID, AUTHENTICATION_TYPE, COMMON, \
                        SYSTIMESTAMP \
                        FROM DBA_ROLES"
        #Query10 
        # (select info trabalhoPDB)
        sql10 = "SELECT PROFILE_ID, PROFILE_NAME, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, TIMESTAMP \
                FROM PROFILES \
                WHERE TIMESTAMP = SYSDATE"
        # (select da orclpdb1)
        sql10_2 = "SELECT PROFILE, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, SYSTIMESTAMP FROM DBA_PROFILES"
        
        
        #EXECUTE QUERY
        res = cur_pdb1.execute(sql1_2)

        #define os "headers" do resultado da query
        columns = [col[0] for col in res.description] 

        #Manipula o tipo/estrutura dos resultados da query
        res.rowfactory = lambda *args: dict(zip(columns, args))

        #Vai buscar o array de resultados da query (já tratados), fetchone() seria suficiente neste caso visto os resultados só terem uma row
        res = res.fetchall() 
        #print(res)

        for row in res:
                if list(row.keys())[0] == 'DBID':
                        try:
                                #print(row)
                                print("\n")
                                insert_sql = "INSERT INTO DATABASE_INSTANCE (DB_ID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME) values (:1, :2, :3, :4, :5, :6, :7, :8)"
                                #print(row.values())
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE DATABASE_INSTANCE SET DB_ID = :1, INSTANCE_NUMBER = :2 ,STARTUP_TIME = :3, VERSION = :4, DB_NAME = :5, INSTANCE_NAME = :6, PLATFORM_NAME = :7, DB_UNIQUE_NAME = :8"
                                #print(row.values())
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()                               
                        
        s = cur_pdb2.execute(sql1)
        s = s.fetchone()
        print(s)

        res = cur_pdb1.execute(sql2_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        for row in res:
                if list(row.keys())[0] == 'username':
                        insert_sql = "INSERT INTO DBA_USERS values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
                        cur_pdb2.execute(insert_sql, row)
                        conn_pdb2.commit()

        #res = cur_pdb1.execute(sql4_2)
        #res = cur_pdb1.execute(sql5_2)
        #res = cur_pdb1.execute(sql6_2)
        #res = cur_pdb1.execute(sql7_2)
        #res = cur_pdb1.execute(sql8_2)
        #res = cur_pdb1.execute(sql9_2)

        # Caso não seja possível verificar os headers podemos fazer o seguinte:
        # Criar um RES para selects de cada tabela e depois é só fazer inserts
        # Esta solução é um bocado merda
        '''
        for row in res:
                #Verificar se a lógica é esta
                if list(row.keys())[0] == 'dbid':
                        insert_sql = "INSERT INTO DATABASE_INSTANCE values (:1, :2, :3, :4, :5, :6, :7, :8)"
                        cur_pdb2.execute(insert_sql, row)
                elif list(row.keys())[0] == 'username':
                        insert_sql = "INSERT INTO DBA_USERS values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
                        cur_pdb2.execute(insert_sql, row)
                elif list(row.keys())[0] == 'user_id':
                        insert_sql = "INSERT INTO USERS_HAS_ROLES values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)"
                        cur_pdb2.execute(insert_sql, row)
                #continuar
        '''

        # Commit dos inserts
        conn_pdb2.commit()


        cur_pdb2.close()
        conn_pdb2.close()
    
        cur_pdb1.close()
        conn_pdb1.close()

if __name__ == '__main__':
        #while True:
        #        sleep(60 - time() % 60)
        main()
