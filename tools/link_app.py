"""Embeds the notebook's exported models (space_fog_models.json) in the Space Fog app.

Usage:  python link_app.py space_fog_models.json space-fog.html
Run it again whenever the notebook has been re-run, so the app uses the newly trained models.
"""
import json
import re
import sys

models_path, app_path = sys.argv[1], sys.argv[2]
models = json.load(open(models_path, encoding="utf-8"))
for key in ("cabin", "rad", "phys"):
    assert key in models, f"{models_path} has no '{key}' model: run the notebook to the end (Part 12)"

payload = json.dumps(models, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")
html = open(app_path, encoding="utf-8").read()
pattern = re.compile(r'(<script id="sfModels" type="application/json">)(.*?)(</script>)', re.S)
assert len(pattern.findall(html)) == 1, "the app has no single <script id=\"sfModels\"> block"
html = pattern.sub(lambda m: m.group(1) + payload + m.group(3), html)
open(app_path, "w", encoding="utf-8").write(html)
print(f"Embedded {len(payload) / 1024:.0f} kB of models in {app_path}")
