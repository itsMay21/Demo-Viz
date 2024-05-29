import plotly.express as px
import pandas as pd
import dash
from dash import dcc, Input, Output, State, html, callback
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc


dash.register_page(__name__,order=4)
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/page3.css']

count_list= ['No', 'Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 

@callback(
        Output("para_dropdown","options"),
        Input("country_dropdown","value"),
)
def change_options(year_dropdown_pg1):
    from pages import settings
    return settings.global_options


@callback(
        Output("world_dist_map", "figure"),
        [Input("para_dropdown","value"),
        Input("year_dropdown_pg3","value")]
)
def generate_world_dist(para_dropdown,year_dropdown_pg3):
    from pages import settings
    if(para_dropdown==None or year_dropdown_pg3==None):
        fig = go.Figure(data=go.Choropleth())
        fig.update_layout(
            # title_text=year_dropdown_pg3+' Global GDP',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            annotations = [dict(
                x=0.55,
                y=0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://data.worldbank.org/indicator">\
                    THE WORLD BANK</a>',
                showarrow = False
            )]
        )
        fig.update_layout(autosize=False,
                    height=600,
                    width=1000,
                    margin={"r":0,"t":0,"l":0,"b":0})
        return fig 

    # df = pd.read_csv('../gdp_percapita_current_updated.csv')
    df = pd.read_csv('./Data_files/' + para_dropdown + '.csv')
    mask = df['Country Name'] == 'World'
    df = df[~mask]
    mask = df['Country Name'] == "High income"
    df = df[~mask]
    mask = df['Country Name'] == 'Low income'
    df = df[~mask]
    mask = df['Country Name'] == 'Lower middle income'
    df = df[~mask]
    mask = df['Country Name'] == 'Upper middle income'
    df = df[~mask]
    fig = go.Figure(data=go.Choropleth(
        locations = df['Country Code'],
        z = df[year_dropdown_pg3],
        text = df['Country Name'],
        colorscale = 'Blues',
        autocolorscale=False,
        # reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        # colorbar_tickprefix = '$',
        colorbar_title = settings.data_dictionary[para_dropdown],
    ))
    fig.update_layout(
        title_text=year_dropdown_pg3+' Global GDP',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations = [dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://data.worldbank.org/indicator">\
                THE WORLD BANK</a>',
            showarrow = False
        )]
    )
    fig.update_layout(autosize=False,
                height=600,
                width=1000,
                margin={"r":0,"t":0,"l":0,"b":0})
    return fig

@callback(
        Output("country_dropdown","value"),
        Input("world_dist_map","clickData")
)
def change_country_dropdown(clickData):
    if clickData is None:
        return None
    return clickData['points'][0]['text']

@callback(
        Output("count_specific","children"),
        Input("country_dropdown","value"),
        Input("para_dropdown","value")
)
def generate_country_specific(country_dropdown,para_dropdown):
    if country_dropdown is None:
        return html.Br()
    if country_dropdown=="No":
        return html.Br()
    if para_dropdown == None:
        return html.Br()
    country=country_dropdown
    global df
    from pages import settings
    if settings.global_k=="No Filter":
        para_dropdown=para_dropdown[:-8]
        df = pd.read_csv('./Data_files/gdp_per_capita.csv')
    elif settings.global_k=="Filter":
        df = pd.read_csv('./Data_files/gdp_per_capita_updated.csv')
    # df1 = pd.read_csv('../pop_tot_updated.csv')
    df1 = pd.read_csv('./Data_files/' + para_dropdown + '.csv')
    df1_t=df1.transpose()
    new_header = df1_t.iloc[0] 
    df1_t = df1_t[4:]
    df1_t.columns = new_header
    df1_t.index.name = 'year'
    df1_t.to_csv('update.csv')
    df1_t = pd.read_csv('update.csv')

    df_t=df.transpose()
    new_header = df_t.iloc[0] 
    df_t = df_t[4:]
    df_t.columns = new_header
    df_t.index.name = 'year'
    df_t.to_csv('update.csv')
    df_t = pd.read_csv('update.csv')

    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    fig2 = px.line(df1_t, x='year', y=country,color=px.Constant("red"),color_discrete_map="identity")
    fig = px.bar(df_t, x="year", y=country)

    fig2.update_traces(yaxis="y2")

    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title="Year"
    subfig.layout.yaxis2.title=settings.data_dictionary[para_dropdown]
    subfig.layout.yaxis1.title="GDP per capita"
    subfig.update_layout(
        title_text="Name: "+country,
    )
    return dcc.Graph(id="country_map",figure=subfig)

@callback(
        Output("modal", "is_open"),
        [Input("country_dropdown", "value")],
        [State("modal", "is_open")]
)
def open_modal(n1, is_open):
    if n1 and n1!="No":
        return True
    # return is_open

layout = html.Div([
    # Text container
    html.Div([
        html.H1('World Distribution Insights', className='title'),
        html.Br(),
        html.H2(
            'Observe factor trends on a worldwide level at a glance with our interactive heatmap. Click on individual nations to delve deeper into detailed information and gain insights into global distribution patterns.',
             className='description')
    ], className='text-container'),

    # Dropdown container
    html.Div([
        dcc.Dropdown(
            options=['No', 'gdp_per_capita'],
            value='gdp_current_updated',
            id="para_dropdown",
            style={"width": "40%"},
            placeholder="Parameter"
        ),
        dcc.Dropdown(
            options=count_list,
            value=None,
            id="country_dropdown",
            style={"width": "40%"},
            placeholder="Country"
        ),
        dcc.Dropdown(
            options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
            value="2018",
            id="year_dropdown_pg3",
            style={"width": "40%"}
        )
    ], className='dropdown-container'),

    # Plot container
    html.Div([
        dcc.Graph(id="world_dist_map")
    ], className='plot-container'),

    # Modal for country-specific data
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Country Specific Data")),
        dbc.ModalBody([
            html.Div(id="count_specific")
        ]),
    ], id="modal", is_open=False, size='lg')
], className="page1_style")
