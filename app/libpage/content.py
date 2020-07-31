import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


    # the style arguments for the main content page.
# the style arguments for the main content page.

CONTENT_STYLE = {
    # 'margin-left': '25%',
    # 'margin-right': '5%',
    'padding': '20px 10p',
    'width': '100%'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

    ########## CONTENT right side ############################
def getHeader(app):
    return dbc.Row(
        [
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('logo.png'), style={'width': '50%', 'textAlign': 'center'}),
                ],
                md=2
            ),
            dbc.Col(
                [
                    html.H4('An Intelligent System for Profile and Skill Identification of ' + \
                            'Human Resources in Colombian Regions using Pruebas Saber Data',
                            style={'font-style': 'italic', 'text-align': 'center'}
                            ),
                    html.Hr()

                ]
                , md=10
            ),
        ],
        style={'background-color': 'white', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}

    )

## first row
content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=3
    )
])
### second row
content_second_row = dbc.Row(
    [
        dbc.Col(
                 id='nothing',
                md=12
                ),
    ]
)

##################  thrid row
content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='map_1'), md=12
        )
    ]
)

######### FORUTH ROW ############
content_fourth_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_5'), md=6
        ),
        dbc.Col(
            dcc.Graph(id='graph_6'), md=6
        )
    ]
)

def getFooter(app):
    return  dbc.Row(
    [
        dbc.Col(
            [

                html.B('Business Problem:'),
                html.P('Nowadays industry and government have a need of selecting and' + \
                       ' knowing the skills and potential of their future collaborators.'),
                html.B('Data:'),
                html.P('Pruebas Saber Pro from the Colombian Institute for Tertiary Education' + \
                       ' Fomentation (ICFES).'
                       ),
                html.H5('DS4A advisors:'),
                html.P('German Prieto - g.prieto@correlation-one.com, Jimmy Jing ' + \
                       ' - jimmy@correlation-one.com ')
            ],
            md=6

        ),  # fin de dbc.Col
        dbc.Col(
            [

                html.B('Participants'),
                html.Ul(
                    [
                        html.Li('Alfonso Cervantes Barragán (barrangana@uninorte.edu.co)'),
                        html.Li('Rafael García (ingrafaelgarciaq@hotmail.com)'),
                        html.Li('Luis Guzmán (lgguzman@uninorte.edu.co)'),
                        html.Li('Julián Rincón (josej.jimenez@urosario.edu.co)'),
                        html.Li('Jorge Vélez (jorgeivanvelez@gmail.com)'),
                        html.Li('Ricardo Villanueva (ricardovillanuevapolanco@gmail.com)'),
                        html.Li('Eduardo Zurek (eduardo.zurek@gmail.com)')
                    ]
                )  ## fin de html.UL
            ],
            md=6

        )  # fin de dbc.Col

    ],
        style={'padding': '10px', 'color': 'white', 'background-color': 'black'}

)  # fin de dbc.Row

def getFooterIcons(app):
    return dbc.Row(
                [  dbc.Col(
                    [
                        html.Img(src='https://correlation1-public.s3-us-west-2.amazonaws.com/training/COLOMBIA+MAIN+SANS+TAG.svg', style={'width': '80%', 'textAlign': 'center'})
                    ],
                    md=3,
                    style={'padding': '35px 10px 0px 10', 'margin-right': '35px'}
                    )  ,
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('mintic.jpg'), style={'width': '100%', 'textAlign': 'center'})
                ],
                md=2,
                style={'padding': '35px 10px 0px 10'}
             )  ,
             dbc.Col(
                [
                    html.Img(src=app.get_asset_url('corlogo.jpeg'), style={'width': '100px', 'textAlign': 'center'})
                ],
                md=3,
                style={'display': 'flex',  'justify-content': 'center', 'margin-left': '35px' }
            )
        ],
                style={ 'background-color': 'white', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'margin-top': '15px'}

            )

############ right side ##############
content = html.Div(
    [
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row
    ],
    style=CONTENT_STYLE
)
