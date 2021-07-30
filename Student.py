import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
studentDf = df.loc[df["student_id"] == "TRL_zet"]
fig = go.Figure(go.Bar(
    x = studentDf.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
))
fig.show()
print(studentDf)
print(studentDf.groupby("level")["attempt"].mean())