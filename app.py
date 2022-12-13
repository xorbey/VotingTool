import dash

from dash import html
import dash_bootstrap_components as dbc
from dash import dcc

#from Callbacks.routes import register_routes

from Frontend.mainview import mainview
from Frontend.navbar import navbar
#Define external stylesheet
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
fonttypes = "https://fonts.googleapis.com/css?family=Source+Sans+Pro"
#Create a flask-app object and get the server (required to run in production)
app = dash.Dash(__name__, external_stylesheets=["assets/Datepicker.css", dbc.themes.BOOTSTRAP, dbc_css, fonttypes])
application = app.server
app.css.config.serve_locally = True
app.title = "iwb"
#Define the layout consisting of the url, the navbar and the container that holds the page content
app.layout = html.Div([navbar, mainview])

#Register callbacks and routes
#register_callbacks(app)
#register_routes(app)

if __name__ == "__main__":
    #Run server, expose it to the internet by setting the host and the port
    #application.run(host='0.0.0.0', port='80', debug=True)
    #     app.run_server(host='0.0.0.0', port='80', debug=True) 
    app.run_server(debug=True)