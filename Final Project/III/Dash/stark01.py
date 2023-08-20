import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

path = "https://raw.githubusercontent.com/AuntiesSnail/myProject-DADS5001/main/Final%20Project/II/stark.csv"
df = pd.read_csv(path)
#print(df.info())


# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
    html.H1("STARK: Stock Performance Price", style={"margin-left": "10px", "font-family": "Arial"})
    ], style={"display": "flex"}),

    dcc.Graph(
        id='stock-graph',
        figure={
            'data': [
                {'x': df['Date'], 'y': df['Close'], 'type': 'line', 'name': 'Stock Close Value'},
            ],
            'layout': {
                'title': 'STARK Price by Date',
                'xaxis': {
                    'title': '',
                },
                'yaxis': {
                    'title': 'STARK Price (THB)'
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
