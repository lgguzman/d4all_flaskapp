
import dash_html_components as html
import dash_bootstrap_components as dbc

# row containing the labels of the parameter
cb_headeroption = dbc.Row(
                     [
                        dbc.Col(
                           [
                                html.I('Parameter',style={'width':'100%','textAlign':'center'})
                           ],
                           md=3,
                           style={'textAlign':'center'}
                        ),
                        dbc.Col(
                             [
                              html.I('Description',style={'width':'100%','textAlign':'center'})
                             ],
                             md=6,
                             style={'textAlign':'center'}
                             
                        ),
                        dbc.Col(
                             [
                                html.I('Selected option',style={'width':'100%','textAlign':'center'})
                             ],
                             md=3,
                             style={'textAlign':'center'}
                             
                        )
                     ]
)

#row containing the profile description labels
profile_description = dbc.Row(
                     [
                        dbc.Col(
                           [
                                html.I('Skills',style={'width':'100%','textAlign':'center','font-size':'18px'})
                           ],
                           md=3,
                           style={'textAlign':'center'}
                        ),
                        dbc.Col(
                             [
                              html.I('Description',style={'width':'100%','textAlign':'center','font-size':'18px'})
                             ],
                             md=9,
                             style={'textAlign':'center'}
                             
                        )
                     ]
)

# Row displaying the chosen search configuration
cb_chosenconfig = dbc.Row(
                       [
                          dbc.Col
                          (
                            [
                               html.B("Search configuration")
                            ],
                            md=3
                          ),
                          dbc.Col
                          (
                            [
                               html.P("Individuals will be selected either based on the chosen profile (specific) or at least " +\
                                      " the profile selected or a better one (cumulative) ",
                                      style={'textAlign':'justify'}
                                      )
                            ],
                            md=6
                            
                          
                          ),
                          dbc.Col
                          (
                            [
                               html.P(id='p_searchconfig',style={'textAlign':'center'})
                            
                            ],
                            md=3
                            
                          )
                       
                       ],
                       style={}
                    )

# Row displaying the type of search
cb_typeofsearch = dbc.Row(
                       [
                          dbc.Col
                          (
                            [
                               html.B("Type of Search")
                            ],
                            md=3
                          ),
                          dbc.Col
                          (
                            [
                               html.P("It refers to the type of clustering mechanism to be used",
                                      style={'textAlign':'justify'}
                                      )
                            ],
                            md=6
                            
                          
                          ),
                          dbc.Col
                          (
                            [
                               html.P(id='p_typesearch',style={'textAlign':'center','text-weight':'bold'})
                            
                            ],
                            md=3
                            
                          )
                       
                       ],
                       style={}
                    )

# Row displaying the reference group
cb_referencegroup = dbc.Row(
                       [
                          dbc.Col
                          (
                            [
                               html.B("Reference group")
                            ],
                            md=3
                          ),
                          dbc.Col
                          (
                            [
                               html.P("It refers to the reference group containing the academic program in which individuals are enrolled",
                                      style={'textAlign':'justify'}
                                      )
                            ],
                            md=6
                            
                          
                          ),
                          dbc.Col
                          (
                            [
                               html.P(id='p_reference',style={'textAlign':'center','text-weight':'bold'})
                            
                            ],
                            md=3
                            
                          )
                       
                       ],
                       style={}
                    )
