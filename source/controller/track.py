import sys
import json
sys.path.append('./source/model')
sys.path.append('./source/utils')
from create import create_track
from ret import make_res

def track(
  tool_name,
  tool_version,
  project_name = None,
  project_uuid = None,
  info = None
):
  result = create_track(
    tool_name,
    tool_version,
    project_name,
    project_uuid,
    info
  )
  if result == '项目未注册':
    return make_res(result)
  elif not result:
    return make_res('未能成功入库，请重试')

  return make_res()

if __name__ == '__main__':
  info = {
    'stage': 'init',
    'typescript': True,
    'eslint': True,
    'stylelint': True,
    'commitlint': False,
    'monitor': False
  }
  info_json = json.dumps(info)
  res = track(
    tool_name = 'hupu-cli',
    tool_version = '0.0.21',
    project_name = 'hp-project-44',
    info = info_json
  )
  print(res)