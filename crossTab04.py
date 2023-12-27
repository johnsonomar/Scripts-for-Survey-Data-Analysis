import pandas as pd
import seaborn as sb 
import matplotlib.pyplot as plt

file_name = "Remote Work Survey.csv"
col1 = "If given the choice which work environment do you prefer?" 
col2 = "Averaged Positive Responses:"

df = pd.read_csv(file_name)

selected_col = df.iloc[:, [2, 15]]

cross_tab = pd.crosstab(selected_col[col1], selected_col[col2])

order = ["Fully On-Site", "Hybrid Model", "Fully Remote"]

stacked_data = cross_tab.stack().reset_index().rename(columns={0: 'Count'})

sb.barplot(x=col1, y='Count', hue=col2, data=stacked_data, palette='viridis', order = order)

plt.title(f"Bivariate Bar Graph of\nAveraged Positive Responses by\nChoice of Workplace")

plt.show()

