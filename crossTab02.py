import pandas as pd
import seaborn as sb 
import matplotlib.pyplot as plt


file_name = "Remote Work Survey.csv"
col1 = "I am able to achieve a better work/life balance by working remotely" 
col2 = "Working remotely has hindered opportunities for growth (ie promotions role enlargement) within my organization"

df = pd.read_csv(file_name)

selected_col = df.iloc[:, [9, 14]]

cross_tab = pd.crosstab(selected_col[col1], selected_col[col2])

sb.heatmap(cross_tab, annot = True, cmap = 'flare', fmt='d', cbar = True)

plt.xlabel(col2)
plt.ylabel(col1)
plt.title("Heatmap 02")

plt.show()
