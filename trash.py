from glob import glob
import pandas as pd
from Utils import *
import ast
import matplotlib.pyplot as plt

add = '/home/goswam_a@WMGDS.WMG.WARWICK.AC.UK/PycharmProjects/SEP/data/Features.csv'
add_expsheet = '/home/goswam_a@WMGDS.WMG.WARWICK.AC.UK/PycharmProjects/SEP/data/Fraction Prediction dataset M3.csv'
df_feat = pd.read_csv(add)
df_exp = pd.read_csv(add_expsheet)


for index, row in df_exp.iterrows():
    A = row['Recipient Polymer Filename (A)']
    B = row['Additive Polymer Filename (B)']
    T = row['Output Polymer Filename (T)']
    frac = row['Frac(B)']

    A_param = np.array(ast.literal_eval(df_feat.loc[df_feat['ID'] == A, 'Angular Frequency'].values[0]), dtype=float)[:28]
    print(A_param)