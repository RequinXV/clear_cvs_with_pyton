# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import scipy.stats as st

# chargement et affichage des données
data = pd.read_csv('operations.csv')

data.dtypes
data['date_operation'] = pd.to_datetime(data['date_operation'])
data.isnull().sum()

# pour afficher uniquement les variables qui ont des valeurs manquantes
nb_na = data.isnull().sum()
nb_na[nb_na>0]
data.loc[data['montant'].isnull(),:]

# on stocke le df des valeurs manquantes dans un nouveau df
data_na = data.loc[data['montant'].isnull(),:]

# pour chaque ligne de mon df, on récupère les index (qui ne changent pas au travers du .loc)
for index in data_na.index:
    # calcul du montant à partir des soldes précédents et actuels
    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope']

data.loc[data['categ'].isnull(),:]

data.loc[data['libelle'] == 'PRELEVEMENT XX TELEPHONE XX XX', :]

data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'

data.loc[data[['date_operation', 'libelle', 'montant', 'solde_avt_ope']].duplicated(keep=False),:]

data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)

data.describe()

i = data.loc[data['montant']==-15000,:].index[0] # récupération de l'index de la transaction à -15000
data.iloc[i-1:i+2,:] # on regarde la transaction précédente et la suivante

data.loc[data['montant']==-15000, 'montant'] = -14.39