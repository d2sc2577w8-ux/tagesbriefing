import subprocess

scripts = ["fetch_weather.py", "fetch_news.py", "fetch_sports_gaming.py"]

for script in scripts:
    print(f"--- Starte {script} ---")
    subprocess.run(["python3", script])

print("Fertig! Alle Daten aktualisiert.")

