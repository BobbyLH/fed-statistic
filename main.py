from flask import Flask, escape, request, url_for, redirect, Response
from markupsafe import escape
import sys
import json
sys.path.append('./source/')
from view.home import home
from view.table import table
import controller.add as c_add
import controller.detail as c_detail
import controller.track as c_track
import controller.remove as c_remove
from utils.ret import make_res
import pandas as pd
import numpy as np
from datetime import datetime
from uuid import UUID

app_name = 'hp-fed-statistic'
server = Flask(app_name)

df_default = pd.DataFrame({'数据读取失败': ['测试数据1', '测试数据2'], '请检查你的数据库连接': ['测试数据3', '测试数据4']})

def generate_df_list(tool_name):
  res = c_detail.detail_tool(tool_name)
  if res['ret'] == 0:
    data = res['data']
    col = [key for key in data[0] if not key == 'id']
    col.insert(0, '序号')
    row = []
    for ind, item in enumerate(data):
      lst = [ind + 1]
      for key in col:
        if key == '序号':
          continue
        loc = item[key]
        if (key == 'createAt'):
          lst.append(str(datetime.fromtimestamp(loc)))
          continue
        if not loc:
          loc = '-'
        lst.append(loc)
      row.append(lst)
    return pd.DataFrame(np.array(row), columns=col)
  return df_default

def generate_df_detail(tool_name):
  res = c_detail.detail_log(tool_name)
  if res['ret'] == 0:
    data = res['data']
    total = len(data)
    col = ['init', 'dev', 'new', 'build', 'release', 'total']
    row = [0, 0, 0, 0, 0, total]
    for item in data:
      info = item['info']
      if info:
        info = json.loads(item['info'])
        stage = info['stage']
        ind = col.index(stage)
        origin = row[ind]
        row[ind] = origin + 1
    return pd.DataFrame(np.array([row]), columns=col)
  return df_default

def generate_df_list_project(tool_name):
  res = c_detail.detail_project(tool_name)
  if res['ret'] == 0:
    data = res['data']
    col = [key for key in data[0] if not key == 'id' and not key == 'uuid']
    col.insert(0, '序号')
    row = []
    for ind, item in enumerate(data):
      lst = [ind + 1]
      for key in col:
        if key == '序号':
          continue
        loc = item[key]
        if (key == 'createAt'):
          lst.append(str(datetime.fromtimestamp(loc)))
          continue
        if not loc:
          loc = '-'
        lst.append(loc)
      row.append(lst)
    return pd.DataFrame(np.array(row), columns=col)
  return df_default

view_dict = {
  '/list/hupu-cli/': {
    'title': '虎扑前端 hupu-cli 版本列表',
    'get_data': lambda : generate_df_list('hupu-cli')
  },
  '/list/project/': {
    'title': 'hupu-cli 应用项目列表',
    'get_data': lambda : generate_df_list_project('hupu-cli')
  },
  '/detail/hupu-cli/': {
    'title': '虎扑前端 hupu-cli 使用详情',
    'get_data': lambda : generate_df_detail('hupu-cli')
  },
}

# view - home
home(
  app_name,
  server = server,
  routes_pathname_prefix = '/'
)

# view - tables
for route in view_dict:
  view = view_dict[route]
  table(
    get_data = view['get_data'],
    name = app_name,
    server = server,
    title = view['title'],
    routes_pathname_prefix = route
  )

def do_response (data):
  if type(data) is str:
    data = make_res(data)
  return Response(json.dumps(data, ensure_ascii = False, cls=UUIDEncoder), content_type='application/json; charset=utf-8')

# add
class UUIDEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, UUID):
      return obj.hex
    return json.JSONEncoder.default(self, obj)

@server.route('/add', methods=['POST'])
def add():
  if request.method != 'POST':
    return do_response('请求方法不匹配')

  content_type = request.content_type
  if not content_type == 'application/json':
    return do_response('请传入正确的数据格式')

  data = json.loads(request.data)
  return do_response(c_add.add(**data))

# track
@server.route('/track', methods=['POST'])
def track():
  if request.method != 'POST':
    return do_response('请求方法不匹配')

  content_type = request.content_type
  if not content_type == 'application/json':
    return do_response('请传入正确的数据格式')

  data = json.loads(request.data)
  return do_response(c_track.track(**data))

# remove
@server.route('/remove', methods=['DELETE'])
def remove():
  if request.method != 'DELETE':
    return do_response('请求方法不匹配')

  content_type = request.content_type
  if not content_type == 'application/json':
    return do_response('请传入正确的数据格式')

  data = json.loads(request.data)
  return do_response(c_remove.remove(**data))