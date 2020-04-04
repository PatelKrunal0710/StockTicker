import pandas as pd 
from pandas_datareader import data
import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output, State

def getstockdata(tickername):
    df = data.DataReader(tickername,start='2020-03-01',end='2020-03-31',data_source='yahoo')
    df = df.reset_index()
    # df.columns = [ 0,1,2,3,4,5]
    # df = df.columns =['','High','Low','Open','Close','Volume','Adj Close']
    print(df.columns)
    return df
getstockdata('AAON')

BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"

app = dash.Dash(external_stylesheets=[BS])

app.layout = html.Div([
    html.Div([
    html.Div([html.H1('Historical Stock Data Visualization',className="text-center")],className="navbar navbar-dark bg-dark text-white"),
],className="container"),
html.Div([
    html.Div([
        dcc.Input(id='Stock Name',placeholder="Enter the Stock Name",className='pt=5 form-control mr-sm-2'),
        html.Button("Submit",id='submitbtn',className="btn btn-primary"),
    ],className="form-inline my-2 my-lg-0")
    ],className="container pt-2"), 
    dcc.Graph(id='stockgraph'),
    
])
@app.callback(
    Output('stockgraph','figure'),
    [Input('submitbtn','n_clicks')],
    [State('Stock Name','value')],)

def getinput(stockname,clicks):
    data1 = []
    if clicks is not None:
        print(clicks)
        df = getstockdata(clicks)        
        data1.append(dict(
            x=df["Date"],
            y=df['High']
        ))        
    return{
        'data':data1,
    }
        
if __name__=='__main__':
    app.run_server(debug=True)