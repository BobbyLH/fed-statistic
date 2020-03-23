import mysql.connector as mysql

try:
  conn = mysql.connect(
    host = 'localhost',
    user = 'hupu',
    passwd = 'hp-fed',
    database = 'hp_fed_statistic'
  )
except:
  print(f'The database connect error')
else:
  sql = 'INSERT INTO hupu_cli(project_type, project_name, stage, count) VALUES ("hybrid", "hp-spa", "init", 1)'
  cursor = conn.cursor(buffered=True)

  cursor.execute(sql)
  conn.commit()





