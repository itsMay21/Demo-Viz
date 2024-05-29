import plotly.express as px
import pandas as pd
import dash
from dash import Dash, dcc, Input, Output, html, callback, ctx
import json
import dash_echarts
from dash.exceptions import PreventUpdate
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


dash.register_page(__name__,order=5)

@callback(
        Output("cross_sect", "figure"),
        [Input("year_dropdown_pg5","value"),
         Input("factor_pg5_1","value"),
         Input("factor_pg5_2","value")]
)
def generate_cross_sect(year_dropdown_pg5,factor_pg5_1,factor_pg5_2):
    year=year_dropdown_pg5
    df_fact_1=pd.read_csv('./Data_files/'+factor_pg5_1+'.csv')
    df_fact_2=pd.read_csv('./Data_files/'+factor_pg5_2+'.csv')
    mask = df_fact_1['Country Name'] == 'World'
    df_fact_1 = df_fact_1[~mask]
    mask = df_fact_1['Country Name'] == "High income"
    df_fact_1 = df_fact_1[~mask]
    mask = df_fact_1['Country Name'] == 'Low income'
    df_fact_1 = df_fact_1[~mask]
    mask = df_fact_1['Country Name'] == 'Lower middle income'
    df_fact_1 = df_fact_1[~mask]
    mask = df_fact_1['Country Name'] == 'Upper middle income'
    df_fact_1 = df_fact_1[~mask]
    mask = df_fact_2['Country Name'] == 'World'
    df_fact_2 = df_fact_2[~mask]
    mask = df_fact_2['Country Name'] == "High income"
    df_fact_2 = df_fact_2[~mask]
    mask = df_fact_2['Country Name'] == 'Low income'
    df_fact_2 = df_fact_2[~mask]
    mask = df_fact_2['Country Name'] == 'Lower middle income'
    df_fact_2 = df_fact_2[~mask]
    mask = df_fact_2['Country Name'] == 'Upper middle income'
    df_fact_2 = df_fact_2[~mask]
    df_fact_1=df_fact_1.sort_values(by=year)

    df_fact_2 = df_fact_2.set_index('Country Name')
    df_fact_2 = df_fact_2.reindex(index=df_fact_1['Country Name'])
    df_fact_2 = df_fact_2.reset_index()

    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    fig = px.line(df_fact_1, x="Country Name", y=year)
    fig2 = px.line(df_fact_2, x="Country Name", y=year)

    fig2.update_traces(yaxis="y2")

    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title="Countries"
    subfig.layout.yaxis.title=factor_pg5_1
    subfig.layout.yaxis2.title=factor_pg5_2
    subfig.update_layout(
        title_text="Year: "+year,
    )

    subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    return subfig

@callback(
        Output("factor_pg5_1","options"),
        Output("factor_pg5_2","options"),
        Input("year_dropdown_pg5","value"),
)
def change_options(year_dropdown_pg1):
    from pages import settings        
    return settings.global_options,settings.global_options

layout = html.Div([
    html.H1('This is our Cross Sectional page'),
    html.Br(),
    dcc.Dropdown(
        options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
        value="2018",
        id="year_dropdown_pg5",
        style={"width": "100%"}
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Population', 'value': 'pop_tot_updated'},
            {'label': 'Population Growth', 'value': 'pop_growth_updated'},
            {'label': 'GDP', 'value': 'gdp_current_updated'},
            {'label': 'GDP per Capita', 'value': 'gdp_per_capita_updated'}
        ],
        value="gdp_per_capita_updated",
        id="factor_pg5_1",
        style={"width": "100%"}
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Population', 'value': 'pop_tot_updated'},
            {'label': 'Population Growth', 'value': 'pop_growth_updated'},
            {'label': 'GDP', 'value': 'gdp_current_updated'},
            {'label': 'GDP per Capita', 'value': 'gdp_per_capita_updated'}
        ],
        value="pop_tot_updated",
        id="factor_pg5_2",
        style={"width": "100%"}
    ),
    dcc.Graph(id="cross_sect")
])