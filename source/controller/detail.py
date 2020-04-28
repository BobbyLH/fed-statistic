import sys
sys.path.append('./source/model')
sys.path.append('./source/utils')
from read import read_tool, read_project, read_log_tool
from ret import make_res

def detail_log(
  tool_name,
  tool_version = None
):
  info_tools = read_log_tool(tool_name, tool_version)
  if info_tools:
    return make_res('成功', info_tools)
  else:
    return make_res('未找到日志信息')

def detail_tool(
  tool_name,
  tool_version = None
):
  info_tools = read_tool(tool_name, tool_version)
  if info_tools:
    info_tools.sort(
      key = lambda val: val['createAt'],
      reverse = True
    )
    return make_res('成功', info_tools)
  else:
    return make_res('未找到工具信息')

def detail_project(
  tool_name,
  tool_version = None
):
  info_projects = []
  info_tools = read_log_tool(tool_name, tool_version)
  if info_tools:
    for item in info_tools:
      project_id = item['project_id']
      if len(info_projects) > 0:
        for ind, info in enumerate(info_projects):
          if info and info['id'] == project_id:
            break
          if ind + 1 == len(info_projects):
            info_projects.append(read_project(project_id = project_id))
      else:
        info_projects.append(read_project(project_id = project_id))
    info_projects.sort(
      key = lambda val: val['createAt'],
      reverse = True
    )
    return make_res('成功', info_projects)
  return make_res('未找到工具信息')

if __name__ == '__main__':
  res = detail_project(
    tool_name = 'hupu-cli'
  )
  print(res)