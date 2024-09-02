import sqlite3
import pandas as pd

def query_db(query):
  conn = sqlite3.connect('app.db')
  return pd.read_sql(query, conn).to_dict(orient='records')