# Row displaying the year
cb_year = dbc.Row(
                       [
                          dbc.Col
                          (
                            [
                               html.B("Search in year")
                            ],
                            md=3
                          ),
                          dbc.Col
                          (
                            [
                               html.P("Chosen year to be analyzed by Profesional Locator",
                                      style={'textAlign':'justify'}
                                      )
                            ],
                            md=6
                            
                          
                          ),
                          dbc.Col
                          (
                            [
                               html.P(id='p_year',style={'textAlign':'center','text-weight':'bold'})
                            
                            ],
                            md=3
                            
                          )
                       
                       ],
                       style={}
                    )

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
                    html.H4('Search parameter and Profile description', style={
                        'textAlign': 'center',
                        'color': 'blue'})
                ]

            ),

            dbc.CardBody(
                [
                    cb_headeroption,
                    html.Hr(),
                    ############## next row config info #################
                    cb_chosenconfig,
                    #html.Hr(),
                    ############### next row type of search ###########
                    cb_typeofsearch,
                    #html.Hr(),
                    ################# next row reference group ###########
                    cb_referencegroup,
                    #html.Hr(),
                    #################  next row year #####################
                    cb_year,
                    html.Br(),
                    ################# chosen profile ###########
                    html.P('Profile description',
                    style={
                      'width':'100%',
                      'font-weight':'bold',
                      'textAlign':'left',
                      'border-bottom':'1px solid gray'
                    }
                    ),
                    ########################################################
                    dbc.Row
                    (
                        [
                            dbc.Col
                            (
                                [
                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('multy-user.png'),style={'width': '50px', 'textAlign': 'center'})
                                        ],
                                        style={'textAlign': 'center'}
                                        )
                                ],
                                md=3
                            ),
                            dbc.Col
                            (
                                [
                                    html.P('The level of cognitive and conceptual demand demonstrated in each particular' + \
                                                       ' competence is categorized in an ascending range of 1 of 4',
                                                       style={'text-align': 'justify', 'padding-left': '10px', 'padding-right': '10px',
                                                              'font-style': 'italic'}
                                                       )
                                ],
                                md=6
                            ),
                            dbc.Col
                            (
                                [
                                    html.Div(
                                        [
                                                                dbc.Button(" 1 ",
                                                                           color="primary",
                                                                           # className='btn btn-primary',
                                                                           style={'border-radius': '25px',
                                                                                  'font-weight': 'bold',
                                                                                  'padding': '2px 10px 2px 10px',
                                                                                  'margin': '0px 5px 0px 5px',
                                                                                  'background-color': '#FF2212'
                                                                                  }
                                                                           ),
                                                                dbc.Button(" 2 ",
                                                                           color="primary",
                                                                           # className='btn btn-primary',
                                                                           style={'border-radius': '25px',
                                                                                  'font-weight': 'bold',
                                                                                  'padding': '2px 10px 2px 10px',
                                                                                  'margin': '0px 5px 0px 5px',
                                                                                  'background-color': '#FFBC82'
                                                                                  }
                                                                           ),
                                                                dbc.Button(" 3 ",
                                                                           color="primary",
                                                                           # className='btn btn-primary',
                                                                           style={'border-radius': '25px',
                                                                                  'font-weight': 'bold',
                                                                                  'padding': '2px 10px 2px 10px',
                                                                                  'margin': '0px 5px 0px 5px',
                                                                                  'background-color': '#DC31FF'
                                                                                  }
                                                                           ),
                                                                dbc.Button(" 4 ",
                                                                           color="primary",
                                                                           # className='btn btn-primary',
                                                                           style={'border-radius': '25px',
                                                                                  'font-weight': 'bold',
                                                                                  'padding': '2px 10px 2px 10px',
                                                                                  'margin': '0px 5px 0px 5px',
                                                                                  'background-color': '#25BC66'
                                                                                  }
                                                                           )

                                        ],
                                        style={'textAlign': 'center'}
                                    )# end of div
                                ],
                                md=3
                            )  # end of col                              
                        ],
                        style={}
                    ), # end of row  
                    profile_description,  
                    html.Br(),
                    ################ next row community skills #############
                    dbc.Row(
                        [
                            dbc.Col
                            (
                                [
                                    html.H5('Community skills',
                                        id='h5_com',
                                        style=
                                         {
                                        'textAlign': 'left',
                                        'boder': '1px solid black',
                                        'width':'100%',
                                         'padding':'5px',
                                         'color':'white'
                                         }
                                     )
                                ],
                                md=3
                       
                            ),
                            dbc.Col
                            (
                                [
                                   html.U("Refer to the knowledge and skills for understanding the exercise of citizenship:",
                                    style={'text-align':'justify'}
                                    ), 
                                   html.Br(),
                                    html.Div(id='div_comunitaria', className='card-text',style={'textAlign':'justify'})
                                ],
                                md=9
                       
                            ) # end of col
                            
                        ]
                    ),
                    html.Br(),
                    ################next row critical reading #####################
                    dbc.Row(
                        [                    
                    
                            dbc.Col
                            (
                               [
                                   html.H5('Critical reading skills',
                                    id='h5_readcritical',
                                    style=
                                         {
                                        'textAlign': 'center',
                                        'boder': '1px solid black',
                                        'width':'100%',
                                         'padding':'5px',
                                         'color':'white'
                                         }
                                    )                                             
                               
                               ],
                               md=3                               
                    
                            ), # end of col
                            dbc.Col
                            (
                               [
                                   html.U("Refer to the abilities to understand, interpret and evaluate texts in everyday life and in non-specialized academic fields:",
                                    style={'text-align':'justify'}
                                    ), 
                                   html.Br(),
                                   html.Div(id='div_readcritical', className='card-text',style={'textAlign':'justify'})                                
                               
                               ],
                               md=9                               
                    
                            ) # end of col
                        ]
                    ), # end of row   
                    html.Br(),
                    ################# next row ####################################
                    dbc.Row(
                        [          
                            
                            dbc.Col
                            (
                                [
                                    html.H5('Communicative skills',
                                        id='h5_comm',
                                        style=
                                         {
                                        'textAlign': 'left',
                                        'boder': '1px solid black',
                                        'width':'100%',
                                         'padding':'5px',
                                         'color':'white'
                                         }
                                    )
                                ],
                                md=3
                                                        
                            ),
                            dbc.Col
                            (
                                [
                                   html.U("Refer to the abilities to understand, interpret and evaluate texts in everyday life and in non-specialized academic fields:",
                                    style={'text-align':'justify'}
                                    ), 
                                   html.Br(),
                                    html.Div(id='div_comescrita',className='card-text',style={'textAlign':'justify'})   
                                
                                ],
                                md=9
                                                        
                            ) # end of col
                        ]
                    ),
                    html.Br(),
                    ##################### next row ###############################
                    dbc.Row(
                        [
                            dbc.Col
                            (
                                [
                                    html.H5('Quantitative Thinking skills',
                                        id='h5_qthinking',
                                        style=
                                         {
                                        'textAlign': 'center',
                                        'boder': '1px solid black',
                                        'width':'100%',
                                         'padding':'5px',
                                         'color':'white'
                                         
                                          
                                         }
                                        )             
                                ],
                                md=3
                                                       
                            ), ## end of col
                            dbc.Col
                            (
                                [
                                    html.U("Refer  to the application of basic mathematics skills to the analysis and interpretation of real-world quantitative problems:",
                                    style={'text-align':'justify'}
                                    ), 
                                    html.Br(),
                                    html.Div(id='div_qthinking', className='card-text',style={'textAlign':'justify'}),
                                ],
                                md=9
                                                       
                            ) # end of col
                        ]
                    ), # end of row                       
                    html.Br(),
                    ##################### next row ################################
                    dbc.Row(
                        [   
                            dbc.Col(
                                [
                                    html.H5('English language Skills',
                                    id='h5_ingles',
                                    style=
                                         {
                                         'textAlign': 'left',
                                         'width':'100%',
                                         'padding':'5px',
                                         'border-radius':'25px',
                                         'border':'1px solid black'
                                         }
                                    )
                                ],
                                md=3
                                  
                            ),   ## end of col
                            dbc.Col(
                                [
                                    html.U("Here are options going from -A1 (no English)  to B2 (highest level):",
                                    style={'text-align':'justify'}
                                    ),
                                    html.Div(id='div_ingles', className='card-text',style={'textAlign':'justify'})
                                
                                ],
                                md=9
                                  
                            )   ## end of col
                        ]    
                    )
                                    
                    ###############################################################
                ],
                style={"width": "100%", 'border-radius': '25px'}
            ),
        ],
        style={'padding':'20px',
        'border':'1px solid black'
       
             
        
        }
    )




    return dbc.Modal(
            [

                dbc.ModalBody(card),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close-centered", className="ml-auto"
                    )
                ),
            ],
            id="modal-centered",
             size='xl',
             style={ 'box-shadow': '0 0 0 0.5em #007bff'}
            
        )




