import sys
sys.path.append('./source/model')
sys.path.append('./source/utils')
from read import read_tool, read_log_tool
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
    return make_res('成功', info_tools)
  else:
    return make_res('未找到工具信息')

if __name__ == '__main__':
  res = detail_log(
    tool_name = 'hupu-cli'
  )
  print(res)