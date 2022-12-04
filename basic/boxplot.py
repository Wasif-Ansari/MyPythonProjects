import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data.head())



import plotly.express as px
fig = px.box(data, y="TV")
fig.show()