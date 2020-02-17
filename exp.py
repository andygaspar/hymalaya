import numpy as np
import pandas as pd
import df_maker as dm
import matplotlib.pyplot as plt
import matplotlib as mpl


df, ottomila, df_rag, ever =dm.make_df()

mpl.rcParams["figure.figsize"] = (12,7)

df=df[df["year"]<2019]

N=df.shape[0]
N_ottomila=ottomila.shape[0]
N_ever=ever.shape[0]
N_nepal=ever[(ever["standard route"]==True) & (ever["host country"]=="Nepal")].shape[0]

print(N,N_ottomila,N_ever,N_nepal)
print(1,N_ottomila/N,N_ever/N,N_nepal/N)


N=sum(df["tot people"])
N_ottomila=sum(ottomila["tot people"])
N_ever=sum(ever["tot people"])
N_nepal=sum(ever[(ever["standard route"]==True) & (ever["host country"]=="Nepal")]["tot people"])
print(N,N_ottomila,N_ever,N_nepal)
print(1,N_ottomila/N,N_ever/N,N_nepal/N)


years=sorted(df["year"].unique())
exp=[]
N_ottomila=[]
N_ever=[]
N_nepal=[]
nep=ever[(ever["standard route"]==True) & (ever["host country"]=="Nepal")]
for year in years:
    ex=df[df["year"]==year]
    ott=ottomila[ottomila["year"]==year]
    ev=ever[ever["year"]==year]
    ne=nep[nep["year"]==year]
    exp.append(ex.shape[0])
    N_ottomila.append(ott.shape[0])
    N_ever.append(ev.shape[0])
    N_nepal.append(ne.shape[0])

plt.plot(years,exp,label="tot expeditions")
plt.plot(years,N_ottomila,label="ottomila")
plt.plot(years,N_ever,label="everest")
plt.plot(years,N_nepal,label="normal route")
plt.legend()


exp=[]
N_ottomila=[]
N_ever=[]
N_nepal=[]
for year in years:
    ex=df[df["year"]==year]
    ott=ottomila[ottomila["year"]==year]
    ev=ever[ever["year"]==year]
    ne=nep[nep["year"]==year]
    exp.append(sum(ex["tot people"]))
    N_ottomila.append(sum(ott["tot people"]))
    N_ever.append(sum(ev["tot people"]))
    N_nepal.append(sum(ne["tot people"]))

plt.plot(years,exp,label="tot people")
plt.plot(years,N_ottomila,label="ottomila")
plt.plot(years,N_ever,label="everest")
plt.plot(years,N_nepal,label="normal route")
plt.legend()




N=sum(df[df["year"]>=2010]["tot people"])
N_ottomila=sum(ottomila[ottomila["year"]>=2010]["tot people"])
N_ever=sum(ever[ever["year"]>=2010]["tot people"])
N_nepal=sum(ever[(ever["standard route"]==True) & (ever["host country"]=="Nepal") &( ever["year"]>=2010)]["tot people"])
print(N,N_ottomila,N_ever,N_nepal)
print(1,N_ottomila/N,N_ever/N,N_nepal/N)






#commercial

not_commercial=[]
everest_commercial=[]
total=[]

for year in years:
    not_commercial.append(df[(df["year"]==year) & (df["commercial"]==False)].shape[0])
    everest_commercial.append(ever[(ever["year"]==year) & (ever["commercial"]==True)].shape[0] +\
    df[(df["year"]==year) & (df["commercial"]==False)].shape[0])
    total.append(df[df["year"]==year].shape[0])

plt.plot(years,total,label="commercial")
plt.plot(years,everest_commercial,label="everest commercial")
plt.plot(years,not_commercial,label="not commercial")
plt.legend()

print("first commercial")
for i in range(len(years)):
    print(years[i],(np.array(total)-np.array(not_commercial))[i])


not_commercial=[]
total=[]

for year in years:
    not_commercial.append(ever[(ever["year"]==year) & (ever["commercial"]==False)].shape[0])
    total.append(ever[ever["year"]==year].shape[0])

plt.plot(years,total)
plt.plot(years,not_commercial,label="not commercial")
plt.legend()



#people on everest
not_commercial=[]
total=[]

for year in years:
    not_commercial.append(sum(ever[(ever["year"]==year) & (ever["commercial"]==False)]["tot people"]))
    total.append(sum(ever[ever["year"]==year]["tot people"]))

plt.plot(years,total)
plt.plot(years,not_commercial,label="not commercial")
plt.legend()
