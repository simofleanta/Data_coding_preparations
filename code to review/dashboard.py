import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
import dash_daq as daq
from dash.dependencies import Input, Output, State
import os
import flask
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

"""Looking for Freelancer, who can check "the code" + edit some diagrams, make them more "beautiful" and readable.

Code in Python with DASH


The code and screnshot can be found in Attachment."""

def dashboard(df, df_s):
    layout = dbc.Container([
        dbc.Row([
            dbc.Col([controls(df.Year, df.District, df['HWB-Klasse'])], md=4, width='auto'),
            dbc.Col(id='board', children=[board(df)], md=8, width='auto')
        ])

    ], fluid=True)

    return layout


def controls(years, dists, hwb):
    min_year = years.sort_values(ascending=True).unique().tolist()[1]
    dist_list = dists.sort_values(ascending=True).unique().tolist()
    dist_drop = [{'label': str(int(dist)), 'value': dist} for dist in dist_list]
    hwb_check = [{'label': item, 'value': item} for item in hwb.sort_values(ascending=True).unique().tolist()]
    main_controls = dbc.Card([
        html.Label(id='years-label', children=['Years']),
        dcc.RangeSlider(
            id='years-slider',
            min=min_year,
            max=max(years),
            step=1,
            value=[2010, 2020],
            marks={min_year: {'label': str(min_year)},
                   max(years): {'label': str(max(years))}
                   }),
        html.Label('Districts', style={"margin-top": "20px"}),
        dcc.Dropdown(id='district-id',
            options=dist_drop,
            value=[1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080],
            multi=True
        ),
        html.Label('HWB Class', style={"margin-top": "20px"}),
        dcc.Checklist(id='hwb-klasse',
            options=hwb_check,
            value=['A', 'B'],
            labelStyle={'display': 'inline-block', 'margin-right': '20px'}
        )
    ], style={'width': '18rem', 'height': '24rem', "margin-top": "30px"}, body=True)

    return main_controls


def board(df, years=None, dists=None, hwbs=None):
    if not years:
        years = [2010, 2020]
    if not dists:
        dists = [1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080]
    if not hwbs:
        hwbs = ['A', 'B']
    df_loc = get_selected(df, years, dists, hwbs)
    board = dbc.Row([
                    dbc.Col([dcc.Graph(id='graph1', figure=graph1(df_loc, years, dists, hwbs))], md=6, width='auto'),
                    dbc.Col([dcc.Graph(id='graph2', figure=graph2(df_loc, years, dists, hwbs))], md=6, width='auto'),
                    dbc.Col([dcc.Graph(id='graph3', figure=graph3(df_loc))], md=6, width='auto'),
                    dbc.Col([dcc.Graph(id='graph4', figure=graph4(df_loc, hwbs))], md=6, width='auto')
            ])
    return board


def graph1(df_loc, years, dists, hwbs):
    selected = df_loc.loc[df_loc.Type == 'Dachgeschosswohnung'].groupby('District').agg({'price_per_m2': np.mean})[
        'price_per_m2']
    general = df_loc.groupby('District').agg({'price_per_m2': np.mean})['price_per_m2']
    labels = selected.index.tolist()
    fig = go.Figure(data=[
                    go.Bar(name='All', x=labels, y=general),
                    go.Bar(name='Selected', x=labels, y=selected)])
    fig.update_layout(barmode='group', legend=dict(yanchor="bottom", y=0.05, xanchor="left", x=0.05))
    return fig


def graph2(df_loc, years, dists, hwbs):
    df_offer = df_loc.loc[df_loc.Year < 2020].groupby('District').agg(
        {'price_per_m2': 'mean', 'HWB-Klasse': 'count'}).sort_values('HWB-Klasse')
    m, b = np.polyfit(df_offer['HWB-Klasse'][1:], df_offer['price_per_m2'][1:], 1)
    fig = go.Figure(data=[
        go.Scatter(name='Offers', x=df_offer['HWB-Klasse'], y=df_offer['price_per_m2'], mode='markers'),
        go.Scatter(name='Trend', x=df_offer['HWB-Klasse'][1:], y=m*df_offer['HWB-Klasse'][1:] + b, mode='lines')
    ])
    fig.update_layout(legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.05))
    return fig


def graph3(df_loc):
    max_year = max(df_loc.Year)
    if max_year > 2021:
        max_year = 2021
    old_df = df_loc[df_loc.Year < (max_year - 3)].copy()
    new_df = df_loc[df_loc.Year > (max_year - 4)].copy()
    old_ap = old_df.groupby('District').agg({'price_per_m2': np.mean})['price_per_m2']
    new_ap = new_df.groupby('District').agg({'price_per_m2': np.mean})['price_per_m2']
    labels = old_ap.index.tolist()
    fig = go.Figure(data=[
                    go.Bar(name='New appartments', x=labels, y=new_ap),
                    go.Bar(name='Old appartments', x=labels, y=old_ap)])
    fig.update_layout(barmode='group', legend=dict(yanchor="bottom", y=0.05, xanchor="left", x=0.05))
    return fig


def graph4(df_loc, hwbs):
    scatters = []
    df_energy = df_loc.groupby(by=['HWB-Klasse', 'District']).agg({'price_per_m2': np.mean})
    df_energy.loc[df_energy['price_per_m2'].isna(), 'price_per_m2'] = 0
    for item in hwbs:
        df_A = df_energy.loc[item]
        tmp = df_A['price_per_m2'].values
        stats = np.concatenate((tmp, [tmp[0]]))
        labels = [str(int(item))for item in list(np.concatenate((df_A.index.tolist(), [df_A.index.tolist()[0]])))]
        scatters.append(go.Scatterpolar(name='Class ' + item, r=stats, theta=labels))
    fig = go.Figure(data=scatters)
    fig.update_traces(fill='toself')
    fig.update_layout(polar=dict(radialaxis_angle=135, angularaxis=dict(direction="clockwise", period=6)))
    return fig


def get_selected(df, years, dists, hwbs):
    df_loc = df.loc[(df['Year'] > years[0] - 1) & (df['Year'] < years[1] + 1)]
    df_loc = df_loc.loc[df_loc.District.isin(dists)]
    df_loc = df_loc.loc[df_loc['HWB-Klasse'].isin(hwbs)]
    df_loc.District = df_loc.District.astype('int64').astype('category')
    return df_loc
