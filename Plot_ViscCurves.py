from glob import glob

import numpy as np
import pandas as pd
from Utils import *
import ast

import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

add = '/home/goswam_a@WMGDS.WMG.WARWICK.AC.UK/PycharmProjects/SEP/data/'
df = pd.read_csv(f'{add}test.csv')
M = df['ID'].values
# print(M)
# M = ['M3', 'M12', 'M12_1', 'M12_2', 'M12_3', 'M12_4', 'M12_5']
M = ['M3', 'M12', 'M12_1', 'M12_1_M3_5', 'M12_1_M3_10', 'M12_1_M3_15', 'M12_1_M3_20', 'M12_1_M3_25', 'M12_1_M3_30']
# M = ['M3', 'M12', 'M12_2', 'M12_2_M3_5', 'M12_2_M3_10', 'M12_2_M3_15', 'M12_2_M3_20', 'M12_2_M3_25', 'M12_2_M3_30']
# M = ['M3', 'M12', 'M12_3', 'M12_3_M3_5', 'M12_3_M3_10', 'M12_3_M3_15', 'M12_3_M3_20', 'M12_3_M3_25', 'M12_3_M3_30']
# M = ['M3', 'M12', 'M12_4', 'M12_4_M3_5', 'M12_4_M3_10', 'M12_4_M3_15', 'M12_4_M3_20', 'M12_4_M3_25', 'M12_4_M3_30']
# M = ['M3', 'M12', 'M12_5', 'M12_5_M3_5', 'M12_5_M3_10', 'M12_5_M3_15', 'M12_5_M3_20', 'M12_5_M3_25', 'M12_5_M3_30']
for m in M:
    visc = np.array(ast.literal_eval(df.loc[df['ID'] == m, 'Complex Viscosity'].values[0]),dtype=float)
    freq = np.array(ast.literal_eval(df.loc[df['ID'] == m, 'Angular Frequency'].values[0]),dtype=float)
    plt.plot(np.log(freq), np.log(visc), label=m)

    plt.xlabel('Frequency')
    plt.ylabel('Viscosity')
    plt.title('M12_1 blends')
    plt.legend()
    plt.savefig(f"{add}viscosity_curve_M12_1_blends.pdf")

