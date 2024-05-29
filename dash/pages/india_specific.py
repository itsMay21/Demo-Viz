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


dash.register_page(__name__,order=6)

with open('district.geojson') as response:
    geodata = json.loads(response.read())



@callback(
        Output("ind_map","figure"),
        Input("ind_economic_dropdown","value"),
        Input("sub_category_dropdown","value"),
        Input("sub_category_dropdown_1","value"),
)
def generate_crop_map(ind_economic_dropdown,sub_category_dropdown,sub_category_dropdown_1):
    if ind_economic_dropdown=="Agriculture":
        if sub_category_dropdown is None:
            file="Arhar"
        else:
            file=sub_category_dropdown
        df_refined=pd.read_csv("Crops/crop_"+ file +".csv")
        fig_gl = px.choropleth_mapbox(
                    df_refined, 
                    geojson = geodata, 
                    locations = df_refined.Districts, 
                    color = df_refined["Production"], 
                    color_continuous_scale = "YlGn",
                    range_color = [max(df_refined["Production"]),min(df_refined["Production"])],
                    featureidkey = "properties.District",
                    mapbox_style = "carto-positron",
                    center = {"lat": 22.5937, "lon": 82.9629},
                    hover_name="STATE",
                    hover_data=['STATE'],
                    zoom = 3.0,
                    animation_frame = df_refined["Crop_Year"],
                    )
    else:
        if sub_category_dropdown_1 is None:
            file="TOTAL CURRENT PRICES"
        else:
            file=sub_category_dropdown_1
        df_refined=pd.read_csv("district_gdp_current_prices.csv")
        fig_gl = px.choropleth_mapbox(
                        df_refined, 
                        geojson = geodata, 
                        locations = df_refined.Districts, 
                        color = df_refined[file], 
                        color_continuous_scale = "YlGn",
                        range_color = [max(df_refined[file]),min(df_refined[file])],
                        featureidkey = "properties.District",
                        mapbox_style = "carto-positron",
                        center = {"lat": 22.5937, "lon": 82.9629},
                        hover_name="STATE",
                        hover_data=['STATE'],
                        zoom = 3.0,
                        # animation_frame = df_refined["Year"],
                        )
    fig_gl.update_layout(autosize=False,
                height=700,
                width=1000,
                margin={"r":0,"t":0,"l":0,"b":0},
                )
    fig_gl.update_traces(marker_line_width=0.3)

    return fig_gl

layout = html.Div([
    html.H1('This is our India Specific page'),
    html.Br(),
    dcc.Dropdown(
                options=["Agriculture","GDP"],
                value="Agriculture",
                id="ind_economic_dropdown",
                style={"width": "40%"}
            ),
    dcc.Dropdown(
                options=['Arhar','Bajra','Banana','Cowpea(Lobia)','Gram','Groundnut','Jowar','Linseed','Maize','Onion','Potato','Ragi','Rice','Soyabean','Sugarcane','Sunflower','Wheat','Barley','Peas & beans (Pulses)','Jute','Oilseeds total'],
                value="Arhar",
                id="sub_category_dropdown",
                style={"width": "40%"}
            ),
    dcc.Dropdown(
                options=["PRIMARY SECTOR","SECONDARY SECTOR","TERTIARY SECTOR","TOTAL CURRENT PRICES","PER CAPITA CURRENT PRICES"],
                value="TOTAL CURRENT PRICES",
                id="sub_category_dropdown_1",
                style={"width": "40%"}
            ),
    dcc.Graph(id="ind_map"),
])