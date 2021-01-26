import cx_Oracle
from random import randint
import string
from time import time, sleep
import time
import datetime
import types
import re
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
        sql1 = "SELECT DB_ID INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME, NUMBER_THREADS \
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
        sql5_1 = "SELECT * FROM TABLESPACES"

        # (select info da orclpdb1 )
        sql5_2 = "SELECT TABLESPACE_NAME, STATUS, CONTENTS, SEGMENT_SPACE_MANAGEMENT FROM DBA_TABLESPACES"
        
        #Query6
        # (select info da trabalhoPDB)
        sql6 = "SELECT CPU_ID, DB_ID, SQL_ID, EXECUTIONS_DELTA. BUFFER_GETS_DELTA, DISK_READS_DELTA, IOWAIT_DELTA, APWAIT_DELTA, \
                CPU_TIME_DELTA, ELAPSED_TIME_DELTA, TIMESTAMP \
                FROM CPU \
                INNER JOIN DATABASE_INSTANCE DBI ON CPU.DB_ID = CPU.DB_ID \
                WHERE TIMESTAMP = SYSDATE"
        sql6_n = "SELECT * FROM CPU"

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
        sql7_1 = "SELECT * FROM MEMORY"

        # (select info da orclpdb1 )
        sql7_2 = "SELECT NAME, VALUE FROM V$SGA"

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
        sql9_1 = "SELECT * FROM ROLES "

        # (select info da orclpdb1 )
        sql9_2 = "SELECT ROLE, ROLE_ID, AUTHENTICATION_TYPE, COMMON, SYSDATE \
                        FROM DBA_ROLES"
        
        #Query10 
        # (select info trabalhoPDB)
        sql10 = "SELECT PROFILE_ID, PROFILE_NAME, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, TIMESTAMP \
                FROM PROFILES \
                WHERE TIMESTAMP = SYSDATE"
        sql10_1 = "SELECT * FROM PROFILES "
        # (select da orclpdb1)
        sql10_2 = "SELECT PROFILE, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, SYSDATE FROM DBA_PROFILES"

        sql10_aux = "SELECT PROFILE, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, SYSDATE FROM DBA_PROFILES WHERE PROFILE = 'DEFAULT' "
        
        
        #EXECUTE QUERY -------- DATABASE_INSTANCE
        print("\nInfo da database_instance na orclpdb1\n")
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
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO DATABASE_INSTANCE (DB_ID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, \
                                         PLATFORM_NAME, DB_UNIQUE_NAME) values (:1, :2, :3, :4, :5, :6, :7, :8)"
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                insert_sql = "UPDATE DATABASE_INSTANCE SET DB_ID = :1, INSTANCE_NUMBER = :2 ,STARTUP_TIME = :3, VERSION = :4, DB_NAME = :5, INSTANCE_NAME = :6, PLATFORM_NAME = :7, DB_UNIQUE_NAME = :8"
                                #print(row.values())
                                cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                else:
                        break                           
                        
        s = cur_pdb2.execute(sql1)
        print("\nInfo da database_instance no trabalho\n")
        columns = [col[0] for col in s.description] 
        s.rowfactory = lambda *args: dict(zip(columns, args))
        #print(s.fetchone())
        s = s.fetchall()
        for row in s:
                if list(row.keys())[0] == 'DB_ID':
                        print(row) 
        

        

        #EXECUTE QUERY -------- ROLES

        print("\nInfo da roles na orclpdb1\n")
        res = cur_pdb1.execute(sql9_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 
         
        for row in res:
                if list(row.keys())[0] == 'ROLE':
                        try:
                                #row['ts'] = datetime.datetime.now()
                                #print(row['ts'])
                                #row['roleId'] = randint(0,1000)
                                print(row)
                                insert_sql = "INSERT INTO ROLES (ROLE_NAME, ROLE_ID, AUTHENTICATION_TYPE, COMMON, TIMESTAMP) values (:1, :2, :3, :4, :5)" 
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                #cur_pdb2.execute(insert_sql, list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                del row['ROLE_ID']
                                insert_sql = "UPDATE ROLES SET ROLE_NAME = :1, AUTHENTICATION_TYPE = :2, COMMON = :3, TIMESTAMP = :4"
                                #cur_pdb2.execute(insert_sql, list(row.values()))
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError:
                                break
                else:
                        break

        s = cur_pdb2.execute(sql9_1)
        print("\nInfo da roles no trabalho\n")
        columns = [col[0] for col in s.description] 
        s.rowfactory = lambda *args: dict(zip(columns, args))
        s = s.fetchall()
        for row in s:
                if list(row.keys())[0] == 'ROLE_ID':
                        print(row)  
        
        

        
        
        #EXECUTE QUERY -------- PROFILES
        print("\nInfo da profiles na orclpdb1\n")

        res = cur_pdb1.execute(sql10_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 

        for row in res:
                if list(row.keys())[0] == 'PROFILE':
                        try:
                                row['PROFILE_ID'] = (randint(0,1000))
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO PROFILES (PROFILE_NAME, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, TIMESTAMP, PROFILE_ID) \
                                         values (:1, :2, :3, :4, :5, :6)"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.TIMESTAMP, cx_Oracle.DB_TYPE_NUMBER)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                del row['PROFILE_ID']
                                insert_sql = "UPDATE PROFILES SET PROFILE_NAME = :1, RESOURCE_NAME = :2, RESOURCE_TYPE = :3, LIMIT = :4, TIMESTAMP = :5"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                else:
                        break
             
        s = cur_pdb2.execute(sql10_1)
        print("\nInfo da profiles no trabalho\n")
        columns = [col[0] for col in s.description] 
        s.rowfactory = lambda *args: dict(zip(columns, args))
        s = s.fetchall()
        for row in s:
                if list(row.keys())[0] == 'PROFILE_ID':
                        print(row)
  

      

        #EXECUTE QUERY -------- MEMORY
        print("\nInfo da memory no orclpdb1\n")
        res = cur_pdb1.execute(sql7_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 
        for row in res:
                if list(row.keys())[0] == 'NAME':
                        print(row)

        print("\n")
        for row in res:
                if list(row.keys())[0] == 'NAME' and list(row.values())[0] == 'Fixed Size': 
                        try:
                                row['MEMORY_ID'] = (randint(0,1000))
                                del row['NAME']
                                ct = datetime.datetime.now()
                                row['TIMESTAMP'] = ct
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO MEMORY (FIXED_SIZE, MEMORY_ID, TIMESTAMP) values (:2, :3, :4)"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                del row['MEMORY_ID']
                                del row['NAME']
                                ct = datetime.datetime.now()
                                row['TIMESTAMP'] = ct
                                insert_sql = "UPDATE MEMORY SET FIXED_SIZE = :1, TIMESTAMP = :2"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                else : 
                        if list(row.keys())[0] == 'NAME' and list(row.values())[0] == 'Variable Size': 
                                try:
                                        row['MEMORY_ID'] = (randint(0,1000))
                                        del row['NAME']
                                        ct = datetime.datetime.now()
                                        row['TIMESTAMP'] = ct
                                        print(row)
                                        print("\n")
                                        insert_sql = "INSERT INTO MEMORY (VARIABLE_SIZE, MEMORY_ID, TIMESTAMP) values (:2, :3, :4)"
                                        cur_pdb2.prepare(insert_sql)
                                        cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                        cur_pdb2.execute(None,list(row.values()))
                                        conn_pdb2.commit()
                                except cx_Oracle.IntegrityError: 
                                        del row['MEMORY_ID']
                                        del row['NAME']
                                        ct = datetime.datetime.now()
                                        row['TIMESTAMP'] = ct
                                        insert_sql = "UPDATE MEMORY SET VARIABLE_SIZE = :1, TIMESTAMP = :2"
                                        cur_pdb2.prepare(insert_sql)
                                        cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER)
                                        cur_pdb2.execute(None,list(row.values()))
                                        conn_pdb2.commit()
                        else:
                                if list(row.keys())[0] == 'NAME' and list(row.values())[0] == 'Database Buffers': 
                                        try:
                                                row['MEMORY_ID'] = (randint(0,1000))
                                                del row['NAME']
                                                ct = datetime.datetime.now()
                                                row['TIMESTAMP'] = ct
                                                print(row)
                                                print("\n")
                                                insert_sql = "INSERT INTO MEMORY (DATABASE_BUFFERS, MEMORY_ID, TIMESTAMP) values (:2, :3, :4)"
                                                cur_pdb2.prepare(insert_sql)
                                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                                cur_pdb2.execute(None,list(row.values()))
                                                conn_pdb2.commit()
                                        except cx_Oracle.IntegrityError: 
                                                del row['MEMORY_ID']
                                                del row['NAME']
                                                ct = datetime.datetime.now()
                                                row['TIMESTAMP'] = ct
                                                insert_sql = "UPDATE MEMORY SET DATABASE_BUFFERS = :1, TIMESTAMP = :2"
                                                cur_pdb2.prepare(insert_sql)
                                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                                cur_pdb2.execute(None,list(row.values()))
                                                conn_pdb2.commit()
                                else:
                                        if list(row.keys())[0] == 'NAME' and list(row.values())[0] == 'Redo Buffers':
                                                try:
                                                        row['MEMORY_ID'] = (randint(0,1000))
                                                        del row['NAME']
                                                        ct = datetime.datetime.now()
                                                        row['TIMESTAMP'] = ct
                                                        print(row)
                                                        print("\n")
                                                        insert_sql = "INSERT INTO MEMORY (REDO_BUFFERS, MEMORY_ID, TIMESTAMP) values (:2, :3, :4)"
                                                        cur_pdb2.prepare(insert_sql)
                                                        cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                                        cur_pdb2.execute(None,list(row.values()))
                                                        conn_pdb2.commit()
                                                except cx_Oracle.IntegrityError: 
                                                        del row['MEMORY_ID']
                                                        del row['NAME']
                                                        ct = datetime.datetime.now()
                                                        row['TIMESTAMP'] = ct
                                                        insert_sql = "UPDATE MEMORY SET REDO_BUFFERS = :1, TIMESTAMP = :2"
                                                        cur_pdb2.prepare(insert_sql)
                                                        cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                                        cur_pdb2.execute(None,list(row.values()))
                                                        conn_pdb2.commit() 
                                        else:
                                                break

                        
        
        print("\nInfo da memory no trabalho\n")
        s = cur_pdb2.execute(sql7_1)
        columns = [col[0] for col in s.description] 
        s.rowfactory = lambda *args: dict(zip(columns, args))
        s = s.fetchall()
        for row in s:
                if list(row.keys())[0] == 'MEMORY_ID':
                        print(row)

        
        #EXECUTE QUERY -------- CPU
        print("\nInfo da cpu no orclpdb1\n")
        res = cur_pdb1.execute(sql6_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 
        for row in res:
                if list(row.keys())[0] == 'DBID':
                        print(row)
                        print("\n")

        
        for row in res:
                if list(row.keys())[0] == 'DBID':
                        try:
                                row['CPU_ID'] = (randint(0,1000))
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO CPU (DB_ID, SQL_ID, EXECUTIONS_DELTA, DISK_READS_DELTA, BUFFER_GETS_DELTA, \
                                         CPU_TIME_DELTA, ELAPSED_TIME_DELTA, IOWAIT_DELTA, APWAIT_DELTA, TIMESTAMP, CPU_ID) values \
                                                 (:1, :2, :3, :5, :4, :8, :9, :6, :7, :10, :11)"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP, cx_Oracle.DB_TYPE_NUMBER)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                del row['CPU_ID']
                                insert_sql = "UPDATE CPU SET DB_ID = :1, SQL_ID = :2, EXECUTIONS_DELTA = :3, DISK_READS_DELTA = :4, BUFFER_GETS_DELTA = :5, CPU_TIME_DELTA = :6, ELAPSED_TIME_DELTA = :7, IOWAIT_DELTA = :8, APWAIT_DELTA = :9, TIMESTAMP = :10"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                else:
                        break
        
        s = cur_pdb2.execute(sql6_n)
        print("\nInfo da cpu no trabalho\n")
        columns = [col[0] for col in s.description] 
        s.rowfactory = lambda *args: dict(zip(columns, args))
        s = s.fetchall()
        for row in s:
                if list(row.keys())[0] == 'CPU_ID':
                        print(row)
                        print("\n")
                        
        #EXECUTE QUERY -------- TABLESPACE
        print("\nInfo da tablespace no orclpdb1\n")
        res = cur_pdb1.execute(sql5_2)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall() 
        for row in res:
                if list(row.keys())[0] == 'TABLESPACE_NAME':
                        print(row)
                        print("\n")

        
        for row in res:
                if list(row.keys())[0] == 'TABLESPACE_NAME':
                        try:
                                row['TABLESPACE_ID'] = (randint(0,1000))
                                ct = datetime.datetime.now()
                                row['TIMESTAMP'] = ct
                                print(row)
                                print("\n")
                                insert_sql = "INSERT INTO TABLESPACES (TABLESPACE_NAME, STATUS, TYPE, SEGMENT_SPACE_MANAGEMENT, TABLESPACE_ID, TIMESTAMP) \
                                         values (:1, :2, :3, :4, :5, :6)"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_NUMBER, cx_Oracle.DB_TYPE_TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                        except cx_Oracle.IntegrityError: 
                                del row['TABLESPACE_ID']
                                insert_sql = "UPDATE TABLESPACES SET TABLESPACE_NAME = :1, STATUS = :2, TYPE = :3, SEGMENT_SPACE_MANAGEMENT = :4, TIMESTAMP = :5"
                                cur_pdb2.prepare(insert_sql)
                                cur_pdb2.setinputsizes(cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_VARCHAR, cx_Oracle.DB_TYPE_TIMESTAMP)
                                cur_pdb2.execute(None,list(row.values()))
                                conn_pdb2.commit()
                else:
                        break

        print("\nInfo da tablespace no trabalho\n")
        res = cur_pdb2.execute(sql5_1)
        columns = [col[0] for col in res.description] 
        res.rowfactory = lambda *args: dict(zip(columns, args))
        res = res.fetchall()
        for row in res:
                if list(row.keys())[0] == 'TABLESPACE_ID':
                        print(row)
                        print("\n")
                
        conn_pdb2.commit()

        cur_pdb2.close()
        conn_pdb2.close()
    
        cur_pdb1.close()
        conn_pdb1.close()

if __name__ == '__main__':
        #while True:
        #        sleep(60 - time() % 60)
        main()
