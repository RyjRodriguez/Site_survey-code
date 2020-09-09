import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##test comment##

filename = r'C:\Users\rrodr\Google Drive\Courses\Python Projects\Site_survey_analysis\vibration_spectrum_data [1velinsec].csv'
df = pd.read_csv(filename , skiprows=3, names=['Hz', 'dBv'])

#convert dBv to V_m
df['v_m'] = df['dBv'].apply(lambda x: 10.00 ** (x /20.00))

#convert V_m to acc w/ 100 volt = 1g
df['acc'] = df['v_m'].apply(lambda x: x/100 * 9.81)

#convert acc to displacement (um)
df['dis'] = (0.5 * df['acc'] * (1/df['Hz']) ** 2) * 10**6
df['log'] = np.log10(df['dis'])


# Hz = list(df['Hz'])
# dis = list(df['dis'])

plt.plot(list(df['Hz']), list(df['dis']), linewidth=0.5)
plt.xlabel('Hz')
plt.ylabel('Displacement, um')
plt.yscale('log')
plt.ylim([10**(-7), 10])
plt.grid(linestyle='-')
plt.title('Vibration Spectrum')
# plt.savefig(r'C:\Users\rrodr\Google Drive\Courses\Python Projects\Site_survey_analysis\vibration_spectrum_data [1velinsec].csv' + filename + '.png', dpi=200)
plt.show()