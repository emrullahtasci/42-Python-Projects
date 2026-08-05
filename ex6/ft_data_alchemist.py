import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    # 1. Başlangıç oyuncu listesi (büyük ve küçük harfli karışık)
    initial_players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {initial_players}")

    # 2. List Comprehension 1: Tüm isimleri baş harfi büyük yapma
    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")

    # 3. List Comprehension 2: Başlangıçta sadece baş harfi büyük olanları filtreleme
    only_capitalized = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")

    # 4. Dict Comprehension 1: İsimleri anahtar, rastgele skorları değer yapma (10 ile 1000 arası)
    score_dict = {name: random.randint(10, 1000) for name in all_capitalized}
    print(f"Score dict: {score_dict}")

    # 5. Skor ortalamasını hesaplama
    avg_score = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(avg_score, 2)}")

    # 6. Dict Comprehension 2: Ortalamanın üstündeki skorları filtreleme
    high_scores = {
        name: score
        for name, score in score_dict.items()
        if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()