# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

def home(name = __name__, server = True, routes_pathname_prefix = '/'):

	external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

	app = dash.Dash(
		name,
		external_stylesheets=external_stylesheets,
		server=server,
		routes_pathname_prefix=routes_pathname_prefix
	)

	colors = {
		'background': '#111111',
		'text': '#7FDBFF'
	}

	app.layout = html.Div(
		style={
			'backgroundColor': colors['background']
		},
		children=[
			html.H1(
				children='虎扑前端工具数据分析',
				style={
					'textAlign': 'center',
					'color': colors['text']
				}
			),

			html.Div(
				children='''
					Dash: A web application framework for Python.
				''',
				style={
					'textAlign': 'center',
					'color': colors['text']
				}
			),

			dcc.Graph(
				id='example-graph',
				figure={
					'data': [
						{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
						{'x': [1, 2, 3], 'y': [2, 4, 5],
								'type': 'bar', 'name': u'Montréal'},
					],
					'layout': {
						'title': 'Dash Data Visualization',
						'plot_bgcolor': colors['background'],
						'paper_bgcolor': colors['background'],
						'font': {
							'color': colors['text']
						}
					}
				}
			)
		]
	)

	return app

if __name__ == '__main__':
	app = home()
	app.run_server(debug=True)
