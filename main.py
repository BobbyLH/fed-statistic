from flask import Flask, escape, request, url_for, redirect
from markupsafe import escape
import sys
import json
sys.path.append('./source/')
from view.home import home
from view.table import table
import controller.add as c_add
import controller.detail as c_detail
import controller.track as c_track
import pandas as pd
import numpy as np
from datetime import datetime

app_name = 'hp-fed-statistic'
server = Flask(app_name)

# view - home
home(
  app_name,
  server = server,
  routes_pathname_prefix = '/'
)

# view - list - hupu-cli
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
        lst.append(loc)
      row.append(lst)
    return pd.DataFrame(np.array(row), columns=col)
  return None

table(
  dataframe = generate_df_list('hupu-cli'),
  name = app_name,
  server = server,
  title=f'虎扑前端 hupu-cli 版本列表',
  routes_pathname_prefix = '/list/hupu-cli/'
)

# view - detail - hupu-cli
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
  return None

table(
  dataframe = generate_df_detail('hupu-cli'),
  name = app_name,
  server = server,
  title=f'虎扑前端 hupu-cli 使用详情',
  routes_pathname_prefix = '/detail/hupu-cli/'
)

# view - list - project
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
        lst.append(loc)
      row.append(lst)
    return pd.DataFrame(np.array(row), columns=col)
  return None

table(
  dataframe = generate_df_list_project('hupu-cli'),
  name = app_name,
  server = server,
  title=f'hupu-cli 应用项目列表',
  routes_pathname_prefix = '/list/project/'
)

# add
@server.route('/add', methods=['POST'])
def add():
  name = request.args.get('name', 'world')
  if request.method == 'POST':
    return '{} Hello'.format(escape(name))
  else:
    return f'Hello, {escape(name)}'

# track
@server.route('/track', methods=['POST'])
def track():
  name = request.args.get('name', 'world')
  if request.method == 'POST':
    return '{} Hello'.format(escape(name))
  else:
    return f'Hello, {escape(name)}'