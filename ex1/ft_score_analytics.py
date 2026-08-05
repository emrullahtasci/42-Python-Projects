import sys

def main() -> None:
    print("===Player Score Analytics==")
    total_arguments = len(sys.argv)
    if total_arguments <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    clean_scores = []
    i = 1
    while i < total_arguments:
        arg = sys.argv[i]
        try:
            score = int(arg)
            clean_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
        i = i + 1
    
    if len(clean_scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    total_players = len(clean_scores)
    total_score = sum(clean_scores)
    avg_score = total_score / total_players
    high_score = max(clean_scores)
    low_score = min(clean_scores)
    score_range = high_score - low_score

    
    print(f"Scores processed: {clean_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {avg_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")

if __name__ == "__main__":
    main()

