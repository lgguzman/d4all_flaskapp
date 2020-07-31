import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.express as px

######### APP STRUCTURE #########
from app.libpage import sidebar, content, sidebar_r, mmap


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
    df = {}
    # Pensamiento critico : razonamiento + lectura critica
    df["pencritico"] = [
        ' He/She has a notion of the authors communicative intention and could establish relationships of ' + \
        ' similarity and order. ',
        ' Understands the global meaning of the text, identifies and interprets explicit information from ' + \
        ' different sources. In addition it applies simple arithmetic procedures. ',
        ' Is able to argue the validity of procedures (arithmetic, algebraic and variational) showing' + \
        ' the ability to project writings from that information. ',
        ' It is also capable of choosing the most appropriate procedure for solving problems. '
    ]

    # conocimiento de comunidad : abarca competencias ciudadanas
    df["competencias"] = [
        ' Demonstrates a notion of the present interests, worldviews, and dimensions of the principles ' + \
        ' consigned in the political constitution.',
        ' He/She is aware of the individual and collective rights of every individual.',
        ' He/She recognizes the primacy of the Constitution over any other rule, in addition ' + \
        ' to the citizen duties enshrined in it. ',
        ' He/She is able to apply general knowledge about social situations for resolution.'
    ]
    ###### foreign lenguage  : ingles
    df["ingles"] = [
        ' Demonstrates elementary knowledge of the foreign language.',
        ' He/She is able to understand and use everyday expressions as well as know how to relate in an ' + \
        ' elementary way. ',
        ' He/She is able to understand phrases and expressions of specific areas, demonstrating mastery ' + \
        ' when executing simple and daily tasks. ',
        ' Is able to understand the main ideas of texts in the foreign language and reproduce them as well ' + \
        ' as produce simple texts, describe experiences and events.']

    ######### Comunicación escrita (disyuntas)
    df["comescrita"] = [
        ' He/She expresses disjointed ideas among themselves, which do not account for ' + \
        ' a coherent approach.',
        ' They present some flaws in their structure and organization, ' + \
        ' which make them lack unity semantics.',
        ' He/She uses a basic structure with a start, middle, and end, although scoring errors ' + \
        ' and cohesion failures can be identified.',
        ' He/She shows different perspectives on the subject, make the approach more complex and allow satisfactory fulfillment of the communicative purpose. It makes proper use of punctuation marks, grammatical references, and connectors.'
    ]

    #########################
    # Dashboard Layout / View
    #########################

    ############## DEFINE APP LAYOUT #################
    # app.layout = html.Div([sidebar, content])
    LAYOUT_STYLE = {
        'padding': '15px 5px 15px 5px',
        'width': '100%',
        'background-color': 'gray'

    }

    ####### LAYOUT #############################
    dash_app.layout = dbc.Container(
        [
            html.Div(
                [

                    content.getHeader(dash_app),
                    html.Hr(),
                    dbc.Row(
                        [
                            dbc.Col(sidebar.sidebar, md=2),
                            dbc.Col(content.content, md=6),
                            dbc.Col(sidebar_r.getComponent(dash_app), md=4)
                        ],

                    ),
                    content.getFooter(dash_app)
                ],
                style={'background-color': 'white', 'padding': '15px 15px 15px 15px'}
            )
        ],
        fluid=True,
        # className='shadow-lg p-3 mb-5 bg-black rounded',
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

    def selected_skill(rrange, check):
        list_color = ['#FF2212', '#FFBC82', '#DC31FF', '#25BC66']

        if not check:
            return {'display': 'none'}
        else:
            return {'background-color': list_color[rrange[0] - 1],
                    'padding': '10px',
                    'color': 'white',
                    'border-radius': '25px',
                    'border-top': '2px solid black',
                    'text-align': 'justify', 'display': 'block'}

    #################### CALLBACK ###############
    ######## listing to competencias values #####
    @dash_app.callback(
        Output(component_id='div_comunitaria', component_property='children'),
        [Input('range_slider_com', 'value'), Input('check_list_com', 'value')]
    )
    def update_perfil_div_com(range_slider_com, check_list_com):
        nivel1 = df["competencias"][0]
        nivel2 = df["competencias"][1]
        nivel3 = df["competencias"][2]
        nivel4 = df["competencias"][3]
        output = ''
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
        else:
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_comunitaria', component_property='style'),
        [Input('range_slider_com', 'value'), Input('check_list_com', 'value')]
    )
    def update_perfil_div_com(range_slider_com, check_list_com):
        return selected_skill(range_slider_com, check_list_com)

    ######## listing to pensamiento critico ##################
    @dash_app.callback(
        Output(component_id='div_pcritico', component_property='children'),
        [Input('range_slider_quam', 'value'), Input('check_list_quam', 'value')]
    )
    def update_perfil_div_pen(range_slider_quam, check_list_quam):
        nivel1 = df["pencritico"][0]
        nivel2 = df["pencritico"][1]
        nivel3 = df["pencritico"][2]
        nivel4 = df["pencritico"][3]
        output = ''
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
        else:
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_pcritico', component_property='style'),
        [Input('range_slider_quam', 'value'), Input('check_list_quam', 'value')]
    )
    def update_perfil_div_pen(range_slider_quam, check_list_quam):
        return selected_skill(range_slider_quam, check_list_quam)

    ######## listing to idioma extrangero ##################
    @dash_app.callback(
        Output(component_id='div_ingles', component_property='children'),
        [Input('range_slider_foreign', 'value'), Input('check_list_foreign', 'value')]
    )
    def update_perfil_div_ingles(range_slider_foreign, check_list_foreign):
        nivel1 = df["ingles"][0]
        nivel2 = df["ingles"][1]
        nivel3 = df["ingles"][2]
        nivel4 = df["ingles"][3]
        # output= df["ingles"][range_slider_foreign[0]-1]
        output = ''
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
        else:
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_ingles', component_property='style'),
        [Input('range_slider_foreign', 'value'), Input('check_list_foreign', 'value')]
    )
    def update_perfil_div_ingles(range_slider_foreign, check_list_foreign):
        return selected_skill(range_slider_foreign, check_list_foreign)

    ######## listing to habilidades comunicativas ##################
    @dash_app.callback(
        Output(component_id='div_comescrita', component_property='children'),
        [Input('range_slider_comm', 'value'), Input('check_list_comm', 'value')]
    )
    def update_perfil_div_comm(range_slider_comm, check_list_comm):
        nivel1 = df["comescrita"][0]
        nivel2 = df["comescrita"][1]
        nivel3 = df["comescrita"][2]
        nivel4 = df["comescrita"][3]
        output = df["comescrita"][range_slider_comm[0] - 1]

        if not check_list_comm:
            return 'No seleccionada'
        else:
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_comescrita', component_property='style'),
        [Input('range_slider_comm', 'value'), Input('check_list_comm', 'value')]
    )
    def update_perfil_div_comm(range_slider_comm, check_list_comm):
        return selected_skill(range_slider_comm, check_list_comm)

    def get_traces():
        # for well_type, dfff in dff.groupby('Well_Type'):
        #     trace = dict(
        #         type='scattermapbox',
        #         lon=dfff['Surface_Longitude'],
        #         lat=dfff['Surface_latitude'],
        #         text=dfff['Well_Name'],
        #         customdata=dfff['API_WellNo'],
        #         name=WELL_TYPES[well_type],
        #         marker=dict(
        #             size=4,
        #             opacity=0.6,
        #         )
        #     )
        #     traces.append(trace);
        return [dict(
                type='scattermapbox',
                lon=-76.4851423,
                lat=5.0855571,
                text='test',
                name='test',
                marker=dict(
                    size=4,
                    opacity=0.6,
                )
            )]

    @dash_app.callback(Output('map_1', 'figure'),
                       [Input('range_slider_comm', 'value')])
    def make_main_figure(range_slider_comm):
        traces = get_traces()
        figure = dict(data=traces, layout=mmap.layout)
        return figure

    # # @dash_app.callback(
    # #    Output('graph_2', 'figure'),
    # #    [Input('submit_button', 'n_clicks')],
    # #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    # #     State('radio_items', 'value')
    # #     ])
    # def update_graph_2(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    #     print(n_clicks)
    #     print(dropdown_value)
    #     print(range_slider_value)
    #     print(check_list_value)
    #     print(radio_items_value)
    #     fig = {
    #         'data': [{
    #             'x': [1, 2, 3],
    #             'y': [3, 4, 5],
    #             'type': 'bar'
    #         }]
    #     }
    #     return fig
    #
    # # @dash_app.callback(
    # #    Output('graph_3', 'figure'),
    # #    [Input('submit_button', 'n_clicks')],
    # #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    # #     State('radio_items', 'value')
    # #     ])
    # def update_graph_3(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    #     print(n_clicks)
    #     print(dropdown_value)
    #     print(range_slider_value)
    #     print(check_list_value)
    #     print(radio_items_value)
    #     df = px.data.iris()
    #     fig = px.density_contour(df, x='sepal_width', y='sepal_length')
    #     return fig
    #
    # # @dash_app.callback(
    # #    Output('graph_4', 'figure'),
    # #    [Input('submit_button', 'n_clicks')],
    # #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    # #     State('radio_items', 'value')
    # #     ])
    # def update_graph_4(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    #     print(n_clicks)
    #     print(dropdown_value)
    #     print(range_slider_value)
    #     print(check_list_value)
    #     print(radio_items_value)  # Sample data and figure
    #     df = px.data.gapminder().query('year==2007')
    #     fig = px.scatter_geo(df, locations='iso_alpha', color='continent',
    #                          hover_name='country', size='pop', projection='natural earth')
    #     fig.update_layout({
    #         'height': 600
    #     })
    #     return fig
    #
    # # @dash_app.callback(
    # #    Output('graph_5', 'figure'),
    # #    [Input('submit_button', 'n_clicks')],
    # #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    # #     State('radio_items', 'value')
    # #     ])
    # def update_graph_5(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    #     print(n_clicks)
    #     print(dropdown_value)
    #     print(range_slider_value)
    #     print(check_list_value)
    #     print(radio_items_value)  # Sample data and figure
    #     df = px.data.iris()
    #     fig = px.scatter(df, x='sepal_width', y='sepal_length')
    #     return fig
    #
    # # @dash_app.callback(
    # #    Output('graph_6', 'figure'),
    # #    [Input('submit_button', 'n_clicks')],
    # #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    # #     State('radio_items', 'value')
    # #     ])
    # def update_graph_6(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    #     print(n_clicks)
    #     print(dropdown_value)
    #     print(range_slider_value)
    #     print(check_list_value)
    #     print(radio_items_value)  # Sample data and figure
    #     df = px.data.tips()
    #     fig = px.bar(df, x='total_bill', y='day', orientation='h')
    #     return fig
    #
    # # @dash_app.callback(
    # #    Output('card_title_1', 'children'),
    # #    [Input('submit_button', 'n_clicks')],
    # #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    # #     State('radio_items', 'value')
    # #     ])
    # def update_card_title_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    #     print(n_clicks)
    #     print(dropdown_value)
    #     print(range_slider_value)
    #     print(check_list_value)
    #     print(radio_items_value)  # Sample data and figure
    #     return 'Card Tile 1 change by call back'
    #
    # # @dash_app.callback(
    # #    Output('card_text_1', 'children'),
    # #    [Input('submit_button', 'n_clicks')],
    # #    [State('dropdown', 'value'), State('range_slider', 'value'), State('check_list', 'value'),
    # #     State('radio_items', 'value')
    # #     ])
    # def update_card_text_1(n_clicks, dropdown_value, range_slider_value, check_list_value, radio_items_value):
    #     print(n_clicks)
    #     print(dropdown_value)
    #     print(range_slider_value)
    #     print(check_list_value)
    #     print(radio_items_value)  # Sample data and figure
    #     return 'Card text change by call back'
    #
    # #############################################
    # # MAIN SERVER
    # #############################################

    return dash_app.server
