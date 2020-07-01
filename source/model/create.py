from uuid import uuid4, UUID
from transaction import transaction
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
  project_uuid = None,
  project_type = None,
  author = None
):
  if not project_name:
    raise ValueError('Please pass correct project name!')
  
  def add(cursor):
    uuid = project_uuid if project_uuid else uuid4()
    sql = sql_add_project(project_name, project_type, uuid, author)
    cursor.execute(sql)
    return project_uuid
  return transaction(add)

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
    cursor.close()
    return tool_id

  return transaction(make_tool)

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
    cursor.close()
    return bool(isAffect)

  return transaction(make_log)

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
      try:
        uuid = UUID(project_uuid)
      except:
        uuid = project_uuid
      sql = sql_find_project(uuid)
    elif project_name:
      sql = sql_find_project_unsafe(project_name)
    else:
      return '参数错误'
    cursor.execute(sql)
    info_project = cursor.fetchone()
    cursor.nextset()

    if not info_project:
      return '项目未注册'
    else:
      project_id = info_project['id']
      # 处理工具信息
      tool_id = create_tool(tool_name, tool_version)

      # 记录日志
      isSuc = create_log(
        project_id,
        tool_id,
        info
      )
      cursor.close()
      return '成功' if isSuc else None

  return transaction(make_track)