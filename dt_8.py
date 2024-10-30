import numpy as np
import matplotlib.pyplot as plt


def energy_simulation(mass, k, b, initial_position, initial_velocity, time_span):
    dt = 0.01
    t = np.arange(0, time_span, dt)

    position = np.zeros_like(t)
    velocity = np.zeros_like(t)

    kinetic_energy = np.zeros_like(t)
    potential_energy = np.zeros_like(t)
    total_energy = np.zeros_like(t)

    position[0] = initial_position
    velocity[0] = initial_velocity

    for i in range(1, len(t)):
        acceleration = (-k * position[i - 1] - b * velocity[i - 1]) / mass
        velocity[i] = velocity[i - 1] + acceleration * dt
        position[i] = position[i - 1] + velocity[i - 1] * dt

        kinetic_energy[i] = 0.5 * mass * velocity[i] ** 2
        potential_energy[i] = 0.5 * k * position[i] ** 2
        total_energy[i] = kinetic_energy[i] + potential_energy[i]

    plt.figure(figsize=(12, 8))

    plt.plot(t, kinetic_energy, label='Kinetic Energy', color='r')
    plt.plot(t, potential_energy, label='Potential Energy', color='b')
    plt.plot(t, total_energy, label='Total Energy', color='g')

    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.title('Energy vs Time for Damped Mass-Spring System')
    plt.legend()
    plt.grid()
    plt.show()


mass = float(input("Enter mass (kg) (Recommended: 1): ") or 1)
k = float(input("Enter spring constant (N/m) (Recommended: 10): ") or 10)
b = float(input("Enter damping coefficient (N*s/m) (Recommended: 0.5): ") or 0.5)
initial_position = float(input("Enter initial displacement (m) (Recommended: 1): ") or 1)
initial_velocity = float(input("Enter initial velocity (m/s) (Recommended: 0): ") or 0)
time_span = float(input("Enter time span (s) (Recommended: 20): ") or 20)

energy_simulation(mass, k, b, initial_position, initial_velocity, time_span)
