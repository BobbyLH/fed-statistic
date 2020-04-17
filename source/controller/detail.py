import sys
sys.path.append('./source/model')
sys.path.append('./source/utils')
from read import read_tool
from ret import make_res

def detail(
  tool_name,
  tool_version = None
):
  info_tools = read_tool(tool_name, tool_version)
  if info_tools:
    return make_res('成功', info_tools)
  else:
    return make_res('未找到工具信息')

if __name__ == '__main__':
  res = detail(
    tool_name = 'hupu-cli',
    tool_version = '0.0.39'
  )
  print(res)