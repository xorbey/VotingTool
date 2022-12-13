import base64

import dash_bootstrap_components as dbc
from dash import  html
import os
import dash_core_components as dcc
import plotly.graph_objects as go
from Frontend.request import request
mainview = dbc.Container(dbc.Col([request, request, request

], width={"size": 6, "offset": 3}))