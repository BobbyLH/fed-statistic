import sys
sys.path.append('./source')
from model.add import add_project, add_tool
from utils.ret import make_res

def add(
  type,
  project_name,
  project_type = None,
  tool_name = None,
  tool_version = None
):
  if type == 'project':
    uuid = add_project(project_name, project_type)
    return make_res('成功', { 'id': uuid })
  elif type == 'tool':
    tool_id = add_tool(tool_name, tool_version)
    return make_res('成功', { 'id': tool_id })
  elif type == 'log':
    return make_res('不允许直接添加日志信息')
  else:
    return make_res('参数错误')
