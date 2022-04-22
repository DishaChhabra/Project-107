import pandas as pd
import plotly.express as px
data = pd.read_csv('https://raw.githubusercontent.com/whitehatjr/Data-Analysis-by-visualisation/master/data.csv')

groups = data.groupby(['student_id', 'level'], as_index=False)['attempt'].mean()
print(groups)

graph = px.scatter(groups, x='student_id', y='level', size='attempt', color='attempt')
graph.show()