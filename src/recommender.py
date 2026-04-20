from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

INT_FIELDS = {"id"}
FLOAT_FIELDS = {"energy", "valence", "danceability", "acousticness", "tempo_bpm"}

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_acousticness: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads a CSV file and returns a list of songs as dictionaries with proper types."""

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {}
            for key, value in row.items():
                if value == "":
                    continue
                if key in INT_FIELDS:
                    song[key] = int(value)
                elif key in FLOAT_FIELDS:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song against user preferences and returns a total score with reasons."""
    score = 0.0
    reasons = []

    # Genre match
    if song.get("genre", "").lower() == user_prefs.get("genre", "").lower():
        score += 1.0
        reasons.append("genre match (+1.0)")

    # Mood match
    if song.get("mood", "").lower() == user_prefs.get("mood", "").lower():
        score += 0.5
        reasons.append("mood match (+0.5)")

    # Energy similarity
    energy_sim = 1 - abs(song.get("energy", 0.0) - user_prefs.get("energy", 0.0))
    score += energy_sim
    reasons.append(f"energy similarity (+{energy_sim:.2f})")

    # Acousticness similarity
    acoustic_sim = 1 - abs(song.get("acousticness", 0.0) - user_prefs.get("target_acousticness", 0.5))
    score += acoustic_sim
    reasons.append(f"acousticness similarity (+{acoustic_sim:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Returns the top-k songs ranked by how well they match the user's preferences."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, ", ".join(reasons)))

    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
