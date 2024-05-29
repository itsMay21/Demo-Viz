import plotly.express as px
import pandas as pd
import dash
from dash import dcc, Input, Output, html, callback
import dash_echarts


dash.register_page(__name__,order=7)

count_list= ['No', 'Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 

data = {
    "name": "Income Distribution (216)",
        "children": [
            {
                "name":"High Income",
                "children":[
                    {
                        "name":"East Asia & Pacific",
                        "children":[
                            {"name": "Australia"},
                            {"name": "Nauru"},
                            {"name": "Brunei Darussalam"},
                            {"name": "New Caledonia"},
                            {"name": "French Polynesia"},
                            {"name": "Hong Kong SAR, China"},
                            {"name": "Japan"},
                            {"name": "Korea, Rep."},
                            {"name": "Macao SAR, China"},
                            {"name": "New Zealand"},
                            {"name": "Singapore"},
                            {"name": "American Samoa"},
                            {"name": "Guam"},
                            {"name": "Northern Mariana Islands"}
                        ]
                    },
                    {
                        "name":"Europe & Central Asia",
                        "children":[
                            {"name": "Czechia"},
                            {"name": "Denmark"},
                            {"name": "Faroe Islands"},
                            {"name": "Greenland"},
                            {"name": "Andorra"},
                            {"name": "Austria"},
                            {"name": "Belgium"},
                            {"name": "Cyprus"},
                            {"name": "Germany"},
                            {"name": "Spain"},
                            {"name": "Estonia"},
                            {"name": "Finland"},
                            {"name": "France"},
                            {"name": "Greece"},
                            {"name": "Croatia"},
                            {"name": "Ireland"},
                            {"name": "Italy"},
                            {"name": "Lithuania"},
                            {"name": "Luxembourg"},
                            {"name": "Latvia"},
                            {"name": "Monaco"},
                            {"name": "Netherlands"},
                            {"name": "Portugal"},
                            {"name": "San Marino"},
                            {"name": "Slovak Republic"},
                            {"name": "Slovenia"},
                            {"name": "Gibraltar"},
                            {"name": "Hungary"},
                            {"name": "Iceland"},
                            {"name": "Romania"},
                            {"name": "Norway"},
                            {"name": "Poland"},
                            {"name": "Channel Islands"},
                            {"name": "United Kingdom"},
                            {"name": "Isle of Man"},
                            {"name": "Sweden"},
                            {"name": "Switzerland"},
                            {"name": "Liechtenstein"}
                        ]
                    },
                    {
                        "name":"Latin America & Caribbean",
                        "children":[
                            {"name": "Aruba"},
                            {"name": "Bahamas, The"},
                            {"name": "Barbados"},
                            {"name": "Cayman Islands"},
                            {"name": "Chile"},
                            {"name": "Antigua and Barbuda"},
                            {"name": "St. Kitts and Nevis"},
                            {"name": "St. Martin (French part)"},
                            {"name": "Guyana"},
                            {"name": "Curaçao"},
                            {"name": "Sint Maarten (Dutch part)"},
                            {"name": "Panama"},
                            {"name": "Trinidad and Tobago"},
                            {"name": "Puerto Rico"},
                            {"name": "Turks and Caicos Islands"},
                            {"name": "British Virgin Islands"},
                            {"name": "Virgin Islands (U.S.)"},
                            {"name": "Uruguay"}
                        ]
                    },
                    {
                        "name":"Middle East & North Africa",
                        "children":[
                            {"name": "Bahrain"},
                            {"name": "Malta"},
                            {"name": "Israel"},
                            {"name": "Kuwait"},
                            {"name": "Oman"},
                            {"name": "Qatar"},
                            {"name": "Saudi Arabia"},
                            {"name": "United Arab Emirates"}
                        ]
                    },
                    {
                        "name":"North America",
                        "children":[
                            {"name": "Bermuda"},
                            {"name": "Canada"},
                            {"name": "United States"}
                        ]
                    },
                    {
                        "name":"Sub-Saharan Africa",
                        "children":[
                            {"name": "Seychelles"},
                        ]
                    }
                ]
            },
            {
                "name":"Upper middle income",
                "children":[
                    {
                        "name":"East Asia & Pacific",
                        "children":[
                            {"name": "Tuvalu"},
                            {"name": "China"},
                            {"name": "Fiji"},
                            {"name": "Indonesia"},
                            {"name": "Malaysia"},
                            {"name": "Thailand"},
                            {"name": "Tonga"},
                            {"name": "Marshall Islands"},
                            {"name": "Palau"}
                        ]
                    },
                    {
                        "name":"Europe & Central Asia",
                        "children":[
                            {"name": "Albania"},
                            {"name": "Armenia"},
                            {"name": "Belarus"},
                            {"name": "Bosnia and Herzegovina"},
                            {"name": "Bulgaria"},
                            {"name": "Montenegro"},
                            {"name": "Kosovo"},
                            {"name": "Georgia"},
                            {"name": "Kazakhstan"},
                            {"name": "North Macedonia"},
                            {"name": "Moldova"},
                            {"name": "Azerbaijan"},
                            {"name": "Serbia"},
                            {"name": "Türkiye"},
                            {"name": "Turkmenistan"},
                            {"name": "Russian Federation"}
                        ]
                    },
                    {
                        "name":"Latin America & Caribbean",
                        "children":[
                            {"name": "Argentina"},
                            {"name": "Belize"},
                            {"name": "Brazil"},
                            {"name": "Colombia"},
                            {"name": "Costa Rica"},
                            {"name": "Cuba"},
                            {"name": "Dominican Republic"},
                            {"name": "Dominica"},
                            {"name": "Grenada"},
                            {"name": "St. Lucia"},
                            {"name": "St. Vincent and the Grenadines"},
                            {"name": "Guatemala"},
                            {"name": "Jamaica"},
                            {"name": "Mexico"},
                            {"name": "Paraguay"},
                            {"name": "Peru"},
                            {"name": "Suriname"},
                            {"name": "Ecuador"},
                            {"name": "El Salvador"}
                        ]
                    },
                    {
                        "name":"Middle East & North Africa",
                        "children":[
                            {"name": "Iraq"},
                            {"name": "West Bank and Gaza"},
                            {"name": "Libya"}
                        ]
                    },
                    {
                        "name":"Sub-Saharan Africa",
                        "children":[
                            {"name": "Botswana"},
                            {"name": "Gabon"},
                            {"name": "Equatorial Guinea"},
                            {"name": "Mauritius"},
                            {"name": "Namibia"},
                            {"name": "South Africa"}
                        ]
                    },
                    {
                        "name":"South Asia",
                        "children":[
                            {"name": "Maldives"}
                        ]
                    }
                ]
            },
            {
                "name":"Lower middle income",
                "children":[
                    {
                        "name":"East Asia & Pacific",
                        "children":[
                            {"name": "Kiribati"},
                            {"name": "Cambodia"},
                            {"name": "Lao PDR"},
                            {"name": "Mongolia"},
                            {"name": "Myanmar"},
                            {"name": "Papua New Guinea"},
                            {"name": "Philippines"},
                            {"name": "Samoa"},
                            {"name": "Solomon Islands"},
                            {"name": "Micronesia, Fed. Sts."},
                            {"name": "Timor-Leste"},
                            {"name": "Vanuatu"},
                            {"name": "Viet Nam"}
                        ]
                    },
                    {
                        "name":"Europe & Central Asia",
                        "children":[
                            {"name": "Kyrgyz Republic"},
                            {"name": "Tajikistan"},
                            {"name": "Ukraine"},
                            {"name": "Uzbekistan"}
                        ]
                    },
                    {
                        "name":"Latin America & Caribbean",
                        "children":[
                            {"name": "Bolivia"},
                            {"name": "Haiti"},
                            {"name": "Honduras"},
                            {"name": "Nicaragua"}
                        ]
                    },
                    {
                        "name":"Middle East & North Africa",
                        "children":[
                            {"name": "Algeria"},
                            {"name": "Djibouti"},
                            {"name": "Egypt, Arab Rep."},
                            {"name": "Iran, Islamic Rep."},
                            {"name": "Jordan"},
                            {"name": "Lebanon"},
                            {"name": "Morocco"},
                            {"name": "Tunisia"}
                        ]
                    },
                    {
                        "name":"Sub-Saharan Africa",
                        "children":[
                            {"name": "Angola"},
                            {"name": "Cabo Verde"},
                            {"name": "Cameroon"},
                            {"name": "Congo, Rep."},
                            {"name": "Comoros"},
                            {"name": "Guinea"},
                            {"name": "Kenya"},
                            {"name": "Lesotho"},
                            {"name": "Mauritania"},
                            {"name": "Ghana"},
                            {"name": "Zambia"},
                            {"name": "Nigeria"},
                            {"name": "São Tomé and Principe"},
                            {"name": "Eswatini"},
                            {"name": "Tanzania"},
                            {"name": "Benin"},
                            {"name": "Côte d'Ivoire"},
                            {"name": "Senegal"},
                            {"name": "Zimbabwe"}
                        ]
                    },
                    {
                        "name":"South Asia",
                        "children":[
                            {"name": "Bangladesh"},
                            {"name": "Bhutan"},
                            {"name": "India"},
                            {"name": "Nepal"},
                            {"name": "Pakistan"},
                            {"name": "Sri Lanka"}
                        ]
                    }
                ]
            },
            {
                "name":"Low income",
                "children":[
                    {
                        "name":"East Asia & Pacific",
                        "children":[
                            {"name": "Korea, Dem. People's Rep."}
                        ]
                    },
                    {
                        "name":"Middle East & North Africa",
                        "children":[
                            {"name": "Syrian Arab Republic"},
                            {"name":"Yemen, Rep."}
                        ]
                    },
                    {
                        "name":"Sub-Saharan Africa",
                        "children":[
                            {"name": "Burundi"},
                            {"name": "Central African Republic"},
                            {"name": "Chad"},
                            {"name": "Congo, Dem. Rep."},
                            {"name": "Eritrea"},
                            {"name": "Ethiopia"},
                            {"name": "Gambia, The"},
                            {"name": "Liberia"},
                            {"name": "Madagascar"},
                            {"name": "Malawi"},
                            {"name": "Mozambique"},
                            {"name": "Rwanda"},
                            {"name": "Sierra Leone"},
                            {"name": "Somalia"},
                            {"name": "South Sudan"},
                            {"name": "Sudan"},
                            {"name": "Uganda"},
                            {"name": "Burkina Faso"},
                            {"name": "Guinea-Bissau"},
                            {"name": "Mali"},
                            {"name": "Niger"},
                            {"name": "Togo"}
                        ]
                    },
                    {
                        "name":"South Asia",
                        "children":[
                            {"name": "Afghanistan"}
                        ]
                    }
                ]
            }
        ]
}

opts = {
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove",
    },
    "series": [
        {
            "type": "tree",
            "data": [data],
            "top": "1%",
            "left": "10%",
            "bottom": "1%",
            "right": "20%",
            "symbolSize": 7,
            "label": {
                "position": "bottom",
                "verticalAlign": "middle",
                "align": "right",
                "fontSize": 12,
                "color": "black",
            },
            "leaves": {
                "label": {
                    "position": "right",
                    "verticalAlign": "middle",
                    "align": "left",
                }
            },
            # "emphasis": {
            #     "focus": 'descendant'
            # },
            "expandAndCollapse": True,
            "animationDuration": 550,
            "animationDurationUpdate": 750,
        },
        
    ],
}

