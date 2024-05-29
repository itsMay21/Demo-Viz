import plotly.express as px
import pandas as pd
import dash
from dash import Dash, dcc, Input, Output, html, callback, ctx,State
import json
import dash_echarts
from dash.exceptions import PreventUpdate
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
import datetime
import io
import os


dash.register_page(__name__,order=10)
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/settings.css']

backup_options=[
    {"label": "Access To Electricity", "value": "access_to_electricity_updated"},
    {"label": "Adjusted Net Income Per Capita", "value": "adjusted_net_income_per_capita_updated"},
    {"label": "Age Dependency Ratio", "value": "age_dependency_ratio_updated"},
    {"label": "Agriculture Percent Gdp", "value": "agriculture_percent_gdp_updated"},
    {"label": "Current Health Expenditure", "value": "current_health_expenditure_updated"},
    {"label": "Education Expend Percent Public Expend", "value": "education_expend_percent_public_expend_updated"},
    {"label": "Electricity Prod Renewable", "value": "electricity_prod_renewable_updated"},
    {"label": "Expense Percent Gdp", "value": "expense_percent_gdp_updated"},
    {"label": "Export Annual Growth", "value": "export_annual_growth_updated"},
    {"label": "Export Percent Of Gdp", "value": "export_percent_of_gdp_updated"},
    {"label": "Female Male Labor Ratio", "value": "female_male_labor_ratio_updated"},
    {"label": "Gdp Current", "value": "gdp_current_updated"},
    {"label": "Gdp Per Capita", "value": "gdp_per_capita_updated"},
    {"label": "Gdp Per Capita percent Growth", "value": "gdp_per_capita_%_growth_updated"},
    {"label": "Imports", "value": "imports_updated"},
    {"label": "Individuals Using The Internet", "value": "individuals_using_the_internet_updated"},
    {"label": "Life Expectancy", "value": "life_expectancy_updated"},
    {"label": "Literacy Rate", "value": "literacy_rate_updated"},
    {"label": "Manufacturing Percent Gdp", "value": "manufacturing_percent_gdp_updated"},
    {"label": "Military Expend", "value": "military_expend_updated"},
    {"label": "Percent Population In Agri", "value": "percent_pop_in_agri_updated"},
    {"label": "Percent Population In Industry", "value": "percent_pop_in_industry_updated"},
    {"label": "Percent Population In Services", "value": "percent_pop_in_services_updated"},
    {"label": "Population Growth", "value": "pop_growth_updated"},
    {"label": "Population Total", "value": "pop_tot_updated"},
    {"label": "R&D Expend Percent Gdp", "value": "r&d_expend_percent_gdp_updated"},
    {"label": "Services Percent Gdp", "value": "services_percent_gdp_updated"}
]

ideal_format=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
ideal_format_alt=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

global global_k
global_k='Filter'

global extra_or_not
extra_or_not="Extrapolate"

global extrapolate_const
extrapolate_const="5"

global extrapolate_delta_cap
extrapolate_delta_cap="5"

global global_options
global_options=[
    {"label": "Access To Electricity", "value": "access_to_electricity_updated"},
    {"label": "Adjusted Net Income Per Capita", "value": "adjusted_net_income_per_capita_updated"},
    {"label": "Age Dependency Ratio", "value": "age_dependency_ratio_updated"},
    {"label": "Agriculture Percent Gdp", "value": "agriculture_percent_gdp_updated"},
    {"label": "Current Health Expenditure", "value": "current_health_expenditure_updated"},
    {"label": "Education Expend Percent Public Expend", "value": "education_expend_percent_public_expend_updated"},
    {"label": "Electricity Prod Renewable", "value": "electricity_prod_renewable_updated"},
    {"label": "Expense Percent Gdp", "value": "expense_percent_gdp_updated"},
    {"label": "Export Annual Growth", "value": "export_annual_growth_updated"},
    {"label": "Export Percent Of Gdp", "value": "export_percent_of_gdp_updated"},
    {"label": "Female Male Labor Ratio", "value": "female_male_labor_ratio_updated"},
    {"label": "Gdp Current", "value": "gdp_current_updated"},
    {"label": "Gdp Per Capita", "value": "gdp_per_capita_updated"},
    {"label": "Gdp Per Capita percent Growth", "value": "gdp_per_capita_%_growth_updated"},
    {"label": "Imports", "value": "imports_updated"},
    {"label": "Individuals Using The Internet", "value": "individuals_using_the_internet_updated"},
    {"label": "Life Expectancy", "value": "life_expectancy_updated"},
    {"label": "Literacy Rate", "value": "literacy_rate_updated"},
    {"label": "Manufacturing Percent Gdp", "value": "manufacturing_percent_gdp_updated"},
    {"label": "Military Expend", "value": "military_expend_updated"},
    {"label": "Percent Population In Agri", "value": "percent_pop_in_agri_updated"},
    {"label": "Percent Population In Industry", "value": "percent_pop_in_industry_updated"},
    {"label": "Percent Population In Services", "value": "percent_pop_in_services_updated"},
    {"label": "Population Growth", "value": "pop_growth_updated"},
    {"label": "Population Total", "value": "pop_tot_updated"},
    {"label": "R&D Expend Percent Gdp", "value": "r&d_expend_percent_gdp_updated"},
    {"label": "Services Percent Gdp", "value": "services_percent_gdp_updated"}
]

