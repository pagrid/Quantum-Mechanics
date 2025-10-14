# -*- coding: utf-8 -*-
"""time-independent-perturbations.ipynb

Time-Independent Perturbations in the Quantum Harmonic Oscillator
----------------------------------------------------------------
Author: Petros Agridos

Description:
This script analyzes time-independent perturbations applied to the quantum harmonic oscillator.
It compares the effects of various perturbations — x^3, x^4, and electric field terms — 
on the energy levels, computing first-order energy corrections numerically.

Dependencies:
    numpy, matplotlib, scipy

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from scipy.integrate import simpson
import math # Import the math module

# Constants
m = 1.0        # Mass (kg)
omega = 1.0    # Angular frequency (rad/s)
hbar = 1.0     # Reduced Planck's constant
alpha = m * omega / hbar

# Define the potential and wavefunctions
x = np.linspace(-5, 5, 1000)

# Harmonic oscillator potential
def harmonic_potential(x):
    return 0.5 * m * omega**2 * x**2

# Compute wavefunctions
energies = []
wavefunctions = []
def wavefunction(n, x):
    norm = 1.0 / np.sqrt(2**n * math.factorial(n)) * (alpha / np.pi)**0.25 # Use math.factorial
    Hn = hermite(n)
    psi = norm * np.exp(-alpha * x**2 / 2) * Hn(np.sqrt(alpha) * x)
    return psi

def energy(n):
    return (n + 0.5) * hbar * omega

for n in range(4):
    energies.append(energy(n))
    wavefunctions.append(wavefunction(n, x))

# Visualization of the harmonic oscillator potential, energies, and probability densities
plt.figure(figsize=(10, 6))
plt.plot(x, harmonic_potential(x), 'k', label="Potential")

for n in range(4):
    psi_squared = wavefunction(n, x)**2
    plt.plot(x, energies[n] + psi_squared, label=f"|ψ(x)| **2 (n={n})")
    plt.axhline(energies[n], color="gray", linestyle="--", alpha=0.6)

plt.title("Quantum Harmonic Oscillator: Potential and Probability Densities")
plt.xlabel("x (m)")
plt.ylabel("Energy (J)")
plt.legend()
plt.grid()
plt.show()

# ------------------ Case 1: Anharmonic Oscillator (x^4 Perturbation) ------------------

lambda_4 = 0.1  # Perturbation strength
def anharmonic_x4_potential(x):
    return harmonic_potential(x) + lambda_4 * x**4

# Compute energy corrections
def energy_correction_x4(n):
    psi_n = wavefunction(n, x)
    V_perturb = lambda_4 * x**4
    return simpson(psi_n**2 * V_perturb, x)

E_corrections_x4 = [energy_correction_x4(n) for n in range(4)]

plt.figure(figsize=(10, 6))
plt.bar(range(4), E_corrections_x4, tick_label=[f"n={n}" for n in range(4)])
plt.title("Energy Corrections: Anharmonic Oscillator (x^4 Perturbation)")
plt.xlabel("State (n)")
plt.ylabel("Energy Correction (J)")
plt.grid()
plt.show()

# ------------------ Case 2: Anharmonic Oscillator (x^3 Perturbation) ------------------

lambda_3 = 0.1  # Perturbation strength
def anharmonic_x3_potential(x):
    return harmonic_potential(x) + lambda_3 * x**3

# Compute energy corrections
def energy_correction_x3(n):
    psi_n = wavefunction(n, x)
    V_perturb = lambda_3 * x**3
    return simpson(psi_n**2 * V_perturb, x)

E_corrections_x3 = [energy_correction_x3(n) for n in range(4)]

plt.figure(figsize=(10, 6))
plt.bar(range(4), E_corrections_x3, tick_label=[f"n={n}" for n in range(4)])
plt.title("Energy Corrections: Anharmonic Oscillator (x^3 Perturbation)")
plt.xlabel("State (n)")
plt.ylabel("Energy Correction (J)")
plt.grid()
plt.show()

# ------------------ Case 3: Oscillator in an Electric Field ------------------

E_field = 0.1  # Electric field strength (V/m)
def electric_field_potential(x):
    return harmonic_potential(x) - m * E_field * x

# Compute energy corrections
def energy_correction_electric_field(n):
    psi_n = wavefunction(n, x)
    V_perturb = -m * E_field * x
    return simpson(psi_n**2 * V_perturb, x)

E_corrections_electric_field = [energy_correction_electric_field(n) for n in range(4)]

plt.figure(figsize=(10, 6))
plt.bar(range(4), E_corrections_electric_field, tick_label=[f"n={n}" for n in range(4)])
plt.title("Energy Corrections: Oscillator in an Electric Field")
plt.xlabel("State (n)")
plt.ylabel("Energy Correction (J)")
plt.grid()
plt.show()

# ------------------ Visualization of Perturbed Potentials ------------------
plt.figure(figsize=(10, 6))
plt.plot(x, harmonic_potential(x), label="Harmonic Potential")
plt.plot(x, anharmonic_x4_potential(x), label="Anharmonic x^4 Potential")
plt.plot(x, anharmonic_x3_potential(x), label="Anharmonic x^3 Potential")
plt.plot(x, electric_field_potential(x), label="Electric Field Potential")
plt.title("Comparison of Potentials")
plt.xlabel("x (m)")
plt.ylabel("Potential Energy (J)")
plt.legend()
plt.grid()
plt.show()
