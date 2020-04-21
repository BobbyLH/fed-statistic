from flask import request, has_request_context
import dash
import dash_core_components as dcc
import dash_html_components as html

def generate_table(dataframe, max_rows):
  return html.Table([
    html.Thead(
      html.Tr([html.Th(col) for col in dataframe.columns])
    ),
    html.Tbody([
      html.Tr([
        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
      ]) for i in range(min(len(dataframe), max_rows))
    ])
  ],
  style={
    'textAlign': 'center',
    'margin': 'auto'
  })

def table(
  get_data,
  max_rows = 30,
  title = '前端工具',
  name = __name__,
  server = True,
  routes_pathname_prefix = '/table/'
):
  def serve_layout():
    if has_request_context() and request.method == 'GET':
      dataframe = get_data()
      return html.Div(children=[
        html.H4(children=title),
        generate_table(dataframe, max_rows)
      ],
      style={
        'textAlign': 'center',
        'margin': '10vh auto 0',
        'max-height': '70vh',
        'overflow': 'auto'
      })
    return html.Div([
      dcc.Location(id='url', refresh=False),
      html.Div(id='page-content')
    ])

  app = dash.Dash(
    name,
    server=server,
    routes_pathname_prefix=routes_pathname_prefix
  )
  app.layout = serve_layout

  return app

if __name__ == '__main__':
  import pandas as pd
  data = {'col1': [1, 2], 'col2': [3, 4]}
  df = pd.DataFrame(data)
  app = table(lambda : df)
  app.run_server(debug=True)