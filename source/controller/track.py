import sys
sys.path.append('./source')
from model.track import track
from utils.ret import make_res

def controller_track(
  tool_name,
  tool_version,
  project_name = None,
  project_uuid = None,
  project_stage = None
):
  result = track(
    tool_name,
    tool_version,
    project_name,
    project_uuid,
    project_stage
  )
  if result == '项目未注册':
    return make_res(result)
  elif not result:
    return make_res('未能成功入库，请重试')

  return make_res()
