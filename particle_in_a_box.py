"""
Quantum Particle in a 1D Infinite Square Well
 """

import matplotlib.pyplot as plt
import numpy as np

# Constants - We use natural units (ħ = m = a = 1), so the numbers are simpler.
h = 1.0  # Planck's constant (ħ) set to 1
m = 1.0  # particle mass
a = 1.0  # well width
V = 0.0  # potential inside the well (0 for infinite well)

# Numerical parameters
dx = a * 0.01  # spatial step size
dE = 0.01  # energy step size
eigen_energies_total = 4  # number of eigenvalues/eigenfunctions to find

# Storage lists
eigenfunctions = []  # list to hold eigenfunction arrays ψ(x)
eigenfunctions_x = []  # list to hold x-values for each ψ
eigenenergies = []  # list to store found energy eigenvalues
x_list = []
psi_list = []

# Main loop to find eigenstates
E = 0.0
counter = 1
while counter <= eigen_energies_total:
    psi = 1.0
    # The inner loop scans energy values until ψ(a) ≈ 0
    # (meaning we’ve found a standing wave that “fits” in the box)
    while abs(psi) > 0.001:
        psi = 0.0
        x = 0.0
        dpsi = 1.0  # initial slope (arbitrary scale)
        E += dE  # try the next energy value
        x_list = []
        psi_list = []

        # Integrate Schrödinger equation using explicit Euler method
        while x <= a:
            ddpsi = 2 * (m / h ** 2) * (V - E) * psi  # second derivative ψ''
            dpsi += ddpsi * dx  # update first derivative
            psi += dpsi * dx  # update ψ
            x += dx
            x_list.append(x)
            psi_list.append(psi)

    # If ψ(a) ≈ 0, we’ve found an eigenvalue → store it
    eigenfunctions.append(psi_list)
    eigenfunctions_x.append(x_list)
    eigenenergies.append(E)
    counter += 1
    # Increase E slightly so we find the next higher energy state in the next loop
    E *= 1.1

# Normalize the eigenfunctions
for i in range(len(eigenfunctions)):
    # Approximate ∫ψ² dx ≈ Σ ψ² * dx
    normConstant = np.dot(eigenfunctions[i], eigenfunctions[i]) * dx
    # Divide each ψ by √(∫ψ² dx) so total probability = 1
    eigenfunctions[i] = [psi / np.sqrt(normConstant) for psi in eigenfunctions[i]]

# Print eigenenergies
print("\nCalculated energy levels:")
for i, energy in enumerate(eigenenergies, start=1):
    print(f"Level {i}: E = {energy:.4f}")

# Plot results
scale_factor = 5  # scaling factor so curves don’t overlap visually
for i in range(len(eigenfunctions)):
    # vertically shift ψ(x) by its energy level E for clarity
    shifted_psi = [eigenenergies[i] + scale_factor * psi for psi in eigenfunctions[i]]
    plt.plot(eigenfunctions_x[i], shifted_psi, label=f"Eigenfunction {i + 1} (E={eigenenergies[i]:.2f})")

plt.xlabel("x (in units of a)")
plt.ylabel(f"Energy + ψ (scaled by {scale_factor})")
plt.title("Particle in a Box: Eigenfunctions at Their Energy Levels")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
