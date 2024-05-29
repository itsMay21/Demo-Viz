import dash
from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.config.suppress_callback_exceptions=True
parity=0
SIDEBAR_OPEN = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "150px",
    "background-color": "black",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "color": "white",
    "padding-top": "50px",
    "overflow-y": "scroll"
}

SIDEBAR_CLOSE = {
    "position": "fixed",
    "top": 0,
    "left": "-150PX",
    "bottom": 0,
    "width": "150px",
    "background-color": "black",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "color": "white",
    "padding-top": "50px",
    "overflow-y": "scroll"
}

CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-right": "2rem",
    "padding": "2rem 1rem"
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "-150px",
    "margin-right": "2rem",
    "padding": "2rem 1rem"
}

SIDEBAR_TOGGLE_STYLE_CLOSE = {
    "transition": "margin-left .5s",
    "margin-left": "-150px",
}

SIDEBAR_TOGGLE_STYLE_OPEN = {
    "transition": "margin-left .5s",
    "margin-left": "0px",
}
# Define the sidebar content
sidebar = html.Div([
    html.Div([
        html.Button('Homepage', id='home', n_clicks=0, className="button_style" ),
        html.Button('World trend', id='pg1', n_clicks=0, className="button_style"),
        html.Button('Factor relation', id='pg2', n_clicks=0, className="button_style"),
        html.Button('World Heatmap', id='pg3', n_clicks=0, className="button_style"),
        html.Button('Sectoral Distrib', id='pg4', n_clicks=0, className="button_style"),
        # html.Button('Cross Sectional', id='pg5', n_clicks=0, className="button_style"),
        html.Button('Income Category', id='pg6', n_clicks=0, className="button_style"),
        html.Button('Parallel Coordinate Map', id='pg8', n_clicks=0, className="button_style"),
        html.Button('Comparison page', id='pg7', n_clicks=0, className="button_style"),
        # html.Button('Comparison page updated', id='pg9', n_clicks=0, className="button_style"),
        html.Button('Settings', id='settings', n_clicks=0, className="button_style"),
    ])
], style=SIDEBAR_OPEN, id="sidebar")

# Define the initial content as an empty div
initial_content = html.Div([
    dcc.Store(id='side_click'),
    dcc.Location(id='url', refresh=False),
    dbc.Button("Close Sidebar", color="primary", className="me-1", id="sidebar-toggle", style=SIDEBAR_TOGGLE_STYLE_OPEN),
    html.Div(id='initial-content',style=CONTENT_STYLE),
], className="content_style")


# Define the app layout
app.layout = html.Div([sidebar, initial_content])

@app.callback(
        [Output("sidebar", "style"),
        Output("initial-content", "style"),
        Output("side_click", "data"),
        Output("sidebar-toggle", "style")],
        Output("sidebar-toggle","children"),
        Input("sidebar-toggle", "n_clicks"),
        [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_CLOSE
            content_style = CONTENT_STYLE1
            sidebar_toggle_style = SIDEBAR_TOGGLE_STYLE_CLOSE
            sidebar_toggle_value = "\u25B6"
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_OPEN
            content_style = CONTENT_STYLE
            sidebar_toggle_style = SIDEBAR_TOGGLE_STYLE_OPEN
            sidebar_toggle_value = "\u25C0" 
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_OPEN
        content_style = CONTENT_STYLE
        sidebar_toggle_style = SIDEBAR_TOGGLE_STYLE_OPEN
        sidebar_toggle_value = "\u25C0"  
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick, sidebar_toggle_style, sidebar_toggle_value

# Callback to update the initial content when "First" button is clicked
@app.callback(
    Output('initial-content', 'children'),
    [Input('pg1', 'n_clicks'),
     Input('pg2', 'n_clicks'),
     Input('pg3', 'n_clicks'),
     Input('pg4', 'n_clicks'),
    #  Input('pg5', 'n_clicks'),
     Input('pg6', 'n_clicks'),
     Input('pg7', 'n_clicks'),
     Input('settings', 'n_clicks'),
     Input('home', 'n_clicks'),
     Input('pg8', 'n_clicks'),
    #  Input('pg9', 'n_clicks'),
     ]
)
def update_initial_content(n_clicks1, n_clicks2, n_clicks3, n_clicks4,n_clicks6,n_clicks7,n_clicks8, n_clicks_home,n_clicks9):
    if any([n_clicks1, n_clicks2, n_clicks3, n_clicks4,n_clicks6,n_clicks7,n_clicks8,n_clicks_home,n_clicks9]):
        button_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'home' or not any([n_clicks1, n_clicks2, n_clicks3,
                                       n_clicks4, n_clicks6, n_clicks7, n_clicks8,n_clicks9]):
            from pages import home_page
            return home_page.layout
        elif button_id == 'pg1':
            from pages import page1
            return page1.layout
        elif button_id == 'pg2':
            from pages import page2
            return page2.layout
        elif button_id == 'pg3':
            from pages import page3
            return page3.layout
        elif button_id == 'pg4':
            from pages import page4
            return page4.layout
        # elif button_id == 'pg5':
        #     from pages import page5
        #     return page5.layout
        elif button_id == 'pg6':
            from pages import page6
            return page6.layout
        elif button_id == 'pg7':
            from pages import page9
            return page9.layout
        elif button_id == 'pg8':
            from pages import page8
            return page8.layout
        # elif button_id == 'pg9':
        #     from pages import page9
        #     return page9.layout
        elif button_id == 'settings':
            from pages import settings
            return settings.layout
    else:
        from pages import home_page
        return home_page.layout
          

if __name__ == '__main__':
    app.run_server(debug=True)
