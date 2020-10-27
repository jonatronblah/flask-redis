import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests
import json
from redistimeseries.client import Client





def create_dashboard(server):
    

    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
        ]  
    )
    
    

    fig = px.line()


    

    dash_app.layout = html.Div(children=[
        html.H1(children='title'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
        html.Button('Submit', id='submit-val', n_clicks=0)
    ])
    
    init_callbacks(dash_app)
   
    return dash_app.server
    
  
#for callbacks in app context

def init_callbacks(dash_app):
    @dash_app.callback(
    Output('example-graph', 'figure'),
    [Input('submit-val', 'n_clicks')]
    )
    def update_graph(n_clicks):
        client = Client(host='redistimeseries', port=6379, db=0, decode_responses=True)
        raddata = client.range('rad_avg_min', 0, -1)
        tempdata = client.range('temp_avg_min', 0, -1)
        
        radlist = []
        for i in raddata:
            radlist.append({'timestamp': str(i[0]), 'radiation':str(i[1])})
        
        templist = []
        for i in tempdata:
            templist.append({'timestamp': str(i[0]), 'temperature':str(i[1])})
        
        r = {'tempdata':templist, 'raddata':radlist}
        
        df_t = pd.DataFrame(r['tempdata'])
        
        df_r = pd.DataFrame(r['raddata'])
        
        df = df_t.merge(df_r)
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

        fig = px.line(df, x = 'timestamp', y = ['temperature', 'radiation'])
        return fig
