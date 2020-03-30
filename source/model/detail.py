import sys
sys.path.append('./source/config')
from ret import ret_list, make_res
from affair import affair
import sqls

def detail(
  name,
  version = None
):
  def get_detail(cursor):

    if version:
      sql = sqls.sql_find_tool_version(name, version)
      cursor.execute(sql)
      info_tool = cursor.fetchone()
      if info_tool:
        sql = sqls.sql_find_log_tool_version(info_tool['id'])
        cursor.execute(sql)
        info_log_tool = cursor.fetchone()
        return make_res('成功', info_log_tool)
      else:
        return make_res('未找到工具信息')
    else:
      sql = sqls.sql_find_tool(name)
      cursor.execute(sql)
      info_tools = cursor.fetchall()
      if info_tools:
        tool_ids = list()
        for info_tool in info_tools:
          tool_ids.append(info_tool['id'])
        sql = sqls.sql_find_log_tool(tool_ids)
        cursor.execute(sql)
        info_logs_tool = cursor.fetchall()
        return make_res('成功', info_logs_tool)
      else:
        return make_res('未找到工具信息')

  return affair(get_detail)

if __name__ == '__main__':
  res = detail(name = 'hupu-cli')
  print(res)