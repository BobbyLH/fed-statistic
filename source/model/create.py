from uuid import uuid4
from routine import routine
from sqls import (sql_add_project,
sql_add_tool,
sql_add_log,
sql_find_log_one,
sql_find_tool_version,
sql_find_project,
sql_find_project_unsafe,
sql_update_log)

def create_project(
  project_name,
  project_type = None
):
  if not project_name:
    raise ValueError('Please pass correct project name!')
  
  def add(cursor):
    project_uuid = uuid4()
    sql = sql_add_project(project_name, project_type, project_uuid)
    cursor.execute(sql)
    return project_uuid
  return routine(add)

def create_tool(
  tool_name,
  tool_version
):
  if not tool_name or not tool_version:
    raise ValueError('Please pass correct parameters!')
  def make_tool(cursor):
    sql = sql_find_tool_version(tool_name, tool_version)
    cursor.execute(sql)
    info_tool = cursor.fetchone()
    if not info_tool:
      sql = sql_add_tool(tool_name, tool_version)
      cursor.execute(sql)
      tool_id = cursor.lastrowid
    else:
      tool_id = info_tool['id']
    return tool_id

  return routine(make_tool)

def create_log(
  project_id,
  tool_id,
  info = None,
):
  if not project_id or not tool_id:
    raise ValueError('Please pass correct parameters!')

  def make_log(cursor):
    sql = sql_add_log(
      project_id = project_id,
      tool_id = tool_id,
      info = info
    )
    cursor.execute(sql)
    isAffect = cursor.rowcount
    return bool(isAffect)

  return routine(make_log)

def create_track(
  tool_name,
  tool_version,
  project_name = None,
  project_uuid = None,
  info = None
):
  def make_track(cursor):
    # 校验项目是否注册
    sql = None
    if project_uuid:
      sql = sql_find_project(project_uuid)
    elif project_name:
      sql = sql_find_project_unsafe(project_name)
    else:
      return '项目未注册'
    cursor.execute(sql)
    info_project = cursor.fetchone()

    if not info_project:
      return '项目未注册'
    else:
      project_id = info_project['id']
      # 处理工具信息
      tool_id = create_tool(tool_name, tool_version)

      # 记录日志
      return create_log(
        project_id,
        tool_id,
        info
      )

  return routine(make_track)