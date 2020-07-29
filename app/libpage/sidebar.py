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
         
        ########### community skills ##########       
        dbc.Card([dbc.Checklist(
            id='check_list_com',
            options=[{
                'label': 'Habilidades comunitarias',
                'value': 'comvalue'
             }
            ],
            #value=['comvalue'],
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
        
        ############# Q-reasoning skills #################
        dbc.Card([dbc.Checklist(
            id='check_list_quam',
            options=[
                {
                    'label': 'Pensamiento crítico',
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
                    'label': 'Idioma extrangero',
                    'value': 'forvalue'
                },
                
            ],
          
            inline=True
        )]),
        dcc.RangeSlider(
            id='range_slider_foreign',
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
        ################ communication skills ############
        
        dbc.Card([dbc.Checklist(
            id='check_list_comm',
            options=[
                {
                    'label': 'Habilidades comunicativas',
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
        
        ############### profesional skills  ##############
        
        dbc.Card([dbc.Checklist(
            id='check_list_prof',
            options=[
                {
                    'label': 'Competencia profesional', 
                    'value': 'provalue'
                }
            ],
           
            inline=True
        )]),
        dcc.RangeSlider(
            id='range_slider_prof',
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
        
        
        ################ profession     ###################
        dbc.Card([dbc.Checklist(
            id='check_list_profesion',
            options=[{
                'label': 'Profesion',
                'value': 'profvalue'
            }
            ],
            inline=True
        )]),
        html.P('ELIJE UNA PROFESIÓN', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown_profesion',
            options=[{
                'label': 'Administracion',
                'value': 'value1'
            }, {
                'label': 'Ingenieria',
                'value': 'value2'
            },
                {
                    'label': 'Comunicación social',
                    'value': 'value3'
                }
            ],
            value=['value1'],  # default value
            multi=True
        ),
        
        ############# años 
        html.P('Choose a year', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown_ano',
               options=[{'label': '2018', 'value': '2018'}, {'label': '2019', 'value': '2019'}],
                value=['2019']
         ),
        ############## genero
        html.P('Choose a gender', style={
            'textAlign': 'center'
        }),
         dcc.Dropdown(
            id='dropdown_genero',
               options=[{'label': 'Male', 'value':'female' }, {'label': 'Female', 'value': 'female'},{'label': 'Both', 'value': 'both'}],
                value=['both']
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
        html.H2('PERFIL', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)



