import plotly.express as px
import pandas as pd
import dash
from dash import dcc, Input, Output, html, callback


dash.register_page(__name__,order=2)

count_list= ['No', 'Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/page1.css']


option_pg1=[{'label':'Population','value':'pop_tot_updated'},
            {'label':'Population Growth','value':'pop_growth_updated'},
            ]

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

@callback(
        Output("factor_pg1","options"),
        Input("year_dropdown_pg1","value"),
)
def change_options(year_dropdown_pg1):
    from pages import settings        
    return settings.global_options

@callback(
        Output("top10_gdp","figure"),
        Input("year_dropdown_pg1","value"),
)
def generate_top_10_gdp(year_dropdown_pg1):
    from pages import settings
    global df_w_gdp
    if settings.global_k=="No Filter":
        df_w_gdp = pd.read_csv('./Data_files/gdp_current.csv')
    elif settings.global_k=="Filter":
        df_w_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')
    if(year_dropdown_pg1==None):
        return px.bar()
    mask = df_w_gdp['Country Name'] == 'World'
    df_w_gdp = df_w_gdp[~mask]
    mask = df_w_gdp['Country Name'] == "High income"
    df_w_gdp = df_w_gdp[~mask]
    mask = df_w_gdp['Country Name'] == 'Low income'
    df_w_gdp = df_w_gdp[~mask]
    mask = df_w_gdp['Country Name'] == 'Lower middle income'
    df_w_gdp = df_w_gdp[~mask]
    mask = df_w_gdp['Country Name'] == 'Upper middle income'
    df_w_gdp = df_w_gdp[~mask]
    sorted_df_w_gdp = df_w_gdp.sort_values(by=year_dropdown_pg1, ascending=False)
    sorted_df_w_gdp_top_10_rows = sorted_df_w_gdp.head(10)
    # sorted_df_w_gdp_top_10_rows=sorted_df_w_gdp_top_10_rows[1:]
    fig = px.bar(sorted_df_w_gdp_top_10_rows,
                  y=year_dropdown_pg1, x="Country Name"
                  )
    fig.layout.xaxis.title="Countries"
    fig.layout.yaxis.title="GDP"
    return fig

@callback(
        Output("factor_vs_year","figure"),
        Input("factor_pg1","value"),
)
def generate_w_factor(factor_pg1):
    from pages import settings
    if settings.global_k=="No Filter":
        factor_pg1=factor_pg1[:-8]
        
    if(factor_pg1==None):
        return px.line(range_x=[1960,2022])
    df_w_fact=pd.read_csv('./Data_files/'+factor_pg1+'.csv')   #df_w_fact=pd.read_csv('./Data_files/'+factor_pg1[:-8]+'.csv') 
    df_w_fact_t=df_w_fact.transpose()
    new_header = df_w_fact_t.iloc[0] 
    df_w_fact_t = df_w_fact_t[4:]
    df_w_fact_t.columns = new_header
    df_w_fact_t.index.name = 'year'
    df_w_fact_t.to_csv('update.csv')
    df_w_fact_t = pd.read_csv('update.csv')

    fig = px.line(df_w_fact_t, x="year", y="World")

    fig.layout.xaxis.title="Year"
    fig.layout.yaxis.title=settings.data_dictionary[factor_pg1]
    return fig

@callback(
    Output("plot_title", "children"),  # Updated Output component ID
    Input("factor_pg1", "value"),
    Input("factor_pg1", "options")  # Include the options as input
)
def update_plot_title(factor_value, factor_options):
    if factor_value is None:
        return "Factor vs. Year"  # Default title when no factor is selected
    else:
        # Get the label of the selected option
        factor_label = [option['label'] for option in factor_options if option['value'] == factor_value][0]
        return f"{factor_label} vs Year" 
    
@callback(
    Output("top10_title", "children"),  # Updated Output component ID
    Input("factor_pg1", "value"),
    Input("factor_pg1", "options")  # Include the options as input
)
def update_top10_title(factor_value, factor_options):
    if factor_value is None:
        return "Top 10 Factors"  # Default title when no factor is selected
    else:
        # Get the label of the selected option
        factor_label = [option['label'] for option in factor_options if option['value'] == factor_value][0]
        return f"Top 10 Nations by {factor_label}"

