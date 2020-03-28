import mysql.connector as mysql
import sqls
from affair import affair

def track(
  project_id,
  tool_name,
  tool_version,
  project_stage = None
):
  res = {}
  def make_track(cursor):
    # 校验项目是否注册
    sql = sqls.sql_find_project(project_id)
    cursor.execute(sql)
    info_project = cursor.fetchone()
    if not info_project:
      res['ret'] = 40100
      res['msg'] = '项目未注册'
      return res
    else:
      # 处理工具信息
      sql = sqls.sql_find_tool(tool_name, tool_version)
      cursor.execute(sql)
      info_tool = cursor.fetchone()
      if not info_tool:
        sql = sqls.sql_add_tool(tool_name, tool_version)
        cursor.execute(sql)
        tool_id = cursor.lastrowid
      else:
        tool_id = info_tool['id']

      # 记录日志
      sql = sqls.sql_find_log(
        project_id,
        tool_id
      )
      cursor.execute(sql)
      info_log = cursor.fetchone()
      if info_log:
        log_id = info_log['id']
        count = info_log['count']
        sql = sqls.sql_update_log(log_id, count + 1)
        cursor.execute(sql)
        isAffect = cursor.rowcount
      else:
        sql = sqls.sql_add_log(
          project_id,
          tool_id,
          project_stage
        )
        cursor.execute(sql)
        isAffect = cursor.rowcount

      # 输出结果
      if isAffect:
        res['msg'] = '成功'
        res['ret'] = 0
      else:
        res['msg'] = '未能成功入库，请重试'
        res['ret'] = 40101

  affair(make_track)
  return res

if __name__ == '__main__':
  res = track(project_id = 3, tool_name = 'hupu-cli', tool_version = '0.0.51')
  print(res)