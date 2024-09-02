import sqlite3

def create_database():
    conn = sqlite3.connect('app.db')

    ## Create Tables Here
    c = conn.cursor()
    c.execute('''
      DROP TABLE IF EXISTS sources;
    ''')
    conn.commit()

    c.execute('''
      CREATE TABLE IF NOT EXISTS sources 
      (
        id INTEGER PRIMARY KEY,
        name TEXT,
        table_name TEXT,
        database TEXT,
        host_ip TEXT,
        port TEXT,
        username TEXT,
        password TEXT
      )
      ;
    ''')
    conn.commit()

    c.execute('''
    INSERT INTO sources
      (name, table_name, database, host_ip, port, username, password)
    VALUES
      ('Today Cache Data', 'cache1', 'rtk_api', '172.0.0.1', '56001', 'username', 'password'),
      ('All Cache Data', 'cache1_all', 'rtk_api', '172.0.0.1', '56001', 'username', 'password')            
    ;
    ''')
    conn.commit()

    # c = conn.cursor()
    # c.execute('''
    #   CREATE TABLE IF NOT EXISTS tasks 
    #   (
    #     id INTEGER PRIMARY KEY,
    #     task TEXT
    #   )
    # ''')
    # conn.commit()

    conn.close()

create_database()