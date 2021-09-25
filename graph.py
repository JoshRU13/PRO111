import plotly.figure_factory as ff
import pandas as pd
df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
fig=ff.create_distplot([data],["score"],show_hist=False)
fig.show()