#plot1
from plotly.offline import iplot,plot
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
trace1=go.Bar(x=[15,50,15,20],y=["x8","x7","x6","x5"],orientation = 'h',marker=dict(color="blue"),name="<b>Negative</b>")
trace2=go.Bar(x=[-15,-45,-5,-35],y=["x4","x3","x2","x1"],orientation = 'h',marker=dict(color="purple"),name="Positive")
layout  = dict(title="<b>Correlation with employees probability of churn</b>",yaxis=dict(title="Variable"),
               font=dict(size=10), showlegend=True)
figure1=dict(data=[trace1,trace2],layout=layout)

#plot2
import quandl
quandl.ApiConfig.api_key = "gP3abojkLwhhgHRD8xG5"
data = quandl.get("FRED/GDP")
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import pandas as pd
x_values = pd.to_datetime(data.index.values)
y_values = data["Value"]
trace = go.Scatter(x=x_values,y=y_values,mode="lines",fill='tozeroy') 
layout = go.Layout(title='<b>US GDP over time</b>')
data = [trace]
figure2 = dict(data=data,layout=layout)



#plot3
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import quandl
quandl.ApiConfig.api_key = "gP3abojkLwhhgHRD8xG5"
info1 = quandl.get("WIKI/GOOGL")
info2=quandl.get("BCHARTS/ABUCOINSUSD")
trace_1 = go.Box(x=info1.Open.pct_change(),name="<b>Google</b>")
trace_2 = go.Box(x=info2.Open.pct_change(),name="<b>Bitcoin</b>")
layout=dict(title="Distribution of Price Change")
data = [trace_2,trace_1]
figure3 = dict(data=data,layout=layout)


#plot4
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import quandl
quandl.ApiConfig.api_key = "gP3abojkLwhhgHRD8xG5"
info1 = quandl.get("WIKI/GOOGL")
info2=quandl.get("BCHARTS/ABUCOINSUSD")

google=info1.Open.pct_change()
google=google.to_frame()
google.reset_index(level=0, inplace=True)
google_4=google.loc[1:4]
google_1pc=round(google_4["Open"][1],3) 
google_2pc=round(google_4["Open"][2],3) 
google_3pc=round(google_4["Open"][3],3) 
google_4pc=round(google_4["Open"][4],3) 

bitcoin=info2.Open.pct_change()
bitcoin=bitcoin.to_frame()

bitcoin.reset_index(level=0, inplace=True)
bitcoin_4=bitcoin.loc[1:4]
bitcoin_1pc=round(bitcoin_4["Open"][1],3) 
bitcoin_2pc=round(bitcoin_4["Open"][2],3) 
bitcoin_3pc=round(bitcoin_4["Open"][3],3) 
bitcoin_4pc=round(bitcoin_4["Open"][4],3) 

from plotly.offline import plot, iplot
import plotly.graph_objs as go

header = dict(values=['Google','Bitcoin'],
              align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
             )
cells = dict(values=[[google_1pc,google_2pc,google_3pc,google_4pc],
                     [bitcoin_1pc,bitcoin_2pc,bitcoin_3pc,bitcoin_4pc]],
             align = ['left','center'],
             fill = dict(color=["yellow","white"])
            )
trace = go.Table(header=header, cells=cells)

data = [trace]
layout = dict(width=500, height=300)
figure4 = dict(data=data, layout=layout)


#plot5
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31',Resource='Idea Validation'),
      dict(Task="Task 2", Start='2018-03-01', Finish='2018-04-15', Resource='Prototyping'),
      dict(Task="Task 3", Start='2018-04-15', Finish='2018-09-30', Resource='Team Formation')]

colors = ['#30a0310', (0.95,0.5,0.1), 'rgb(10,125,205)']
figure5 = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True,title="Startup Roadmap")
