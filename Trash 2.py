from glob import glob
import pandas as pd
from Utils import *
import ast
import matplotlib.pyplot as plt





add = '/home/goswam_a@WMGDS.WMG.WARWICK.AC.UK/PycharmProjects/SEP/data/test.csv'
A = 'M12'
B = 'M3'
T = 'M6'

df = pd.read_csv(add)

T_visc = np.array(ast.literal_eval(df.loc[df['ID'] == T, 'Complex Viscosity'].values[0]),dtype=float)
A_visc = np.array(ast.literal_eval(df.loc[df['ID'] == A, 'Complex Viscosity'].values[0]),dtype=float)
B_visc = np.array(ast.literal_eval(df.loc[df['ID'] == B, 'Complex Viscosity'].values[0]),dtype=float)


A_param = np.array(ast.literal_eval(df.loc[df['ID'] == A, 'CY_Params'].values[0]),dtype=float)
B_param = np.array(ast.literal_eval(df.loc[df['ID'] == B, 'CY_Params'].values[0]),dtype=float)
T_param = np.array(ast.literal_eval(df.loc[df['ID'] == T, 'CY_Params'].values[0]),dtype=float)


A_feat = CY_to_feature_vector(A_param)
B_feat = CY_to_feature_vector(B_param)
T_feat = CY_to_feature_vector(T_param)


x_pred= estimate_x_from_features(A_feat, B_feat, T_feat)


T_pred = (1 - x_pred)*A_visc+ x_pred*B_visc
freq = np.array(ast.literal_eval(df.loc[df['ID'] == T, 'Angular Frequency'].values[0]), dtype=float)
plt.plot( np.log(freq), np.log(T_pred), label='pred')
plt.plot(np.log(freq), np.log(T_visc), label=T)
plt.plot(np.log(freq), np.log(A_visc), label=A)
plt.plot(np.log(freq), np.log(B_visc), label=B)

# plt.plot(np.log(T_pred), np.log([0,1,2,3]), label='pred')
# plt.plot(np.log(T_param), np.log([0,1,2,3]), label='GT')

plt.xlabel('Frequency')
plt.ylabel('Viscosity')
plt.title('validation')
plt.legend()
plt.savefig(f"{add}Validation_M12toM6.pdf")

print(x_pred)

