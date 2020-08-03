# Create global chart template
mapbox_access_token = 'pk.eyJ1IjoibGdndXptYW4iLCJhIjoiY2tibnlhc2V6MXhkNzMxbXl2bXJxcjlmeiJ9.vh_VD4rzpTZW-Wa23kt-lg'

layout = dict(
    autosize=True,
    height=640,
    automargin=True,
    margin=dict(
        l=30,
        r=30,
        b=20,
        t=40
    ),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    mapbox_style="carto-darkmatter",
    showlegend=False,
    title='',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(
            lon=-76.4851423,
            lat=5.0855571
        ),
        zoom=5,
    )
)
