import sys
sys.path.append('./source/model')
sys.path.append('./source/utils')
from delete import delete_project
from ret import make_res

def remove(
  type,
  project_uuid
):
  if (type == 'project'):
    return make_res(delete_project(project_uuid))
  else:
    return make_res('暂不支持该服务')

if __name__ == '__main__':
  res = remove(
    'project',
    '8446f9b0-8bd3-4fd4-8215-0ff609a5e7b31'
  )
  print(res)