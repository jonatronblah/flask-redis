import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd






def create_dashboard(server):
    

    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
        ]  
    )

    df = pd.DataFrame({"x": [1, 2, 3], "SF": [4, 1, 2], "Montreal": [2, 4, 5]})

    fig = px.bar(df, x="x", y=["SF", "Montreal"], barmode="group")


    

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
    
    #init_callbacks(dash_app)
   
    return dash_app.server
    
  
#for callbacks in app context

def init_callbacks(dash_app):
    @dash_app.callback(
    Output('example-graph', 'figure'),
    [Input('submit-val', 'n_clicks')]
    )
    def update_graph(n_clicks):
        df = pd.DataFrame({"x": [1, 2, 3], "San Fran": [4, 1, 2], "Montreal": [2, 4, 5]})

        fig = px.bar(df, x="x", y=["San Fran", "Montreal"], barmode="group")
        return fig