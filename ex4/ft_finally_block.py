#!/usr/bin/env python3

class BitkiHatasi(Exception):
    def __init__(self, mesaj):
        super().__init__(mesaj)


def bitkiyi_sula(bitki_adi: str) -> None:
    # Arkadaşının kullandığı güvenli ve şık capitalize kontrolü
    if bitki_adi == bitki_adi.capitalize():
        print(f"{bitki_adi} sulanıyor: [OK]")
    else:
        raise BitkiHatasi(f"Sulama için geçersiz bitki adı: '{bitki_adi}'")


def sulama_sistemini_test_et() -> None:
    print("=== Bahçe Sulama Sistemi ===")
    
    # --- 1. Bölüm: Geçerli Bitkiler Testi ---
    print("Geçerli bitkiler test ediliyor...")
    print("Sulama sistemi açılıyor")

    try:
        bitkiler = ["Domates", "Marul", "Havuç"]
        for bitki in bitkiler:
            bitkiyi_sula(bitki)
    finally:
        print("Sulama sistemi kapatılıyor\n")

    # --- 2. Bölüm: Geçersiz Bitkiler Testi ---
    print("Geçersiz bitkiler test ediliyor...")
    print("Sulama sistemi açılıyor")

    try:
        bitkiyi_sula("Domates")
        bitkiyi_sula("marul")  # Küçük harf olduğu için hata patlatacak
    except BitkiHatasi as e:
        print(f"BitkiHatasi yakalandı: {e}")
        print(".. testler sonlandırılıyor ve ana programa dönülüyor")
        return
    finally:
        print("Sulama sistemi kapatılıyor")
        print("\nHata olsa bile temizlik her zaman yapılır!")


if __name__ == "__main__":
    sulama_sistemini_test_et()