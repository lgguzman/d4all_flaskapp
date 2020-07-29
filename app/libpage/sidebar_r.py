
import dash_html_components as html
import dash_bootstrap_components as dbc

def getComponent(app):
    SIDEBAR_STYLE = {
    #    'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
       # 'width': '20%',
        'padding': '20px 10px',
        'background-color': '#f8f9fa'
    }

    card = dbc.Card(
        [
            dbc.CardHeader(
             [
                html.H4(' Construcción del Perfil ', style={
                'textAlign': 'center',
                'color':'blue'})
             ]

            ),

            dbc.CardBody(
                [

                    html.Div(
                           [
                               html.Img(src=app.get_asset_url('multy-user.png'),style={'width':'20%','textAlign':'center'}),
                           ],
                           style={'textAlign':'center'}

                        ),
                    html.P('El nivel de exigencia cognitivas y conceptuales demostrado en cada competencia particular' + \
                           ' esta categorizada en un rango ascendente de 1 de 4',
                           style={'padding-left':'10px','padding-right':'10px','font-style':'italic'}
                           ),
                    html.Div(
                             [
                               dbc.Button(" 1 ",
                                         color="primary",
                                         #className='btn btn-primary',
                                         style={'border-radius': '25px',
                                                'font-weight': 'bold',
                                                'padding':'2px 10px 2px 10px',
                                                'margin':'0px 5px 0px 5px',
                                                'background-color':'#FF2212'
                                                }
                                         ),
                               dbc.Button(" 2 ",
                                         color="primary",
                                         #className='btn btn-primary',
                                         style={'border-radius': '25px',
                                                'font-weight': 'bold',
                                                'padding':'2px 10px 2px 10px',
                                                'margin':'0px 5px 0px 5px',
                                                'background-color':'#FFBC82'
                                                }
                                         ),
                                dbc.Button(" 3 ",
                                         color="primary",
                                         #className='btn btn-primary',
                                         style={'border-radius': '25px',
                                                'font-weight': 'bold',
                                                'padding':'2px 10px 2px 10px',
                                                'margin':'0px 5px 0px 5px',
                                                'background-color':'#DC31FF'
                                                }
                                          ),
                                dbc.Button(" 4 ",
                                         color="primary",
                                         #className='btn btn-primary',
                                         style={'border-radius': '25px',
                                                'font-weight': 'bold',
                                                'padding':'2px 10px 2px 10px',
                                                'margin':'0px 5px 0px 5px',
                                                'background-color':'#25BC66'
                                                }
                                         ),

                             ],
                             style={'textAlign':'center'}
                    ),

                    html.Hr(),
                    html.H5('Habilidades comunitarias:',
                    id='h5_com',
                    style={
                         'textAlign': 'left',
                        'boder':'1px solid black'
                    }),

                    html.Div(id='div_comunitaria',className='card-text'),

                    html.H5('Pensamiento crítico',
                    id='h5_pcritico',
                    style={
                            'textAlign': 'left',
                            'boder':'1px solid black'
                        }),
                    html.Div(id='div_pcritico',className='card-text'),
                    html.H5('Habilidades comunicativas', style={
                            'textAlign': 'left',
                            'boder':'1px solid black'
                        }),
                     html.Div(id='div_comescrita'),
                    html.H5('Idioma extrangero', style={
                            'textAlign': 'left',
                            'boder':'1px solid black'
                        }),

                    html.Div(id='div_ingles',className='card-text'),
                    html.H5('Competencia profesional', style={
                            'textAlign': 'left',
                            'boder':'1px solid black'
                        }),
                    html.Div(id='div_profesional',className='card-text'),

                ],
                style={"width": "100%",'border-radius':'25px'}
                ),
            ]
    )




    return html.Div(
        [
            card


        ],
        style=SIDEBAR_STYLE
    )



