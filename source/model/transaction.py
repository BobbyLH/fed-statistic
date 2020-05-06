import types
import sys
sys.path.append('./source/config')
import mysql.connector as mysql
from mysql.connector.errors import Error
from database import dev, prod

env = dev

def transaction(fn):
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
        except mysql.DataError as e:
          res = str(e)
          print('Mysql DataError: ', res)
        except mysql.OperationalError as e:
          res = str(e)
          print('Mysql OperationalError: ', res)
        except mysql.InternalError as e:
          res = str(e)
          print('Mysql InternalError: ', res)
        except mysql.IntegrityError as e:
          res = str(e)
          print('Mysql IntegrityError: ', res)
        except mysql.NotSupportedError as e:
          res = str(e)
          print('Mysql NotSupportedError: ', res)
        except mysql.ProgrammingError as e:
          res = str(e)
          print('Mysql ProgrammingError: ', res)
        except mysql.Error as e:
          res = str(e)
          print('Mysql Error: ', res)
        except:
          res = str(sys.exc_info())
          print('Unknown error: ', res)

      try:
        conn.commit()
      except:
        res = str(sys.exc_info())
        print('Mysql commit error: ', res)
      finally:
        conn.close()

      if hasError:
        raise TypeError(res)
      else:
        return res
    except:
      conn.rollback()
    