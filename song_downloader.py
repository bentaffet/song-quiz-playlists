import subprocess
import os
import sys


install_spotdl = input("Do you need to install spotdl? (y/n) ").lower()
if install_spotdl == 'y':
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "spotdl"], check=True)
        print("spotdl installed successfully")
    except subprocess.CalledProcessError as e:
        print("Failed to install spotDL.")
        print(e)

install_ffmpeg = input("Do you need to install ffmpeg? (y/n) ").lower()
if install_ffmpeg == 'y':
    try:
        subprocess.run([sys.executable, "-m", "spotdl", "--download-ffmpeg"], check=True)
        print("ffmpeg installed successfully!")
    except subprocess.CalledProcessError as e:
        print("Failed to install FFmpeg.")
        print(e)

playlist_link_list = [('https://open.spotify.com/playlist/31LVuXlRYRVq4Z6krWGedS?si=1c576d71637244b3', '60s'),
                      ('https://open.spotify.com/playlist/5KmBulox9POMt9hOt3VV1x?si=91bb0f2504a642a9', '70s'),
                      ('https://open.spotify.com/playlist/19PgP2QSGPcm6Ve8VhbtpG?si=f0f2b905b9cb42c0', '80s'),
                      ('https://open.spotify.com/playlist/3C64V048fGyQfCjmu9TIGA?si=7f0e3aab308e43a5', '90s'),
                      ('https://open.spotify.com/playlist/5JBCdq5x9YbODn9XAqFY0f?si=c405adc106804ecf', '2000s'),
                      ('https://open.spotify.com/playlist/6dzWCbiW5HjxaBMuo5THnn?si=8dba56ddea94414c', '2010s'),
                      ('https://open.spotify.com/playlist/4vSTV61efRmetmaoz95Vet?si=be19efb6dffc4e6c', '2020s'),
                      ('https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=7e75cd8cf3654f87', 'Todays Top Hits'),
                      ('https://open.spotify.com/playlist/6tJ7yq9VRd2vO4oBHvVKsM?pi=yMZAQpUnQKu3W', 'Will Wise Classic Rock')
                      ]

current_directory = os.getcwd()

subprocess.run(["mkdir", "songs"])

for item in playlist_link_list:
    link, playlist_name = item

    output_directory = os.path.join(current_directory, "songs", playlist_name)
    os.makedirs(output_directory, exist_ok=True)

    result = subprocess.run([
        "python3",
        "-m", "spotdl",
        "download",
        link,
        "--output", output_directory  # <-- specify download folder
    ], capture_output=True, text=True)

    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