global data_dictionary
data_dictionary = {
    "access_to_electricity": "Access To Electricity",
    "access_to_electricity_updated": "Access To Electricity",
    "adjusted_net_income_per_capita": "Adjusted Net Income Per Capita",
    "adjusted_net_income_per_capita_updated": "Adjusted Net Income Per Capita",
    "age_dependency_ratio": "Age Dependency Ratio",
    "age_dependency_ratio_updated": "Age Dependency Ratio",
    "agriculture_percent_gdp": "Agriculture Percent Gdp",
    "agriculture_percent_gdp_updated": "Agriculture Percent Gdp",
    "air_transport_freight": "Air Transport Freight",
    "air_transport_freight_updated": "Air Transport Freight",
    "birth_rate_per_1000_people": "Birth Rate Per 1000 People",
    "birth_rate_per_1000_people_updated": "Birth Rate Per 1000 People",
    "CO2_emmissions_metric_tons_per_capita": "Co2 Emmissions Metric Tons Per Capita",
    "CO2_emmissions_metric_tons_per_capita_updated": "Co2 Emmissions Metric Tons Per Capita",
    "current_account_balance_percent_gdp": "Current Account Balance Percent Gdp",
    "current_account_balance_percent_gdp_updated": "Current Account Balance Percent Gdp",
    "current_health_expenditure": "Current Health Expenditure",
    "current_health_expenditure_updated": "Current Health Expenditure",
    "education_expend_percent_public_expend": "Education Expend Percent Public Expend",
    "education_expend_percent_public_expend_updated": "Education Expend Percent Public Expend",
    "electricity_prod_renewable": "Electricity Prod Renewable",
    "electricity_prod_renewable_updated": "Electricity Prod Renewable",
    "expense_percent_gdp": "Expense Percent Gdp",
    "expense_percent_gdp_updated": "Expense Percent Gdp",
    "export_annual_growth": "Export Annual Growth",
    "export_annual_growth_updated": "Export Annual Growth",
    "export_percent_of_gdp": "Export Percent Of Gdp",
    "export_percent_of_gdp_updated": "Export Percent Of Gdp",
    "female_male_labor_ratio": "Female Male Labor Ratio",
    "female_male_labor_ratio_updated": "Female Male Labor Ratio",
    "fertility_rate_per_1000_women": "Fertility Rate Per 1000 Women",
    "fertility_rate_per_1000_women_updated": "Fertility Rate Per 1000 Women",
    "gdp_current": "Gdp Current",
    "gdp_current_updated": "Gdp Current",
    "gdp_per_capita": "Gdp Per Capita",
    "gdp_per_capita_updated": "Gdp Per Capita",
    "gdp_per_capita_%_growth": "Gdp Per Capita % Growth",
    "gdp_per_capita_%_growth_updated": "Gdp Per Capita % Growth",
    "gdp_per_capita_%_growth_updated1": "Gdp Per Capita % Growth Updated1",
    "gdp_per_capita_%_growth_updated1_updated": "Gdp Per Capita % Growth Updated1",
    "gross_savings_percent_gdp": "Gross Savings Percent Gdp",
    "gross_savings_percent_gdp_updated": "Gross Savings Percent Gdp",
    "hospital_beds_per_1000": "Hospital Beds Per 1000",
    "hospital_beds_per_1000_updated": "Hospital Beds Per 1000",
    "imports": "Imports",
    "imports_updated": "Imports",
    "individuals_using_the_internet": "Individuals Using The Internet",
    "individuals_using_the_internet_updated": "Individuals Using The Internet",
    "labor_force_participation_rate_percent_population": "Labor Force Participation Rate Percent Population",
    "labor_force_participation_rate_percent_population_updated": "Labor Force Participation Rate Percent Population",
    "life_expectancy": "Life Expectancy",
    "life_expectancy_updated": "Life Expectancy",
    "literacy_rate": "Literacy Rate",
    "literacy_rate_updated": "Literacy Rate",
    "manufacturing_percent_gdp": "Manufacturing Percent Gdp",
    "manufacturing_percent_gdp_updated": "Manufacturing Percent Gdp",
    "military_expend": "Military Expend",
    "military_expend_updated": "Military Expend",
    "percent_pop_in_agri": "Percent Population In Agri",
    "percent_pop_in_agri_updated": "Percent Population In Agri",
    "percent_pop_in_industry": "Percent Population In Industry",
    "percent_pop_in_industry_updated": "Percent Population In Industry",
    "percent_pop_in_services": "Percent Population In Services",
    "percent_pop_in_services_updated": "Percent Population In Services",
    "pop_growth": "Population Growth",
    "pop_growth_updated": "Population Growth",
    "pop_tot": "Population Total",
    "pop_tot_updated": "Population Total",
    "r&d_expend_percent_gdp": "R&D Expend Percent Gdp",
    "r&d_expend_percent_gdp_updated": "R&D Expend Percent Gdp",
    "services_percent_gdp": "Services Percent Gdp",
    "services_percent_gdp_updated": "Services Percent Gdp"
}

