from transaction import transaction
from sqls import (sql_find_tool_version, 
sql_find_log_tool, 
sql_find_tool,
sql_find_log_tools,
sql_find_project,
sql_find_all_project,
sql_find_log_join_tool
)

def read_tool(
  name,
  version = None
):
  def get_tool(cursor):
    if version:
      sql = sql_find_tool_version(name, version)
      cursor.execute(sql)
      return cursor.fetchone()
    else:
      sql = sql_find_tool(name)
      cursor.execute(sql)
      return cursor.fetchall()

  return transaction(get_tool)

def read_project(
  project_uuid = None,
  project_id = None
):
  def get_project(cursor):
    sql = sql_find_project(
      project_uuid = project_uuid,
      project_id = project_id
    )
    cursor.execute(sql)
    return cursor.fetchone()

  return transaction(get_project)

def read_projects():
  def get_projects(cursor):
    sql = sql_find_all_project()
    cursor.execute(sql)
    return cursor.fetchall()

  return transaction(get_projects)

def read_log_tool(
  name,
  version = None
):
  def get_log_tool(cursor):
    sql = sql_find_log_join_tool(name, version)
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()
    # if version:
    #   sql = sql_find_tool_version(name, version)
    #   cursor.execute(sql)
    #   info_tool = cursor.fetchone()
    #   if info_tool:
    #     sql = sql_find_log_tool(info_tool['id'])
    #     cursor.execute(sql)
    #     return cursor.fetchall()
    # else:
    #   sql = sql_find_tool(name)
    #   cursor.execute(sql)
    #   info_tools = cursor.fetchall()
    #   if info_tools:
    #     tool_ids = list()
    #     for info_tool in info_tools:
    #       tool_ids.append(info_tool['id'])
    #     sql = sql_find_log_tools(tool_ids)
    #     cursor.execute(sql)
    #     return cursor.fetchall()

  return transaction(get_log_tool)