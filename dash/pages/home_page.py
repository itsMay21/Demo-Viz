import dash
from dash import html

dash.register_page(__name__, order=1, path='/')

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/home_page.css']

layout = html.Div([
    html.H1('CS661: BIG DATA VISUAL ANALYTICS', className='Title center-aligned'),
    html.H2('END TERM PROJECT', className='center-aligned'),
    html.H3('DEMOGRAPHIC VISUALIZATION', className='center-aligned'),
    
    html.Div([
        html.H3('Description of Project'),
        html.P(
            'Welcome to our interactive platform designed to explore global economics '
            'through data visualization and analysis. Navigate through our seven-page journey '
            'to delve into the factors shaping the world GDP and gain insights into the global '
            'economic landscape.'
        ),
        html.H4('The page introductions are as follows:'),
        html.Ul([
            html.Li('Global GDP Trends: Explore visuals showcasing global GDP trends and influencing parameters.'),
            html.Li('Country-Specific Correlations: View scatterplots illustrating correlations between GDP and various factors across countries.'),
            html.Li('Countrywise Factor Distribution: Discover the distribution of potential GDP-affecting factors across countries.'),
            html.Li("Sectorial Impact on GDP: Examine the effects of primary, secondary, and tertiary sectors on a country's GDP."),
            html.Li('Income Distribution Analysis: Analyze income distribution among countries, highlighting its impact on various other factors'),
            html.Li('Country-to-Country Comparison: Compare countries based on GDP and related factors using our interactive tool.'),
        ])
    ], className='container center-aligned'),

    html.Div([
        html.H3('Group Members'),
        html.Table([
            html.Tr([
                html.Td('Aastik Guru'), 
                html.Td('Aatman Jain'),       
                html.Td('Atharv'),    
                html.Td('Abhishek Mishra'),    
            ]),
            html.Tr([
                html.Td('Manan Kalavadia'), 
                html.Td('Mayank Saini'),
                html.Td('Siddhant'),
                html.Td('Yash Gupta'), 
            ])
        ])
    ], className='container center-aligned'),

    html.Div([
        html.H3('Course Instructor'),
        html.Img(src='https://soumyadutta-cse.github.io/images/sdutta_BW.png', alt='Dr. Saumya Dutta', className='instructor-image', style={'width': '150px'}),
        html.P(html.A('Dr. Saumya Dutta', href='https://soumyadutta-cse.github.io/',target="_blank"))
    ], className='container center-aligned'),

    html.Div([
        html.H3('Source Code'),
        html.P(html.A('Github Repository', href='https://github.com/CS661-project',target="_blank"))
    ], className='container center-aligned'),

    html.Div([
        html.H3('References'),
        html.A("THE WORLD BANK", href='https://data.worldbank.org/indicator', target="_blank"),
        html.Br(),
        html.A("Dash Documentation", href='https://dash.plotly.com/', target="_blank"),
    ], className='container center-aligned')
])
