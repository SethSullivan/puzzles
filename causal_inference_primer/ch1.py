# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# %% Study Question 1.2.1
# a) Mistaking correlation for causation. People who make more money can afford to get married, or they just have more time to get married since they aren't worried about money
#    Also, more money means someone else is more likely to marry you.
# b) The direction of causality is wrong here. More fires means they hire more firefighters
# c) People who hurry are already late in the first place. bad causality again

# %% Study question 1.2.2
# a)
print(90 / 380)


# %%
fig, ax = plt.subplots()
x = np.linspace(0, 1, 100)
y = stats.beta.pdf(x, 2, 5)
ax.plot(x, y)
ax.set_title("Beta Distribution with a=2, b=5")
ax.set_xlabel("x")
plt.show()
ax.set_ylabel("Probability Density Function")
