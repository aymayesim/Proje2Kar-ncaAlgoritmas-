import streamlit as st
import sys

sys.path.append("/content/aco_usak_elektrik_rutasi")

from data.addresses import USAK_ADDRESSES
from data.google_maps_utils import geocode_addresses
from core.haversine import build_haversine_matrix
from core.ant_algorithm import run_aco
from visual.plotting import plot_route, plot_convergence
from config import (
    DEFAULT_ANT_COUNT,
    DEFAULT_ITERATIONS,
    DEFAULT_ALPHA,
    DEFAULT_BETA,
    DEFAULT_RHO,
    DEFAULT_Q
)

# -------------------------------------------------
# Streamlit Başlık
# -------------------------------------------------
st.set_page_config(page_title="ACO Rota Optimizasyonu", layout="wide")

st.markdown("""
# 🐜 Karınca Kolonisi Algoritması ile Rota Optimizasyonu (Uşak Elektrik Arızaları)

Elektrik firması, Uşak ilinde 15 farklı mahallede aynı anda arıza bildirimi almıştır.
Tek bir teknik ekip, tüm lokasyonları minimum toplam mesafe ile gezerek arızalara müdahale etmelidir.
Bu uygulama, Google Maps API'den alınan **gerçek koordinatlar** ve
**Karınca Kolonisi Algoritması (ACO)** ile en kısa rotayı yaklaşık olarak hesaplar.
""")

# -------------------------------------------------
# ACO Parametreleri
# -------------------------------------------------
st.sidebar.header("⚙️ ACO Parametreleri")

ant_count = st.sidebar.slider("Karınca Sayısı", 5, 100, DEFAULT_ANT_COUNT)
iterations = st.sidebar.slider("İterasyon Sayısı", 10, 300, DEFAULT_ITERATIONS)
alpha = st.sidebar.slider("Alpha (feromon etkisi)", 0.1, 5.0, DEFAULT_ALPHA)
beta = st.sidebar.slider("Beta (sezgisel bilgi etkisi)", 0.1, 5.0, DEFAULT_BETA)
rho = st.sidebar.slider("Rho (buharlaşma oranı)", 0.1, 1.0, DEFAULT_RHO)
q = DEFAULT_Q

st.sidebar.info("Parametreleri ayarladıktan sonra aşağıdan hesaplama başlatılabilir.")

# -------------------------------------------------
# Buton
# -------------------------------------------------
if st.button("Rotayı Hesapla"):
    # 1) Koordinatları çek (Google Maps API)
    with st.spinner("Google Maps API'den koordinatlar çekiliyor..."):
        coords = geocode_addresses(USAK_ADDRESSES)

    st.success("Koordinatlar alındı!")
    st.write("**İlk 3 konum (adres, enlem, boylam):**")
    st.write(coords[:3])

    # 2) Haversine ile mesafe matrisi
    with st.spinner("Kuş uçuşu mesafe matrisi oluşturuluyor..."):
        dist_matrix = build_haversine_matrix(coords)

    st.success("Mesafe matrisi oluşturuldu!")

    # 3) ACO'yu çalıştır
    with st.spinner("Karınca Kolonisi Algoritması çalıştırılıyor..."):
        best_path, best_length, best_history = run_aco(
            dist_matrix,
            ant_count=ant_count,
            n_iterations=iterations,
            alpha=alpha,
            beta=beta,
            rho=rho,
            q=q
        )

    st.success("Rota hesaplandı!")

    # -------------------------------------------------
    # SONUÇLAR
    # -------------------------------------------------
    st.subheader("📍 En İyi Rota Sırası (Mahalleler):")
    route_names = [USAK_ADDRESSES[i] for i in best_path]
    for name in route_names:
        st.write("- ", name)

    st.subheader(f"📏 En Kısa Toplam Mesafe (tahmini kuş uçuşu): **{best_length:.2f} km**")

    # -------------------------------------------------
    # Grafikler
    # -------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🗺️ Rota Görselleştirme")
        fig1 = plot_route(coords, best_path)
        st.pyplot(fig1)

    with col2:
        st.subheader("📉 Yakınsama Grafiği")
        fig2 = plot_convergence(best_history)
        st.pyplot(fig2)
