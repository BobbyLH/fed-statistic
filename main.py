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
uuid = 'f9958eac-ad8f-41d4-9647-b5c22a5b2ead'
# track
@app.route('/track', methods=['GET', 'POST'])
def track():
  name = request.args.get('name', 'world')
  if request.method == 'POST':
    return '{} Hello'.format(escape(name))
  else:
    return f'Hello, {escape(name)}'

@app.route('/detail/<dimension>')
def detail(dimension):
  return 'dimension %s' % escape(dimension)

with app.test_request_context():
    print(url_for('track'))
    print(url_for('track', next='/'))
    print(url_for('detail', dimension='list'))