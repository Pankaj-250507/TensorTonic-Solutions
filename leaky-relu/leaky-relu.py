import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    ans = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] <0:
            ans[i] = x[i]*alpha
        else:
            ans[i] = x[i]
    return ans
            