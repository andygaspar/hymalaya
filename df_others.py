import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gash=pd.read_csv("data/altri_8000_csv/gasherbrumI.csv",sep=",")
gash_death=pd.read_csv("data/altri_8000_csv/GasherbrumI_fatalities.csv")
gash_death
gash[gash.year==1977]


def date_to_int(df):
    for item in ["date","month","year"]:
        df[item]=df[item].to_numpy().astype(int)
    return df

def to_new_df(name,df_exp):
    columns=["peak","year","members"]
    new_df=pd.DataFrame(columns=columns)
    df_exp=date_to_int(df_exp)
    for year in np.unique(df_exp["year"]):
        df=df_exp[df_exp["year"]==year]
        for month in np.unique(df["month"]):
            dff=df[df["month"]==month]
            for day in np.unique(dff["date"]):
                dfff=dff[dff["date"]==day]
                new_df=new_df.append(pd.DataFrame(\
                dict(zip(columns,[name,year,dfff.shape[0]])),\
                index=[0]),ignore_index=True)
    return new_df


new_df= to_new_df("gasherbrumI",gash)




df_nanga=pd.read_csv("data/altri_8000_csv/nangaparbat-summits.csv")
df_nanga=to_new_df("nangaparbat",df_nanga)



def to_print(df):
    summits=[]
    for year in np.unique(df["year"]):
        summits.append(sum(df[df["year"]==year]["members"]))
    return np.unique(df["year"]),np.array(summits)


nan_plot=to_print(df_nanga)
plt.plot(nan_plot[0],nan_plot[1])
