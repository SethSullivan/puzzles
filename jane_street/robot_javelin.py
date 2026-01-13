import numpy as np
import matplotlib.pyplot as plt


# %% Functions
def throw_javelin():
    throw_dist = np.random.uniform()

    return throw_dist


def throw_again(throw_dist: float) -> bool:
    if throw_dist < 0.5:
        return True
    else:
        return False


def decide_result(
    r1_throws: tuple[float, float], r2_throws: tuple[float, float]
) -> int:
    if r1_throws[1] is not None:
        final_r1_throw = r1_throws[1]
    else:
        final_r1_throw = r1_throws[0]

    if r2_throws[1] is not None:
        final_r2_throw = r2_throws[1]
    else:
        final_r2_throw = r2_throws[0]

    if final_r1_throw > final_r2_throw:
        return 1
    else:
        return 0


# %%
r1_throws = []
r2_throws = []
r1_result = []
for i in range(1000):
    r1_throw1 = throw_javelin()
    r2_throw1 = throw_javelin()

    r1_throw_again = throw_again(r1_throw1)
    if r1_throw_again:
        r1_throw2 = throw_javelin()
    else:
        r1_throw2 = None

    r2_throw_again = throw_again(r2_throw1)
    if r2_throw_again:
        r2_throw2 = throw_javelin()
    else:
        r2_throw2 = None

    r1_throws.append((r1_throw1, r1_throw2))
    r2_throws.append((r2_throw1, r2_throw2))

    r1_result.append(decide_result(r1_throws[i], r2_throws[i]))

x = 1
print(x)
