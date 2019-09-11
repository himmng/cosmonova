import numpy as np
def eta(a, Omega_m):
    s = np.power(1.0 / Omega_m - 1.0, 1.0 / 3.0)

    etav = 2.0 * np.sqrt(np.power(s, 3.0) + 1.0) * np.power((np.power(a, (-4.0)) -
                                                             0.1540 * s * np.power(a, (-3.0)) +
                                                             0.4304 * np.power(s, 2.0) * np.power(a, (-2.0)) +
                                                             0.19097 * np.power(s, 3.0) * np.power(a, -1.0) +
                                                             0.066941 * np.power(s, 4.0)), -1.0 / 8.0)
    return etav


def D(Omega_m, z):
    Dl = 3000.0 * (1.0 + z) * (eta(1.0, Omega_m) - eta(1.0 / (1.0 + z), Omega_m))

    return Dl


def mu(Omega_m, h, z):
    muv = (25.0 - 5.0 * (np.log10(h)) + 5.0 * (np.log10(D(Omega_m, z))))
    return muv