@callback(
        Output("factor_pg6","options"),
        Input("year_dropdown_pg6","value"),
)
def change_options(year_dropdown_pg1):
    from pages import settings        
    return settings.global_options

def generate_animation_bar(factor_pg6):
    if(factor_pg6==None):
        return px.bar()
    from pages import settings 
    df_fact=pd.read_csv('./Data_files/'+factor_pg6+'.csv')
    val=["Upper middle income","Lower middle income","Low income","High income"]
    df_fact=df_fact[df_fact['Country Name'].isin(val)]

    df_fact=pd.melt(df_fact, id_vars=['Country Name'], value_vars=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'])

    # sorted_df_fact = df_fact.sort_values(by=year_dropdown_pg6, ascending=False)
    # print(df_fact)
    df_fact=df_fact.set_axis(['Income Category','year',settings.data_dictionary[factor_pg6]],axis=1)
    fig = px.bar(df_fact, x="Income Category", y=settings.data_dictionary[factor_pg6],animation_frame="year")

    fig.layout.yaxis.title=settings.data_dictionary[factor_pg6]
    return fig

@callback(
        Output("stacked_bar_pg6","figure"),
        Input("factor_pg6","value"),
)
def update_stacked_bar_pg6(factor_pg6):
    return generate_animation_bar(factor_pg6)

layout = html.Div([
    html.Div(className="text-container",
             children=[
                 html.H1('Economic Tier Overview', className='title'),
                 html.Br(),
                 html.H2(
                    "Explore countries grouped by income levels to understand how factors, amenities, and quality of life vary across different economic categories. Witness the developmental trajectory of these nations over the years in relation to their income levels.",
                    className='description'),
             ]
             ),
    html.Div([
    dash_echarts.DashECharts(
        option = opts,
        id='echarts',
        style={
            "width": '80vw',
            "height": '100vh',
        }
    ),
    dcc.Dropdown(
                options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
                value="2018",
                id="year_dropdown_pg6",
                # style={"width": "100%"},
                style={"display": "None"}
            ),
    dcc.Dropdown(
                options=[
                    {'label': 'Population', 'value': 'pop_tot_updated'},
                    {'label': 'Population Growth', 'value': 'pop_growth_updated'},
                    {'label': 'GDP', 'value': 'gdp_current_updated'},
                ],
                value="pop_tot_updated",
                id="factor_pg6",
                style={"width": "100%"}
            ),
    dcc.Graph(id="stacked_bar_pg6"),

])
], className="page1_style")

