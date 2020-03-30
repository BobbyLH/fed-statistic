import sys
sys.path.append('./source')
from model.detail import get_detail_tool
from utils.ret import make_res

def detail(
  type,
  tool_name,
  tool_version = None
):
  if type == 'tool':
    info_tools = get_detail_tool(tool_name, tool_version)
    if info_tools:
      return make_res('成功', info_tools)
    else:
      return make_res('未找到工具信息')
