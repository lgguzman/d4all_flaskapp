import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px




def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    df = pd.read_csv('./app/data/2019-2.csv', dtype=object) #, nrows=1000)
    df.columns = map(str.lower, df.columns)
    last_col_name = 'estu_areareside'
    col_num = [col for col, pos in enumerate(df.columns.str.find(last_col_name)) if pos != -1]
    col_num = col_num[0] + 1
    mydf = df[df.columns[:col_num]]
    mydf['periodo'] = mydf['periodo'].apply(lambda  x: str(x)+'-')
    data_final = mydf['periodo'].value_counts().reset_index()

    takers_fig = px.bar(data_final, x='index', y='periodo',
                 labels={'index': 'Term', 'periodo': 'Number of test takers [log]'})
    takers_fig.update_layout(yaxis_type="log")
    nationalities = mydf['estu_nacionalidad'].value_counts().reset_index()
    nationalities = nationalities[(nationalities['estu_nacionalidad'] > 10)]
    nationalities_fig = px.bar(nationalities, x='index', y='estu_nacionalidad',
                        labels={'index': 'NATIONALITY', 'estu_nacionalidad': 'Number of test takers [log]'})
    nationalities_fig.update_layout(yaxis_type="log")

    gnr = df['estu_genero'].value_counts().reset_index()
    gender_fig = px.bar(gnr, x='index', y='estu_genero',
                 labels={'index': 'Gender', 'estu_genero': 'Number of test takers [log]'})

    depto =  df['estu_depto_reside'].value_counts().reset_index()
    depto_fig = px.bar(depto, x='index', y='estu_depto_reside',
                        labels={'index': 'Depto', 'estu_depto_reside': 'Number of test takers [log]'})
    depto_fig.update_layout(yaxis_type="log")
    # Create Dash Layout
    dash_app.layout = html.Div([
        html.H2("SABER PRO 2019-2", id='title'),  # Creates the title of the app
        dcc.Graph(figure=takers_fig, id='takers'),
        dcc.Graph(figure=nationalities_fig, id='nationatlities'),
        dcc.Graph(figure=gender_fig, id='genders'),
        dcc.Graph(figure=depto_fig, id='depto'),
    ])






    # fig.show()





    # mydf['periodo'].value_counts().plot.bar(rot=0, logy=True)

    return dash_app.server