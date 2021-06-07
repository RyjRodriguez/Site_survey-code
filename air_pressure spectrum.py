import matplotlib.pyplot as plt
import csv

filename = r"C:\filepath"
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

df = [float(x) for x in header]


plt.plot(df)
plt.title('Air Pressure')
plt.xlabel('Series')
plt.ylabel('kPa')
plt.tight_layout()
#plt.savefig(r"C:filepath\filename.png", dpi=300)
plt.show()