@callback(
        Output("settings_store","data"),
        Input("settings_dropdown","value"),
)
def generate_settings_store(settings_dropdown):
    # print('i m in: ',settings_dropdown)
    global global_k
    global_k=settings_dropdown
    return settings_dropdown

@callback(
        Output("settings_store3","data"),
        Input("settings_dropdown_extra_or_not","value"),
)
def generate_settings_store(settings_dropdown_extra_or_not):
    # print('i m in: ',settings_dropdown)
    global extra_or_not
    extra_or_not=settings_dropdown_extra_or_not
    return settings_dropdown_extra_or_not

@callback(
        Output("settings_store1","data"),
        Input("extrapolate_settings","value"),
)
def generate_extrapolate_store(extrapolate_settings):
    global extrapolate_const
    extrapolate_const=extrapolate_settings
    return extrapolate_settings

@callback(
        Output("settings_store2","data"),
        Input("extrapolate_dela_cap_settings","value"),
)
def generate_extrapolate_store(extrapolate_dela_cap_settings):
    global extrapolate_delta_cap
    extrapolate_delta_cap=extrapolate_dela_cap_settings
    return extrapolate_dela_cap_settings

def generate_updated_file(df,filename,flag=0,extra_const="5"):
    countries=[
    "Africa Eastern and Southern",
    "Africa Western and Central",
    "Arab World",
    "Central Europe and the Baltics",
    "Caribbean small states",
    "East Asia & Pacific (excluding high income)",
    "Early-demographic dividend",
    "East Asia & Pacific",
    "Europe & Central Asia (excluding high income)",
    "Europe & Central Asia",
    "Euro area",
    "European Union",
    "Fragile and conflict affected situations",
    # "High income",
    "Heavily indebted poor countries (HIPC)",
    "IBRD only",
    "IDA & IBRD total",
    "IDA total",
    "IDA blend",
    "IDA only",
    "Latin America & Caribbean (excluding high income)",
    "Latin America & Caribbean",
    "Least developed countries: UN classification",
    # "Low income",
    # "Lower middle income",
    "Low & middle income",
    "Late-demographic dividend",
    "Middle East & North Africa",
    "Middle income",
    "Middle East & North Africa (excluding high income)",
    "North America",
    "OECD members",
    "Other small states",
    "Pre-demographic dividend",
    "Pacific island small states",
    "Post-demographic dividend",
    "South Asia",
    "Sub-Saharan Africa (excluding high income)",
    "Sub-Saharan Africa",
    "Small states",
    "East Asia & Pacific (IDA & IBRD)",
    "Europe & Central Asia (IDA & IBRD)",
    "Latin America & Caribbean (IDA & IBRD)",
    "Middle East & North Africa (IDA & IBRD)",
    "South Asia (IDA & IBRD)",
    "Sub-Saharan Africa (IDA & IBRD)",
    # "Upper middle income",
    # "World",
    "Sub-Saharan Africa (IDA & IBRD countries)",
    "East Asia & Pacific (IDA & IBRD countries)",
    "Europe & Central Asia (IDA & IBRD countries)",
    "Latin America & the Caribbean (IDA & IBRD countries)",
    "Middle East & North Africa (IDA & IBRD countries)",
    "Not classified",
    ]

    for row in df.iterrows():
        if row[1]['Country Name'] in countries:
            df=df.drop(row[0])
    max_value_lim=0
    min_value_lim=0
    for iter in range(2):
        if(iter==1):
            if flag==1:
                df= pd.read_csv('./Data_files/'+filename[:-4]+"_updated.csv") 
            else:
                df= pd.read_csv('./Data_files/uploaded_'+filename[:-4]+"_updated.csv")
        for index,row in df.iterrows():
            max_value_lim=0
            min_value_lim=0
            # print(df.at[index,'2020'])
            max_delta_lim=int(extrapolate_delta_cap)
            min_delta_lim=-int(extrapolate_delta_cap)
            # print(max_delta_lim)
            b_yr=1960
            f_yr=-1
            count=0
            delta=0
            delta_f=0
            # if(iter==0):
            for j in range(1960,2023):
                if(pd.isna(row[str(j)])==True):
                    continue
                max_value_lim=max(max_value_lim,float(row[str(j)]))
                min_value_lim=min(min_value_lim,float(row[str(j)]))
                # if row['Country Name']=='Eritrea':
                #     print('in : ',max_value_lim, min_value_lim)
            for i in range(1960,2023):
                # print(row[str(i)],'\n')
                #no value read till now
                if(count==0 and pd.isna(row[str(i)])):
                    delta=0
                    f_yr=-1
                    # print("in1")
                    continue
                #value read but not first
                elif(pd.isna(row[str(i)])!=True and count!=0):
                    delta=0
                    f_yr=-1
                    b_yr=i
                    # print("in2")

                # first value read
                elif(pd.isna(row[str(i)])!=True and count==0):
                    delta=0
                    f_yr=-1
                    b_yr=i
                    count=1
                    # print(index,i,"in3")
                elif(pd.isna(row[str(i)]) and count!=0):
                    # print(index,i,"in4")
                    if(f_yr!=-1):
                        df.at[index,str(i)]=row[str(b_yr)]+delta*(i-b_yr)
                        # print(row[str(b_yr)]+delta*(i-b_yr))
                        # print()
                    else:
                        for j in range(b_yr+1,2023):
                            if(pd.isna(row[str(j)])):
                                continue
                            else:
                                f_yr=j
                                delta=(row[str(j)]-row[str(b_yr)])/(j-b_yr)
                                break
                        if(f_yr!=-1):
                            df.at[index,str(i)]=row[str(b_yr)]+delta*(i-b_yr)
                            # print(row[str(b_yr)]+delta*(i-b_yr))
                            # print()
                        else:
                            if(extra_or_not=="No Extrapolate"):
                                break
                            if(iter==1):
                                # print("in final case")
                                # df.to_csv(filename+"_updated.csv")
                                # df = pd.read_csv(filename+"_updated.csv")
                                div=0
                                for k in range(int(extra_const)):
                                    if b_yr-k-1<1960:
                                        continue
                                    if row[str(b_yr-k-1)]==0:
                                        # print("exc1")
                                        break
                                    if((row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]>max_delta_lim):
                                        delta_f=delta_f+max_delta_lim
                                    elif((row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]<min_delta_lim):
                                        delta_f=delta_f+min_delta_lim
                                    else:
                                        delta_f=delta_f+(row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]
                                    # delta_f=delta_f+(row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]
                                    div=div+1
                                if div==0:
                                    # print("exc2")
                                    delta_f=0
                                else:
                                    delta_f=delta_f/div
                                for j in range(b_yr+1,2023):
                                    if(row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))<max_value_lim) and (row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))>min_value_lim):
                                        df.at[index,str(j)]=row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))
                                    else:
                                        # if row['Country Name']=='Eritrea':
                                        #     print('in : ',max_value_lim, min_value_lim)
                                        df.at[index,str(j)]=max_value_lim if row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))>max_value_lim else min_value_lim
                                    # print(index,row[str(b_yr)]*(pow((1+delta_f),(j-b_yr))))
                                break

        # print(df)
        if flag==1:
            df.to_csv('./Data_files/'+filename[:-4]+"_updated.csv",index=False)   
        else:
            df.to_csv('./Data_files/uploaded_'+filename[:-4]+"_updated.csv",index=False)

