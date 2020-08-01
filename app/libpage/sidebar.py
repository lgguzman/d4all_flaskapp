#Basics Requirements
import dash_core_components as dcc
import dash_html_components as html


#Dash Bootstrap Components
import dash_bootstrap_components as dbc 



# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    #    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    # 'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

controls = dbc.FormGroup(
    [

        ############ SEARCH CONFIGURATION
        html.Br(),
        html.B('SEARCH CONFIGURATION',
               style={
                   'textAlign': 'center'
               }),

        html.Br(),
        dcc.Dropdown(
            id='dropdown_config',
            options=[
                {'label': 'Specific', 'value': 0},
                {'label': 'Cumulative', 'value': 1}
            ],
            value=0
        ),

        ########### community skills ##########
        html.Br(),

        html.B('CHOOSE THE PROFILE', style={
            'textAlign': 'center'
        }),



        dbc.Card([dbc.Checklist(
            id='check_list_com',
            options=[{
                'label': 'Community skills',
                'value': 'comvalue'
            }
            ],
            # value=['comvalue'],
            inline=True
        )]),
        dcc.RangeSlider(
            id='range_slider_com',
            min=1,
            max=4,
            step=1,
            value=[1],
            marks={
                1: {'label': '1', 'style': {'color': '#77b0b1'}},
                2: {'label': '2'},
                3: {'label': '3'},
                4: {'label': '4', 'style': {'color': '#f50'}}
            }
        ),

        ############# Critical Reading skills #################
        dbc.Card([dbc.Checklist(
            id='check_list_quam',
            options=[
                {
                    'label': 'Critical reading',
                    'value': 'quamvalue'
                }
            ],
            inline=True
        )]),
        dcc.RangeSlider(
            id='range_slider_quam',
            min=1,
            max=4,
            step=1,
            value=[1],
            marks={
                1: {'label': '1', 'style': {'color': '#77b0b1'}},
                2: {'label': '2'},
                3: {'label': '3'},
                4: {'label': '4', 'style': {'color': '#f50'}}
            }
        ),
        ############# Foreign language  ###################

        dbc.Card([dbc.Checklist(
            id='check_list_foreign',
            options=[
                {
                    'label': 'Foreign language skills',
                    'value': 'forvalue'
                },

            ],

            inline=True
        )]),
        dcc.Dropdown(
            id='dropdown_foreign',
            options=[{
                'label': '-A1',
                'value': '0'
            }, {
                'label': 'A1',
                'value': '1'
            },
                {
                    'label': 'A2',
                    'value': '2'
                },
                {
                    'label': 'B1',
                    'value': '3'
                },
                {
                    'label': 'B2',
                    'value': '4'
                }
            
            ],
            value='1'
        ),
        ################ communication skills ############

        dbc.Card([dbc.Checklist(
            id='check_list_comm',
            options=[
                {
                    'label': 'Communicative skills',
                    'value': 'comyvalue'
                }
            ],

            inline=True
        )]),
        dcc.RangeSlider(
            id='range_slider_comm',
            min=1,
            max=4,
            step=1,
            value=[1],
            marks={
                1: {'label': '1', 'style': {'color': '#77b0b1'}},
                2: {'label': '2'},
                3: {'label': '3'},
                4: {'label': '4', 'style': {'color': '#f50'}}
            }
        ),

        ############### quantitative thinking skills  ##############

        dbc.Card([dbc.Checklist(
            id='check_list_qthinking',
            options=[
                {
                    'label': 'Quantitative thinking skills',
                    'value': 'qthinkingvalue'
                }
            ],

            inline=True
        )]),
        dcc.RangeSlider(
            id='range_slider_qthinking',
            min=1,
            max=4,
            step=1,
            value=[1],
            marks={
                1: {'label': '1', 'style': {'color': '#77b0b1'}},
                2: {'label': '2'},
                3: {'label': '3'},
                4: {'label': '4', 'style': {'color': '#f50'}}
            }
        ),

        
        html.Br(),
        html.B('CHOOSE A REFERENCE GROUP', style={
            'textAlign': 'left'
        }),
        dcc.Dropdown(
            id='dropdown_profesion',
            options=[
            {
                'label': 'Fine arts and Design',
                'value': 2
            },
            {
                'label': 'Natural and exact Sciences',
                'value': 5
            },
            {
                    'label': 'Social Sciences',
                    'value': 6
             },
             {
                    'label': 'Humanities',
                    'value': 13
             },   
             {
                    'label': 'Law',
                    'value': 9
             },   
             {
                    'label': 'Communication, journalism and advertising',
                    'value': 7
             },   
             {
                    'label': 'Military and naval Sciences',
                    'value': 4
             },   
             {
                    'label': 'Agricultural Sciences',
                    'value': 3
             },   
             {
                    'label': 'Management and related',
                    'value': 0
             },   
             {
                    'label': 'Education',
                    'value': 11
             },   
             {
                    'label': 'Arquitecture and urban planning',
                    'value': 1
             },   
             {
                    'label': 'Engineering',
                    'value': 14
             },
             {
                    'label': 'Health care',
                    'value': 18
             },
             {
                    'label': 'Medicine',
                    'value': 15
             },
             {
                    'label': 'Recreation and Sports',
                    'value': 17
             },
             {
                    'label': 'Economy',
                    'value': 10
             },
             {
                    'label': 'Accounting and related',
                    'value': 8
             },
             {
                    'label': 'Psychology',
                    'value': 16
             },   
             {
                    'label': 'Nursing',
                    'value': 12
             }   
            ],
            value=1
            
        ),

        ############# años
        html.Br(),
        html.B('Choose a year', style={
            'textAlign': 'left'
        }),
        dcc.Dropdown(
            id='dropdown_ano',
            options=[{'label': '2018', 'value': '2018'}, {'label': '2019', 'value': '2019'}],
            value='2019'
        ),

        ## rafael ###
        ############# años
        html.Br(),
        html.B('TYPE OF SEARCH', style={
            'textAlign': 'left'
        }),
        dcc.Dropdown(
            id='dropdown_search',
            options=[
                {'label': 'Centralized', 'value': 0},
                {'label': 'Decrentralized', 'value': 1}
            ],
            value=0
        ),

        ########### submit button ##############

        html.Br(),
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            block=True

        ),
    ]
)
########### SIDEBAR left side #######################
sidebar = html.Div(
    [
      html.H2(['Profile', html.I(id='info-button', n_clicks=0, className='fa fa-info-circle', style={'font-size':'18px'})], style=TEXT_STYLE) ,
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)



