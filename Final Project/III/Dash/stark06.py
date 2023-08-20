import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objects as go

# Reading the CSV
path = "https://raw.githubusercontent.com/AuntiesSnail/myProject-DADS5001/main/Final%20Project/II/thl_cablebusiness.csv"
df = pd.read_csv(path)

# Extract years from the first column of the dataframe
years = df['Company'].astype(str).tolist()

# Dash App Initialization
app = dash.Dash(__name__)

# Define a' list of custom colors
colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4']

# Create a Plotly Figure using graph_objects
fig = go.Figure()

# Add a trace for each company and assign color
for index, col in enumerate(df.columns[1:]):  # Skip the 'Company' column
    fig.add_trace(go.Scatter(x=years, y=df[col].tolist(), mode='lines+markers', name=col, line=dict(color=colors[index])))

# Define the layout properties for the figure
fig.update_layout(title='',
                  xaxis_title='Year',
                  yaxis_title='Total Revenue',
                  template = "plotly_white")

app.layout = html.Div([
    
    html.Div([
    html.H1("STARK: Revenue Comparison among Companies in Cable/Wire Business", style={"margin-left": "10px", "font-family": "Arial"})
    ], style={"display": "flex"}),
        
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
