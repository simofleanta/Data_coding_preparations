import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
import dash_daq as daq
from dash.dependencies import Input, Output, State
import os
import flask
from dashboard import dashboard
import pandas as pd
import numpy as np
from dashboard import board

df = pd.read_pickle('main.pkl')
df_s = pd.read_pickle('distr.pkl')


def navBar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Dashboard", href="/")),
            dbc.NavItem(dbc.NavLink("Data view", href="/data")),
        ],
        brand="Appartments dashboard",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.layout = html.Div([dcc.Location(id='loc', refresh=True),
                       navBar(),
                       html.Div(id='page-content', children=[])])


@app.callback(Output('page-content', 'children'),
              [Input('loc', 'pathname')])
def return_layout(pathname):
    if pathname == '/':
        return dashboard(df, df_s)
    elif pathname == '/data':
        return None
    else:
        return html.P('Error ' + str(pathname))


@app.callback(
    Output('years-label', 'children'),
    Input('years-slider', 'value')
)
def years_update(value):
    return 'Years {years[0]} - {years[1]}'.format(years=(value[0], value[1]))

@app.callback(
    Output('board', 'children'),
    [Input('district-id', 'value'),
     Input('years-slider', 'value'),
     Input('hwb-klasse', 'value')]
)
def board_update(dists, years, hwbs):
    return board(df, years=years, dists=dists, hwbs=hwbs)


if __name__ == '__main__':
    app.run_server(debug=True)
