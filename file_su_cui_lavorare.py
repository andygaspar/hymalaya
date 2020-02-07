import numpy as np
import pandas as pd

#importare il modulo df
import df_maker as dm


"""
    questo è un sample di come importare il dataframe

    possiamo lavorare su file separati e usare df e df_others come moduli da importare

"""


#importare il data frame completo
df=dm.make_df()

#usare la funzione search
dm.search("ann",df)
