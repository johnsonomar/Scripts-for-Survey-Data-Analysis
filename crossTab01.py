import pandas as pd
import seaborn as sb 
import matplotlib.pyplot as plt


file_name = "Remote Work Survey.csv"
col1 = "I am more productive when I work outside of the office" 
col2 = "I am able to achieve a better work/life balance by working remotely"

df = pd.read_csv(file_name)

selected_col = df.iloc[:, [5, 9]]

cross_tab = pd.crosstab(selected_col[col1], selected_col[col2])

sb.heatmap(cross_tab, annot = True, cmap = 'flare', fmt='d', cbar = True)

plt.xlabel(col2)
plt.ylabel(col1)
plt.title("Heatmap 01")

plt.show()
