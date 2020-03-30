from uuid import uuid4
from affair import affair
import sqls

def add_project(
  project_name,
  project_type = None
):
  if not project_name:
    raise ValueError('Please pass correct project name!')

  project_uuid = uuid4()
  sql = sqls.sql_add_project(project_name, project_type, project_uuid)
  affair(lambda cursor: cursor.execute(sql))
  return project_uuid

def add_tool(
  tool_name = None,
  tool_version = None
):
  if not tool_name or not tool_version:
    raise ValueError('Please pass correct parameters!')
  def add(cursor):
    sql = sqls.sql_find_tool_version(tool_name, tool_version)
    cursor.execute(sql)
    info_tool = cursor.fetchone()
    if not info_tool:
      sql = sqls.sql_add_tool(tool_name, tool_version)
      cursor.execute(sql)
      tool_id = cursor.lastrowid
    else:
      tool_id = info_tool['id']
    return tool_id

  return affair(add)

def add_log(
  project_id,
  tool_id,
  project_stage = None,
):
  if not project_id or not tool_id:
    raise ValueError('Please pass correct parameters!')

  def add(cursor):
    sql = sqls.sql_find_log_one(tool_id, project_id)
    cursor.execute(sql)
    info_log = cursor.fetchone()
    if info_log:
      log_id = info_log['id']
      count = info_log['count']
      sql = sqls.sql_update_log(log_id, count + 1)
      cursor.execute(sql)
      isAffect = cursor.rowcount
    else:
      sql = sqls.sql_add_log(
        project_id = project_id,
        tool_id = tool_id,
        project_stage = project_stage
      )
      cursor.execute(sql)
      isAffect = cursor.rowcount
    return isAffect

  return affair(add)

if __name__ == '__main__':
  from random import randrange
  project_uuid = add_project(project_name = f'hp-project-{randrange(1, 1000)}', project_type = 'hybrid')
  print(project_uuid)
  tool_id = add_tool(tool_name = f'hupu-cli', tool_version = f'0.0.{randrange(1, 100)}')
  print(tool_id)