import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# initialize data of lists.
data_ = {'Noticia_1':[1, 0.06, 0.24],
        'Noticia_2':[0.06, 1, 0.7],
        'Noticia_3':[0.24, 0.7, 1]}
 
# Creates pandas DataFrame.
df = pd.DataFrame(data_, index =['Noticia_1',
                                'Noticia_2',
                                'Noticia_3'])

sns.heatmap(data=df, cmap="Greens", annot=True)
plt.show()
