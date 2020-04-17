import sys
sys.path.append('./source/config')
import mysql.connector as mysql
from database import dev, prod

env = dev

def routine(fn):
  try:
    conn = mysql.connect(
      host = env['host'],
      user = env['user'],
      passwd = env['passwd'],
      database = env['database']
    )
  except:
    print('The database connect error!')
  else:
    res = None
    try:
      cursor = conn.cursor(dictionary=True)
      if fn and str(type(fn)) == "<class 'function'>":
        try:
          res = fn(cursor)
        except OSError as e:
          print('System error: ', str(e))
        except ValueError as e:
          print('Value error: ', str(e))
        except:
          print('The callback occured error: ', str(sys.exc_info()[0]))
          raise TypeError
      conn.commit()
      conn.close()
      return res
    except:
      conn.rollback()
    