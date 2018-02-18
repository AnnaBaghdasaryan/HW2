import dash
import dash_core_components as dcc
import dash_html_components as html
from app2 import figure1
from app2 import figure2
from app2 import figure3
from app2 import figure4
from app2 import figure5


app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div([

# Heading

        html.Div([
          html.H1("", className='four columns'),
          html.H2("Homework 3",style={'color': 'purple',"font-family":'Comic Sans MS','font-weight':'strong','font-weight':'bold','fontSize': 32}, className='four columns'),
          html.H1("", className='four columns')
          ], className="row"),
# Barplot
        html.Div([
          html.Div("Homework 3 assumes the development of this web application using Dash and Plotly in Python. You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does.Quandl is used as a data source for 4 plots among 6, while the other 2 are based on user provided data. Some of the Quandl based plots require minor analysis using pandas. You are encouraged to follow below mentioned steps to complete the HW:",style={'font-family':'calibri','fontSize':18}, className='four columns'),
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 1**"),style={'font-family':'calibri','font-weight':'strong','fontSize': 16}),html.Div(["The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or correlation value differences will be neglected."])]), style={'font-family':'calibri','fontSize': 18},className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_1", figure= figure1,className='four columns'))
            ])
         ], className= "row"),
# Line graph
        html.Div([
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 2**"),style={'font-family':'calibri','font-weight':'strong','fontSize': 16}),html.Div(["One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph."])]),style={'font-family':'calibri','fontSize':18},className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_2", figure= figure2,className='six columns'))
            ]),
          html.Div("", className='two columns'),
          
         ], className= "row"),

# Box Plot+Table
        html.Div([
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 3 and 4**"),style={'font-family':'calibri','font-weight':'strong','fontSize': 16}),html.Div(["One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph."])]),style={'font-family':'calibri','fontSize':18},className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_3", figure= figure3,className='four columns'))
            ]),
          html.Div([
              (dcc.Graph(id="figure_4", figure= figure4,className='four columns'))
            ]),
         ], className= "row"),

# Last Graph 
        html.Div([
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 5**"),style={'font-family':'calibri','font-weight':'strong','fontSize': 16}),html.Div(["Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole January, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap"])]), style={'font-family':'calibri','fontSize':18},className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_5", figure= figure5,className='six columns'))
            ]),
          html.Div("", className='two columns'),
         ], className= "row"),

    ])

if __name__ == '__main__':
  app.run_server(debug=True)