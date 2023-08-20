import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd


data = {
    'Year': ['2019', '2020', '2021', '2022/Q3'],
    'A/R Net': [3464.59, 6041.75, 15570.82, 19615.42],
    'Inventories': [3671.42, 8618, 10486.81, 15104.16],
    'Total Liabilities': [10341.33, 23552.77, 32550.85, 38362.30]
}

df = pd.DataFrame(data)


df['A/R Net'] = pd.to_numeric(df['A/R Net'])
df['Inventories'] = pd.to_numeric(df['Inventories'])
df['Total Liabilities'] = pd.to_numeric(df['Total Liabilities'])


years = df['Year'].tolist()
ar_net_values = df['A/R Net'].tolist()
inventories_values = df['Inventories'].tolist()
total_liabilities_values = df['Total Liabilities'].tolist()

# Plotly figures
bar_ar_net = go.Bar(x=years, y=ar_net_values, name='A/R Net', marker=dict(color='#118DFF'),text=ar_net_values, textposition='outside')
bar_inventories = go.Bar(x=years, y=inventories_values, name='Inventories', marker=dict(color='#12239E'),text=inventories_values, textposition='outside')
line_total_liabilities = go.Scatter(x=years, y=total_liabilities_values, mode='lines+markers', name='Total Liabilities', line=dict(color='#800000'), yaxis='y2')

layout = go.Layout(
    title='Accounts Receivable Net and Inventories over Years',
    xaxis=dict(title='Year'),
    yaxis=dict(title='A/R Net and Inventories'),
    yaxis2=dict(title='Total Liabilities', overlaying='y', side='right'),
    barmode='group',
    template = "plotly_white",
    height = 500
)

fig = go.Figure(data=[bar_ar_net, bar_inventories, line_total_liabilities], layout=layout)

# Dash app setup
app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
    html.H1("STARK: Key Financial Metrics", style={"margin-left": "10px", "font-family": "Arial"})
    ], style={"display": "flex"}),
    
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
