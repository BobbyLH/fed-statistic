import types
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
    print('The database connect error: ', str(sys.exc_info()[0]))
  else:
    res = None
    try:
      cursor = conn.cursor(dictionary=True)
      if fn and isinstance(fn, types.FunctionType):
        hasError = True
        try:
          res = fn(cursor)
          hasError = False
        except OSError as e:
          res = str(e)
          print('System error: ', res)
        except ValueError as e:
          res = str(e)
          print('Value error: ', res)
        except IndexError as e:
          res = str(e)
          print('Index error: ', res)
        except KeyError as e:
          res = str(e)
          print('Key error: ', res)
        except MemoryError as e:
          res = str(e)
          print('Memory error: ', res)
        except LookupError as e:
          res = str(e)
          print('Lookup error: ', res)
        except NameError as e:
          res = str(e)
          print('Name error: ', res)
        except:
          res = str(sys.exc_info()[0])
          print('Unknown error: ', res)

      conn.commit()
      conn.close()
      if hasError:
        raise TypeError(res)
      else:
        return res
    except:
      conn.rollback()
    