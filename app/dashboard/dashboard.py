import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Output
from dash.dependencies import Input
from sqlalchemy import create_engine


class DataBaseDashboard:

    def __init__(self):
        DB_HOSTNAME = 'ds4a-team-17-project.cjq7gkzfvgm7.us-east-1.rds.amazonaws.com'
        DB_DATABASE = 'icfes'
        DB_USERNAME = 'team17'
        DB_PASSWORD = 'team171234'
        try:
            self.ref_grp = pd.read_csv("/home/ec2-user/data4all/app/data/reference_groups.csv", encoding="utf-8")
            self.coord = pd.read_excel('/home/ec2-user/data4all/app/data/Coordenadas_Colombia_202061.xls')
        except Exception as inst:
            print("unable to load data")
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)
        self.engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}',
                                    pool_pre_ping=True)

    def count(self, column, database="sb1120192"):
        select = "SELECT " + "\"" + column + "\" AS label, "
        count = "COUNT(\"" + column + "\") AS " + column
        from_select = " FROM " + database
        group = " GROUP BY \"" + column + "\""
        return pd.read_sql_query(select + count + from_select + group, con=self.engine)

    def get(self, column, y, limit, database="sb1120192"):
        select = "SELECT " + "\"" + column + "\" AS label, "
        count = " \"" + y + "\" AS puntaje"
        from_select = " FROM " + database
        limit_select = " LIMIT " + str(limit)
        return pd.read_sql_query(select + count + from_select + limit_select, con=self.engine)

    def fetch_info(self, cty_sk,
                   ctc_rd,
                   fl_sk,
                   cmm_sk,
                   qtt_tk,
                   year,
                   ref_grp_index,
                   greather_or_equal):
        t = sorted(list(self.ref_grp["GRUPOREFERENCIA"].unique()))
        cmp2 = "("
        for l in list(self.ref_grp[self.ref_grp["GRUPOREFERENCIA"] == t[ref_grp_index]]["ESTU_SNIES_PRGMACADEMICO"]):
            cmp2 = cmp2 + str(l) + ","
        cmp2 = cmp2[:-1] + ")"
        icfes_qry = '''select 
                    count("ESTU_SNIES_PRGMACADEMICO"),
                    "ESTU_INST_CODMUNICIPIO"'''
        icfes_qry = icfes_qry + \
                    "from " + "gene" + year + "3"
        if greather_or_equal == 0:
            cmp0 = '''"MOD_COMPETEN_CIUDADA_DESEM" = ''' + str(cty_sk) + ''' and ''' + \
                   '''"MOD_LECTURA_CRITICA_DESEM" = ''' + str(ctc_rd) + ''' and ''' + \
                   '''"MOD_COMUNI_ESCRITA_DESEM" = ''' + str(cmm_sk) + ''' and ''' + \
                   '''"MOD_RAZONA_CUANTITAT_DESEM" = ''' + str(qtt_tk) + ''' and ''' + \
                   '''"MOD_INGLES_DESEM" in '''
            if fl_sk == "0":
                cmp1 = "('-A1')"
            elif fl_sk == "1":
                cmp1 = "('A1')"
            elif fl_sk == "2":
                cmp1 = "('A2')"
            elif fl_sk == "3":
                cmp1 = "('B1')"
            else:
                cmp1 = "('B2')"
            cmp0 = cmp0 + cmp1
        else:
            cmp0 = '''"MOD_COMPETEN_CIUDADA_DESEM" >= ''' + str(cty_sk) + ''' and ''' + \
                   '''"MOD_LECTURA_CRITICA_DESEM" >= ''' + str(ctc_rd) + ''' and ''' + \
                   '''"MOD_COMUNI_ESCRITA_DESEM" >= ''' + str(cmm_sk) + ''' and ''' + \
                   '''"MOD_RAZONA_CUANTITAT_DESEM" >= ''' + str(qtt_tk) + ''' and ''' + \
                   '''"MOD_INGLES_DESEM" in '''
            if fl_sk == "0":
                cmp1 = "('-A1','A1','A2','B1','B2')"
            elif fl_sk == "1":
                cmp1 = "('A1','A2','B1','B2')"
            elif fl_sk == "2":
                cmp1 = "('A2','B1','B2')"
            elif fl_sk == "3":
                cmp1 = "('B1','B2')"
            else:
                cmp1 = "('B2')"
            cmp0 = cmp0 + cmp1
        icfes_qry = icfes_qry + " where " + cmp0 + \
                    '''and "ESTU_SNIES_PRGMACADEMICO" in ''' + cmp2 + \
                    ''' GROUP BY "ESTU_INST_CODMUNICIPIO";'''
        icfes_df = pd.read_sql_query(icfes_qry, con=self.engine)
        icfes_df = pd.merge(icfes_df,
                            self.coord,
                            how='inner',
                            left_on=['ESTU_INST_CODMUNICIPIO'],
                            right_on=['Código municipio'])
        icfes_df.drop_duplicates(['ESTU_INST_CODMUNICIPIO'],
                                 keep='first', inplace=True)
        return icfes_df



