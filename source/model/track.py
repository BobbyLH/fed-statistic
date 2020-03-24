import mysql.connector as mysql
import sql

try:
  conn = mysql.connect(
    host = 'localhost',
    user = 'hupu',
    passwd = 'hp-fed',
    database = 'hp_fed_statistic'
  )
except:
  print('The database connect error')
else:
  
  sql = sql.sql_add_project(
    project_type='spa-react',
    project_name='hp-spa'
  )
  cursor = conn.cursor(buffered=True)

  cursor.execute(sql)
  conn.commit()





