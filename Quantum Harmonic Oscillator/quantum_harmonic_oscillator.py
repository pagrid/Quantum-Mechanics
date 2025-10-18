# -*- coding: utf-8 -*-
"""
quantum_harmonic_oscillator.ipynb

Quantum Harmonic Oscillator Simulation
---------------------------------------
Author: Petros Agridos

Description:
This script visualizes the quantum harmonic oscillator — one of the fundamental models in quantum mechanics.
It computes and plots the potential energy curve, energy eigenvalues, and corresponding normalized Hermite–Gaussian wavefunctions.

It produces two main figures:
1. Energy levels and probability densities |ψₙ(x)|² superimposed on the potential.
2. Normalized eigenfunctions ψₙ(x) for n = 0–4, showing their oscillatory structure and parity.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite
from math import factorial, sqrt, pi

# ----------------------------------------------------
# PARAMETERS (ħ = m = ω = 1)
# ----------------------------------------------------
hbar = 1.0
m = 1.0
omega = 1.0
alpha = np.sqrt(m * omega / hbar)
x_min, x_max = -4.5, 4.5
N = 1000  # Number of spatial grid points (sampling resolution)
x = np.linspace(x_min, x_max, N)

# ----------------------------------------------------
# POTENTIAL FUNCTION
# ----------------------------------------------------
def potential(x):
    return 0.5 * m * omega**2 * x**2

# ----------------------------------------------------
# NORMALIZED WAVEFUNCTION ψₙ(x)
# ----------------------------------------------------
def wavefunction(n, x):
    """Compute normalized Hermite-Gaussian wavefunction ψₙ(x)."""
    norm = 1 / np.sqrt(2**n * factorial(n) * sqrt(pi))
    Hn = eval_hermite(n, x)
    psi = norm * np.exp(-0.5 * x**2) * Hn
    return psi

# ----------------------------------------------------
# ENERGY LEVELS
# ----------------------------------------------------
def energy(n):
    return (n + 0.5) * hbar * omega

# ----------------------------------------------------
# COMBINED DIAGRAM: ENERGY LEVELS + |ψₙ|²
# ----------------------------------------------------
def plot_combined_diagram(max_n=3):
    plt.figure(figsize=(10, 6))
    V = potential(x)
    plt.plot(x, V, 'k-', label="Potential $V(x)$", zorder=1)

    for n in range(max_n + 1):
        psi = wavefunction(n, x)
        prob_density = psi**2
        E_n = energy(n)

        # scale wavefunctions for visibility
        scale = 0.5 * (x_max - x_min) / max(prob_density.max(), 1)
        plt.plot(x, scale * prob_density + E_n, label=f"$|\\psi_{n}(x)|^2$", zorder=2)

        plt.axhline(E_n, color="gray", linestyle="dotted", linewidth=0.8)
        plt.text(x_max + 0.1, E_n, f"$E_{n} = {E_n:.1f}\\,\\hbar\\omega$", fontsize=9, va="center")

    plt.title("Quantum Harmonic Oscillator: Energies and Probability Densities")
    plt.xlabel("$x$")
    plt.ylabel("Energy / Probability Density")
    plt.legend(loc="upper right", fontsize=8)
    plt.grid(alpha=0.3)
    plt.xlim(x_min, x_max)
    plt.ylim(-0.5, energy(max_n) + 1)
    plt.show()

# ----------------------------------------------------
# NEW: NORMALIZED EIGENFUNCTIONS ψₙ(x)
# ----------------------------------------------------
def plot_wavefunctions(max_n=4):
    plt.figure(figsize=(10, 6))
    for n in range(max_n + 1):
        psi = wavefunction(n, x)
        plt.plot(x, psi, label=f"$\psi_{n}(x)$")
    plt.title("Normalized Eigenfunctions of the Quantum Harmonic Oscillator")
    plt.xlabel("$x$")
    plt.ylabel("$\psi_n(x)$")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.xlim(x_min, x_max)
    plt.show()

# ----------------------------------------------------
# RUN BOTH PLOTS
# ----------------------------------------------------
plot_combined_diagram(max_n=3)
plot_wavefunctions(max_n=4)
