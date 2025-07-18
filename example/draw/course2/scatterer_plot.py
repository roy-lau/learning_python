import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



'''
  1. 散点图示例
'''


# # reading the database
# data = pd.read_csv("tips.csv")

# # Scatter plot with day against tip
# plt.scatter(data['day'], data['tip'])

# # Adding Title to the Plot
# plt.title("Scatter Plot")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# plt.show()


'''
  2. 散点图示例 - 自定义颜色和大小
'''


# # reading the database
# data = pd.read_csv("tips.csv")

# # Scatter plot with day against tip
# plt.scatter(data['day'], data['tip'], c=data['size'], 
#             s=data['total_bill'])

# # Adding Title to the Plot
# plt.title("Scatter Plot")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# plt.colorbar()

# plt.show()


'''
  3. 散点图示例 - 使用 scatterplot() 函数绘制
'''

# reading the database
# data = pd.read_csv("tips.csv")

# sns.scatterplot(x='day', y='tip', data=data,)
# plt.show()

'''
  4. 散点图示例 - 使用 scatterplot() 函数区分性别绘制
'''

# reading the database
data = pd.read_csv("tips.csv")

sns.scatterplot(x='day', y='tip', data=data,
               hue='sex')
plt.show()