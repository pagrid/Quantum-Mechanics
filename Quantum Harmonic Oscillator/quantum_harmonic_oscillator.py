# -*- coding: utf-8 -*-
"""quantum_harmonic_scillator.ipynb

Quantum Harmonic Oscillator Simulation
------------------------------
Author: Petros Agridos
Description:
This script visualizes the quantum harmonic oscillator — one of the fundamental models in quantum mechanics.
It computes and plots the potential energy curve, energy eigenvalues, and corresponding normalized Hermite–Gaussian wavefunctions.
The code illustrates how quantized energy levels emerge naturally from the Schrödinger equation and how the probability densities evolve for each state
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite
from math import factorial, sqrt, pi

# ----------------------------------------------------
# PARAMETERS (in natural units where ħ = m = ω = 1)
# ----------------------------------------------------
hbar = 1.0
m = 1.0
omega = 1.0
alpha = np.sqrt(m * omega / hbar)  # Scaling factor
x_min, x_max = -4.5, 4.5           # Range for x
N = 1000                           # Number of grid points
x = np.linspace(x_min, x_max, N)

# ----------------------------------------------------
# POTENTIAL FUNCTION: V(x) = (1/2) m ω² x²
# ----------------------------------------------------
def potential(x):
    return 0.5 * m * omega**2 * x**2

# ----------------------------------------------------
# HERMITE-GAUSSIAN WAVEFUNCTION ψₙ(x)
# ----------------------------------------------------
def wavefunction(n, x):
    """
    Compute the normalized wavefunction for the nth energy level.
    ψₙ(x) = N * Hₙ(x) * exp(-x² / 2)
    where N = (1 / sqrt(2ⁿ n! √π))
    """
    norm = 1 / np.sqrt(2**n * factorial(n) * sqrt(pi))
    Hn = eval_hermite(n, x)  # Hermite polynomial
    psi = norm * np.exp(-0.5 * x**2) * Hn
    return psi

# ----------------------------------------------------
# ENERGY LEVELS: Eₙ = (n + 1/2) ħω
# ----------------------------------------------------
def energy(n):
    return (n + 0.5) * hbar * omega

# ----------------------------------------------------
# PLOT POTENTIAL, WAVEFUNCTIONS, AND ENERGY LEVELS
# ----------------------------------------------------
def plot_combined_diagram(max_n=3):
    plt.figure(figsize=(10, 6))
    V = potential(x)

    # Plot potential
    plt.plot(x, V, 'k-', label="Potential $V(x)$", zorder=1)

    # Plot each energy level and corresponding |ψₙ(x)|²
    for n in range(max_n + 1):
        psi = wavefunction(n, x)
        prob_density = psi**2
        E_n = energy(n)

        # Scale the wavefunctions for visualization
        scale = 0.5 * (x_max - x_min) / max(prob_density.max(), 1)
        plt.plot(x, scale * prob_density + E_n, label=f"$|\\psi_{n}(x)|^2$", zorder=2)

        # Draw horizontal energy line
        plt.axhline(E_n, color="black", linestyle="dotted", linewidth=0.8)
        plt.text(x_max + 0.1, E_n, f"$E_{n} = {E_n:.1f}\\,\\hbar\\omega$", fontsize=9, va="center")

    # Labels and formatting
    plt.title("Quantum Harmonic Oscillator: Energies and Probability Densities")
    plt.xlabel("$x$")
    plt.ylabel("Energy / Probability Density")
    plt.legend(loc="upper right", fontsize=8)
    plt.grid(alpha=0.3)
    plt.xlim(x_min, x_max)
    plt.ylim(-0.5, energy(max_n) + 1)
    plt.show()

# ----------------------------------------------------
# RUN THE PLOT
# ----------------------------------------------------
plot_combined_diagram(max_n=3)
