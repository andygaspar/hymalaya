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


    df["tot people"]=df["members"]+df["sherpas"]
    df["tot death"]= df["members died"]+df["sherpas died"]



    boolean={"VERO":True,"FALSO":False}
    for key in boolean.keys():
        df["success"]=np.where((df["success"] == key),boolean[key],df["success"])
        df["sherpas free"]=np.where((df["sherpas free"] == key),boolean[key],df["sherpas free"])
        df["o2"]=np.where((df["o2"] == key),boolean[key],df["o2"])
        df["o2 missing data"]=np.where((df["o2 missing data"] == key),boolean[key],df["o2 missing data"])

    df["sherpas free"]=(df["sherpas"]==0)

    commercial=df["agency"].to_numpy().astype(str)
    commercial=np.where(commercial=='nan','not_com',commercial)
    commercial=np.where(commercial=='None','not_com',commercial)
    commercial=np.where(commercial=='None (went direct to Tibet?)','not_com',commercial)
    commercial=np.where(commercial=='None (permit arranged directly with TMA)','not_com',commercial)
    df["commercial"]=(commercial!='not_com')


    # compute success on other routes
    success=pd.read_csv("data/himalayan_csv/success.csv",sep=",")
    boolean={"VERO":True,"FALSO":False}
    for key in boolean.keys():
        success["sr2"]=np.where((success["sr2"] == key),boolean[key],success["sr2"])
        success["sr3"]=np.where((success["sr3"] == key),boolean[key],success["sr3"])
        success["sr4"]=np.where((success["sr4"] == key),boolean[key],success["sr4"])


    new_success=[]
    for i in range(df.shape[0]):
        if success.iloc[i]["sr2"]==True or success.iloc[i]["sr3"]==True\
         or success.iloc[i]["sr4"]==True or df.loc[i]["success"]==True:
            new_success.append(True)
        else:
            new_success.append(False)

    df["success"]=new_success

    #make 8000


    ottomila=df[df["height"]>=8000].copy(deep=True)
    ottomila["peak"].unique()

    ev=['Everest']
    lo=['Lhotse','Lhotse Shar','Lhotse Middle']
    kan=[ 'Kangchenjunga','Kangchenjunga Central','Kangchenjunga South', 'Yalung Kang']
    ann=['Annapurna I East','Annapurna I Middle','Annapurna I']
    mak=['Makalu']
    cho=['Cho Oyu']
    man=['Manaslu']
    dha=['Dhaulagiri I']

    main_peak=[]
    for peak in ottomila["peak"]:
        if peak in ev:
            main_peak.append("Everest")
        if peak in lo:
            main_peak.append("Lhotse")
        if peak in kan:
            main_peak.append("Kangchenjunga")
        if peak in ann:
            main_peak.append("Annapurna")
        if peak in mak:
            main_peak.append("Makalu")
        if peak in cho:
            main_peak.append("Cho Oyu")
        if peak in man:
            main_peak.append("Manaslu")
        if peak in dha:
            main_peak.append("Dhaulagiri")

    ottomila["main peak"]=np.array(main_peak).copy()



    #raggruppati
    ann=['Annapurna I','Annapurna I East','Annapurna I Middle','Annapurna II',\
    'Annapurna III','Annapurna IV','Annapurna South','Gangapurna','Gangapurna West']
    kan=[ 'Kangchenjunga','Kangchenjunga Central','Kangchenjunga South', \
    'Yalung Kang','Kangbachen']
    dha =['Dhaulagiri I','Dhaulagiri II','Dhaulagiri III','Dhaulagiri IV',\
    'Dhaulagiri V','Dhaulagiri VI','Putha Hiunchuli','Churen Himal Central',\
     'Churen Himal East', 'Churen Himal West','Gurja Himal']
    lo=['Lhotse','Lhotse Shar','Lhotse Middle']
    mak=['Makalu','Makalu II']
    cho=['Cho Oyu']
    man=['Manaslu', 'Manaslu North']
    ev= ["Everest"]


    df_rag=df.copy(deep=True)

    new_peak=[]
    is_ottomila=[]
    for peak in df_rag["peak"]:
        if peak in ev:
            new_peak.append( "Everest")
            is_ottomila.append(True)
        if peak in lo:
            new_peak.append( "Lhotse")
            is_ottomila.append(True)
        if peak in kan:
            new_peak.append( "Kangchenjunga")
            is_ottomila.append(True)
        if peak in ann:
            new_peak.append( "Annapurna")
            is_ottomila.append(True)
        if peak in mak:
            new_peak.append( "Makalu")
            is_ottomila.append(True)
        if peak in cho:
            new_peak.append( "Cho Oyu")
            is_ottomila.append(True)
        if peak in man:
            new_peak.append( "Manaslu")
            is_ottomila.append(True)
        if peak in dha:
            new_peak.append( "Dhaulagiri")
            is_ottomila.append(True)
        if peak not in (ann+kan+dha+lo+mak+cho+man+ev):
            new_peak.append(peak)
            is_ottomila.append(False)


    df_rag["peak"]=new_peak
    df_rag["ottomila"]=is_ottomila

    #boolean sponsored
    sponsor=[]

    for sp in df["sponsor"]:
        if type(sp)==float:
            if np.isnan(sp):
                sponsor.append(False)
            else:
                print(sp)
        else:
            sponsor.append(True)

    df["sponsored"]=np.array(sponsor)
    ever=df[df["peak"]=="Everest"].copy(deep=True)


    return df, ottomila, df_rag, ever





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



def com_not_com(df):
    commercial=[]
    not_commercial=[]
    for year in np.unique(df["year"]):
        pippo=df[(df["year"]==year)]
        pippo=pippo[pippo["commercial"]==True]
        commercial.append(pippo.shape[0])
        pippo=df[(df["year"]==year)]
        pippo=pippo[pippo["commercial"]==False]
        not_commercial.append(pippo.shape[0])
    return np.array(commercial),np.array(not_commercial)
