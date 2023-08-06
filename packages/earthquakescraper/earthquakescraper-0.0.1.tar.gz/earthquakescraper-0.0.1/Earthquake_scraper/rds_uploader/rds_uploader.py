import pandas as pd
from sqlalchemy import create_engine

DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
# Change it for your AWS endpoint
ENDPOINT = '' # The endpoint of your AWS RDS
USER = 'postgres'
PASSWORD = '' # Your password
PORT = 5432
DATABASE = 'postgres'
engine = create_engine(
    f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

engine.connect()

data = pd.read_csv('df.csv')
data.head()

data.to_sql('earthquake_dataset', engine, if_exists='replace')
df = pd.read_sql_table('earthquake_dataset', engine)
df.head()
