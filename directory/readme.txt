# To select all tables from in db
c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
# To print result
c.fetchall()
