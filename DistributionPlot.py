import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('/Users/maciejgajewski/Pokemon/data/pokemon_types_source.csv', sep=',', index_col=0)

sns.set(style="darkgrid")
ax = sns.countplot(x="Type_1", data   =data)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()