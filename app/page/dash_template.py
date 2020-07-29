import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px

######### APP STRUCTURE #########
from app.libpage import  sidebar, content,sidebar_r


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )


    ###########################################################################################
    # Data Manipulation / Model
    ###########################################################################################
    ########  niveles de desempeño ############################
    ### nivel 1 : 0 - 125
    ### nivel 2 : 126 a 156
    ### nivel 3 : 157 a 198
    ### nivel 4 : 199 a 300
    ## Fuente:  #https://www.icfes.gov.co/documents/20143/1210096/Niveles+de+desempeno+competencias+ciudadanas+Saber+Pro.pdf/ae70a#ad3-8ccc-7ac9-87ad-7197c96c6903
    df={}
    # Pensamiento critico : razonamiento + lectura critica
    df["pencritico"] = [
     'Tiene noción de la intención comunicativa del autor y podría establecer relaciones de similitud y ordén. ',
     'Comprende el sentido global del texto, identifica e interpreta información explicita de diferentes fuentes' + \
     'Además que aplica procedimientos aritméticos sencillos.',
     ' Es capaz de argumentar la validez de procedimientos (aritméticos, algebraicos y variacionales) mostrando' + \
     'la capacidad de proyectar escritos a partir de esa información.',
     ' Además es capaz de elegir el procedimiento más adecuado para la solución  de problemas'
    ]

    # conocimiento de comunidad : abarca competencias ciudadanas
    df["competencias"] = [
    'Demuestra una noción de los intereses,  cosmovisiones  y  dimensiones  presentes  de los principios ' + \
    ' consignados en la constitución política.',
    ' Se es conciente de los derechos individuales y colectivos de todo individuo.',
    ' Reconoce la primacía de   la   Constitución   sobre   cualquier   otra   norma, además de los deberes ' + \
    ' ciudadanos  consagrados  en ella. ',
    ' Es capaz de aplicar conocimientos generales sobre situaciones sociales para su resolución.'
    ]
    ###### foreign lenguage  : ingles
    df["ingles"] = [
    ' Demuestra conocimientos elementales del idioma extrangeros.',
    ' Es capaz de comprender y utilizar expresiones cotidianas como tambíen sabe relacionarse de forma' + \
    ' elemental.',
    ' Es capaz de comprender frases y expresiones de areas especificas, demostrando dominio al momento de' +  \
    ' ejecutar tareas simples y cotidianas.',
    ' Es capaz de comprender las ideas principales de textos en la lengua extrangera y reproducirlos' +  \
    ' como también producir textos sencillos, describir experiencias y acontecimientos.']

    ######### Comunicación escrita (disyuntas)
    df["comescrita"]=[
    'Expresan ideas desarticuladas entre sí, que no dan cuenta de un planteamiento coherente. ',
    'Presentan algunas fallas en su estructura y organización, que hacen que estos carezcan de unidad ' +  \
    'semántica. ',
    ' Emplean  una  estructura  básica  con  un inicio, un desarrollo y un cierre, aunque puede identificarse' + \
    ' errores de puntuación y fallas de cohesión.',
    ' Muestran diferentes perspectivas sobre el tema, complejizan el planteamiento y permiten cumplir ' +  \
    ' satisfactoriamente con el  propósito  comunicativo. Hace uso adecuado de signos de puntuación, ' + \
    ' referencias gramaticales y conectores.'
    ]


    #########################
    # Dashboard Layout / View
    #########################




    ############## DEFINE APP LAYOUT #################
    #app.layout = html.Div([sidebar, content])
    LAYOUT_STYLE={
        'padding': '15px 5px 15px 5px',
        'width':'100%',
        'background-color':'gray'


    }

    dash_app.layout  = dbc.Container(
        [
            html.Div([

           dbc.Row(
                [
                   dbc.Col(
                     [
                          html.Img(src=dash_app.get_asset_url('logo.png'),style={'width':'100%','textAlign':'center'}),
                     ],
                     md=2
                   ),
                   dbc.Col(
                       [
                         html.H4('An Intelligent System for Profile and Skill Identification of ' + \
                                'Human Resources in Colombian Regions using Pruebas Saber Data',
                                style={'font-style':'italic','text-align':'center'}
                                ),
                         html.Hr()

                       ]
                       ,md=8
                   ),
                   dbc.Col(
                       [
                         html.H3(' Proyecto DS4A',
                         style={
                            'textAlign': 'center',
                            'color':'blue'
                          }),
                         html.H5(' Colombia 2020',style={'textAlign':'center'}),
                         html.H4(' CORRELATION ONE ', style={'color':'#ff9900','textAlign':'center'}),
                         html.H5('Team 17',style={'textAlign': 'center'}),
                         html.B('Patrocinado por:'),
                         html.Img(src=dash_app.get_asset_url('mintic.jpg'),style={'width':'100%','textAlign':'center'})
                       ],
                       md=2,
                       style={'padding':'35px 10px 0px 10'}
                   ),
                ],


            ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(sidebar.sidebar, md=2),
                    dbc.Col(content.content, md=6),
                    dbc.Col(sidebar_r.getComponent(dash_app), md=4)
                ],

            ),
            dbc.Row(
                [
                      dbc.Col(
                            [

                                html.B('Business Problem:'),
                                 html.P('Nowadays industry and government have a need of selecting and' + \
                                ' knowing the skills and potential of their future collaborators.'),
                                 html.B('Data:'),
                                 html.P('Pruebas Saber Pro from the Colombian Institute for Tertiary Education' +  \
                                ' Fomentation (ICFES).'
                                ),
                                html.H5('Monitores/Tutores de DS4A son'),
                                html.P('German Prieto - g.prieto@correlation-one.com, Jimmy Jing ' + \
                                       ' - jimmy@correlation-one.com ')
                            ],
                            md=6,
                            style={}

                      ), # fin de dbc.Col
                      dbc.Col(
                           [
                               html.Br(),
                               html.H5('Participantes'),
                               html.Ul(
                                    [
                                       html.Li('Alfonso Cervantes Barragán (barrangana@uninorte.edu.co)'),
                                       html.Li('Rafael García (ingrafaelgarciaq@hotmail.com)'),
                                       html.Li('Luis Guzmán'),
                                       html.Li('Julián Rincón (josej.jimenez@urosario.edu.co)'),
                                       html.Li('Jorge Vélez (jorgeivanvelez@gmail.com)'),
                                       html.Li('Ricardo Villanueva (ricardovillanuevapolanco@gmail.com)'),
                                       html.Li('Eduardo Zurek (eduardo.zurek@gmail.com)')
                                    ]
                                 )  ## fin de html.UL
                           ],
                           md=6,
                           style={}

                      )  # fin de dbc.Col
                ],
                style={'padding':'10px','color':'white','background-color':'black'}

             )    # fin de dbc.Row


            ],
            style={'background-color':'white','padding':'15px 15px 15px 15px'}
            )
        ],
        fluid=True,
        #className='shadow-lg p-3 mb-5 bg-black rounded',
        style=LAYOUT_STYLE
    )
    #############################################
    # Interaction Between Components / Controller
    #############################################

    ############### STYLE FUNCTIONS #############
    ## función : selected_skill
    ## Cambia el color del perfil dependiendo del nivel de desempeño.
    ## Parametros rrange : valor numerico (de 1 a 4 indica el nivel de desempeño)
    ##            check  : lista (indica si checkbox esta elegida)

    def selected_skill(rrange,check):
         list_color=['#FF2212','#FFBC82','#DC31FF','#25BC66']

         if not check:
            return {'display':'none'}
         else :
            return {'background-color':list_color[rrange[0]-1],
                'padding':'10px',
                'color':'white',
                'border-radius':'25px',
                'border-top':'2px solid black',
                 'text-align':'justify','display':'block'}

    #################### CALLBACK ###############
    ######## listing to competencias values #####
    @dash_app.callback(
        Output(component_id='div_comunitaria', component_property='children'),
        [Input('range_slider_com', 'value'),Input('check_list_com', 'value')]
    )
    def update_perfil_div_com(range_slider_com, check_list_com):
        nivel1 = df["competencias"][0]
        nivel2 = df["competencias"][1]
        nivel3 = df["competencias"][2]
        nivel4 = df["competencias"][3]
        output=''
        if range_slider_com[0] == 1:
            output = nivel1
        elif range_slider_com[0] == 2:
            output = nivel1 + nivel2
        elif range_slider_com[0] == 3:
            output = nivel1 + nivel2 + nivel3
        elif range_slider_com[0] == 4:
            output = nivel1 + nivel2 + nivel3 + nivel4

        if not check_list_com:
            return 'No seleccionada'
        else :
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_comunitaria', component_property='style'),
        [Input('range_slider_com', 'value'),Input('check_list_com', 'value')]
    )
    def update_perfil_div_com(range_slider_com, check_list_com):
        return selected_skill(range_slider_com,check_list_com)


    ######## listing to pensamiento critico ##################
    @dash_app.callback(
        Output(component_id='div_pcritico', component_property='children'),
        [Input('range_slider_quam', 'value'),Input('check_list_quam', 'value')]
    )
    def update_perfil_div_pen(range_slider_quam, check_list_quam):
        nivel1 = df["pencritico"][0]
        nivel2 = df["pencritico"][1]
        nivel3 = df["pencritico"][2]
        nivel4 = df["pencritico"][3]
        output=''
        if range_slider_quam[0] == 1:
            output = nivel1
        elif range_slider_quam[0] == 2:
            output = nivel1 + nivel2
        elif range_slider_quam[0] == 3:
            output = nivel1 + nivel2 + nivel3
        elif range_slider_quam[0] == 4:
            output = nivel1 + nivel2 + nivel3 + nivel4

        if not check_list_quam:
            return 'No seleccionada'
        else :
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_pcritico', component_property='style'),
        [Input('range_slider_quam', 'value'),Input('check_list_quam', 'value')]
    )
    def update_perfil_div_pen(range_slider_quam, check_list_quam):
        return selected_skill(range_slider_quam,check_list_quam)

    ######## listing to idioma extrangero ##################
    @dash_app.callback(
        Output(component_id='div_ingles', component_property='children'),
        [Input('range_slider_foreign', 'value'),Input('check_list_foreign', 'value')]
    )
    def update_perfil_div_ingles(range_slider_foreign, check_list_foreign):
        nivel1 = df["ingles"][0]
        nivel2 = df["ingles"][1]
        nivel3 = df["ingles"][2]
        nivel4 = df["ingles"][3]
        #output= df["ingles"][range_slider_foreign[0]-1]
        output=''
        if range_slider_foreign[0] == 1:
            output = nivel1
        elif range_slider_foreign[0] == 2:
            output = nivel1 + nivel2
        elif range_slider_foreign[0] == 3:
            output = nivel1 + nivel2 + nivel3
        elif range_slider_foreign[0] == 4:
            output = nivel1 + nivel2 + nivel3 + nivel4

        if not check_list_foreign:
            return 'No seleccionada'
        else :
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_ingles', component_property='style'),
        [Input('range_slider_foreign', 'value'),Input('check_list_foreign', 'value')]
    )
    def update_perfil_div_ingles(range_slider_foreign, check_list_foreign):
        return selected_skill(range_slider_foreign,check_list_foreign)

    ######## listing to habilidades comunicativas ##################
    @dash_app.callback(
        Output(component_id='div_comescrita', component_property='children'),
        [Input('range_slider_comm', 'value'),Input('check_list_comm', 'value')]
    )
    def update_perfil_div_comm(range_slider_comm, check_list_comm):
        nivel1 = df["comescrita"][0]
        nivel2 = df["comescrita"][1]
        nivel3 = df["comescrita"][2]
        nivel4 = df["comescrita"][3]
        output= df["comescrita"][range_slider_comm[0]-1]


        if not check_list_comm:
            return 'No seleccionada'
        else :
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_comescrita', component_property='style'),
        [Input('range_slider_comm', 'value'),Input('check_list_comm', 'value')]
    )
    def update_perfil_div_comm(range_slider_comm, check_list_comm):
        return selected_skill(range_slider_comm,check_list_comm)


    #@dash_app.callback(
    #    Output('graph_2', 'figure'),
    #    [Input('submit_button', 'n_clicks')],
    #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    #     State('radio_items', 'value')
    #     ])
    def update_graph_2(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
        print(n_clicks)
        print(dropdown_value)
        print(range_slider_value)
        print(check_list_value)
        print(radio_items_value)
        fig = {
            'data': [{
                'x': [1, 2, 3],
                'y': [3, 4, 5],
                'type': 'bar'
            }]
        }
        return fig


    #@dash_app.callback(
    #    Output('graph_3', 'figure'),
    #    [Input('submit_button', 'n_clicks')],
    #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    #     State('radio_items', 'value')
    #     ])
    def update_graph_3(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
        print(n_clicks)
        print(dropdown_value)
        print(range_slider_value)
        print(check_list_value)
        print(radio_items_value)
        df = px.data.iris()
        fig = px.density_contour(df, x='sepal_width', y='sepal_length')
        return fig


    #@dash_app.callback(
    #    Output('graph_4', 'figure'),
    #    [Input('submit_button', 'n_clicks')],
    #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    #     State('radio_items', 'value')
    #     ])
    def update_graph_4(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
        print(n_clicks)
        print(dropdown_value)
        print(range_slider_value)
        print(check_list_value)
        print(radio_items_value)  # Sample data and figure
        df = px.data.gapminder().query('year==2007')
        fig = px.scatter_geo(df, locations='iso_alpha', color='continent',
                             hover_name='country', size='pop', projection='natural earth')
        fig.update_layout({
            'height': 600
        })
        return fig


    #@dash_app.callback(
    #    Output('graph_5', 'figure'),
    #    [Input('submit_button', 'n_clicks')],
    #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    #     State('radio_items', 'value')
    #     ])
    def update_graph_5(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
        print(n_clicks)
        print(dropdown_value)
        print(range_slider_value)
        print(check_list_value)
        print(radio_items_value)  # Sample data and figure
        df = px.data.iris()
        fig = px.scatter(df, x='sepal_width', y='sepal_length')
        return fig


    #@dash_app.callback(
    #    Output('graph_6', 'figure'),
    #    [Input('submit_button', 'n_clicks')],
    #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    #     State('radio_items', 'value')
    #     ])
    def update_graph_6(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
        print(n_clicks)
        print(dropdown_value)
        print(range_slider_value)
        print(check_list_value)
        print(radio_items_value)  # Sample data and figure
        df = px.data.tips()
        fig = px.bar(df, x='total_bill', y='day', orientation='h')
        return fig


    #@dash_app.callback(
    #    Output('card_title_1', 'children'),
    #    [Input('submit_button', 'n_clicks')],
    #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    #     State('radio_items', 'value')
    #     ])
    def update_card_title_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
        print(n_clicks)
        print(dropdown_value)
        print(range_slider_value)
        print(check_list_value)
        print(radio_items_value)  # Sample data and figure
        return 'Card Tile 1 change by call back'


    #@dash_app.callback(
    #    Output('card_text_1', 'children'),
    #    [Input('submit_button', 'n_clicks')],
    #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    #     State('radio_items', 'value')
    #     ])
    def update_card_text_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
        print(n_clicks)
        print(dropdown_value)
        print(range_slider_value)
        print(check_list_value)
        print(radio_items_value)  # Sample data and figure
        return 'Card text change by call back'

    #############################################
    # MAIN SERVER
    #############################################

    return dash_app.server


