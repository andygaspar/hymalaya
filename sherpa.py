import numpy as np
import pandas as pd
import df_maker as dm
import matplotlib.pyplot as plt
import matplotlib as mpl


df, ottomila, df_rag=dm.make_df()

mpl.rcParams["figure.figsize"] = (10,7)


#assoluti *************************************



tot_people= sum(df["tot people"])
tot_died= sum(df["tot death"])

#frequentazione

freq=dict()
for peak in df["peak"].unique():
    freq[peak]=sum(df[df["peak"]==peak]["tot people"])

ordered={k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}
ordered


# morti

df.sort_values("tot death",ascending=False).iloc[:20]

freq=dict()
for peak in df["peak"].unique():
    freq[peak]=sum(df[df["peak"]==peak]["tot death"])

ordered={k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}
ordered

# morti relativi


freq=dict()
for peak in df["peak"].unique():
    freq[peak]=sum(df[df["peak"]==peak]["tot death"])/sum(df[df["peak"]==peak]["tot people"])

ordered={k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}
ordered







#8000 **********************************************

ottomila_death=sum(ottomila["tot death"])
ever=ottomila[ottomila["peak"]=="Everest"]
print(tot_died, ottomila_death, sum(ever["tot death"]))


# assoluti
peak_death=dict()
for peak in ottomila["peak"].unique():
    peak_death[peak]= sum(ottomila[ottomila["peak"]==peak]["tot death"])

ordered={k: v for k, v in sorted(peak_death.items(), key=lambda item: item[1],reverse=True)}
ordered


# relativi
peak_death=dict()
for peak in ottomila["peak"].unique():
    peak_death[peak]= sum(ottomila[ottomila["peak"]==peak]["tot death"])\
    /sum(ottomila[ottomila["peak"]==peak]["tot people"])

ordered={k: v for k, v in sorted(peak_death.items(), key=lambda item: item[1],reverse=True)}
ordered




#raggruppati ***********************************
ottomila.shape
ott=df_rag[df_rag["ottomila"]==True]
ott.shape[0]
ott_death=sum(ott["tot death"])
ever=ott[ott["peak"]=="Everest"]
print(tot_died, ott_death, sum(ever["tot death"]))


# assoluti
peak_death=dict()
for peak in ott["peak"].unique():
    peak_death[peak]= sum(ott[ott["peak"]==peak]["tot death"])

ordered={k: v for k, v in sorted(peak_death.items(), key=lambda item: item[1],reverse=True)}
ordered


# relativi
peak_death=dict()
for peak in ott["peak"].unique():
    peak_death[peak]= sum(ott[ott["peak"]==peak]["tot death"])\
    /sum(ott[ott["peak"]==peak]["tot people"])

ordered={k: v for k, v in sorted(peak_death.items(), key=lambda item: item[1],reverse=True)}
ordered



# success death ***********
succ=df[df["success"]==True]

# assoluti
people_success=dict()
for peak in succ["peak"].unique():
    tot_success=sum(succ[succ["peak"]==peak]["member summit"]+succ[succ["peak"]==peak]["sherpas summit"])
    people_success[peak]= tot_success

ordered={k: v for k, v in sorted(people_success.items(), key=lambda item: item[1],reverse=True)}
ordered


# relativi
peak_death=dict()
for peak in succ["peak"].unique():
    peak_death[peak]= sum(succ[succ["peak"]==peak]["tot death"])\
    /sum(succ[succ["peak"]==peak]["member summit"]+succ[succ["peak"]==peak]["sherpas summit"])

ordered={k: v for k, v in sorted(peak_death.items(), key=lambda item: item[1],reverse=True)}
ordered





#raggruppati  success***********************************
ottomila.shape
ott=df_rag[df_rag["ottomila"]==True]
ott=ott[ott["success"]==True]
ott.shape[0]
ott_death=sum(ott["tot death"])
ever=ott[ott["peak"]=="Everest"]
print(tot_died, ott_death, sum(ever["tot death"]))


people_success=dict()
for peak in ott["peak"].unique():
    tot_ottess=sum(ott[ott["peak"]==peak]["member summit"]+ott[ott["peak"]==peak]["sherpas summit"])
    people_success[peak]= tot_ottess

ordered={k: v for k, v in sorted(people_success.items(), key=lambda item: item[1],reverse=True)}
ordered


# relativi
peak_death=dict()
for peak in ott["peak"].unique():
    peak_death[peak]= sum(ott[ott["peak"]==peak]["tot death"])\
    /sum(ott[ott["peak"]==peak]["member summit"]+ott[ott["peak"]==peak]["sherpas summit"])

ordered={k: v for k, v in sorted(peak_death.items(), key=lambda item: item[1],reverse=True)}
ordered









#sherpas *****************************


climbers = sum(df["members"])
sherpas = sum(df["sherpas"])


print(tot_people, climbers, sherpas)


climbers_died= sum(df["members died"])
sherpas_died = sum(df["sherpas died"])

print(tot_died, climbers_died, sherpas_died)

tot=[]
cl=[]
sh=[]
df_ever=df[df["peak"]=="Everest"]
years=np.sort(df_ever["year"].unique())
years
for year in years:
    df_year=df_ever[df_ever["year"]==year]
    tot.append( sum(df_year["members died"]+df_year["sherpas died"]))
    cl.append(sum(df_year["members died"]))
    sh.append(sum(df_year["sherpas died"]))

plt.plot(years,tot,label="total")
plt.plot(years,cl,label="climbers")
plt.plot(years,sh,label="sherpas")
plt.legend()

print(max(tot),years[np.argmax(tot)])

df_victims=pd.DataFrame({"year":years, "tot":tot, "members":cl, "sherpas":sh})

df_victims.sort_values("sherpas",ascending=False)



#sharpas commercial vs non
df_com=df[df["commercial"]==True]

sherp_com= sum(df_com["sherpas"])
sherp_not_com= sherpas-sherp_com

print(sherp_com,sherp_not_com)


sherpas_com_died=sum(df_com["sherpas died"])
sherpas_died_not_com=sherpas_died-sherpas_com_died

print(sherpas_died, sherpas_com_died, sherpas_died_not_com)



# mortality rate over the years
death_rate=[]
df=df[df["tot people"]>0]

for year in sorted(df["year"].unique()):
    death_rate.append(sum(df[df["year"]==year]["tot death"])/sum(df[df["year"]==year]["tot people"]))


plt.plot(sorted(df["year"].unique()),death_rate)
plt.xticks(sorted(df["year"].unique()))
