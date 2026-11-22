"""Pull the latest published snapshot from gta6brands.com into data/. Read-only on the site."""
import json, os, urllib.request, hashlib
BASE = "https://www.gta6brands.com"
def get(url): return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "gta6brands-repo-sync"}), timeout=60).read()
latest = json.loads(get(f"{BASE}/data/latest.json"))
snap = latest["snapshot"]; man = json.loads(get(latest["manifest"]))
out = f"data/snapshots/{snap}"; os.makedirs(out, exist_ok=True); os.makedirs("data/latest", exist_ok=True)
for f in man["files"]:
    if f["name"] not in ("tracker.json", "tracker.csv", "tracker.md"): continue
    body = get(f["url"])
    if f.get("sha256") and hashlib.sha256(body).hexdigest() != f["sha256"]: raise SystemExit(f"checksum mismatch: {f['name']}")
    for d in (out, "data/latest"): open(f"{d}/{f['name']}", "wb").write(body)
for d in (out, "data/latest"): open(f"{d}/manifest.json", "w").write(json.dumps(man, ensure_ascii=False, indent=1))
open("data/changelog.json", "wb").write(get(f"{BASE}/data/changelog.json"))
print("synced", snap)
