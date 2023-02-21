import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import scipy.stats as st

data = pd.read_csv('operations.csv')


data['date_operation'] = pd.to_datetime(data['date_operation'])

data_na = data.loc[data['montant'].isnull(),:]

for index in data_na.index:

    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope']

data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'


data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)

data.loc[data['montant']==-15000, 'montant'] = -14.39
data.to_csv('operationsClean.csv', index=False)