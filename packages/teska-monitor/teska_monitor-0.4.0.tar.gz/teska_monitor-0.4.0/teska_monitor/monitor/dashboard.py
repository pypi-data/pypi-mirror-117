# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import json

from psutil import cpu_count, virtual_memory

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from teska_monitor import telemetry
from teska_monitor.db import read


external_stylesheets = [
#    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    dbc.themes.BOOTSTRAP
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# build a Navigation bar
navbar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(dbc.NavbarBrand("TeSKA Monitor", className="ml-3")),
                dbc.NavLink(dbc.Button('Refresh', id='refresh-button', color='link'))
            ],
            style={'justify-content': 'space-between', 'width': '100%'},
            align='center'
        ),
    ],
    color="dark",
    dark=True
)

# GENERAL LAYOUT
app.layout = dbc.Container(
    children=[
        # html.H1(children='Monitoring Dashboard'),

        # html.Div(children='''
        #     Dash: A web application framework for Python.
        # '''),
        navbar,

        # --> dev only
        # html.Button("Refresh", id = "refresh-button"),
        html.Code("waiting for data", id = "output"),
        # <--

        # TOP ROW 
        # use for current data, filled by telemetry.get_all callback
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='example-graph',
                ),
                sm=12,
                md=6,
                lg=3,
            ),
            dbc.Col(
                dcc.Graph(
                    id='bullet-graph',
                ),
                sm=12,
                md=6,
                lg=3
            ),
            # This id can be changed and the graph can be used
            dbc.Col(
                dcc.Graph(
                    id='graph-3',
                ),
                sm=12,
                md=6,
                lg=3
            ),
            # This id can be changed and the graph can be used
            dbc.Col(
                dcc.Graph(
                    id='graph-4',
                ),
                sm=12,
                md=6,
                lg=3
            )
        ], className="m-0"),


        # 'Historic' Data
        # Append Rows for data filled by database read() callback(s)
        
        dbc.Row([
            # this row always takes the full width
            dbc.Col(
                dcc.Graph(
                    id='history-graph'
                ),
                sm=12
            )
        ], className="m-0"),

        # two graphs - uncomment to use it
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='graph-6'
                ),
                sm=12,
                md=6
            ),
            dbc.Col(
                dcc.Graph(
                    id='graph-7'
                ),
                sm=12,
                md=6
            ),
        ], className="m-0")
    ],
    fluid=True,
    className="p-0 m-0"
)


# CALLBACK FUNCTIONS
@app.callback(
    Output(component_id='output', component_property='children'),
    Output(component_id= 'example-graph', component_property='figure'),
    Output(component_id= 'bullet-graph', component_property= 'figure'),
    Input(component_id= 'refresh-button', component_property='n_clicks')
)
def update_output_div(input_value):
    data = telemetry.get_all()

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = data["cpu_usage"],
        delta = {'reference': 100},
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "CPU Usage"},
        gauge = {'axis': {'range': [0, 100]}}
    ))

    labels = ["used memory", "free memory"]
    values = [data["virtual_memory"], 100 - data["virtual_memory"]]
    
    figs = go.Figure(data=[go.Pie(labels=labels, values=values)])


    return 'Output: {}'.format(data), fig, figs


@app.callback(
    Output(component_id="history-graph", component_property= 'figure'),
    Input(component_id= 'refresh-button', component_property='n_clicks')
)
def update_history_graph(input_value):
    data = read()

    x = []
    y = []

    for d in data:
        x.append(d["dtime"])

    for d in data:
        y.append(d["cpu_usage"])    

    fig = go.Figure(data=go.Scatter(x=x, y=y))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
