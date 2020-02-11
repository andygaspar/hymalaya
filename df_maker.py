import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def make_df():

    df_hym=pd.read_csv("data/himalayan_csv/exped.csv",sep=",")
    peaks=pd.read_csv("data/himalayan_csv/peaks.csv",sep=",")


    df=df_hym.copy(deep=True)
    df["height"]=np.zeros(df_hym.shape[0])
    df["peak"]=np.array([None for i in range(df.shape[0])])
    df["region"]=np.array([None for i in range(df.shape[0])])


    for id in np.unique(df["peak id"]):
        df['height'] = np.where((df["peak id"] == id),peaks[peaks["peak id"]==id]["height"].values[0],df["height"])
        df['region'] = np.where((df["peak id"] == id),peaks[peaks["peak id"]==id]["region"].values[0],df["region"])
        df['peak'] = np.where((df["peak id"] == id),peaks[peaks["peak id"]==id]["name"].values[0],df["peak"])


    df["season"]=df["season"].astype(str,copy=False)
    season={"0":"unknown","1":"spring", '3':"autumn",'2':"summer", '4':"winter"}
    for key in season.keys():
        df["season"]=np.where((df["season"] == key),season[key],df["season"])


    region= {0:"Unclassified",1: "Kangchenjunga-Janak" , 5: "Annapurna-Damodar-Peri", 2: "Khumbu-Rolwaling-Makalu", 6: "Dhaulagiri-Mukut", 3: "Langtang-Jugal",7:"Kanjiroba-Far West", 4:"Manaslu-Ganesh"}
    for key in region.keys():
        df["region"]=np.where((df["region"] == key),region[key],df["region"])


    df["host country"]=df["host country"].astype(str,copy=False)
    host_country={"0":"unknown","1":"Nepal", "2":"China", "3":"India"}
    for key in host_country.keys():
        df["host country"]=np.where((df["host country"] == key),host_country[key],df["host country"])



    boolean={"VERO":True,"FALSO":False}
    for key in boolean.keys():
        df["success"]=np.where((df["success"] == key),boolean[key],df["success"])
        df["sherpas free"]=np.where((df["sherpas free"] == key),boolean[key],df["sherpas free"])
        df["o2"]=np.where((df["o2"] == key),boolean[key],df["o2"])
        df["o2 missing data"]=np.where((df["o2 missing data"] == key),boolean[key],df["o2 missing data"])

    """
        questo è il comando per riordinare le colonne
        df=df[ [ nome_prima_colonna, nome_seconda_colonna,.... ] ]

        ricordati che con df.columns stampi i nomi delle colonne (nel caso tu abbia bisogno di vederli)

        se vuoi effettivamente cambiare l'ordine se puoi fallo in questa funzione, prima del return, poi pusha così
        lavoriamo sullo stesso dataframe


    """
    pippo=df["agency"].to_numpy().astype(str)
    pippo=np.where(pippo=='nan','not_com',pippo)
    pippo=np.where(pippo=='None','not_com',pippo)
    pippo=np.where(pippo=='None (went direct to Tibet?)','not_com',pippo)
    pippo=np.where(pippo=='None (permit arranged directly with TMA)','not_com',pippo)
    np.unique(pippo)

    return df




def search(mount_prefix,df):
    words=[]
    for peak in np.unique(df["peak"]):
        PEAK=peak.lower()
        common=0
        for i in range(len(mount_prefix)-1):
            for j in range(len(PEAK)-1):
                if mount_prefix[i]==PEAK[j] and mount_prefix[i+1]==PEAK[j+1] :
                    common+=1;
        if common>=len(mount_prefix)*3/4-1:
            words.append(peak)

    return words
