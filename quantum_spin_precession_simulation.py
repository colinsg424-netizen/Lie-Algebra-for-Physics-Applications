import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
from groups import SU

# get SU(2) generators (Pauli matrices)
gens = SU(2)

# spin operators
Sx = gens[0]
Sy = gens[1]
Sz = gens[2]

# Magnetic field
Bx, By, Bz = 0.0, 0.0, 1.0

# Hamiltonian (set gamma = 1, ħ = 1 units)
H = Bx * Sx + By * Sy + Bz * Sz

# initial state (spinor)
psi0 = np.array([1, 1], dtype=complex)
psi0 /= np.linalg.norm(psi0)

# Bloch vector mapping
def bloch_vector(psi):
    x = np.vdot(psi, Sx @ psi).real
    y = np.vdot(psi, Sy @ psi).real
    z = np.vdot(psi, Sz @ psi).real
    return np.array([x, y, z])
  
# Time evolution operator
def evolve_bloch(psi0, H, dt, steps):
  U_step = expm(-1j * H * dt)
  psi = psi0.copy()
  traj = []
  for i in range(steps):
    psi = U_step @ psi
    psi /= np.linalg.norm(psi)
    traj.append(bloch_vector(psi))
  return np.array(traj)

# Simulation
dt = 0.05
steps = 200
traj = evolve_bloch(psi0, H, dt, steps)

# Plot Bloch sphere trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(traj[:, 0], traj[:, 1], traj[:, 2])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("SU(2) Spin-1/2 Bloch Sphere Precession")

plt.show()
