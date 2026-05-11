import numpy as np

states = ["Soleado", "Nublado", "Lluvioso"]
obs_map = {"sin_paraguas": 0, "con_paraguas": 1}

A = np.array([
    [0.8, 0.15, 0.05],
    [0.2, 0.6, 0.2],
    [0.2, 0.3, 0.5]
])

B = np.array([
    [0.9, 0.1],
    [0.5, 0.5],
    [0.2, 0.8]
])

pi = np.array([0.6, 0.3, 0.1])

obs_seq = [obs_map["con_paraguas"], obs_map["con_paraguas"], obs_map["sin_paraguas"]]

def viterbi(obs_seq):
    T = len(obs_seq)
    N = len(states)

    delta = np.zeros((T, N))
    psi = np.zeros((T, N), dtype=int)

    delta[0] = pi * B[:, obs_seq[0]]

    for t in range(1, T):
        for j in range(N):
            probs = delta[t-1] * A[:, j]
            psi[t, j] = np.argmax(probs)
            delta[t, j] = np.max(probs) * B[j, obs_seq[t]]

    path = np.zeros(T, dtype=int)
    path[-1] = np.argmax(delta[-1])

    for t in range(T-2, -1, -1):
        path[t] = psi[t+1, path[t+1]]

    return [states[i] for i in path]

print(viterbi(obs_seq))