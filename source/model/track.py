import mysql.connector as mysql
import sqls
from affair import affair

def track(
  project_name = 1,
  project_type = 1,
  project_id = 1,
  project_stage = 1,
  tool_name = 1,
  tool_version = 1,
  tool_id = 1
):
  def make_track(cursor):
    sql = sqls.sql_find_tool(tool_id)
    cursor.execute(sql)
    print(cursor.stored_results())
    for row in cursor:
      print(row)

  affair(make_track)

track(tool_id = 2)