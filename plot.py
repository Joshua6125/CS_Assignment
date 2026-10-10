import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('istherecorrelation.csv', sep=';')

x = df['Year'].to_numpy()
y1 = df['WO [x1000]'].to_numpy()
y2 = df['NL Beer consumption [x1000 hectoliter]'].to_numpy()

fig, ax1 = plt.subplots()

ax1.plot(x, y1, color="tab:blue")
ax1.set_xlabel("Year")
ax1.set_ylabel("WO [x1000]", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.plot(x, y2, color="tab:orange")
ax2.set_ylabel("NL Beer consumption x1000 hectoliter", color="tab:orange")
ax2.tick_params(axis="y", labelcolor="tab:orange")

plt.title("Beer")
fig.tight_layout()
plt.savefig('plot.png', dpi=300)
plt.show()