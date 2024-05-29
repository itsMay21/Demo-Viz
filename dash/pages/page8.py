import plotly.express as px
import pandas as pd
import dash
from dash import dcc, Input, Output, html, callback


dash.register_page(__name__,order=5)
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/page8.css']

count_list= ['Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 


@callback(
        Output("factor_pg8","options"),
        Input("year_dropdown_pg8","value"),
)
def change_options(year_dropdown_pg8):
    from pages import settings
    return settings.global_options


@callback(
        Output("parallel_coordinate", "figure"),
        [Input("year_dropdown_pg8","value"),
         Input("factor_pg8","value"),
         Input("country_pg8", "value"),
        ]
)
def generate_parallel_coordinate(year_dropdown_pg8,factor_pg8, country_pg8):
    lab={}
    from pages import settings
    if (len(country_pg8)==0):
        l=['Country Name', 'Country Code']
        df_final = pd.read_csv('income_cat.csv')
        for fact in factor_pg8:
            df_fact = pd.read_csv('./Data_files/' + fact + '.csv')
            df_fact = df_fact.drop(['2023'], axis=1, errors='ignore')
            mask = df_fact['Country Name'] == 'World'
            df_fact = df_fact[~mask]
            mask = df_fact['Country Name'] == "High income"
            df_fact = df_fact[~mask]
            mask = df_fact['Country Name'] == 'Low income'
            df_fact = df_fact[~mask]
            mask = df_fact['Country Name'] == 'Lower middle income'
            df_fact = df_fact[~mask]
            mask = df_fact['Country Name'] == 'Upper middle income'
            df_fact = df_fact[~mask]
            header_list=['Country Name', 'Country Code',fact+" "+ 'Indicator Name', fact+" "+ 'Indicator Code', fact+" "+ '1960', fact+" "+ '1961', fact+" "+ '1962', fact+" "+ '1963', fact+" "+ '1964', fact+" "+ '1965', fact+" "+ '1966', fact+" "+ '1967', fact+" "+ '1968', fact+" "+ '1969', fact+" "+ '1970', fact+" "+ '1971', fact+" "+ '1972', fact+" "+ '1973', fact+" "+ '1974', fact+" "+ '1975', fact+" "+ '1976', fact+" "+ '1977', fact+" "+ '1978', fact+" "+ '1979', fact+" "+ '1980', fact+" "+ '1981', fact+" "+ '1982', fact+" "+ '1983', fact+" "+ '1984', fact+" "+ '1985', fact+" "+ '1986', fact+" "+ '1987', fact+" "+ '1988', fact+" "+ '1989', fact+" "+ '1990', fact+" "+ '1991', fact+" "+ '1992', fact+" "+ '1993', fact+" "+ '1994', fact+" "+ '1995', fact+" "+ '1996', fact+" "+ '1997', fact+" "+ '1998', fact+" "+ '1999', fact+" "+ '2000', fact+" "+ '2001', fact+" "+ '2002', fact+" "+ '2003', fact+" "+ '2004', fact+" "+ '2005', fact+" "+ '2006', fact+" "+ '2007', fact+" "+ '2008', fact+" "+ '2009', fact+" "+ '2010', fact+" "+ '2011', fact+" "+ '2012', fact+" "+ '2013', fact+" "+ '2014', fact+" "+ '2015', fact+" "+ '2016', fact+" "+ '2017', fact+" "+ '2018', fact+" "+ '2019', fact+" "+ '2020', fact+" "+ '2021', fact+" "+ '2022']
            df=df_fact.set_axis(header_list,axis=1)
            df_final = pd.merge(df_final, df, on=l)
            lab[fact+' '+year_dropdown_pg8]=settings.data_dictionary[fact]
        
        dim_list = [element+' '+year_dropdown_pg8 if isinstance(element, str) else element for element in factor_pg8]
        # print(lab)
        fig = px.parallel_coordinates(df_final,color='Income Group',
                                dimensions=dim_list,
                                color_continuous_scale=px.colors.diverging.Tealrose,
                                color_continuous_midpoint=2,
                                range_color=[0,3],
                                labels=lab)
        fig.update_coloraxes(colorbar_tickvals=[0,1, 2, 3])
        return fig
    
    if type(factor_pg8)==str:
        return html.Br()
    
    # print(factor_pg8)
    l=['Country Name', 'Country Code']
    df_final = pd.read_csv('income_cat.csv')

    for fact in factor_pg8:
        df_fact = pd.read_csv('./Data_files/' + fact + '.csv')
        df_fact = df_fact.drop(['2023'], axis=1, errors='ignore')

        df_fact = df_fact.loc[df_fact['Country Name'].isin(country_pg8)]
        header_list=['Country Name', 'Country Code',fact+" "+ 'Indicator Name', fact+" "+ 'Indicator Code', fact+" "+ '1960', fact+" "+ '1961', fact+" "+ '1962', fact+" "+ '1963', fact+" "+ '1964', fact+" "+ '1965', fact+" "+ '1966', fact+" "+ '1967', fact+" "+ '1968', fact+" "+ '1969', fact+" "+ '1970', fact+" "+ '1971', fact+" "+ '1972', fact+" "+ '1973', fact+" "+ '1974', fact+" "+ '1975', fact+" "+ '1976', fact+" "+ '1977', fact+" "+ '1978', fact+" "+ '1979', fact+" "+ '1980', fact+" "+ '1981', fact+" "+ '1982', fact+" "+ '1983', fact+" "+ '1984', fact+" "+ '1985', fact+" "+ '1986', fact+" "+ '1987', fact+" "+ '1988', fact+" "+ '1989', fact+" "+ '1990', fact+" "+ '1991', fact+" "+ '1992', fact+" "+ '1993', fact+" "+ '1994', fact+" "+ '1995', fact+" "+ '1996', fact+" "+ '1997', fact+" "+ '1998', fact+" "+ '1999', fact+" "+ '2000', fact+" "+ '2001', fact+" "+ '2002', fact+" "+ '2003', fact+" "+ '2004', fact+" "+ '2005', fact+" "+ '2006', fact+" "+ '2007', fact+" "+ '2008', fact+" "+ '2009', fact+" "+ '2010', fact+" "+ '2011', fact+" "+ '2012', fact+" "+ '2013', fact+" "+ '2014', fact+" "+ '2015', fact+" "+ '2016', fact+" "+ '2017', fact+" "+ '2018', fact+" "+ '2019', fact+" "+ '2020', fact+" "+ '2021', fact+" "+ '2022']

        df=df_fact.set_axis(header_list,axis=1)
        df_final = pd.merge(df_final, df, on=l)

        lab[fact+' '+year_dropdown_pg8]=settings.data_dictionary[fact]
    
    # print(lab)
    dim_list = [ element+' '+year_dropdown_pg8 if isinstance(element, str) else element for element in factor_pg8]
    
    fig = px.parallel_coordinates(df_final,color='Income Group',
                            dimensions=dim_list,
                            color_continuous_scale=px.colors.diverging.Tealrose,
                            color_continuous_midpoint=2,
                            range_color=[0,3],
                            labels=lab)
    fig.update_coloraxes(colorbar_tickvals=[0,1, 2, 3])
    return fig


layout = html.Div([
    html.Div(className='header-container',
             children=[
                 html.Div(className='header-image')
             ]
             ),
    html.Div(className="content-container",
             children=[
                 html.H1('Exploring Global Economic Factors with Parallel Coordinates', className='title'),
                 html.Br(),
                 html.H2(
                     'Offers a deep dive into global economic dynamics through parallel coordinate visualization. Explore trends and correlations between various factors like population, literacy rate, and GDP across different countries, providing valuable insights into socioeconomic landscapes.',
                     className='description')
             ]
             ),
    html.Br(),
    html.Div(className="dropdown-container",
             children=[
                 html.Div(className="dropdown-item",
                          children=[
                              html.Label("Select Year:"),
                              dcc.Dropdown(
                                  options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
                                  value="2018",
                                  id="year_dropdown_pg8",
                                  style={"width": "100%"},
                                  clearable=False
                              )
                          ]
                          ),
                 html.Div(className="dropdown-item",
                          children=[
                              html.Label("Select Factor:"),
                              dcc.Dropdown(
                                  options=[
                                      {'label': 'Population', 'value': 'pop_tot_updated'},
                                      {'label': 'Literacy Rate', 'value': 'literacy_rate_updated'},
                                      {'label': 'GDP', 'value': 'gdp_current_updated'},
                                      {'label': 'GDP per Capita', 'value': 'gdp_per_capita_updated'}
                                  ],
                                  value=['literacy_rate_updated','pop_tot_updated','gdp_current_updated'],
                                  id="factor_pg8",
                                  multi=True,
                                  style={"width": "100%", "white-space": "pre-wrap"}
                              )
                          ]
                          ),
                 html.Div(className="dropdown-item",
                          children=[
                              html.Label("Select Country:"),
                              dcc.Dropdown(
                                  options=[{'label': country, 'value': country} for country in count_list],
                                  value=['India', 'China', 'United States'],
                                  id="country_pg8",
                                  multi=True,
                                  style={"width": "100%", "white-space": "pre-wrap"}
                              )
                          ]
                          ),
             ]
             ),
    dcc.Graph(id="parallel_coordinate"),
], className="container")