"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        {
            "name": "High-Energy Pop",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "target_acousticness": 0.15
        },
        {
            "name": "Chill Lofi",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.38,
            "target_acousticness": 0.80
        },
        {
            "name": "High Energy Sad (Adversarial)",
            "genre": "blues",
            "mood": "sad",
            "energy": 0.95,
            "target_acousticness": 0.10
        },
        {
            "name": "Classical Conflict (Impossible Combo)",
            "genre": "classical",
            "mood": "energetic",
            "energy": 0.90,
            "target_acousticness": 0.10
        },
        {
            "name": "Extreme Low (0.0 Values)",
            "genre": "metal",
            "mood": "angry",
            "energy": 0.0,
            "target_acousticness": 0.0
        },
        {
            "name": "Extreme High (1.0 Values)",
            "genre": "electronic",
            "mood": "euphoric",
            "energy": 1.0,
            "target_acousticness": 1.0
        },
        {
            "name": "Case Sensitivity Test",
            "genre": "Pop",
            "mood": "Happy",
            "energy": 0.85,
            "target_acousticness": 0.15
        },
        {
            "name": "Balanced Neutral Test",
            "genre": "jazz",
            "mood": "melancholic",
            "energy": 0.5,
            "target_acousticness": 0.5
        }
    ]

    for p in profiles:
        print("\n" + "=" * 40)
        print("PROFILE:", p["name"])
        print("=" * 40)

        recs = recommend_songs(p, songs, k=5)

        for song, score, explanation in recs:
            print(f"{song['title']} - {score:.2f}")
            print(explanation)
            print()


if __name__ == "__main__":
    main()