import plotly.express as px
import pandas as pd
import dash
from dash import dcc, Input, Output, html, callback


dash.register_page(__name__,order=3)
df_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/page2.css']

@callback(
        Output("factor_pg2","options"),
        Input("year_dropdown_pg2","value"),
)
def change_options(year_dropdown_pg1):
    from pages import settings
    return settings.global_options


@callback(
    Output("factor_vs_gdp","figure"),
    Input("year_dropdown_pg2","value"),
    Input("factor_pg2","value"),
    Input("yaxis-type","value"),
    Input("xaxis-type","value"),
    Input("trendline_dropdown_pg2","value"),
    Input("trendline_slider_pg2","value"),
    suppress_callback_exceptions=True
)
def generate_factor_vs_gdp(year_dropdown_pg2, factor_pg2, yaxis_type, xaxis_type, trendline_type,trendline_slider_pg2):

    if(year_dropdown_pg2==None or factor_pg2==None):
        return px.scatter()
    global df_gdp
    from pages import settings
    if settings.global_k=="No Filter":
        factor_pg2=factor_pg2[:-8]
        df_gdp = pd.read_csv('./Data_files/gdp_current.csv')
    elif settings.global_k=="Filter":
        df_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')
        
    df_fact = pd.read_csv('./Data_files/' + factor_pg2 + '.csv')

    df_gdp_f = df_gdp[['Country Name', year_dropdown_pg2]]
    df_fact_f = df_fact[['Country Name', year_dropdown_pg2]]

    df_final = pd.merge(df_gdp_f, df_fact_f, on=['Country Name'])
    mask = df_final['Country Name'] == 'World'
    df_final = df_final[~mask]
    mask = df_final['Country Name'] == "High income"
    df_final = df_final[~mask]
    mask = df_final['Country Name'] == 'Low income'
    df_final = df_final[~mask]
    mask = df_final['Country Name'] == 'Lower middle income'
    df_final = df_final[~mask]
    mask = df_final['Country Name'] == 'Upper middle income'
    df_final = df_final[~mask]
    fig = px.scatter(df_final, x=year_dropdown_pg2 + '_x', y=year_dropdown_pg2 + '_y', hover_name='Country Name')
    if trendline_type == 'ols':
        fig = px.scatter(df_final, x=year_dropdown_pg2 + '_x', y=year_dropdown_pg2 + '_y', hover_name='Country Name', trendline=trendline_type)
    elif trendline_type == 'lowess':
        fig = px.scatter(df_final, x=year_dropdown_pg2 + '_x', y=year_dropdown_pg2 + '_y', hover_name='Country Name', trendline=trendline_type, trendline_options=dict(frac=trendline_slider_pg2))
    if trendline_type == 'ewm':
        fig = px.scatter(df_final, x=year_dropdown_pg2 + '_x', y=year_dropdown_pg2 + '_y', hover_name='Country Name', trendline=trendline_type, trendline_options=dict(halflife=trendline_slider_pg2))
    if trendline_type == 'rolling':
        fig = px.scatter(df_final, x=year_dropdown_pg2 + '_x', y=year_dropdown_pg2 + '_y', hover_name='Country Name', trendline=trendline_type, trendline_options=dict(window=trendline_slider_pg2))
    
    fig.layout.xaxis.title = "GDP"
    fig.layout.yaxis.title = settings.data_dictionary[factor_pg2]
    fig.update_yaxes(type='linear' if yaxis_type == 'Linear' else 'log')
    fig.update_xaxes(type='linear' if xaxis_type == 'Linear' else 'log')
    
    return fig

@callback(
    Output("trendline_slider_pg2","min"),
    Output("trendline_slider_pg2","max"),
    Output("trendline_slider_pg2","step"),
    Output("trendline_slider_pg2","value"),
    Input("trendline_dropdown_pg2","value"),
)
def generate_trendline_slider(trendline_dropdown_pg2):
    if trendline_dropdown_pg2=='lowess':
        return 0.1,1,0.1,0.6
    elif trendline_dropdown_pg2=='ewm':
        return 1,10,1,2
    elif trendline_dropdown_pg2=='rolling':
        return 2,10,1,5
    else:
        return None, None, None, None


# Define the layout using containers
layout = html.Div([
    # Text container
    html.Div(className='header-container',
             children=[
                 html.Div(className='header-image')
             ]
             ),
    html.Div(className="content-container",
             children=[
                 html.H1('Factor-GDP Dynamics', className='title'),
                 html.Br(),
                 html.H2(
                     "Delve into the relationship between factor values/levels and GDP across countries. Through visual scatterplots, we uncover trends and correlations, shedding light on the interdependencies shaping economic performance.",
                     className='description')
             ]
             ),
    html.Br(),
    # Dropdowns and radio buttons container
    html.Div(className='controls-container',
             children=[
                 html.Div([
                     html.Label('Select Year:', className='control-label'),
                     dcc.Dropdown(
                         options=[{'label': str(year), 'value': str(year)} for year in range(1960, 2023)],
                         value="2018",
                         id="year_dropdown_pg2",
                         className='dropdown-control'
                     ),
                 ], className='control-item'),
                 html.Div([
                     html.Label('Select Factor:', className='control-label'),
                     dcc.Dropdown(
                         options=[
                             {'label': 'Population', 'value': 'pop_tot_updated'},
                             {'label': 'Population Growth', 'value': 'pop_growth_updated'},
                         ],
                         value="pop_tot_updated",
                         id="factor_pg2",
                         className='dropdown-control'
                     ),
                 ], className='control-item'),
                 html.Div([
                     html.Label('X-axis type:', className='control-label'),
                     dcc.RadioItems(
                         options=[
                             {'label': 'Linear', 'value': 'Linear'},
                             {'label': 'Log', 'value': 'Log'}
                         ],
                         value='Linear',
                         id='xaxis-type',
                         className='radio-control'
                     )
                 ], className='control-item'),
                 html.Div([
                     html.Label('Y-axis type:', className='control-label'),
                     dcc.RadioItems(
                         options=[
                             {'label': 'Linear', 'value': 'Linear'},
                             {'label': 'Log', 'value': 'Log'}
                         ],
                         value='Linear',
                         id='yaxis-type',
                         className='radio-control'
                     )
                 ], className='control-item'),
                 html.Div([
                     html.Label('Select Trendline:', className='control-label'),
                     dcc.Dropdown(
                         options=[
                             {'label': 'OLS', 'value': 'ols'},
                             {'label': 'Lowess', 'value': 'lowess'},
                             {'label': 'EWM', 'value': 'ewm'},
                             {'label': 'Rolling', 'value': 'rolling'}
                         ],
                         value=None,
                         id='trendline_dropdown_pg2',
                         className='dropdown-control',
                         placeholder="Trendline Type"
                     ),
                     dcc.Slider(
                         id='trendline_slider_pg2',
                         min=2,
                         max=10,
                         step=1,
                         value=5,
                         className='slider-control'
                     ),
                 ], className='control-item-2'),
             ]),
    # Graph container

        dcc.Graph(id="factor_vs_gdp")

], className='page1_style')


