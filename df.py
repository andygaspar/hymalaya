import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("data/himalayan_csv/exped.csv",sep=",")
peaks=pd.read_csv("data/himalayan_csv/peaks.csv",sep=",")

done


monte=dict(zip(peaks["name"],peaks["peak_id"]))
monteID=dict(zip(peaks["peak_id"],peaks["name"]))


def search(mount_prefix):
    words=[]
    for peak in monte.keys():
        PEAK=peak.lower()
        common=0
        for i in range(len(mount_prefix)-1):
            for j in range(len(PEAK)-1):
                if mount_prefix[i]==PEAK[j] and mount_prefix[i+1]==PEAK[j+1] :
                    common+=1;
        if common>=len(mount_prefix)*3/4-1:
            words.append(peak)

    return words

#esempio di come funziona il search
search("annap")
