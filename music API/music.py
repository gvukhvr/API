import requests

def get_tracks(artist_name, api_key):
    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "artist.gettoptracks",
        "artist": artist_name,
        "api_key": api_key,
        "format": "json",
        "limit": 10  
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "toptracks" in data:
        print(f"Top tracks '{artist_name}':\n")
        for i, track in enumerate(data["toptracks"]["track"], start=1):
            print(f"{i}. {track['name']}")
    else:
        print("error:", data.get("message", "error))

API_KEY = "57dd3ce68cb9d939d64a71da86627321"
artist = input("Singer name: ")
get_tracks(artist, API_KEY)
