import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
  1. 柱状图示例
'''


# # reading the database
# data = pd.read_csv("tips.csv")

# # Bar chart with day against tip
# plt.bar(data['day'], data['tip'])

# plt.title("Bar Chart")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# # Adding the legends
# plt.show()


'''
  2. 柱状图示例 - 使用 barplot() 函数绘制
'''

# reading the database
data = pd.read_csv("tips.csv")

sns.barplot(x='day',y='tip', data=data, 
            hue='sex')

plt.show()
