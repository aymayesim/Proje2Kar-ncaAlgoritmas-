import matplotlib.pyplot as plt

def plot_route(coords, best_path):
    """
    coords: [(adres, lat, lon), ...]
    best_path: şehir indislerinin listesi
    Dönüş: matplotlib Figure nesnesi
    """
    lats = []
    lons = []
    labels = []

    for idx in best_path:
        addr, lat, lon = coords[idx]
        lats.append(lat)
        lons.append(lon)
        labels.append(str(idx))

    # Turu kapatmak için başlangıcı sona ekle
    lats.append(lats[0])
    lons.append(lons[0])
    labels.append(labels[0])

    fig, ax = plt.subplots()
    ax.plot(lons, lats, marker="o")
    for x, y, lab in zip(lons, lats, labels):
        ax.text(x, y, lab)

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("ACO - En İyi Bulunan Rota (Kuş Uçuşu Koordinatlar)")
    ax.grid(True)
    return fig


def plot_convergence(best_history):
    """
    best_history: iterasyonlara göre en iyi rota uzunluğu listesi
    Dönüş: matplotlib Figure nesnesi
    """
    fig, ax = plt.subplots()
    ax.plot(range(1, len(best_history)+1), best_history, marker="o")
    ax.set_xlabel("İterasyon")
    ax.set_ylabel("En iyi rota uzunluğu (km)")
    ax.set_title("ACO Yakınsama Grafiği")
    ax.grid(True)
    return fig
