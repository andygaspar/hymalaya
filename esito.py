import numpy as np
import pandas as pd
import df_maker as dm
import matplotlib.pyplot as plt
import matplotlib as mpl



df, ottomila, df_rag=dm.make_df()
df.rename(columns={"ending cause.1":"ending"},inplace=True)
df["ending"]=df["ending"].astype(int)
mpl.rcParams["figure.figsize"] = (10,7)
names=["unknown","suc 1","suc 2","suc 3","bad wather","bad conditions","accidents",\
"illness","lack supplies","time out","too hard","no basecamp"," no attempt to climb"\
,"attempt rumored","other"]
cause=dict(zip(range(14),names))





causes=[]
for end in df["ending"].unique():
    causes.append(df[df["ending"]==end].shape[0])

plt.bar(df["ending"].unique(),causes)

df[df["ending"]==10].shape[0]/df.shape[0]
df_ever[df_ever["ending"]==10].shape[0]/df_ever.shape[0]



df_ever=df[df["peak"]=="Everest"]

causes=[]
for end in df_ever["ending"].unique():
    causes.append(df_ever[df_ever["ending"]==end].shape[0])

plt.bar(df_ever["ending"].unique(),causes)


df_ever.shape[0]
ever_success=df_ever[df_ever["success"]==True]
ever_success["tot people"]-(ever_success["member summit"]+ever_success["sherpas summit"])

causes=[]
for end in ever_success["ending"].unique():
    causes.append(ever_success[ever_success["ending"]==end].shape[0])

plt.bar(ever_success["ending"].unique(),causes)


df_ever[(df_ever["success"]==True) & (df_ever["ending"]=="10")]
