def find_tool():
  # 校验项目是否注册
  sql = sqls.sql_find_project(project_uuid)
  cursor.execute(sql)
  info_project = cursor.fetchone()