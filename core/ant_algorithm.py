import numpy as np

def run_aco(
    distance_matrix,
    ant_count=30,
    n_iterations=80,
    alpha=1.0,
    beta=2.0,
    rho=0.5,
    q=100
):
    """
    distance_matrix : n x n mesafe matrisi (km)
    Dönüş:
        best_path      : en iyi tur (indisler)
        best_length    : en iyi turun uzunluğu (km)
        best_history   : iterasyonlara göre en iyi uzunluk listesi
    """
    n_cities = distance_matrix.shape[0]

    # Feromon matrisi (başlangıçta hepsi aynı)
    pheromone = np.ones((n_cities, n_cities))

    # Sezgisel bilgi: 1 / mesafe
    heuristic = 1.0 / (distance_matrix + 1e-10)  # 0 bölünmesini engelle
    np.fill_diagonal(heuristic, 0.0)

    best_length = np.inf
    best_path = None
    best_history = []

    for it in range(n_iterations):
        all_paths = []
        all_lengths = []

        for ant in range(ant_count):
            # Her karınca rastgele bir şehirden başlayabilir
            start = np.random.randint(0, n_cities)
            path = [start]
            visited = set(path)

            # Tüm şehirleri gez
            for _ in range(n_cities - 1):
                i = path[-1]

                # Ziyaret edilmemiş şehirler
                candidates = [j for j in range(n_cities) if j not in visited]

                # Olasılık hesabı (pheromone^alpha * heuristic^beta)
                tau = pheromone[i, candidates] ** alpha
                eta = heuristic[i, candidates] ** beta
                probs = tau * eta
                if probs.sum() == 0:
                    probs = np.ones_like(probs)
                probs = probs / probs.sum()

                j = np.random.choice(candidates, p=probs)
                path.append(j)
                visited.add(j)

            # Tura dönüş (başlangıca geri)
            length = 0.0
            for k in range(len(path) - 1):
                length += distance_matrix[path[k], path[k+1]]
            # İstersen turu kapat: başlangıca dön
            length += distance_matrix[path[-1], path[0]]

            all_paths.append(path)
            all_lengths.append(length)

            # En iyi çözümü güncelle
            if length < best_length:
                best_length = length
                best_path = path

        # Feromon buharlaşması
        pheromone *= (1 - rho)

        # Feromon birikimi
        for path, length in zip(all_paths, all_lengths):
            deposit = q / length
            for k in range(len(path) - 1):
                i, j = path[k], path[k+1]
                pheromone[i, j] += deposit
                pheromone[j, i] += deposit
            # Turu kapat (başlangıca geri)
            i, j = path[-1], path[0]
            pheromone[i, j] += deposit
            pheromone[j, i] += deposit

        best_history.append(best_length)

    return best_path, best_length, best_history
