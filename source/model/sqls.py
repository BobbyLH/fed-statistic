import time

# table-project-sql
def sql_add_project(project_name, project_type, project_uuid):
  if not project_name or not project_type or not project_uuid:
    raise ValueError('lack critical parameters')
  ts = int(time.time() * 1000)
  return str('INSERT INTO project(name, type, uuid, createAt) VALUES ("{}", "{}", "{}", {})').format(project_name, project_type, project_uuid, ts)

def sql_find_project_unsafe(project_name):
  if not project_name:
    raise ValueError('lack critical parameters')
  return 'SELECT * FROM project WHERE name="%s"' % (project_name)

def sql_find_project(
  project_uuid = None,
  project_id = None
):
  if not project_uuid and not project_id:
    raise ValueError('lack critical parameters')
  if project_uuid:
    return 'SELECT * FROM project WHERE uuid="%s"' % (project_uuid)
  return 'SELECT * FROM project WHERE id="%s"' % (project_id)

def sql_find_all_project():
  return 'SELECT * FROM project'

# table-tool-sql
def sql_add_tool(tool_name, tool_version):
  if not tool_name or not tool_version:
    raise ValueError('lack critical parameters')
  ts = int(time.time() * 1000)
  return f'INSERT INTO tool(name, version, createAt) VALUES ("{tool_name}", "{tool_version}", {ts})'

def sql_find_tool(tool_name):
  if not tool_name:
    raise ValueError('lack critical parameters')
  return 'SELECT * FROM tool WHERE name="%s"' % (tool_name)

def sql_find_tool_version(tool_name, tool_version):
  return 'SELECT * FROM tool WHERE name="%s" AND version="%s"' % (tool_name, tool_version)

def sql_find_all_tool():
  return 'SELECT * FROM tool'

# table-log-sql
def sql_add_log(project_id, tool_id, info = None):
  if not info:
    return f'INSERT INTO log (project_id, tool_id) VALUES ({project_id}, {tool_id})'
  return f'INSERT INTO log (project_id, tool_id, info) VALUES ({project_id}, {tool_id}, \'{info}\')'

def sql_find_log_tools(tool_ids):
  if not tool_ids or len(tool_ids) == 0:
    raise ValueError('lack critical parameters')
  condition_ids = ''
  for i in range(len(tool_ids)):
    tool_id = tool_ids[i]
    condition_str = f'tool_id={tool_id} OR '
    if i == len(tool_ids) - 1:
      condition_str = f'tool_id={tool_id}'
    condition_ids += condition_str
  return f'SELECT * FROM log WHERE {condition_ids}'

def sql_find_log_tool(tool_id):
  if not tool_id:
    raise ValueError('lack critical parameters')
  return f'SELECT * FROM log WHERE tool_id={tool_id}'

def sql_find_log_one(tool_id, project_id):
  if not tool_id or not project_id:
    raise ValueError('lack critical parameters')
  return f'SELECT * FROM log WHERE tool_id={tool_id} AND project_id={project_id}'

def sql_update_log(log_id, info):
  if not log_id or not info:
    raise ValueError('lack critical parameters')
  return f'UPDATE log SET info={info} WHERE id={log_id}'
