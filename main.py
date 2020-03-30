from flask import Flask, escape, request, url_for
from markupsafe import escape
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

publickey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCKKqFcEpUwEJEJj1b434F5NkGRhKGMHCgeOl0L+RMNf4G6w2JLa8v6HXJZRdSA/sr5NGrHg9jXyudl+LoDKM1rHP90S8/S9ZW7eg5q6Upp5PcAGMDeQwFarlKMFwphvmJKHmGgDXrliLDk0nsVw6duVl/RGJPkL/KQ29bEHrkxIwIDAQAB'

# add
@app.route('/add/<type>', methods=['POST'])
def fn_add():
  name = request.args.get('name', 'world')
  if request.method == 'POST':
    return '{} Hello'.format(escape(name))
  else:
    return f'Hello, {escape(name)}'

# track
@app.route('/track', methods=['POST'])
def fn_track():
  name = request.args.get('name', 'world')
  if request.method == 'POST':
    return '{} Hello'.format(escape(name))
  else:
    return f'Hello, {escape(name)}'

# detial
@app.route('/detail/<dimension>', methods=['GET'])
def fn_detail(dimension):
  return 'dimension %s' % escape(dimension)

with app.test_request_context():
    print(url_for('track'))
    print(url_for('track', next='/'))
    print(url_for('detail', dimension='list'))