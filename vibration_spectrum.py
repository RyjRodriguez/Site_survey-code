import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##test comment##

filename = '/Users/sanskruti/Desktop/tOSU tings/summer21/Vibration Measurements/20210610-0001_PRB105_FR/20210610-0001_PRB105_FR_5.csv'
filename2 = '/Users/sanskruti/Desktop/tOSU tings/summer21/Vibration Measurements/20210609-0001_PRB101_FR/20210609-0001_PRB101_FR_01.csv'
filename3 = '/Users/sanskruti/Desktop/tOSU tings/summer21/Vibration Measurements/20210609-0001_PRB155_FR/20210609-0001_PRB155_FR_03.csv'
df = pd.read_csv(filename , skiprows=3, names=['Hz', 'dBv'])
df2 = pd.read_csv(filename2, skiprows=3, names=['Hz', 'dBv'])
df3 = pd.read_csv(filename3, skiprows=3, names=['Hz', 'dBv'])

#convert dBv to V_m
df['v_m'] = df['dBv'].apply(lambda x: 10.00 ** (x /20.00))
df2['v_m'] = df2['dBv'].apply(lambda x: 10.00 ** (x /20.00))
df3['v_m'] = df3['dBv'].apply(lambda x: 10.00 ** (x /20.00))

#convert V_m to acc w/ 100 volt = 1g
df['acc'] = df['v_m'].apply(lambda x: x/100 * 9.81)
df2['acc'] = df2['v_m'].apply(lambda x: x/100 * 9.81)
df3['acc'] = df3['v_m'].apply(lambda x: x/100 * 9.81)

#convert acc to displacement (um)
df['dis'] = (0.5 * df['acc'] * (1/df['Hz']) ** 2) * 10**6
df['log'] = np.log10(df['dis'])

df2['dis'] = (0.5 * df2['acc'] * (1/df['Hz']) ** 2) * 10**6
df2['log'] = np.log10(df2['dis'])

df3['dis'] = (0.5 * df3['acc'] * (1/df['Hz']) ** 2) * 10**6
df3['log'] = np.log10(df3['dis'])

# Hz = list(df['Hz'])
# dis = list(df['dis'])

plt.plot(list(df['Hz']), list(df['dis']), linewidth=0.5)
plt.plot(list(df2['Hz']), list(df2['dis']), linewidth=0.5)
plt.plot(list(df3['Hz']), list(df3['dis']), linewidth=0.5)
plt.xlabel('Hz')
plt.ylabel('Displacement, um')
plt.yscale('log')
plt.ylim([10**(-7), 10])
plt.grid(linestyle='-')
plt.title('Vibration Spectrum')
# plt.savefig(r'filepath' + filename + '.png', dpi=200)
plt.show()