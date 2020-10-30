import cx_Oracle


# XE =
#   (DESCRIPTION =
#     (ADDRESS = (PROTOCOL = TCP)(HOST = BLRKEC382015D.ad.infosys.com)(PORT = 1521))
#     (CONNECT_DATA =
#       (SERVER = DEDICATED)
#       (SERVICE_NAME = XE)
#     )
#   )


class Oracle_Connection():
    def ora_conn(self):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
        conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
        self.c = conn.cursor()


# if needed, place an 'r' before any parameter in order to address special characters such as '\'.
# dsn_tns = cx_Oracle.makedsn(r'BLRKEC382015D.ad.infosys.com', '1521', service_name='XE')
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')

# if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)

c = conn.cursor()
cur_select = conn.cursor()

c.execute('select * from emp where rownum <= 3') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()


# cur_createTab = conn.cursor()
# cur_createTab.execute('create table RecordONE(ID NUMBER(9), NAME VARCHAR2(9))')

def create_table():
    # working fine below stmt:
    # cur_select.execute('create table RecordONE(ID NUMBER(9), NAME VARCHAR2(9))')

    # Find max(id) from table
    cur_select.execute('select max(id) from RecordONE')

    for max_id in cur_select:
        print(max_id[0])

    if max_id[0] is None:
        new_id = 1
        print(new_id)
    else:
        new_id = max_id[0]
        new_id +=1
        stmt = "INSERT INTO RecordONE (Id, Name) VALUES(:Id, :Name)"
        c.execute(stmt, (new_id, 'jay'))
        conn.commit()


create_table()

def data_entry():

    stmt = "INSERT INTO RecordONE (Id, Name) VALUES(:Id, :Name)"
    rows = [(1, 'sanjay')]
    c.executemany(stmt, rows)
    c.execute(stmt, (2, 'jay'))
    conn.commit()

#data_entry()
