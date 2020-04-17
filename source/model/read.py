from affair import affair
from sqls import sql_find_tool_version, sql_find_log_tool, sql_find_tool, sql_find_log_tools

def read_tool(
  name,
  version = None
):
  def get_detail_tool(cursor):

    if version:
      sql = sql_find_tool_version(name, version)
      cursor.execute(sql)
      info_tool = cursor.fetchone()
      if info_tool:
        sql = sql_find_log_tool(info_tool['id'])
        cursor.execute(sql)
        return cursor.fetchall()
    else:
      sql = sql_find_tool(name)
      cursor.execute(sql)
      info_tools = cursor.fetchall()
      if info_tools:
        tool_ids = list()
        for info_tool in info_tools:
          tool_ids.append(info_tool['id'])
        sql = sql_find_log_tools(tool_ids)
        cursor.execute(sql)
        return cursor.fetchall()

  return get_detail_tool(get_detail)

if __name__ == '__main__':
  res = read_tool(name = 'hupu-cli')
  print(res)