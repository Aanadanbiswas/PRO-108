from numpy import False_
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv(r'Brands.csv')

Graph = ff.create_distplot([df['Avg Rating'].tolist()], ['Mobile Rating'], show_hist=False)

Graph.show()