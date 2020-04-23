import sys
sys.path.append('./source/model')
sys.path.append('./source/utils')
from create import create_project, create_tool
from ret import make_res

def add(
  type,
  **kwargs
):
  if type == 'project':
    project_name = kwargs['project_name']
    project_type = kwargs['project_type']
    author = kwargs['author']
    try:
      uuid = create_project(project_name, project_type, author)

      if not uuid:
        return make_res('未能成功入库，请重试')

      return make_res('成功', { 'id': uuid })
    except ValueError as e:
      return make_res(e)
  elif type == 'tool':
    tool_name = kwargs['tool_name']
    tool_version = kwargs['tool_version']
    try:
      tool_id = create_tool(tool_name, tool_version)

      if not tool_id:
        return make_res('未能成功入库，请重试')

      return make_res('成功', { 'id': tool_id })
    except ValueError as e:
      return make_res(e)
  elif type == 'log':
    return make_res('不允许直接添加日志信息')
  else:
    return make_res('参数错误')

if __name__ == '__main__':
  from random import randrange
  data1 = {
    'project_name': f'hp-project-{randrange(1, 1000)}',
    'project_type': 'hybrid'
  }
  res1 = add(
    type='project',
    **data1
  )
  print(res1)
  data2 = {
    'tool_name': f'hupu-cli',
    'tool_version': f'0.0.{randrange(1, 100)}'
  }
  res2 = add(
    type='tool',
    **data2
  )
  print(res2)