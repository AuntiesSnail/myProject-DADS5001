import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

path = r"D:\My Study\Master Degree\DADS\06._Summer_2022\DADS5001\2nd_Half\Final Project\II\stark_summary.csv"
df = pd.read_csv(path)


years = [str(x) for x in df.columns[1:].tolist()]
years = ['Q3/2022' if x == '2022' else x for x in years]
revenue = df[df['Year'] == 'Total Revenue (MB)'].iloc[0, 1:].tolist()
net_profit = df[df['Year'] == 'Net Profit'].iloc[0, 1:].tolist()


# Initialize the Dash app
app = dash.Dash(__name__)

default_color = '#118DFF'
# App layout
app.layout = html.Div([
    html.Div([
    html.H1("STARK: Revenue and Profit", style={"margin-left": "10px", "font-family": "Arial"})
    ], style={"display": "flex"}),
    
    dcc.Graph(id='bar-graph',
              config={'displayModeBar': True, 'editable': True},
              figure={
                  'data': [
                      go.Bar(x=years, y=revenue, marker_color=default_color, text=revenue, textposition='outside')
                  ],
                  'layout': go.Layout(
                      title='Total Revenue over Years',
                      xaxis=dict(title='Year',type ='category'),
                      yaxis=dict(title='Total Revenue (MB)'),
                      clickmode='event+select',
                      height=500
                  )
              }),
   
    html.Div([
    html.H1("xxxxxxxxxx", style={"margin-left": "10px", "font-family": "Arial", "color":"White"})
    ], style={"display": "flex"}),

    dcc.Input(id='color-picker', value=default_color, type='color'),
    dcc.Graph(
        id='profit-graph',
        figure={
            'data': [
             go.Bar(x=years, y=net_profit , marker_color=default_color, text=net_profit, textposition='outside')
            ],
            'layout': go.Layout(
                title='Net Profit by Year',
                xaxis=dict(title = 'Year', type = 'category'),
                yaxis=dict(title ='Net Profit'),
                height=500
               
            )
        }
    )
], style={'columnCount': 2})

@app.callback(
    dash.dependencies.Output('bar-graph', 'figure'),
    [dash.dependencies.Input('color-picker', 'value')]
)
def update_graph(color_value):
    revenue_figure = {
        'data': [
            go.Bar(x=years, y=revenue, marker_color=default_color, text=revenue, textposition='outside')
        ],
        'layout': go.Layout(
            title='Total Revenue over Years',
            xaxis=dict(title='Year', type='category'),
            yaxis=dict(title='Total Revenue (MB)'),
            clickmode='event+select'
        )
    }
    
    profit_figure = {
        'data': [
            go.Bar(x=years, y=net_profit, marker_color=default_color, text=net_profit, textposition='outside')
        ],
        'layout': go.Layout(
            title='Net Profit by Year',
            xaxis=dict(title='Year', type='category'),
            yaxis=dict(title='Net Profit')
        )
    }
    
    return revenue_figure, profit_figure

if __name__ == '__main__':
    app.run_server(debug=True)
