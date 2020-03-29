import sys
sys.path.append('./source/config')
from ret import ret_list, make_res
from affair import affair
import sqls

def detail(
  name,
  version = None
):
  res = {}
  def get_detail(cursor):

    if version:
      sql = sqls.sql_find_tool_version(name, version)
      cursor.execute(sql)
      info_tool = cursor.fetchone()
      if info_tool:
        sql = sqls.sql_find_log_tool_version(info_tool['id'])
        cursor.execute(sql)
        info_log_tool = cursor.fetchone()
        res = make_res('成功', info_log_tool)
        return res
      else:
        res = make_res('未找到工具信息')
        return res
    else:
      sql = sqls.sql_find_tool(name)
      cursor.execute(sql)
      info_tool = cursor.fetchmany()