def get_bar_fig(connection, column, database):
    data_final = connection.count(column, database)
    column_lc = column.lower()
    data_final['label'] = data_final['label'].apply(lambda x: str(x) + ' ')
    takers_fig = px.bar(data_final, x='label', y=column_lc, color=column_lc,
                        labels={'label': 'Term', column_lc: 'Number of test takers [log]'})
    takers_fig.update_layout(yaxis_type="log")
    return takers_fig


def get_box_fig(connection, column,y, limit,  database):
    data_final = connection.get(column, y, limit, database)
    data_final['label'] = data_final['label'].apply(lambda x: str(x) + ' ')
    takers_fig = px.box(data_final, x='label', y='puntaje', color='label')
    return takers_fig



def create_dashboard2(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    connection = DataBaseDashboard()
    # App Layout
    dash_app.layout = html.Div(
        children=[
            # Error Message
            html.Div(id="error-message"),
            # Top Banner
            html.Div(
                className="study-browser-banner row",
                children=[
                    html.H2(className="h2-title", children="ICFES (DATA4ALL)"),
                    html.H2(className="h2-title-mobile", children="ICFES (DATA4ALL)"),
                ],
            ),
            # Body of the App
            html.Div(
                className="row app-body",
                children=[
                    # User Controls
                    html.Div(
                        className="four columns card",
                        children=[
                            html.Div(
                                className="bg-white user-control",
                                children=[
                                    html.Div(
                                        className="padding-top-bot",
                                        children=[
                                            html.H6("Select Database"),
                                            dcc.Dropdown(id="study-dropdown",
                                                         options=[
                                                             {"label": "Saber Pro 2019", "value": "gene20193"},
                                                             {
                                                                 "label": "Saber 11 2019",
                                                                 "value": "sb1120192",
                                                             },
                                                         ],
                                                         value="sb1120192",
                                                         ),
                                        ],
                                    ),
                                    html.Div(
                                        className="padding-top-bot",
                                        children=[
                                            html.H6("Select Target"),
                                            dcc.Dropdown(id="column-dropdown",
                                                         options=[
                                                             {"label": "Periodo", "value": "PERIODO"},
                                                             {
                                                                 "label": "Nacionalidad",
                                                                 "value": "ESTU_NACIONALIDAD",
                                                             },
                                                             {
                                                                 "label": "Genero",
                                                                 "value": "ESTU_GENERO",
                                                             },
                                                             {
                                                                 "label": "Departamento",
                                                                 "value": "ESTU_DEPTO_RESIDE",
                                                             }
                                                         ],
                                                         value="PERIODO",
                                                         ),
                                        ],
                                    ),
                                    html.Div(
                                        className="padding-top-bot",
                                        children=[
                                            html.H6("Select N Samples (Only for Box chart)"),
                                            dcc.Dropdown(id="limit-dropdown",
                                                         options=[
                                                             {"label": "100", "value": 100},
                                                             {
                                                                 "label": "500",
                                                                 "value": 500,
                                                             },
                                                             {
                                                                 "label": "1000",
                                                                 "value": 1000,
                                                             },
                                                             {
                                                                 "label": "2000",
                                                                 "value": 2000,
                                                             },
                                                             {
                                                                 "label": "5000",
                                                                 "value": 5000,
                                                             },
                                                         ],
                                                         value=1000,
                                                         ),
                                        ],
                                    ),
                                    html.Div(
                                        className="padding-top-bot",
                                        children=[
                                            html.H6("Choose the type of plot"),
                                            dcc.RadioItems(
                                                id="chart-type",
                                                options=[
                                                    {"label": "Count Bar", "value": "bar"},
                                                    {
                                                        "label": "Score Box",
                                                        "value": "box",
                                                    },
                                                ],
                                                value="bar",
                                                labelStyle={
                                                    "display": "inline-block",
                                                    "padding": "12px 12px 12px 0px",
                                                },
                                            ),
                                        ],
                                    ),
                                ],
                            )
                        ],
                    ),
                    # Graph
                    html.Div(
                        className="eight columns card-left",
                        children=[
                            html.Div(
                                className="bg-white",
                                children=[
                                    html.H5("Animal data plot"),
                                    dcc.Loading(
                                        children=dcc.Graph(id="plot")
                                    )
                                ],
                            )
                        ],
                    ),
                    dcc.Store(id="error", storage_type="memory"),
                ],
            ),
        ]
    )
    # Callback to generate error message
    # Also sets the data to be used
    # If there is an error use default data else use uploaded data
    @dash_app.callback(
        Output("plot", "figure"),
        [Input("chart-type", "value"), Input("study-dropdown", "value"), Input("column-dropdown", "value"), Input("limit-dropdown", "value")]
    )
    def update_output(chart_type, database, column, limit):
        return get_bar_fig(connection, column, database) if chart_type == 'bar' else get_box_fig(connection, column, "PUNT_GLOBAL", limit, database)

    return dash_app.server


