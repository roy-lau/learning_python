# importing the modules
from bokeh.plotting import figure, output_file, show
import pandas as pd


'''
  1. 柱状图示例
'''

# # instantiating the figure object
# graph = figure(title = "Bokeh Bar Chart")

# # reading the database
# data = pd.read_csv("tips.csv")

# # plotting the graph
# graph.vbar(data['total_bill'], top=data['tip'])

# # displaying the model
# show(graph)


'''
  2. 柱状图示例 - 增加交互功能，点击图例隐藏对应柱状图
'''


# instantiating the figure object
graph = figure(title = "Bokeh Bar Chart")

# reading the database
data = pd.read_csv("tips.csv")

# plotting the graph
graph.vbar(data['total_bill'], top=data['tip'], 
           legend_label = "Bill VS Tips", color='green')

graph.vbar(data['tip'], top=data['size'], 
           legend_label = "Tips VS Size", color='red')

graph.legend.click_policy = "hide"

# displaying the model
show(graph)