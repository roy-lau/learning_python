import plotly.express as px
import pandas as pd

# 准备数据
data = {'Fruit': ['Apple', 'Banana', 'Orange', 'Grape'],
        'Quantity': [20, 30, 15, 25]}
df = pd.DataFrame(data)

# 绘制柱状图
fig = px.bar(df, x='Fruit', y='Quantity')

# 显示图表
fig.show()