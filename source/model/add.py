from uuid import uuid4
from affair import affair
import sqls

def add_project(
  project_name = None,
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

  sql = sqls.sql_add_tool(tool_name, tool_version)    
  affair(lambda cursor: cursor.execute(sql))

def add_log(
  project_name = None,
  project_id = None,
  project_stage = None,
  tool_name = None,
  tool_id = None
):
  if not project_name or not project_id or not tool_name or not tool_id:
    raise ValueError('Please pass correct parameters!')

  sql = sqls.sql_add_log(
    project_name = project_name,
    project_id = project_id,
    project_stage = project_stage,
    tool_name = tool_name,
    tool_id = tool_id
  )
  affair(lambda cursor: cursor.execute(sql))
