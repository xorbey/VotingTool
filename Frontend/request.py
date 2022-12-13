import base64

import dash_bootstrap_components as dbc
from dash import  html
import os
import dash_core_components as dcc
import plotly.graph_objects as go

request = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H4("Feature Request Tool"),
            html.H6("Ich hätte gerne ein Tool, mit dem man Features benennen kann Ich hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kannIch hätte gerne ein Tool, mit dem man Features benennen kann"),
            dbc.Row([dbc.Col("Owner", style={"font-weight":"bold"}), dbc.Col("Hashtags", style={"font-weight":"bold"})]),
            dbc.Row([dbc.Col("Mark"), dbc.Col("#bla, #bli, #blu")])
            
        ]
        ,width=10),
        dbc.Col([
            dbc.Row(html.Button(
                [html.Div(className = "triangle-buttons__triangle triangle-buttons__triangle--t")] , className ="triangle-buttons")),
            dbc.Row(html.Button(
                [html.Div(className = "triangle-buttons__triangle triangle-buttons__triangle--b")] , className ="triangle-buttons"))
        ], width=1)
    ],className='divBorder')
])