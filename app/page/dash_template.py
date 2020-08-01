import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import json
import pandas as pd
from random import randint
import plotly.express as px

######### APP STRUCTURE #########
from sklearn.cluster import DBSCAN

from app.dashboard.dashboard import DataBaseDashboard
from app.libpage import sidebar, content, sidebar_r, mmap


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']
    )

    connection = DataBaseDashboard()

    ###########################################################################################
    # Data Manipulation / Model
    ###########################################################################################
    ########  niveles de desempeño ############################
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
                    sidebar_r.getComponent(dash_app),
                    dbc.Row(
                        [
                            dbc.Col(sidebar.sidebar, md=3),
                            dbc.Col(content.content, md=9)
                        ],

                    ),
                    content.getFooter(dash_app),
                    content.getFooterIcons(dash_app),

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
        [Input('dropdown_foreign', 'value'), Input('check_list_foreign', 'value')]
    )
    def update_perfil_div_ingles(dropdown_foreign, check_list_foreign):
        nivel1 = df["ingles"][0]
        nivel2 = df["ingles"][1]
        nivel3 = df["ingles"][2]
        nivel4 = df["ingles"][3]
        # output= df["ingles"][range_slider_foreign[0]-1]
        output = ''
        if dropdown_foreign == "1":
            output = nivel1
        elif dropdown_foreign == "2":
            output = nivel1 + nivel2
        elif dropdown_foreign == "3":
            output = nivel1 + nivel2 + nivel3
        elif dropdown_foreign == "4":
            output = nivel1 + nivel2 + nivel3 + nivel4

        if not check_list_foreign:
            return 'No seleccionada'
        else:
            return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='div_ingles', component_property='style'),
        [Input('dropdown_foreign', 'value'), Input('check_list_foreign', 'value')]
    )
    def update_perfil_div_ingles(dropdown_foreign, check_list_foreign):
        return selected_skill([int(dropdown_foreign)], check_list_foreign)

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
        Output("modal-centered", "is_open"),
        [Input("info-button", "n_clicks"), Input("close-centered", "n_clicks")],
        [State("modal-centered", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    @dash_app.callback(
        Output(component_id='div_comescrita', component_property='style'),
        [Input('range_slider_comm', 'value'), Input('check_list_comm', 'value')]
    )
    def update_perfil_div_comm(range_slider_comm, check_list_comm):
        return selected_skill(range_slider_comm, check_list_comm)

    def data_for_map(df1):
        dbs = DBSCAN(eps=650 / 6371,
                     min_samples=1,
                     metric='haversine').fit(df1[['Longitud', 'Latitud']],
                                             sample_weight=df1['count'])
        df1["clus_db"] = dbs.labels_
        count_cluster_grouped = df1.groupby('clus_db'). \
            sum().sort_values(by='count', ascending=False). \
            reset_index()
        df2 = df1[df1['clus_db'].isin(list(count_cluster_grouped.clus_db))]
        return df2

    def cluster_selection(df2,
                          minimun_number_of_elements=0,
                          criterium='all'):
        # criterium: ['max','min','all']
        # df3 = df2.sort_values(by=['count'])
        # df3 = df3[df3['count'] >= minimun_number_of_elements]
        # if criterium == 'min':
        #     df3 = df3.head(2)
        # elif criterium == 'max':
        #     df3 = df3.tail(2)
        # return df3
        count_cluster_grouped = df2.groupby('clus_db').sum().sort_values(by='count', ascending=False)

        count_clus_filtered = count_cluster_grouped[count_cluster_grouped['count'] >= minimun_number_of_elements]
        count_clus_filtered.reset_index(inplace=True)

        if criterium == 'max':
            return df2[df2['clus_db'] == int(count_clus_filtered.head(n=1).clus_db)]
        elif criterium == 'min':
            return df2[df2['clus_db'] == int(count_clus_filtered.tail(n=1).clus_db)]
        return df2

    def get_traces(cty_sk=2,
                   ctc_rd=4,
                   fl_sk="0",
                   cmm_sk=4,
                   qtt_tk=4,
                   year="2018",
                   ref_grp_index=10,
                   greather_or_equal=1,
                   criterium='all'):

        try:
            df1 = connection.fetch_info(cty_sk, ctc_rd, fl_sk, cmm_sk, qtt_tk, year, ref_grp_index, greather_or_equal)
            df2 = cluster_selection(df2=data_for_map(df1), criterium=criterium)
            traces = []
            colormap = []
            grouped = df2.groupby('clus_db')
            for i in range(len(grouped)+5):
                colormap.append('#%06X' % randint(0, 0xFFFFFF))
            for ctype, dfff in grouped:
                trace = dict(
                    type='scattermapbox',
                    lon=dfff['Longitud'],
                    lat=dfff['Latitud'],
                    name=ctype,
                    text=dfff['Nombre municipio'],
                    marker=dict(
                        size=dfff["count"].apply(lambda x: min(max(x,8),40)),
                        opacity=0.8,
                        cmin=0,
                        cmax=20,
                        color=colormap[ctype],
                        color_continuous_scale=px.colors.diverging.Tealrose,
                        color_continuous_midpoint=1
                    )
                )
                traces.append(trace)
            # traces.append(dict(
            #         type='scattermapbox',
            #         lon=df2['Longitud'],
            #         lat=df2['Latitud'],
            #         name=str(df2['clus_db']),
            #         text=df2['Nombre municipio'],
            #
            #         color_continuous_scale=px.colors.diverging.Tealrose,
            #
            #         marker=dict(
            #             size=df2["count"].apply(lambda x: min(max(x, 10), 40)),
            #             cmin=0,
            #             cmax=20,
            #             color=df2['clus_db'],
            #             color_continuous_midpoint=1,
            #             opacity=1,
            #
            #         )
            # ))
            return traces
        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)
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

    def get_map(cty_sk=2,
                   ctc_rd=4,
                   fl_sk="0",
                   cmm_sk=4,
                   qtt_tk=4,
                   year="2018",
                   ref_grp_index=10,
                   greather_or_equal=1,
                   criterium='all'):


        df1 = connection.fetch_info(cty_sk, ctc_rd, fl_sk, cmm_sk, qtt_tk, year, ref_grp_index,
                                    greather_or_equal)
        df2 = cluster_selection(df2=data_for_map(df1), criterium=criterium)


        px.scatter_mapbox(df2,
                          lat="Latitud",
                          lon="Longitud",
                          color="clus_db",
                          color_continuous_scale=px.colors.cyclical.Phase,
                          size_max=15,
                          size="count",
                          zoom=3.8,
                          mapbox_style="carto-darkmatter",
                          width=1200,
                          height=800, )

    @dash_app.callback(Output('map_1', 'figure'),
                       [ Input('submit_button', 'n_clicks') ],
                       [State('range_slider_comm', 'value'), #State('check_list_comm', 'value'),
                        State('range_slider_com', 'value'), #State('check_list_com', 'value'),
                        State('range_slider_quam', 'value'),# State('check_list_quam', 'value'),
                        State('range_slider_qthinking', 'value'),# State('check_list_qthinking', 'value'),
                        State('dropdown_foreign', 'value'), #State('check_list_foreign', 'value'),
                        State('dropdown_config', 'value') ,
                        State('dropdown_profesion', 'value') ,
                        State('dropdown_ano', 'value') ,
                        State('dropdown_search', 'value') ,

                        ])
    def make_main_figure(submit_button,
                         range_slider_comm, #check_list_comm,
                         range_slider_com, #check_list_com,
                         range_slider_quam, #check_list_quam,
                         range_slider_qthinking,# check_list_qthinking,
                         dropdown_foreign, #check_list_foreign,
                         dropdown_config,
                         dropdown_profesion,
                         dropdown_ano,
                         dropdown_search):
        traces = get_traces(cty_sk=range_slider_com[0],
                            ctc_rd=range_slider_quam[0],
                            cmm_sk=range_slider_comm[0],
                            qtt_tk=range_slider_qthinking[0],
                            year=dropdown_ano,
                            ref_grp_index=dropdown_profesion,
                            greather_or_equal=dropdown_config,
                            fl_sk=dropdown_foreign,
                            criterium=dropdown_search)
        figure = dict(data=traces, layout=mmap.layout)
        # return get_map(cty_sk=range_slider_com[0],
        #                     ctc_rd=range_slider_quam[0],
        #                     cmm_sk=range_slider_comm[0],
        #                     qtt_tk=range_slider_qthinking[0],
        #                     year=dropdown_ano,
        #                     ref_grp_index=dropdown_profesion,
        #                     greather_or_equal=dropdown_config,
        #                     fl_sk=dropdown_foreign,
        #                     criterium=dropdown_search)
        return figure

    @dash_app.callback([Output('graph_1', 'figure'),
                        Output('graph_2', 'figure'),
                        Output('graph_3', 'figure'),
                        Output('graph_4', 'figure'),
                        Output('graph_5', 'figure'),
                        ],
                       [Input('submit_button', 'n_clicks')],
                       [State('dropdown_profesion', 'value'),
                        State('dropdown_ano', 'value'),

                        ])
    def make_others_figure(submit_button,
                         dropdown_profesion,
                         dropdown_ano ):
        data = connection.data_for_dash_histograms(dropdown_profesion,dropdown_ano)
        figure1 = px.bar(data.groupby(["MOD_COMPETEN_CIUDADA_DESEM"]).count().reset_index(), x='MOD_COMPETEN_CIUDADA_DESEM', y="MOD_INGLES_DESEM",
                        title='Community skills', labels={'MOD_COMPETEN_CIUDADA_DESEM': 'level', 'MOD_INGLES_DESEM': 'Frequency'} )
        figure2 = px.bar(data.groupby(["MOD_LECTURA_CRITICA_DESEM"]).count().reset_index(), x='MOD_LECTURA_CRITICA_DESEM', y="MOD_INGLES_DESEM",
                        title='Critical reading skills',labels={'MOD_LECTURA_CRITICA_DESEM': 'level', 'MOD_INGLES_DESEM': 'Frequency'} )
        figure3 = px.bar(data.groupby(["MOD_INGLES_DESEM"]).count().reset_index(), x='MOD_INGLES_DESEM', y="MOD_COMUNI_ESCRITA_DESEM" ,
                        title='English language skills',labels={'MOD_INGLES_DESEM': 'level', 'MOD_COMUNI_ESCRITA_DESEM': 'Frequency'} )
        figure4 = px.bar(data.groupby(["MOD_COMUNI_ESCRITA_DESEM"]).count().reset_index(), x='MOD_COMUNI_ESCRITA_DESEM', y="MOD_INGLES_DESEM" ,
                        title='Communicative skills',labels={'MOD_COMUNI_ESCRITA_DESEM': 'level', 'MOD_INGLES_DESEM': 'Frequency'} )
        figure5 = px.bar(data.groupby(["MOD_RAZONA_CUANTITAT_DESEM"]).count().reset_index(), x='MOD_RAZONA_CUANTITAT_DESEM', y="MOD_INGLES_DESEM",
                        title='Quantitative thinking skills',labels={'MOD_RAZONA_CUANTITAT_DESEM': 'level', 'MOD_INGLES_DESEM': 'Frequency'} )
        return figure1, figure2, figure3, figure4, figure5

    # #############################################
    # # MAIN SERVER
    # #############################################

    return dash_app.server
