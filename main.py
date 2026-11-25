import os

EXCUSE = "In my defence, the map labelled that lake a shortcut, and the ducks crossing it looked far more confident than you do right now."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(EXCUSE)
os.chmod(path, 0o644)
