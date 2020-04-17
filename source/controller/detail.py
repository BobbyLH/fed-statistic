import sys
sys.path.append('./source')
from model.read import read_tool
from utils.ret import make_res

def detail(
  tool_name,
  tool_version = None
):
  info_tools = read_tool(tool_name, tool_version)
  if info_tools:
    return make_res('成功', info_tools)
  else:
    return make_res('未找到工具信息')
