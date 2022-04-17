#Steps of data visualization

#Step 1
#import libraries

import seaborn as sns
import matplotlib.pyplot as plt

#step 2
#set a theme
sns.set_theme(style="ticks", color_codes=True)


#step 3. We can also import our own data
# import dataset
kashti= sns.load_dataset("titanic")
print(kash)


# #step 4
# # plot basic graph
# p= sns.countplot(x= "", y="" , data= kashti)
# plt.show()
