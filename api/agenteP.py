import cx_Oracle
from time import time, sleep
from random import randint
import string
import datetime


#def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
#    return ''.join(random.choice(chars) for x in range(size))

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
        sql6_2 = " SELECT DBID as DBID2, SQL_ID, EXECUTIONS_DELTA, DISK_READS_DELTA, BUFFER_GETS_DELTA, CPU_TIME_DELTA, ELAPSED_TIME_DELTA, \
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
        sql9_2 = "SELECT ROLE, AUTHENTICATION_TYPE, COMMON, \
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
                else:
                        break                            
                        
        #s = cur_pdb2.execute(sql1)
        #s = s.fetchone()
        #print(s)

        res = cur_pdb1.execute(sql2_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        for row in res:
                if list(row.keys())[0] == 'USERNAME':
                        try:
                                print("row no for do USERNAME: ")
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO USERS (USER_ID, USERNAME, ACCOUNT_STATUS, EXPIRY_DATE, DEFAULT_TABLESPACE, TEMPORARY_TABLESPACE, \
                                        CREATED, COMMON, LAST_LOGIN, TIMESTAMP, PROFILE_ID) values (:2, :1, :3, :4, :5, 'null' , :6, :8, :9, :10, '-1')"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE USERS SET USER_ID = :1, USERNAME = :2, ACCOUNT_STATUS = :3, EXPIRY_DATE = :4, DEFAULT_TABLESPACE = :5, TEMPORARY_TABLESPACE = :6, CREATED = :7, COMMON = :8, LAST_LOGIN = :9, TIMESTAMP = :10, PROFILE_ID = :11"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break
         

        
        ########## !!!!!!!!!!!!!!!!!!!!!!! #############################
        #ver melhor esta porque é necessário aceder à nossa BD creio eu
        res = cur_pdb1.execute(sql3)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall()
        #sql_special = "SELECT USER_ID, ROLE_ID FROM USERS"
        ########## !!!!!!!!!!!!!!!!!!!!!!! #############################
        

        
        res = cur_pdb1.execute(sql4_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        for row in res:
                if list(row.keys())[0] == 'FILE_NAME':
                        try:
                                print("row no for do FILE_NAME: ")
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO DATAFILES (DATAFILE_ID, DATAFILE_NAME, DIRECTORY, TOTAL_SPACE, AUTOEXTENSIBLE, FREE_SPACE, STATUS, TIMESTAMP, TABLESPACE_ID, DB_ID) values (:2, :1, 'NULL', :4, :5, :6, :7, :8, '-1', '-1')"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE DATAFILES SET DATAFILE_ID = :1, DATAFILE_NAME = :2, DIRECTORY = :3, TOTAL_SPACE = :4, AUTOEXTENSIBLE = :5, FREE_SPACE = :6, STATUS = :7, TIMESTAMP = :8, TABLESPACE_ID = :9, DB_ID = :10"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break
         


        res = cur_pdb1.execute(sql5_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        
        for row in res:
                if list(row.keys())[0] == 'TABLESPACE_NAME':
                        try:
                                print("row no for do TABLESPACE_NAME: ")
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO TABLESPACES (TABLESPACE_ID, TABLESPACE_NAME, STATUS, TYPE, SEGMENT_SPACE_MANAGEMENT, TIMESTAMP, DB_ID) values ('-1', :1, :2, 'null', :4, :5, '-1')"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE TABLESPACES SET TABLESPACE_ID = :1, TABLESPACE_NAME = :2, STATUS = :3, TYPE = :4, SEGMENT_SPACE_MANAGEMENT = :5, TIMESTAMP = :6, DB_ID = :7"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break
        


        res = cur_pdb1.execute(sql6_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        
        for row in res:
                if list(row.keys())[0] == 'DBID2':
                        try:
                                print("row no for do DBID2: ")
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO CPU (CPU_ID, DB_ID, SQL_ID, EXECUTIONS_DELTA. BUFFER_GETS_DELTA, \
                                        DISK_READS_DELTA, IOWAIT_DELTA, APWAIT_DELTA, CPU_TIME_DELTA, ELAPSED_TIME_DELTA, TIMESTAMP) values \
                                                 ('-1', :1, :2, :3, :5, :4, :8, :9, :6, :7, :10)"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE CPU SET CPU_ID = :1, DB_ID = :2, SQL_ID = :3, EXECUTIONS_DELTA = :4, BUFFER_GETS_DELTA = :5, DISK_READS_DELTA = :6, IOWAIT_DELTA = :7, APWAIT_DELTA = :8, CPU_TIME_DELTA = :9, ELAPSED_TIME_DELTA = :10, TIMESTAMP = :11"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break
        

        res = cur_pdb1.execute(sql7_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 


        for row in res:
                if list(row.keys())[0] == 'memory_id': #VERIFICAR QUAL É ESTA KEY
                        try:
                                print("row no for do memory_id: ")
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO MEMORY (MEMORY_ID, FIXED_SIZE, VARIABLE_SIZE, DATABASE_BUFFERS, REDO_BUFFERS, TIMESTAMP, DB_ID) values (:1, :2, :3, :4, :5, :6, :7)"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE MEMORY SET MEMORY_ID = :1, FIXED_SIZE = :2, VARIABLE_SIZE = :3, DATABASE_BUFFERS = :4, REDO_BUFFERS = :5, TIMESTAMP = :6, DB_ID = :7"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break
        
        res = cur_pdb1.execute(sql8_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        for row in res:
                if list(row.keys())[0] == 'pid':
                        try:
                                print("row no for do pid: ")
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO SESSIONS (SESSION_ID, SAMPLE_TIME, SQL_ID, SQL_OP_NAME, SQL_PLAN_OPERATION, WAIT_CLASS, WAIT_TIME, SESSION_TYPE, SESSION_STATE, TIME_WAITED, TIMESTAMP, USER_ID) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE SESSIONS SET SESSION_ID = :1, SAMPLE_TIME = :2, SQL_ID = :3, SQL_OP_NAME = :4, SQL_PLAN_OPERATION = :5, WAIT_CLASS = :6, WAIT_TIME = :7, SESSION_TYPE = :8, SESSION_STATE = :9, TIME_WAITED = :10, TIMESTAMP = :11, USER_ID = :12"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break

        res = cur_pdb1.execute(sql9_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

         
        for row in res:
                if list(row.keys())[0] == 'ROLE':
                        try:
                                print("row no for do role: ")
                                print(row)
                                print("\n")
                                row['timestamp'] = datetime.datetime.now()
                                row['roleId'] = randint(0,1000)
                                insert_sql = "INSERT INTO ROLES (ROLE_ID, ROLE_NAME, AUTHENTICATION_TYPE, COMMON, TIMESTAMP) values (:5, :1, :2, :3, :4)"
                                cur_pdb2.setinputsizes(None, None, None, cx_Oracle.TIMESTAMP)
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE ROLES SET ROLE_ID = :5, ROLE_NAME = :1, AUTHENTICATION_TYPE = :2, COMMON = :3, TIMESTAMP = :4"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break

        res = cur_pdb1.execute(sql10_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        for row in res:
                if list(row.keys())[0] == 'PROFILE':
                        try:
                                print("row no for do profile: ")
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO PROFILES (PROFILE_ID, PROFILE_NAME, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, TIMESTAMP) \
                                         values ('-1', :1, :2, :3, :4, :5)"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE PROFILES SET PROFILE_ID = :1, PROFILE_NAME = :2, RESOURCE_NAME = :3, RESOURCE_TYPE = :4, LIMIT = :5, TIMESTAMP = :6"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break

        conn_pdb2.commit()

        cur_pdb2.close()
        conn_pdb2.close()
    
        cur_pdb1.close()
        conn_pdb1.close()

if __name__ == '__main__':
        #while True:
        #        sleep(60 - time() % 60)
        main()
