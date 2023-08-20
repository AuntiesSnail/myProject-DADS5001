import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

path = "https://raw.githubusercontent.com/AuntiesSnail/myProject-DADS5001/main/Final%20Project/II/stark_summary.csv"
df = pd.read_csv(path)

# Transpose, reset the index, and set the first row as the header
df = df.transpose()
df.columns = df.iloc[0]
df = df[1:].reset_index()
df.rename(columns={"index": "Year"}, inplace=True)
df["D/E"] = df["D/E"].str.replace(',', '').astype(float)

years = df["Year"].tolist()
de_values = df["D/E"].tolist()

# Create the D/E line
line_de = go.Scatter(x=years, y=de_values, mode='lines+markers', name='D/E')

# Create the target line with y=1
line_target = go.Scatter(x=years, y=[1]*len(years), mode='lines', name='Target', line=dict(color='#800000'))

# Combine both lines in one figure
fig = go.Figure([line_de, line_target])
fig.update_layout(
    title={
        'text': 'D/E over Years',
        'font': {'size': 24, 'color': 'black'}
    },
    xaxis_title='Year',
    yaxis_title='D/E',
    height=600,
    width=1000,
    template="plotly_white"
)
fig.update_yaxes(range=(0,7))

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
    html.H1("STARK: Debt of Equity Ratio (D/E)", style={"margin-left": "10px", "font-family": "Arial"})
    ], style={"display": "flex"}),
        
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
