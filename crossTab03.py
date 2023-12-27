import pandas as pd
import seaborn as sb 
import matplotlib.pyplot as plt


file_name = "Remote Work Survey.csv"
col1 = "How likely are you to select a job based on the work environment?" 
col2 = "I am more productive when I work outside of the office"

df = pd.read_csv(file_name)

selected_col = df.iloc[:, [4, 5]]

cross_tab = pd.crosstab(selected_col[col1], selected_col[col2])

sb.heatmap(cross_tab, annot = True, cmap = 'flare', fmt='d', cbar = True)

plt.xlabel(col2)
plt.ylabel(col1)
plt.title("Heatmap 03")

plt.show()
