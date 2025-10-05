# quantum-particle-in-a-box
Numerical solution of the 1D Schrödinger equation for a particle in a box using Python


# Quantum Particle in a 1D Infinite Square Well

Goal
----
Numerically find the first few energy eigenvalues and eigenfunctions ψₙ(x)
for a particle confined in an infinite potential well using a simple
shooting method with the explicit Euler integration scheme.

Theory
------
The time-independent Schrödinger equation (TISE) is:

    - (ħ² / 2m) * (d²ψ / dx²) + V(x)ψ = Eψ

For an infinite potential well:
    - V(x) = 0 inside (0 ≤ x ≤ a)
    - V(x) = ∞ outside
    - Boundary conditions: ψ(0) = 0 and ψ(a) = 0

Inside the well, since V = 0, the equation becomes:

    ψ''(x) = (2m / ħ²) * (V - E)ψ = -k² ψ,
    where k² = 2mE / ħ²

Analytic solution (for reference):
    ψₙ(x) = √(2/a) * sin(nπx/a)
    Eₙ = (n²π²ħ²) / (2ma²)

Numerical idea (the "shooting" method)
--------------------------------------
1. Choose a trial energy E.
2. Integrate Schrödinger’s equation from x = 0 → a.
3. If ψ(a) ≈ 0, that energy is (approximately) an eigenvalue.
4. Increase E until you find the next eigenstate.

We use natural units (ħ = m = a = 1) so the numbers are simple.
