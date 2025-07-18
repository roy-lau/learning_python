import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 准备数据
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Sales': [100, 120, 150, 130, 160]}
df = pd.DataFrame(data)

# 绘制折线图
sns.lineplot(x='Year', y='Sales', data=df)

# 添加标题和标签
plt.title('Sales Trend Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')

# 显示图表
plt.show()