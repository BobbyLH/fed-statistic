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
  dataframe,
  max_rows = 30,
  title = '前端工具',
  name = __name__,
  server = True,
  routes_pathname_prefix = '/table/'
):
  app = dash.Dash(
    name,
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'],
    server=server,
    routes_pathname_prefix=routes_pathname_prefix
  )
  app.layout = html.Div(children=[
    html.H4(children=title),
    generate_table(dataframe, max_rows)
  ],
  style={
    'textAlign': 'center',
    'margin': '10vh auto 0',
    'max-height': '70vh',
    'overflow': 'auto'
  })

  return app

if __name__ == '__main__':
  import pandas as pd
  data = {'col1': [1, 2], 'col2': [3, 4]}
  df = pd.DataFrame(data)
  app = table(df)
  app.run_server(debug=True)