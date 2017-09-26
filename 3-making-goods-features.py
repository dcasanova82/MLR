import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

np.random.seed(8)

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=["red", "blue"], label=["Greyhounds", "Labs"])
plt.legend(prop={"size": 10})
plt.xlabel("dog height")
plt.ylabel("# of dogs")
plt.show()