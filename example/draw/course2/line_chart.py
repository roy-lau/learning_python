import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
  1. 折线图示例
'''

# # reading the database
# data = pd.read_csv("tips.csv")

# # Scatter plot with day against tip
# plt.plot(data['tip'])
# plt.plot(data['size'])

# # Adding Title to the Plot
# plt.title("Scatter Plot")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# plt.show()


'''
  2. 折线图示例 - 使用 lineplot() 函数绘制
'''

# reading the database
data = pd.read_csv("tips.csv")

# using only data attribute
sns.lineplot(data=data.drop(['total_bill'], axis=1))
plt.show()
