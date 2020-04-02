import sys
sys.path.append('./source')
from model.track import make_track
from utils.ret import make_res

def track(
  project_uuid,
  tool_name,
  tool_version,
  project_stage = None
):
  def make_track(cursor):
    # 校验项目是否注册
    sql = sqls.sql_find_project(project_uuid)
    cursor.execute(sql)
    info_project = cursor.fetchone()

    if not info_project:
      return make_res('项目未注册')
    else:
      project_id = info_project['id']
      # 处理工具信息
      tool_id = add_tool(tool_name, tool_version)

      # 记录日志
      isAffect = add_log(
        project_id,
        tool_id,
        project_stage
      )

      if not isAffect:
        return make_res('未能成功入库，请重试')

      return make_res() 

  return affair(make_track)
