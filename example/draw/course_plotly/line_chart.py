
'''
  1. 折线图示例 - 点击图例切换
'''

# import plotly.express as px
# import pandas as pd

# # reading the database
# data = pd.read_csv("tips.csv")

# # plotting the scatter chart
# fig = px.line(data, y='tip', color='sex')

# # showing the plot
# fig.show()


'''
  2. 折线图示例 - 创建 Sliders 和 Selector
'''

import plotly.graph_objects as px
import pandas as pd

# reading the database
data = pd.read_csv("tips.csv")

plot = px.Figure(data=[px.Scatter(
    y=data['tip'],
    mode='lines',)
])

plot.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)

plot.show()