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

    A_param = np.array(ast.literal_eval(df_feat.loc[df_feat['ID'] == A, 'CY_Params'].values[0]), dtype=float)
    B_param = np.array(ast.literal_eval(df_feat.loc[df_feat['ID'] == B, 'CY_Params'].values[0]), dtype=float)
    T_param = np.array(ast.literal_eval(df_feat.loc[df_feat['ID'] == T, 'CY_Params'].values[0]), dtype=float)
    # x_pred = estimate_x_from_features(A_param, B_param, T_param)

    A_feat = CY_to_feature_vector(A_param)
    B_feat = CY_to_feature_vector(B_param)
    T_feat = CY_to_feature_vector(T_param)

    x_pred = estimate_x_from_features(A_feat, B_feat, T_feat)





    print(A, '-----', B, '-----',T, '-----', frac, '-----', x_pred)