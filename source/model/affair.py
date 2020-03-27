import sys
sys.path.append('./source/config')
import mysql.connector as mysql
from database import dev, prod

env = dev

def affair(fn):
  try:
    conn = mysql.connect(
      host = env['host'],
      user = env['user'],
      passwd = env['passwd'],
      database = env['database']
    )
  except:
    print('The database connect error')
  else:
    try:
      cursor = conn.cursor(dictionary=True)
      if fn and str(type(fn)) == "<class 'function'>":
        fn(cursor)
      conn.commit()
      conn.close()
    except:
      conn.rollback()
    