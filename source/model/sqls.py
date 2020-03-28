import time

# table-project-sql
def sql_add_project(project_name, project_type):
  ts = int(time.time())
  return str('INSERT INTO project(name, type, createAt) VALUES ("{}", "{}", {})').format(project_name, project_type, ts)

def sql_find_project(project_id):
  return 'SELECT * FROM project WHERE id=%d' % (project_id)

def sql_find_all_project():
  return 'SELECT * FROM project'

# table-tool-sql
def sql_add_tool(tool_name, tool_version):
  return f'INSERT INTO tool(name, version) VALUES ("{tool_name}", "{tool_version}")'

def sql_find_tool(tool_name, tool_version):
  return 'SELECT * FROM tool WHERE name="%s" AND version="%s"' % (tool_name, tool_version)

def sql_find_all_tool():
  return 'SELECT * FROM tool'

# table-log-sql
def sql_add_log(project_id, tool_id, project_stage = None):
  ts = int(time.time())
  if not project_stage:
    return f'INSERT INTO log(project_id, tool_id, count, createAt) VALUES ({project_id}, {tool_id}, 1, {ts})'

  return f'INSERT INTO log(project_id, project_stage, tool_id, count, createAt) VALUES ({project_id}, "{project_stage}", {tool_id}, 1, {ts})'

def sql_find_log(project_id, tool_id):
  return f'SELECT * FROM log WHERE project_id={project_id} AND tool_id={tool_id}'

def sql_update_log(log_id, count):
  if not log_id or not count:
    raise ValueError('lack critical parameters')
  return f'UPDATE log SET count={count} WHERE id={log_id}'
