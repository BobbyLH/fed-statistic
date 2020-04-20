# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

def home(name = __name__, server = True, routes_pathname_prefix = '/'):


	app = dash.Dash(
		name,
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
				children='虎扑前端CLI脚手架数据分析',
				style={
					'textAlign': 'center',
					'color': colors['text']
				}
			),

			html.A(
				children='''
					GitLab 地址
				''',
				href='http://gitlab.hupu.com/foundation-frontend/hupu-cli',
				target='_blank',
				style={
					'display': 'block',
					'textAlign': 'center',
					'color': 'gold',
					'fontSize': '16px',
					'margin': '20px auto'
				}
			),

			html.Ul(
				children=[
					html.Li(
						html.A(
							children='hupu-cli 版本列表',
							href='/list/hupu-cli',
							style={
								'color': 'white'
							}
						)
					),
					html.Li(
						html.A(
							children='hupu-cli 使用情况',
							href='/detail/hupu-cli',
							style={
								'color': 'white'
							}
						)
					),
					html.Li(
						html.A(
							children='hupu-cli 接入项目',
							href='/list/project',
							style={
								'color': 'white'
							}
						)
					)
				],
				style={
					'listStyleType': 'cjk-ideographic',
					'textAlign': 'center',
					'fontSize': '20px',
					'color': 'white'
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
						'title': 'Powered by Dash And Flask',
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
