import sys
import json
sys.path.append('./source')
from model.create import create_track
from utils.ret import make_res

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
  info = json.dumps(info)
  print(info)
  # track(
  #   'hupu-cli',
  #   '0.0.39',
  #   'hp-project-393',
  #   ''
  # )