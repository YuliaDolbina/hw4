from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)
Base = declarative_base()
session = sessionmaker(bind=db, expire_on_commit=False)


def test_connection():
    query = session().scalar(text("select 1;"))
    assert query == 1


def test_select():
    rows = session().execute(text("select * from company")).fetchall()
    assert rows[0][0] == 1


def test_select_one_row():
    company_id = 119
    sql_statement = text(f"select * from company where id = {company_id}")
    row = session().execute(sql_statement).fetchone()
    assert row[0] == company_id