@callback(
        Output("top10_factor","figure"),
        Input("year_dropdown_pg1","value"),
        Input("factor_pg1","value"),
)
def generate_top_10_factor(year_dropdown_pg1,factor_pg1):
    # from pages import settings
    # print(settings.global_k)
    from pages import settings
    if settings.global_k=="No Filter":
        factor_pg1=factor_pg1[:-8]
    if(year_dropdown_pg1==None or factor_pg1==None):
        return px.bar()
    df_w_fact=pd.read_csv('./Data_files/'+factor_pg1+'.csv')
    mask = df_w_fact['Country Name'] == 'World'
    df_w_fact = df_w_fact[~mask]
    mask = df_w_fact['Country Name'] == "High income"
    df_w_fact = df_w_fact[~mask]
    mask = df_w_fact['Country Name'] == 'Low income'
    df_w_fact = df_w_fact[~mask]
    mask = df_w_fact['Country Name'] == 'Lower middle income'
    df_w_fact = df_w_fact[~mask]
    mask = df_w_fact['Country Name'] == 'Upper middle income'
    df_w_fact = df_w_fact[~mask]
    sorted_df_w_fact = df_w_fact.sort_values(by=year_dropdown_pg1, ascending=False)
    sorted_df_w_fact_top_10_rows = sorted_df_w_fact.head(10)
    # sorted_df_w_fact_top_10_rows=sorted_df_w_fact_top_10_rows[1:]
    fig = px.bar(sorted_df_w_fact_top_10_rows,
                  y="Country Name", x=year_dropdown_pg1
                  )
    fig.layout.xaxis.title=settings.data_dictionary[factor_pg1]
    fig.layout.yaxis.title="Countries"
    return fig

layout = html.Div([
    html.Div(className='header-container',
             children=[
                 html.Div(className='header-image')
             ]
             ),
    html.Div(className="content-container",
             children=[
                 html.H1('Global Insights: Exploring World GDP and Socioeconomic Trends', className='title'),
                 html.Br(),
                 html.H2(
                     'Discover the intricate web of relationships between world GDP and various factors such as population, population growth, healthcare, poverty, and more. Explore how these factors interrelate and shape global trends.',
                     className='description')
             ]
             ),
    html.Div(className="dropdown-container",
             children=[
                 html.Div(className="dropdown-item",
                          children=[
                              html.Label("Select Year:"),
                              dcc.Dropdown(
                                  options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
                                  value="2018",
                                  id="year_dropdown_pg1",
                                  style={"width": "100%"}
                              )
                          ]
                          ),
                 html.Div(className="dropdown-item",
                          children=[
                              html.Label("Select Factor:"),
                              dcc.Dropdown(
                                  options=[
                                      {'label': 'Population', 'value': 'pop_tot_updated'},
                                      {'label': 'Population Growth', 'value': 'pop_growth_updated'},
                                  ],
                                  value="pop_tot_updated",
                                  id="factor_pg1",
                                  style={"width": "100%"}
                              )
                          ]
                          ),
             ]
             ),

    html.Div(className="plot-container",
             children=[
                 html.Div(className="plot-item",
                          children=[
                              html.H3("World GDP vs. Year"),
                              dcc.Graph(id="world_gdp", figure=fig, style={"height": "300px"})
                          ]
                          ),
                 html.Div(className="plot-item",
                          children=[
                              html.H3(id="plot_title", className="plot-title"),
                              dcc.Graph(id="factor_vs_year", style={"height": "300px"})
                          ]
                          ),
                 html.Div(className="plot-item",
                          children=[
                              html.H3("Top 10 GDP Countries"),
                              dcc.Graph(id="top10_gdp", style={"height": "300px"})
                          ]
                          ),
                 html.Div(className="plot-item",
                          children=[
                              html.H3(id="top10_title", className="plot-title"),
                              dcc.Graph(id="top10_factor", style={"height": "300px"})
                          ]
                          ),
             ]
             ),
], className="page1_style")