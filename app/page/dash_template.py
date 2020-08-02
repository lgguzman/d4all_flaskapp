import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import json
import pandas as pd
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
    
    message_specific='Included are those who  '
    message_cumulative='Excluded are those who only '
    df = {}
    dfno = {}
    # quantitative thinking
    df["pencritico"] = [
        ' identified explicit information from a single source, which was presented in tables or bar graphs with little data ',
        ' used simple arithmetic procedures from the given information ',
        ' were able to argue the validity of procedures (arithmetic, algebraic and variational) ',
        ' were capable of choosing the most appropriate procedure for solving problems '
    ]
    
    # critical reading
    df["readcritico"] = [
        ' identified elements of the text such as the theme, structure, among others as well as the communicative intention of the author ', 
        ' understood the global meaning from the cohesion elements, identified textual typology, discursive strategies, and recognized ' + \
        ' the functions of language to understand the meaning of the text ',
        ' went beyond the explicit information in the text, mastering the text comprehension strategies, could project writings from the text information ',
        ' valued the global content of the text based on local elements, the relationships between them, and their position in a given context from a hypothetical perspective '
    ]


    # conocimiento de comunidad : abarca competencias ciudadanas
    df["competencias"] = [
        ' demonstrated a notion of the present interests, worldviews, and dimensions of the principles ' + \
        ' consigned in the political constitution ',
        ' were aware of the individual and collective rights of every individual ',
        ' recognized the primacy of the Constitution over any other rule, in addition ' + \
        ' to the citizen duties enshrined in it ',
        ' were able to apply general knowledge about social situations for resolution. '
    ]
    ###### foreign lenguage  : ingles
    df["ingles"] = [
        ' could not show a minimum English knowledge  ',  #-A1
        ' understand, use everyday expressions, can ask for and give basic personal information ', #A1 
        ' are able to understand frequently used phrases and expressions related to especially relevant areas of experience ' + \
        ' They how to communicate on time, carry out simple and daily tasks and describe in simple terms aspects of her past and her environment ', #A2
        ' are able to understand the main points of clear texts, can deal with most situations that may arise during a journey, ' + \
        ' describe experiences, events and desires as well as justify briefly, share opinions or explain plans ', #B1
        ' are able to understand the main ideas of complex texts that deal with concrete abstract topics, ' +  \
        ' can relate to native speakers with a sufficient degree of fluency and naturalness, produce clear and detailed texts ' + \
        ' on various topics, as well as defend a point of view on general topics indicating the pros ' + \
        ' and cons of the different options.'  #B2
        ]
    dfno["ingles"] = [
        ' could not show a minimum English knowledge  ',  #-A1
        ' did not understand or used everyday expressions or could not ask for and give basic personal information very well ', #A1 
        ' were not able to understand frequently used phrases and expressions related to especially relevant areas of experience, ' + \
        ' did not know how to communicate on time, did not carry out simple and daily tasks and describe in simple terms aspects of her past and her environment ', #A2
        ' were not able to understand the main points of clear texts, could not deal with most situations that may arise during a journey, ' + \
        ' did not describe experiences, events and desires as well as justify briefly, share opinions or explain plans very well', #B1
        ' were not able to understand the main ideas of complex texts that deal with concrete abstract topics, ' +  \
        ' can relate to native speakers with a sufficient degree of fluency and naturalness, produce clear and detailed texts ' + \
        ' on various topics, as well as were not able to defend a point of view on general topics indicating the pros ' + \
        ' and cons of the different options.'  #B2
        ]   
        
    ######### Comunicación escrita (disyuntas)
    df["comescrita"] = [
        ' expressed disjointed ideas among themselves, which did not account for ' + \
        ' a coherent approach ',
        ' presented some flaws in their structure and organization, ' + \
        ' which made them lack unity semantics ',
        ' used a basic structure with a start, middle, and end, although scoring errors ' + \
        ' and cohesion failures could be identified ',
        ' showed different perspectives on the subject, made the approach more complex and allowed satisfactory fulfillment of the communicative purpose. It made proper use of punctuation marks, grammatical references, and connectors '
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
    def selected_config_fun(options,value):
        for adic in options:
            if adic['value'] == value:
                return adic['label']
                
        return " Not selected"        
    
    @dash_app.callback(
        Output(component_id='p_searchconfig', component_property='children'),
        [Input('dropdown_config', 'options'),Input('dropdown_config','value')]
    )
    def selected_config(dropdown_c_options,dropdown_c_value):
        return selected_config_fun(dropdown_c_options,dropdown_c_value)
    
    
    @dash_app.callback(
        Output(component_id='p_typesearch', component_property='children'),
        [Input('dropdown_search', 'options'),Input('dropdown_search','value')]
    )
    def selected_config(dropdown_s_options,dropdown_s_value):
        return selected_config_fun(dropdown_s_options,dropdown_s_value)
    
    @dash_app.callback(
        Output(component_id='p_reference', component_property='children'),
        [Input('dropdown_profesion', 'options'),Input('dropdown_profesion','value')]
    )
    def selected_config(dropdown_p_options,dropdown_p_value):
        return selected_config_fun(dropdown_p_options,dropdown_p_value)
                
    @dash_app.callback(
        Output(component_id='p_year', component_property='children'),
        [Input('dropdown_ano', 'options'),Input('dropdown_ano','value')]
    )
    def selected_config(dropdown_a_options,dropdown_a_value):
        return selected_config_fun(dropdown_a_options,dropdown_a_value)
        
    ############### STYLE FUNCTIONS #############
    ## función : selected_skill
    ## Cambia el color del perfil dependiendo del nivel de desempeño.
    ## Parametros rrange : valor numerico (de 1 a 4 indica el nivel de desempeño)
    ##            check  : lista (indica si checkbox esta elegida)

    def selected_skill(rrange):
        list_color = ['#FF2212', '#FFBC82', '#DC31FF', '#25BC66']
        return {'background-color': list_color[rrange[0] - 1],'border-radius':'25px','color':'white','padding':'5px','textAlign':'center'}
           

    #################### CALLBACK ###############
    ######## listing to competencias values #####
    @dash_app.callback(
        Output(component_id='div_comunitaria', component_property='children'),
        [Input('range_slider_com', 'value'), Input('dropdown_config','value')]
    )
    def update_perfil_div_com(range_slider_com,dropdown_config):
        nivel1 = df["competencias"][0]
        nivel2 = df["competencias"][1]
        nivel3 = df["competencias"][2]
        nivel4 = df["competencias"][3]
        output = ''
       
        # specific
        if int(dropdown_config) == 0:
            if range_slider_com[0] == 1:
                output = message_specific + nivel1
            elif range_slider_com[0] == 2:
                output = message_specific + nivel1 + ' and ' + nivel2
            elif range_slider_com[0] == 3:
                output = message_specific + nivel1 + ', '+ nivel2 + ' and '+  nivel3
            elif range_slider_com[0] == 4:
                output = message_specific + nivel1 + ', ' +  nivel2 + ', ' +  nivel3 + ' and ' + nivel4
        else: # cumulative
            if range_slider_com[0] == 1:
                output = "Included are the participants with all levels of skills."
            elif range_slider_com[0] == 2:
                output = message_cumulative + nivel1 + "."
            elif range_slider_com[0] == 3:
                output = message_cumulative + nivel1 + ' and '+ nivel2 + "."
            elif range_slider_com[0] == 4:
                output = message_cumulative + nivel1 + ', ' +  nivel2 + ' and ' +  nivel3 + " . "
        
        return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='h5_com', component_property='style'),
        [Input('range_slider_com', 'value')]
    )
    def update_perfil_div_com(range_slider_com):
        return selected_skill(range_slider_com)

    ######## listing reading critical ##################
    @dash_app.callback(
        Output(component_id='div_readcritical', component_property='children'),
        [Input('range_slider_quam', 'value'), Input('dropdown_config','value')]
    )
    def update_perfil_div_read(range_slider_quam, dropdown_config):
        nivel1 = df["readcritico"][0]
        nivel2 = df["readcritico"][1]
        nivel3 = df["readcritico"][2]
        nivel4 = df["readcritico"][3]
        output = ''
                    
        # specific
        if int(dropdown_config) == 0:
            if range_slider_quam[0] == 1:
                output = message_specific + nivel1
            elif range_slider_quam[0] == 2:
                output = message_specific + nivel1 + ' and ' + nivel2
            elif range_slider_quam[0] == 3:
                output = message_specific + nivel1 + ', '+ nivel2 + ' and '+  nivel3
            elif range_slider_quam[0] == 4:
                output = message_specific + nivel1 + ', ' +  nivel2 + ', ' +  nivel3 + ' and ' + nivel4
        else:
            if range_slider_quam[0] == 1:
                output = "Included are the participants with all levels of skills."
            elif range_slider_quam[0] == 2:
                output = message_cumulative + nivel1 + "."
            elif range_slider_quam[0] == 3:
                output = message_cumulative + nivel1 + ' and '+ nivel2 + "."
            elif range_slider_quam[0] == 4:
                output = message_cumulative + nivel1 + ', ' +  nivel2 + ' and ' +  nivel3 + " . "    

        
        return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='h5_readcritical', component_property='style'),
        [Input('range_slider_quam', 'value')]
    )
    def update_perfil_div_r(range_slider_quam):
        return selected_skill(range_slider_quam)
        
    ######## listing quantitative reasoning ##################
    @dash_app.callback(
        Output(component_id='div_qthinking', component_property='children'),
        [Input('range_slider_qthinking', 'value'), Input('dropdown_config','value')]
    )
    def update_perfil_div_pen(range_slider_qthinking, dropdown_config):
        nivel1 = df["pencritico"][0]
        nivel2 = df["pencritico"][1]
        nivel3 = df["pencritico"][2]
        nivel4 = df["pencritico"][3]
        output = ''
                  
        # specific
        if int(dropdown_config) == 0:
            if range_slider_qthinking[0] == 1:
                output = message_specific + nivel1
            elif range_slider_qthinking[0] == 2:
                output = message_specific + nivel1 + ' and ' + nivel2
            elif range_slider_qthinking[0] == 3:
                output = message_specific + nivel1 + ', '+ nivel2 + ' and '+  nivel3
            elif range_slider_qthinking[0] == 4:
                output = message_specific + nivel1 + ', ' +  nivel2 + ', ' +  nivel3 + ' and ' + nivel4
        else:
            if range_slider_qthinking[0] == 1:
                output = "Included are the participants with all levels of skills."
            elif range_slider_qthinking[0] == 2:
                output = message_cumulative + nivel1 + "."
            elif range_slider_qthinking[0] == 3:
                output = message_cumulative + nivel1 + ' and '+ nivel2 + "."
            elif range_slider_qthinking[0] == 4:
                output = message_cumulative + nivel1 + ', ' +  nivel2 + ' and ' +  nivel3 + " . "    

        
        return '{}'.format(output)

    @dash_app.callback(
        Output(component_id='h5_qthinking', component_property='style'),
        [Input('range_slider_qthinking', 'value')]
    )
    def update_perfil_div_pen(range_slider_qthinking):
        return selected_skill(range_slider_qthinking)

    ######## listing to language skills ##################
    @dash_app.callback(
        Output(component_id='div_ingles', component_property='children'),
        [Input('dropdown_foreign', 'value'), Input('dropdown_config', 'value')]
    )
    
    def update_perfil_div_ingles(dropdown_foreign, dropdown_config):
        nivel1 = df["ingles"][0]  #-A1
        nivel2 = df["ingles"][1]  #A1
        nivel3 = df["ingles"][2]  #A2
        nivel4 = df["ingles"][3]  #B1
        nivel5 = df["ingles"][4]  #B2
        nivel1no = dfno["ingles"][0]  #no -A1
        nivel2no = dfno["ingles"][1]  #no A1
        nivel3no = dfno["ingles"][2]  #no A2
        nivel4no = dfno["ingles"][3]  #no B1
        nivel5no = dfno["ingles"][4]  #no B2
        # output= df["ingles"][range_slider_foreign[0]-1]
        output = ''
        
        if int(dropdown_config) == 0:
            if int(dropdown_foreign) == 0:
                output = "(-A1) : " + message_specific + nivel1 
            elif int(dropdown_foreign) == 1:
                output = "(A1) : "  + message_specific + nivel2 
            elif int(dropdown_foreign) == 2:
                output = "(A2) : "  + message_specific + nivel3 
            elif int(dropdown_foreign) == 3:
                output = "(B1) : "  + message_specific + nivel4 
            elif int(dropdown_foreign) == 4:
                output = "(B2) : "  + message_specific + nivel5 
        else:
            if int(dropdown_foreign) == 0:
                output = "Includes are all with no or at least a minimum level of english skills"
            elif int(dropdown_foreign) == 1:
                output = "Excluded are those who" + nivel1no + "."
            elif int(dropdown_foreign) == 2:
                output = "Excluded are those who" + nivel2no + ' and ' + nivel1no + "."
            elif int(dropdown_foreign) == 3:
                output =  "Excluded are those who"+ nivel1no + ', ' +  nivel2no + ' and ' +  nivel3no + " . "   
            elif int(dropdown_foreign) == 4:
                output = "Excluded are those who" + nivel1no + ', ' +  nivel2no + ' , ' +  nivel3no + " and " + nivel4no + "."          
 
        return '{}'.format(output)

    ######## listing to habilidades comunicativas ##################
    @dash_app.callback(
        Output(component_id='div_comescrita', component_property='children'),
        [Input('range_slider_comm', 'value'), Input('dropdown_config', 'value')]
    )
    def update_perfil_div_comm(range_slider_comm, dropdown_config):
        nivel1 = df["comescrita"][0]
        nivel2 = df["comescrita"][1]
        nivel3 = df["comescrita"][2]
        nivel4 = df["comescrita"][3]
        #output = df["comescrita"][range_slider_comm[0] - 1]

        # specific
        if dropdown_config == 0:
            if range_slider_comm[0] == 1:
                output = message_specific + nivel1
            elif range_slider_comm[0] == 2:
                output = message_specific + nivel1 + ' and ' + nivel2
            elif range_slider_comm[0] == 3:
                output = message_specific + nivel1 + ', '+ nivel2 + ' and '+  nivel3
            elif range_slider_comm[0] == 4:
                output = message_specific + nivel1 + ', ' +  nivel2 + ', ' +  nivel3 + ' and ' + nivel4
        else:
            if range_slider_comm[0] == 1:
                output = "Included are the participants with all levels of skills."
            elif range_slider_comm[0] == 2:
                output = message_cumulative + nivel1 + "."
            elif range_slider_comm[0] == 3:
                output = message_cumulative + nivel1 + ' and '+ nivel2 + "."
            elif range_slider_comm[0] == 4:
                output = message_cumulative + nivel1 + ', ' +  nivel2 + ' and ' +  nivel3 + " . "   
       
       
       
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
        Output(component_id='h5_comm', component_property='style'),
        [Input('range_slider_comm', 'value')]
    )
    def update_perfil_div_comm(range_slider_comm):
        return selected_skill(range_slider_comm)

     
    ####################################################################################################

    def data_for_map(df1):
        dbs = DBSCAN(eps=600 / 6371,
                     min_samples=1,
                     metric='haversine').fit(df1[['Longitud', 'Latitud']])#,sample_weight=df1['count'])
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

            for ctype, dfff in df2.groupby('clus_db'):
                trace = dict(
                    type='scattermapbox',
                    lon=dfff['Longitud'],
                    lat=dfff['Latitud'],
                    name=str(ctype),
                    text=dfff['Nombre municipio'],
                    marker=dict(
                        size=dfff["count"].apply(lambda x: min(max(x,10),30)),
                        opacity=0.8,
                    )
                )
                traces.append(trace)
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
                        labels={'MOD_COMPETEN_CIUDADA_DESEM': 'Community skills level', 'MOD_INGLES_DESEM': 'Count'} )
        figure2 = px.bar(data.groupby(["MOD_LECTURA_CRITICA_DESEM"]).count().reset_index(), x='MOD_LECTURA_CRITICA_DESEM', y="MOD_INGLES_DESEM",
                        labels={'MOD_LECTURA_CRITICA_DESEM': 'Critical reading skills level', 'MOD_INGLES_DESEM': 'Count'} )
        figure3 = px.bar(data.groupby(["MOD_INGLES_DESEM"]).count().reset_index(), x='MOD_INGLES_DESEM', y="MOD_COMUNI_ESCRITA_DESEM" ,
                        labels={'MOD_INGLES_DESEM': 'English language skills level', 'MOD_COMUNI_ESCRITA_DESEM': 'Count'} )
        figure4 = px.bar(data.groupby(["MOD_COMUNI_ESCRITA_DESEM"]).count().reset_index(), x='MOD_COMUNI_ESCRITA_DESEM', y="MOD_INGLES_DESEM" ,
                        labels={'MOD_COMUNI_ESCRITA_DESEM': 'Communicative skills level', 'MOD_INGLES_DESEM': 'Count'} )
        figure5 = px.bar(data.groupby(["MOD_RAZONA_CUANTITAT_DESEM"]).count().reset_index(), x='MOD_RAZONA_CUANTITAT_DESEM', y="MOD_INGLES_DESEM",
                        labels={'MOD_RAZONA_CUANTITAT_DESEM': 'Quantitative thinking skills level', 'MOD_INGLES_DESEM': 'Count'} )
        return figure1, figure2, figure3, figure4, figure5

    # #############################################
    # # MAIN SERVER
    # #############################################

    return dash_app.server
