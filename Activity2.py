import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('Data.csv')
fig = ff.create_distplot([df['Weight(Pounds)'].tolist()],['Weight(Pounds)'],show_hist=False)
fig.show()