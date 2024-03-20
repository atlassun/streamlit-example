# importer la librairie dash pour la visualisation
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

app.layout = html.Div(children=[
			html.H1('Démo dash'), 
			dcc.Graph(id='example',
					figure ={
						'data': [
							{'x': [1,2,3,4,5], 'y':[10,20,30,40,50], 'type':'line','name':'Age'},
							{'x': [1,2,3,4,5], 'y':[160,180,160,175,150], 'type':'bar','name':'Hauteur Heights'},
							],
						'layout':{
							'title':'Basic DashBoard'
						}
						
					
					
					})
			
			])



if __name__ == '__main__':
	app.run_server(debug=True)

