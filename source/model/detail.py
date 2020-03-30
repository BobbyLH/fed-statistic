from affair import affair
import sqls

def get_detail_tool(
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
        return cursor.fetchall()
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
        return cursor.fetchall()

  return affair(get_detail)

if __name__ == '__main__':
  res = get_detail_tool(name = 'hupu-cli')
  print(res)