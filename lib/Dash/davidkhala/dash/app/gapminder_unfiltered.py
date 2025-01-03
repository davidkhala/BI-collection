from dash import Dash, html, dcc, callback, Output, Input
from plotly import express
import pandas

df = pandas.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash()

app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country == value]
    return express.line(dff, x='year', y='pop')


@app.server.route('/health')
def is_health():
    return 'OK'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
