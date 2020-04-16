import mysql.connector as mysql
import sqls
from affair import affair
from add import add_tool, add_log

def track(
  tool_name,
  tool_version,
  project_name = None,
  project_uuid = None,
  info = None
):
  def make_track(cursor):
    # 校验项目是否注册
    sql = None
    if project_uuid:
      sql = sqls.sql_find_project(project_uuid)
    elif project_name:
      sql = sqls.sql_find_project_unsafe(project_name)
    else:
      return '项目未注册'
    cursor.execute(sql)
    info_project = cursor.fetchone()

    if not info_project:
      return '项目未注册'
    else:
      project_id = info_project['id']
      # 处理工具信息
      tool_id = add_tool(tool_name, tool_version)

      # 记录日志
      return add_log(
        project_id,
        tool_id,
        info
      )

  return affair(make_track)

if __name__ == '__main__':
  res = track(project_uuid = '9419c3c3-79e3-41a0-a924-f0f8314a66fc', tool_name = 'hupu-cli', tool_version = '0.0.4')
  print(res)