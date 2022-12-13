import dash_bootstrap_components as dbc
import dash_core_components as dcc

### Navbar, the href attributes define the urls of the pages
navbar = dbc.NavbarSimple(

    brand="Zeiss Tech Hub",
    brand_href="#",
    color="primary",
    dark=True,
)