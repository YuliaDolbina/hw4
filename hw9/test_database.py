from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'app_users'


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]
    assert row1[0] == 1


def test_select_one_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 105).fetchall()
       


    
