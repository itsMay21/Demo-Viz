import plotly.express as px
import pandas as pd
import dash
from dash import Dash, dcc, Input, Output, html, callback, ctx, clientside_callback
import dash_bootstrap_components as dbc
import json
import dash_echarts
from dash.exceptions import PreventUpdate
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from math import ceil

dash.register_page(__name__,order=8)

count_list= ['Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/page7.css']

# df_w_fact=pd.read_csv('./Data_files/pop_tot_updated.csv') #global, will implement

df_w_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')

df_w_gdp_t=df_w_gdp.transpose()
new_header = df_w_gdp_t.iloc[0] 
df_w_gdp_t = df_w_gdp_t[4:]
df_w_gdp_t.columns = new_header
df_w_gdp_t.index.name = 'year'
df_w_gdp_t.to_csv('update.csv')
df_w_gdp_t = pd.read_csv('update.csv')

fig = px.line(df_w_gdp_t, x="year", y="World")

fig.layout.xaxis.title="Year"
fig.layout.yaxis.title="GDP"
# subfig.update_layout(
#     title_text="Name: "+country,
# )

@callback(
        Output("factor_pg7","options"),
        Input("country_dropdown_pg7","value"),
)
def change_options(year_dropdown_pg1):
    from pages import settings
    return settings.global_options


@callback(
        Output("fig_pg7","figure"),
        Input("country_dropdown_pg7","value"),
        Input("factor_pg7","value"),
)
def generate_w_factor(country_dropdown_pg7,factor_pg7):

    if(factor_pg7==None or len(country_dropdown_pg7)==0):
        return px.line()

    df_w_fact=pd.read_csv('./Data_files/'+factor_pg7+'.csv')
    df_w_fact_t=df_w_fact.transpose()
    new_header = df_w_fact_t.iloc[0] 
    df_w_fact_t = df_w_fact_t[4:]
    df_w_fact_t.columns = new_header
    df_w_fact_t.index.name = 'year'
    df_w_fact_t.to_csv('update.csv')
    df_w_fact_t = pd.read_csv('update.csv')
    
    df1=pd.melt(df_w_fact_t, id_vars=['year'], value_vars=country_dropdown_pg7)
    # df1.to_csv('test2.csv')
    constant_factor=len(country_dropdown_pg7)
    fig = px.line(df1, x="year", y="value", facet_col="variable",facet_col_wrap=2,
            facet_row_spacing=0.08, # default is 0.07 when facet_col_wrap is used
            facet_col_spacing=0.08, # default is 0.03
            height=400*ceil(constant_factor/2), width=1100,)

    fig.layout.xaxis.title="Year"
    fig.layout.yaxis.title=factor_pg7
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    # fig.update_yaxes(matches=None)
    return fig

layout = html.Div([
    html.Div(className="text-container",
             children=[
                 html.H1('Country Insights: Comparative Analysis Across Nations'),
                 html.Br(),
                 html.H2(
                     'Explore comprehensive data comparing key indicators across four distinct countries, revealing insights into their socio-economic landscapes and global interactions',
                     className='description')
             ]
             ),
    html.Div(className="dropdown-container",
             children=[
                 dcc.Dropdown(
                     options=count_list,
                     value=['India', 'China', 'Japan', 'United States'],
                     id="country_dropdown_pg7",
                     multi=True,
                     style={"width": "90%"}
                 ),
                 dcc.Dropdown(
                     options=[
                         {'label': 'GDP', 'value': 'gdp_current_updated'},
                         {'label': 'Population', 'value': 'pop_tot_updated'},
                         {'label': 'Population Growth', 'value': 'pop_growth_updated'},
                     ],
                     value="gdp_current_updated",
                     id="factor_pg7",
                     style={"width": "70%"}
                 ),
             ]
             ),
    html.Div(className="plot-container",
             children=[
                 dcc.Graph(id="fig_pg7"),
             ]
             ),
             dbc.Button([html.Span("\u25B2")], color="primary", className="me-1", id='scroll-to-top-btn', n_clicks=0, style={'position': 'fixed', 'bottom': '20px', 'right': '20px'})

])
clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks) {
            window.scrollTo({top: 0, behavior: 'smooth'});
        }
        return 0;
    }
    """,
    Output('scroll-to-top-btn', 'n_clicks'),
    Input('scroll-to-top-btn', 'n_clicks')
)

