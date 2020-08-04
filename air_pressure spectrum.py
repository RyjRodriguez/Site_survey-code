import matplotlib.pyplot as plt
import csv

filename = r"C:\Users\rrodr\Google Drive\Courses\Python Projects\Site_survey_analysis\air_pressure_spectrum_data.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

df = [float(x) for x in header]


plt.plot(df)
plt.title('Air Pressure')
plt.xlabel('Series')
plt.ylabel('kPa')
plt.tight_layout()
plt.savefig(r"C:\Users\rrodr\Google Drive\Courses\Python Projects\Site_survey_analysis\air_pressure_spectrum.png", dpi=300)
plt.show()