from flask import Flask, escape, request
import sys
sys.path.append('./source/')
from view.home import home

app_name = 'hp-fed-statistic'
app = Flask(app_name)

# view - home
home(
  app_name,
  server = app,
  routes_pathname_prefix = '/'
)

# track
@app.route('/track')
def track():
  name = request.args.get('name', 'world')
  return f'Hello, {escape(name)}'

@app.route('/detail-list')
def detail_list():
  name = request.args.get('name', 'world')
  return f'Hello, {escape(name)}'

@app.route('/detail-item')
def detail_item():
  name = request.args.get('name', 'world')
  return f'Hello, {escape(name)}'