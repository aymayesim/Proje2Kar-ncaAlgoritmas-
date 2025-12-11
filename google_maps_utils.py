import os
import googlemaps

def get_gmaps_client():
    """
    Ortam değişkeninden GOOGLE_MAPS_API_KEY'i alır ve Google Maps Client nesnesi oluşturur.
    """
    api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Google API key bulunamadı! Colab'de os.environ ile API key'i tanımlamayı unutmayın.")
    return googlemaps.Client(key=api_key)


def geocode_addresses(addresses):
    """
    Adres listesini alır ve Google Maps Geocoding API ile (adres, lat, lon) bilgilerini döndürür.
    Dönüş formatı:
    [
        ("Kemalöz Mahallesi, Uşak", 38.67, 29.37),
        ...
    ]
    """
    gmaps = get_gmaps_client()
    results = []

    for addr in addresses:
        geocode = gmaps.geocode(addr)
        if not geocode:
            raise ValueError(f"Adres bulunamadı: {addr}")

        loc = geocode[0]["geometry"]["location"]
        lat, lng = loc["lat"], loc["lng"]

        results.append((addr, lat, lng))

    return results
