import plotly.express as px
import pandas as pd
import dash
from dash import dcc, Input, Output, html, callback, clientside_callback
import dash_bootstrap_components as dbc

dash.register_page(__name__,order=10)

count_list= ['Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/page7.css']

@callback(
        Output("factor_pg9","options"),
        Input("country_dropdown_pg9","value"),
)
def change_options(year_dropdown_pg1):
    from pages import settings
    return settings.global_options

@callback(
        Output("fig_pg9","children"),
        Input("country_dropdown_pg9","value"),
        Input("factor_pg9","value"),
)
def generate_comparison_charts(country_dropdown_pg9,factor_pg9):
    from pages import settings
    if type(factor_pg9)==str:
        df_w_fact=pd.read_csv('./Data_files/'+factor_pg9+'.csv')

        df_w_fact_t=df_w_fact.transpose()
        new_header = df_w_fact_t.iloc[0] 
        df_w_fact_t = df_w_fact_t[4:]
        df_w_fact_t.columns = new_header
        df_w_fact_t.index.name = 'year'
        df_w_fact_t.to_csv('update.csv')
        df_w_fact_t = pd.read_csv('update.csv')

        df1=pd.melt(df_w_fact_t, id_vars=['year'], value_vars=country_dropdown_pg9)
        df1=df1.set_axis(['year','Country',settings.data_dictionary[factor_pg9]],axis=1)
        fig = px.line(df1, x="year", y=settings.data_dictionary[factor_pg9], color='Country')
        fig.layout.yaxis.title=settings.data_dictionary[factor_pg9]
        fig.update_layout(hovermode="x unified",width=600)
        return dcc.Graph(figure=fig)
    
    else:
        fig_list=[]
        h=[]
        i=0
        for fact in factor_pg9:
            df_w_fact=pd.read_csv('./Data_files/'+fact+'.csv')

            df_w_fact_t=df_w_fact.transpose()
            new_header = df_w_fact_t.iloc[0] 
            df_w_fact_t = df_w_fact_t[4:]
            df_w_fact_t.columns = new_header
            df_w_fact_t.index.name = 'year'
            df_w_fact_t.to_csv('update.csv')
            df_w_fact_t = pd.read_csv('update.csv')

            df1=pd.melt(df_w_fact_t, id_vars=['year'], value_vars=country_dropdown_pg9)
            # print(df1)
            df1=df1.set_axis(['year','Country',settings.data_dictionary[fact]],axis=1)
            fig = px.line(df1, x="year", y=settings.data_dictionary[fact], color='Country')
            fig.layout.yaxis.title=settings.data_dictionary[fact]
            fig.update_layout(hovermode="x unified",width=600)
            if (i%2==0):
                h.append(dcc.Graph(figure=fig))
                i=i+1
            else:
                h.append(dcc.Graph(figure=fig))
                fig_list.append(html.Div(h,style={"display":"flex"}))
                i=i+1
                h=[]
        if(len(h)!=0):
            fig_list.append(h[0])
        return fig_list

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
                 html.Label("Select Countries:"),
                 dcc.Dropdown(
                     options=count_list,
                     value=['India', 'China', 'Japan', 'United States'],
                     id="country_dropdown_pg9",
                     multi=True,
                     style={"width": "90%"}
                 ),
                 html.Label("Select Factors:"),
                 dcc.Dropdown(
                     options=[
                         {'label': 'GDP', 'value': 'gdp_current_updated'},
                         {'label': 'Population', 'value': 'pop_tot_updated'},
                         {'label': 'Population Growth', 'value': 'pop_growth_updated'},
                         {'label': 'Agriculture %GDP Updated', 'value': 'agriculture_percent_gdp_updated'},
                     ],
                     value="gdp_current_updated",
                     id="factor_pg9",
                     multi=True,
                     style={"width": "70%"}
                 ),
             ]
             ),
    html.Div(className="plot-container",
             children=[
                 html.Div(id="fig_pg9"),
             ]
             ),
             dbc.Button([html.Span("\u25B2")], color="primary", className="me-1", id='to_top', n_clicks=0, style={'position': 'fixed', 'bottom': '20px', 'right': '20px'})

], className="page1_style")
clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks) {
            window.scrollTo({top: 0, behavior: 'smooth'});
        }
        return 0;
    }
    """,
    Output('to_top', 'n_clicks'),
    Input('to_top', 'n_clicks')
)

