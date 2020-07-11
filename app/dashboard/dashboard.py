import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine


class DataBaseDashboard:

    def __init__(self):
        DB_HOSTNAME = 'ds4a-team-17-project.cjq7gkzfvgm7.us-east-1.rds.amazonaws.com'
        DB_DATABASE = 'icfes'
        DB_USERNAME = 'team17'
        DB_PASSWORD = 'team171234'
        self.engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}', pool_pre_ping=True)

    def get_all(self, database="sb1120192"):
        return pd.read_sql_query("""
           SELECT  "ESTU_NACIONALIDAD",
           "ESTU_GENERO", 
           "PERIODO",
           "ESTU_DEPTO_RESIDE" 
           """ + " FROM " + database  , con=self.engine)

    def get_periodo(self, database="sb1120192"):
        return pd.read_sql_query("""
           SELECT   
           "PERIODO" AS label, 
           COUNT("PERIODO") AS PERIODO
           """ +  " FROM " + database + """ GROUP BY "PERIODO"
           """  , con=self.engine)

    def get_nacionalidad(self, database="sb1120192"):
        return pd.read_sql_query("""
           SELECT   
           "ESTU_NACIONALIDAD" AS label, 
           COUNT("ESTU_NACIONALIDAD") AS ESTU_NACIONALIDAD
           """ +  " FROM " + database + """ GROUP BY "ESTU_NACIONALIDAD"
           """  , con=self.engine)

    def get_genero(self, database="sb1120192"):
        return pd.read_sql_query("""
           SELECT   
           "ESTU_GENERO" AS label, 
           COUNT("ESTU_GENERO") AS ESTU_GENERO
           """ +  " FROM " + database + """ GROUP BY "ESTU_GENERO"
           """  , con=self.engine)

    def get_dpto(self, database="sb1120192"):
        return pd.read_sql_query("""
           SELECT   
           "ESTU_DEPTO_RESIDE" AS label, 
           COUNT("ESTU_DEPTO_RESIDE") AS ESTU_DEPTO_RESIDE
           """ +  " FROM " + database + """ GROUP BY "ESTU_DEPTO_RESIDE"
           """  , con=self.engine)



def get_general_figs(connection, database):
    data_final = connection.get_periodo(database)
    data_final['label'] = data_final['label'].apply(lambda x: str(x) + '-')
    takers_fig = px.bar(data_final, x='label', y='periodo',
                         labels={'label': 'Term', 'periodo': 'Number of test takers [log]'})
    takers_fig.update_layout(yaxis_type="log")

    nationalities = connection.get_nacionalidad(database)
    nationalities = nationalities[(nationalities['estu_nacionalidad'] > 10)]
    nationalities_fig = px.bar(nationalities, x='label', y='estu_nacionalidad',
                                labels={'label': 'NATIONALITY', 'estu_nacionalidad': 'Number of test takers [log]'})
    nationalities_fig.update_layout(yaxis_type="log")

    gnr = connection.get_genero(database)
    gender_fig = px.bar(gnr, x='label', y='estu_genero',
                         labels={'label': 'Gender', 'estu_genero': 'Number of test takers [log]'})

    depto = connection.get_dpto(database)
    depto_fig = px.bar(depto, x='label', y='estu_depto_reside',
                        labels={'label': 'Depto', 'estu_depto_reside': 'Number of test takers [log]'})
    depto_fig.update_layout(yaxis_type="log")
    return takers_fig, nationalities_fig, gender_fig, depto_fig


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/api/dashapp/'
    )

    connection = DataBaseDashboard()

    # test =pd.read_sql_query('''SELECT table_catalog, table_schema, table_name, table_type
    #                      FROM information_schema.tables
    #                      WHERE table_name LIKE '%%pro%%'
    #                      ORDER BY table_name DESC;
    #                      ''', con=database.engine)
    # print(test.head(80))

    ##SABER 11
    takers_fig, nationalities_fig, gender_fig, depto_fig = get_general_figs(connection, "sb1120192")

    ##SABER 12

    takers_fig2, nationalities_fig2, gender_fig2, depto_fig2 = get_general_figs(connection, "gene20193")

    # Create Dash Layout
    dash_app.layout = html.Div([
        html.H2("SABER 11 2019-2", id='title'),  # Creates the title of the app
        dcc.Graph(figure=takers_fig, id='takers'),
        dcc.Graph(figure=nationalities_fig, id='nationatlities'),
        dcc.Graph(figure=gender_fig, id='genders'),
        dcc.Graph(figure=depto_fig, id='depto'),
        html.H2("SABER PRO 2019-2", id='title2'),  # Creates the title of the app
        dcc.Graph(figure=takers_fig2, id='takers2'),
        dcc.Graph(figure=nationalities_fig2, id='nationatlities2'),
        dcc.Graph(figure=gender_fig2, id='genders2'),
        dcc.Graph(figure=depto_fig2, id='depto2'),
    ])


    return dash_app.server