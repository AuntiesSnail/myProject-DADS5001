import pandas as pd
import dash
from dash import dcc
from dash import html

def preprocess_data(path, start_date, end_date):
    df = pd.read_csv(path)
    df = df[df['Date'] != 'Remark:']
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['Date'])
    
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    filtered_df = df.loc[mask]
    return filtered_df

def create_layout(dataframe, column_name, line_name):
    return dcc.Graph(
        id=line_name.replace(" ", "-").lower() + '-graph',
        figure={
            'data': [
                {'x': dataframe['Date'], 'y': dataframe[column_name], 'type': 'line', 'name': line_name},
            ],
            'layout': {
                'title': 'Stock Line Graph',
                'xaxis': {
                    'title': 'Date',
                    'tickformat': '%b %Y',
                    'nticks': 12
                },
                'yaxis': {
                    'title': column_name
                }
            }
        }
    )

# Paths to datasets
path1 = r"D:\My Study\Master Degree\DADS\06._Summer_2022\DADS5001\2nd_Half\Final Project\II\stark.csv"
path2 = r"D:\My Study\Master Degree\DADS\06._Summer_2022\DADS5001\2nd_Half\Final Project\II\cwt.csv"

start_date = "01/01/2021"
end_date = "31/03/2023"

# Preprocess data for both datasets
filtered_df1 = preprocess_data(path1, start_date, end_date)
filtered_df2 = preprocess_data(path2, start_date, end_date)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    create_layout(filtered_df1, 'Close', 'Stock Close Value Dataset 1'),
    create_layout(filtered_df2, 'Close', 'Stock Close Value Dataset 2')
])

if __name__ == '__main__':
    app.run_server(debug=True)
