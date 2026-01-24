# %% Calculate probability of getting a certain number when rolling two dice
import numpy as np
import matplotlib.pyplot as plt
import data_visualization as dv

dv.set_plot_style("cashaback_dark.mplstyle")
wheel = dv.ColorWheel()


# %% Functions
# Our dice rolls are coming from uniform distributions U[1,7]
def roll_dice():
    die1 = np.random.randint(1, 7)
    die2 = np.random.randint(1, 7)
    return die1 + die2


def roll_weighted_dice(weights1, weights2):
    die1 = np.random.choice(np.arange(1, 7), p=weights1)
    die2 = np.random.choice(np.arange(1, 7), p=weights2)
    return die1 + die2


def monte_carlo(n: int, model):
    outcomes = []
    for i in range(n):
        outcome = model()
        outcomes.append(outcome)

    return outcomes


# %% Run unweighted simulation
n = 100000
res = monte_carlo(n, roll_dice)
# Calculate probabilities of each outcome
probs = [res.count(i) / n for i in range(2, 13)]

# %% Plot results
plt.close("all")
fig, ax = plt.subplots()

ax.bar(np.arange(2, 13), probs, color=wheel.rak_blue)
ax.set_xticks(np.arange(2, 13))
ax.set_xlabel("Sum of Two Dice")
ax.set_ylabel("Probability")
fig.savefig("./figures/monte_carlo_dice.png", dpi=300)
plt.show()


# %% Run weighted simulation
# Let's say die 1 is biased towards 6 and die 2 is biased towards 1
weights1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]  # Die 1 weights
weights2 = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]  # Die 2 weights
