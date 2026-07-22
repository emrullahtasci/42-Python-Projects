def input_temperatur(temp_str : str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp} °C bitkiler icin cok sicak!(maks 40 °C)")
    elif temp < 0:
        raise ValueError(f"{temp} °C bitkiler icin cok soguk !(min 0 °C)")

    return temp

def test_temperature()->None :
    print("=== Sera Sicakliği Denetleyici ===")
    
    test_degerleri = ["25","abc","100","-50"]
    for val in test_degerleri:
        try:
            print(f"Gelen veri: '{val}' ")
            sonuc = input_temperatur(val)
            print(f"Sicaklik su an {sonuc}")
        except ValueError as e :
            print(f"Hata yakalandi : {e}")

    print("Tum testler tamamlandi - program cokmedi!")


if __name__ == "__main__":
    test_temperature()