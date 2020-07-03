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
  project_version = None,
  project_type = None,
  info = None
):
  infoDict = info if info else dict()
  infoDict['project_version'] = project_version
  infoDict['project_type'] = project_type
  result = create_track(
    tool_name,
    tool_version,
    project_name,
    project_uuid,
    info = json.dumps(infoDict)
  )
  if result:
    return make_res(result)
  else:
    return make_res('未能成功入库，请重试')

if __name__ == '__main__':
  info = {
    'stage': 'build',
    'typescript': True,
    'eslint': True,
    'stylelint': True,
    'commitlint': False,
    'monitor': False
  }
  res = track(
    tool_name = 'hupu-cli',
    tool_version = '0.0.17',
    project_name = 'hp-project-381',
    info = info
  )
  print(res)