import mysql.connector as mysql
import sys

params_cli = sys.argv[1:]
mysql_configs = {
  'host': 'localhost',
  'user': 'root',
  'passwd': ''
}

for param in params_cli:
  param = param.split('=')
  mysql_configs[param[0]] = param[1]

print(mysql_configs)
conn = mysql.connect(
  host = mysql_configs['host'],
  user = mysql_configs['user'],
  passwd = mysql_configs['passwd']
)

sql_create_database = 'CREATE DATABASE hp_fed_statistic'

sql_create_user = 'CREATE USER hupu@localhost IDENTIFIED BY "hp-fed"'

sql_grant_database = 'GRANT ALL ON hp_fed_statistic.* TO hupu@localhost'

sql_use_database = 'USE hp_fed_statistic'

sql_create_table_project = 'CREATE TABLE project (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, type VARCHAR(255), uuid VARCHAR(255) NOT NULL, createAt INT(11) NOT NULL)'

sql_create_table_tool = 'CREATE TABLE tool (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, version VARCHAR(255), createAt INT(11) NOT NULL)'

sql_create_table_log = 'CREATE TABLE log (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, project_id INT(11) NOT NULL, tool_id INT(11) NOT NULL, project_stage VARCHAR(255), count INT(11) NOT NULL)'

cursor = conn.cursor(buffered=True)
cursor.execute(sql_create_database)
cursor.execute(sql_create_user)
cursor.execute(sql_grant_database)
cursor.execute(sql_use_database)
cursor.execute(sql_create_table_project)
cursor.execute(sql_create_table_tool)
cursor.execute(sql_create_table_log)
conn.commit()
conn.close()