def parse_contents(contents, filename, date):
    if 'csv' not in filename:
        return html.Div([
        html.H5(filename),
        html.H5("Error file is not in correct format, ideally should be in csv!!")
    ])
    content_type, content_string = contents.split(',')
    print(filename)
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df.to_csv('./Data_files/uploaded_'+filename,index=False)
            uploaded_list=df.columns.tolist()
            if(uploaded_list!=ideal_format and uploaded_list!=ideal_format_alt):
                # print("i m not uploading")
                return html.Div([
                    html.H5(filename),
                    html.H5("Error file is not in correct format, header should be!!"),
                    html.H5(uploaded_list)
                ])
            else:
                # print("i m uploading")
                global_options.append({'label':'uploaded_'+filename[:-4],'value':'uploaded_'+filename[:-4]+'_updated'})
                data_dictionary['uploaded_'+filename[:-4]]='uploaded_'+filename[:-4]
                data_dictionary['uploaded_'+filename[:-4]+"_updated"]='uploaded_'+filename[:-4]+"_updated"
                generate_updated_file(df,filename)
   
    except Exception as e:
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@callback(
        Output('output-data-upload', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
        State('upload-data', 'last_modified')
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

@callback(
        Output('del_div', 'children'),
        Input('delete_button', 'n_clicks'),
        prevent_initial_call=True
)
def delete_uploaded_files(n_clicks):
    directory_path = './Data_files'
    prefix = 'uploaded'
    l=["removed files: "]
    l.append('\n')
    for filename in os.listdir(directory_path):
        if filename.startswith(prefix):
            file_path = os.path.join(directory_path, filename)
            os.remove(file_path)
            l.append(filename)
            l.append('\n')
        global global_options
        global_options=backup_options.copy()
        data_dictionary.pop('uploaded_'+filename[:-4],None)
        data_dictionary.pop('uploaded_'+filename[:-4]+"_updated",None)
    # print("inside")
    return l

@callback(
        Output('filter_div', 'children'),
        Input('filter_button', 'n_clicks'),
        prevent_initial_call=True
)
def filter_files(n_clicks):
    directory_path = './Data_files'
    p1="electricity"
    p2="export_per"
    p3="imports"
    p4="individuals"
    d_list=["electricity","export_per"]
    for filename in os.listdir(directory_path):
        # if filename.startswith(p1):
        #     continue
        # if filename.startswith(p2):
        #     continue
        # if filename.startswith(p3):
        #     continue
        # if filename.startswith(p4):
        #     continue
        if filename.endswith("_updated.csv"):
            continue
        print(filename)
        df=pd.read_csv('./Data_files/'+filename)
        generate_updated_file(df,filename,1,extrapolate_const)
    return "DONE!!"


layout = html.Div([
    dcc.Store(id='settings_store'),
    dcc.Store(id='settings_store1'),
    dcc.Store(id='settings_store2'),
    dcc.Store(id='settings_store3'),

    html.Div([
        html.Label('Filter:', className='label', style={'font-family': 'Arial'}),
        dcc.RadioItems(
            options=[
                {'label': 'Filter', 'value': 'Filter'},
                {'label': 'No Filter', 'value': 'No Filter'}
            ],
            value='Filter',
            id='settings_dropdown',
            inline=True,
            persistence=True,
            className='radio-container'
        ),
    ], className='container-blue'),

    html.Div([
        html.Label('Extrapolation:', className='label', style={'font-family': 'Arial'}),
        dcc.RadioItems(
            options=[
                {'label': 'Extrapolate', 'value': 'Extrapolate'},
                {'label': 'No Extrapolate', 'value': 'No Extrapolate'}
            ],
            value='Extrapolate',
            id='settings_dropdown_extra_or_not',
            inline=True,
            className='radio-container'
        ),
    ], className='container-blue'),

    html.Div([
        html.Label('Select extrapolation Constant:', className='label', style={'font-family': 'Arial'}),
        dcc.Dropdown(
            options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            value="5",
            id="extrapolate_settings",
            clearable=False,
            style={"width": "80%"},  # Increase the width to 100%
            className='dropdown-container'
        ),
    ], className='container-blue'),

    html.Div([
        html.Label('Select extrapolation delta cap:', className='label', style={'font-family': 'Arial'}),
        dcc.Dropdown(
            options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"],
            value="5",
            id="extrapolate_dela_cap_settings",
            clearable=False,
            style={"width": "80%"},  # Increase the width to 100%
            className='dropdown-container'
        ),
    ], className='container-blue'),

    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '99%',
                'height': '250px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),
    ], className='container-blue'),

    html.Div([
        html.Button('Delete', id='delete_button', n_clicks=0, className='button'),
        html.Button('Filter', id='filter_button', n_clicks=0, className='button'),
    ], className='container-blue'),

    html.Div(id="del_div", children="files deleted: ", className='result-container'),
    html.Div(id="filter_div", children="files filtered: ", className='result-container')
], className="page1_style")


