import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
std=statistics.stdev(data)
print("mean",mean)
print("stdev",std)

def randomset(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
meanlist=[]
for i in range(0,1000):
    setupmean=randomset(100)
    meanlist.append(setupmean)
mean=statistics.mean(meanlist)
print("sampling mean",mean)
std=statistics.stdev(meanlist)
print("sampling deviation",std)

first_sd_start,first_sd_end=mean-std,mean+std
second_sd_start,second_sd_end=mean-(2*std),mean+(2*std)
third_sd_start,third_sd_end=mean-(3*std),mean+(3*std)

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
mean1=statistics.mean(data)
print("mean1",mean1)
fig=ff.ff.create_distplot([meanlist],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="mean of sample"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="sd1 end"))
fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
mean2=statistics.mean(data)
print("mean2",mean2)
fig=ff.ff.create_distplot([meanlist],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.17],mode="lines",name="mean of sample"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="sd1 end"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="sd2 end"))
fig.show()

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
mean3=statistics.mean(data)
print("mean3",mean3)
fig=ff.ff.create_distplot([meanlist],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean3,mean3],y=[0,0.17],mode="lines",name="mean of sample"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="sd3 end"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="sd2 end"))
fig.show()

zscore1=(mean1-mean)/std
print("zscore 1",zscore1)
zscore2=(mean2-mean)/std
print("zscore 2",zscore2)
zscore3=(mean3-mean)/std
print("zscore 3",zscore3)