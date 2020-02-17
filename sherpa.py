import numpy as np
import pandas as pd
import df_maker as dm
import matplotlib.pyplot as plt
import matplotlib as mpl


df, ottomila, df_rag, ever =dm.make_df()

mpl.rcParams["figure.figsize"] = (10,7)


#assoluti *************************************

ever.sort_values("year",ascending=False,inplace=True)


tot_people= sum(df["tot people"])
tot_died= sum(df["tot death"])

def print_stats():
    print("Global Himalaya\n")
    print("Tot people ",tot_people)
    print("Tot died ",tot_died)
    print("Death rate %.2f" % (tot_died/tot_people))
    print("\nSherpas rate %.2f" % (sum(df["sherpas"])/tot_people))
    print("Sherpas death rate %.2f" % (sum(df["sherpas died"])/tot_died))

    print("\n\nEverest\n")
    print("Everest global death rate %.2f" % (sum(ever["tot death"])/sum(ever["tot people"])))
    print("sherpas rate %.2f" % (sum(ever["sherpas"])/sum(ever["tot people"])))
    print("Sherpas death rate %.2f" % (sum(ever["sherpas died"])/sum(ever["tot death"])))

    ever_sh=ever[ever["sherpas free"]==False].sort_values("year",ascending=False)
    print("\nEverest exp with sherpas")
    print("Sherpas rate %.2f" % (sum(ever_sh["sherpas"])/sum(ever_sh["tot people"])))
    print("Sherpas death rate %.2f" % (sum(ever_sh["sherpas died"])/sum(ever_sh["tot death"])))

    print("\nRate of Everest commercial exp whitout sherpas %.2f" %\
     (ever[(ever["commercial"]==True) & (ever["sherpas free"]==True)].shape[0]/ \
     (ever[ever["commercial"]==True].shape[0])))


    ever_com_sh=ever_sh[ever_sh["commercial"]==True]
    print("\nEverest comm exp with sherpas")
    print("Sherpas rate %.2f" % (sum(ever_com_sh["sherpas"])/sum(ever_com_sh["tot people"])))
    print("Sherpas death rate %.2f" % (sum(ever_com_sh["sherpas died"])/sum(ever_com_sh["tot death"])))

    pro=ever[(ever["commercial"]==False) & (ever["sherpas free"]==True)]
    not_com=ever[ever["commercial"]==False]
    not_com_sh=not_com[not_com["sherpas free"]==False]
    print("\nPros death rate %.2f" % (sum(pro["tot death"])/sum(pro["tot people"])))
    print("\nNot commercial sherpas rate %.2f" % (sum(not_com["sherpas"])/sum(not_com["tot people"])))
    print("Not commercial sherpas death rate %.2f" % (sum(not_com["sherpas died"])/sum(not_com["tot death"])))
    print("\nNot commercial with sherpas  rate %.2f" % (sum(not_com_sh["sherpas"])/sum(not_com_sh["tot people"])))
    print("Not commercial with sherpas death rate %.2f" % (sum(not_com_sh["sherpas died"])/sum(not_com_sh["tot death"])))


print_stats()
ever

pro=ever[(ever["commercial"]==False) & (ever["sherpas free"]==True)]
not_com=ever[ever["commercial"]==False]
not_com_sh=not_com[not_com["sherpas free"]==False]
j=0
for i in ll["route"]:
    print(i)

j

ll=ever[(ever["standard route"]!="VERO") & (ever["standard route"]!="FALSO")]
ll
years=ever_sh["year"].unique()
sh_died=[]
tot_died=[]
for year in years:
    sh_died.append(sum(ever_sh[ever_sh["year"]==year]["sherpas died"]))
    tot_died.append(sum(ever_sh[ever_sh["year"]==year]["tot death"]))

plt.plot(years,tot_died,label="tot")
plt.plot(years,sh_died)
sum(ever_sh["sherpas died"])

sum(df["sherpas died"])

ag=ever[ever["commercial"]==True]
ag[ag["sherpas free"]==True].shape



#*******************************************

ever[(ever["standard route"]==True) & (ever["route"]!="S Col-SE Ridge")]




sorted(ever["route"].unique().astype(str))
ever[ever["route"].astype(str)=="nan"]
