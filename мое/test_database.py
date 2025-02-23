from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'alembic_version'


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]
    assert row1[0] == 1


def test_select_one_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 105).fetchall()

    assert len(rows) == 0


def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"is_active\" = :is_active and id >= :id")
    rows = db.execute(sql_statement, id = 96, is_active = True).fetchall()

    assert len(rows) == 11


def test_insert_company():
    db = create_engine(db_connection_string)
    sql = text("insert into company (\"name\") values (:new_name)")

    rows = db.execute(sql, new_name='SQL school')

def test_update_company():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")
    db.execute(sql, descr="updated", id=119)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    db.execute(sql, id=121)


### pytest hw9/test_database.py
    
