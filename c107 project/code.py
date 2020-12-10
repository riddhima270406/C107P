import pandas as pd
import csv
import plotly.graph_objects as pg

rc = pd.read_csv("data.csv")

print(rc.groupby("Roll No")["Marks In Percentage"].mean())

fig = pg.Figure(pg.Scatter(
    x = rc.groupby("Roll No")["Marks In Percentage"].mean(),
    y = ['Marks In Percentage']
    ))

fig.show()
