# -*- coding: utf-8 -*-
"""
quantum_tunneling_simulation.py

Quantum Tunneling through a Potential Barrier
---------------------------------------------
Author: Petros Agridos

Description:
This script numerically explores the quantum tunneling phenomenon
for a particle encountering a rectangular potential barrier.

It computes and visualizes:
    - Transmission probability (T) as a function of particle energy (E)
    - Dependence of T on the barrier width (a)

Physics background:
For a rectangular barrier of height V0 and width a, a particle
with energy E < V0 can still tunnel through with probability T(E, a).

Formula:
    κ = sqrt(2m(V0 - E)) / ħ
    T = 1 / (1 + (V0² * sinh²(κa)) / (4E(V0 - E)))

Dependencies:
    numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------
# Physical constants (set to 1 for simplicity)
# --------------------------------------------
ħ = 1.0
m = 1.0

# --------------------------------------------
# Parameters
# --------------------------------------------
V0 = 1.0                              # Barrier height
a_values = [0.2, 0.5, 1.0, 1.5, 2.0]  # Barrier widths to compare
E = np.linspace(0.01, 2.0, 400)       # Energy range

# --------------------------------------------
# Transmission coefficient function
# --------------------------------------------
def transmission(E, V0, a):
    T = np.zeros_like(E)
    for i, Ei in enumerate(E):
        if Ei < V0:
            kappa = np.sqrt(2 * m * (V0 - Ei)) / ħ
            T[i] = 1 / (1 + (V0**2 * np.sinh(kappa * a)**2) / (4 * Ei * (V0 - Ei)))
        else:
            k = np.sqrt(2 * m * (Ei - V0)) / ħ
            T[i] = 1 / (1 + (V0**2 * np.sin(k * a)**2) / (4 * Ei * (Ei - V0)))
    return T

# --------------------------------------------
# Plot Transmission for different barrier widths
# --------------------------------------------
plt.figure(figsize=(9, 6))

for a in a_values:
    T = transmission(E, V0, a)
    plt.plot(E, T, label=f'a = {a}')

plt.title("Quantum Tunneling — Transmission vs Energy")
plt.xlabel("Energy E (in arbitrary units)")
plt.ylabel("Transmission Probability T(E)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

