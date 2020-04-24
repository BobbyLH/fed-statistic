from uuid import UUID
from routine import routine
from sqls import (sql_delete_project, 
sql_delete_log, 
sql_find_log_id_join_project,
sql_find_project
)

def delete_project(
  project_uuid
):
  if not project_uuid:
    return '参数错误'
  def del_project(cursor):
    try:
      uuid = UUID(project_uuid)
    except:
      uuid = project_uuid
    sql = sql_find_project(project_uuid = uuid)
    cursor.execute(sql)
    info_project = cursor.fetchone()
    if not info_project:
      return '项目未注册'

    sql = sql_find_log_id_join_project(uuid)
    cursor.execute(sql)
    ids = cursor.fetchall()
    ids_str = ''
    for item in ids:
      i = item['id']
      ids_str += f'{i},'
    if not ids_str == '':
      ids_str = ids_str[:-1]
      sql = sql_delete_log(ids_str)
      cursor.execute(sql)

    sql = sql_delete_project(uuid)
    cursor.execute(sql)
    isAffect = cursor.rowcount
    if not bool(isAffect):
      return '项目删除失败'

    return '成功'

  return routine(del_project)