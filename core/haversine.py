
import numpy as np
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # km
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)

    a = sin(dphi/2)**2 + cos(phi1) * cos(phi2) * sin(dlambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def build_haversine_matrix(coords):
    """
    coords: [(adres, lat, lon), ...]
    çıktı: n x n mesafe matrisi (km)
    """
    n = len(coords)
    mat = np.zeros((n, n), dtype=float)

    for i in range(n):
        _, lat1, lon1 = coords[i]
        for j in range(n):
            if i == j:
                mat[i, j] = 0.0
            else:
                _, lat2, lon2 = coords[j]
                mat[i, j] = haversine_distance(lat1, lon1, lat2, lon2)
    return mat
