import numpy as np
import pandas as pd

#importare il modulo df
import df_maker as dm





#importare il data frame completo
df=dm.make_df()

#usare la funzione search
dm.search("ann",df)

print(df["peak"])


everest=df[df["peak id"]=="EVER"]
print(everest["peak"])

cho=df[df["peak"]=="Cho Oyu"]
cho.sort_values("year")
cho=cho[cho["year"]==1954]
cho["success"]
ever.columns


dm.search("cho",df)

df[df["height"]>8000]
