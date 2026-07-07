from glob import glob
import pandas as pd
from Utils import *



add = '/home/goswam_a@WMGDS.WMG.WARWICK.AC.UK/PycharmProjects/SEP/data/Offline/'
save_add = '/home/goswam_a@WMGDS.WMG.WARWICK.AC.UK/PycharmProjects/SEP/data/'
feature_rows = []


for file in glob(f'{add}*.csv'):
    filename = file.split('/')[-1].split('.csv')[0]
    print(filename)
    df = pd.read_csv(file, skiprows=[1, 2])

    omega = df['Angular Frequency']
    eta_complex = df['Complex Viscosity']

    params = fit_carreau_yasuda(omega, eta_complex)

    eta_fit = carreau_yasuda(omega, *params)
    # Compute fit quality
    relative_error = np.mean(
        np.abs((eta_complex - eta_fit) / eta_complex)
    )
    print(f'Fit Error: {relative_error:.4f}')

    feature_rows.append({
        'ID': filename,
        'Angular Frequency': omega.tolist(),
        'Complex Viscosity': eta_complex.tolist(),
        'CY_Params': params.tolist(),
    })

feature_df = pd.DataFrame(feature_rows, columns=['ID', 'Angular Frequency', 'Complex Viscosity', 'CY_Params'])
print(feature_df)
feature_df.to_csv(f'{save_add}test.csv', index=False)

