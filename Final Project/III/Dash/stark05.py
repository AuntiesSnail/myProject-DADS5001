import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

path = r"D:\My Study\Master Degree\DADS\06._Summer_2022\DADS5001\2nd_Half\Final Project\II\stark_summary.csv"
df = pd.read_csv(path)

# Transpose, reset the index
df = df.transpose()
df.columns = df.iloc[0]
df = df[1:].reset_index()
df.rename(columns={"index": "Year"}, inplace=True)



df['Operating Cash Flow'] = df['Operating Cash Flow'].str.replace(',', '').astype(float)

years = df["Year"].tolist()
years = ["Q3/2022" if year == "2022" else year for year in years]

op_cash = df["Operating Cash Flow"].tolist()


fig = go.Figure( )
fig.add_trace(go.Bar(x=years, 
                     y=op_cash, 
                     name='Operating Cash Flow', 
                     marker=dict(color='#118DFF'), 
                     text=op_cash, 
                     textposition='outside')
                )
fig.update_layout(title='Operating Cash Flow over Years', 
                  xaxis_title='Year', 
                  yaxis_title='Operating Cash Flow',
                  height=600,
                  template = "plotly_white")

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
    html.H1("STARK: Operating Cash Flow", style={"margin-left": "10px", "font-family": "Arial"})
    ], style={"display": "flex"}),
    
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)