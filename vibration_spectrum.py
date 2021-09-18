import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##test comment##

filename = '/Users/sanskruti/Downloads/OneDrive_2_9-17-2021/20210914-0001-slab5/20210914-0001-slab5_1.csv'
filename2 = '/Users/sanskruti/Downloads/OneDrive_2_9-17-2021/20210914-0001-slab5/20210914-0001-slab5_2.csv'
filename3 = '/Users/sanskruti/Downloads/OneDrive_2_9-17-2021/20210914-0001-slab5/20210914-0001-slab5_3.csv'
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

#convert acc to velocity (microns/seconds)
df['dis'] = (0.5 * df['acc'] * (1/df['Hz'])) * 10**6
#df['log'] = np.log10(df['dis'])

df2['dis'] = (0.5 * df2['acc'] * (1/df['Hz'])) * 10**6
#df2['log'] = np.log10(df2['dis'])

df3['dis'] = (0.5 * df3['acc'] * (1/df['Hz'])) * 10**6
df3['log'] = np.log10(df3['dis'])

#convert Hz to seconds
df['seconds'] = (1/df['Hz'])
df2['seconds'] = (1/df['Hz'])
df3['seconds'] = (1/df['Hz'])

# Hz = list(df['Hz'])
# dis = list(df['dis'])

#plots data

plt.plot(list(df['Hz']), list(df['dis']), linewidth=0.5, label = '1')
plt.plot(list(df2['Hz']), list(df2['dis']), linewidth=0.5, label = '2')
plt.plot(list(df3['Hz']), list(df3['dis']), linewidth=0.5, label = '3')


#smoothed data
windowSize = 10

series = df.squeeze()
#print(type(series))
print(series)
rolling = series.rolling(windowSize)
mean = rolling.mean()
print(mean)
sdList = mean.values.tolist()
sdNew = sdList[windowSize - 1]

#plt.plot(sdNew, linewidth = 2, label = 'Smooth')

plt.xlabel('Hz')
plt.ylabel('Velocity, um/seconds')
plt.yscale('log')
plt.ylim([10**(-4), 10])
plt.xlim([0, 400])
plt.grid(linestyle='-')
plt.legend(loc = 'best')
plt.title('Vibration Spectrum- Center Tuesday')
# plt.savefig(r'filepath' + filename + '.png', dpi=200)
plt.show()