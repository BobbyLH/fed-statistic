import sys
sys.path.append('./source/model')
sys.path.append('./source/utils')
from create import create_project, create_tool
from ret import make_res

def add(
  type,
  project_name = None,
  project_type = None,
  tool_name = None,
  tool_version = None
):
  if type == 'project':
    uuid = create_project(project_name, project_type)
    return make_res('成功', { 'id': uuid })
  elif type == 'tool':
    tool_id = create_tool(tool_name, tool_version)
    return make_res('成功', { 'id': tool_id })
  elif type == 'log':
    return make_res('不允许直接添加日志信息')
  else:
    return make_res('参数错误')

if __name__ == '__main__':
  from random import randrange
  res1 = add(
    type='project',
    project_name = f'hp-project-{randrange(1, 1000)}',
    project_type = 'hybrid'
  )
  print(res1)
  res2 = add(
    type='tool',
    tool_name = f'hupu-cli',
    tool_version = f'0.0.{randrange(1, 100)}'
  )
  print(res2)