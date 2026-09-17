#!/usr/bin/env python3
"""
Sincroniza las maquetas de la carpeta publica de Google Drive con propuestas/<slug>/index.html.

- Lista los archivos text/html de la carpeta (Drive API v3, solo lectura, clave de API publica).
- Cada archivo se llama maqueta-<slug>.html  ->  propuestas/<slug>/index.html
- Solo escribe si el contenido cambia. Nunca borra nada. Nunca toca la raiz del repo.
"""
import json, os, re, sys, urllib.parse, urllib.request

FOLDER_ID = os.environ["DRIVE_FOLDER_ID"]
API_KEY   = os.environ["DRIVE_API_KEY"]
BASE      = "https://www.googleapis.com/drive/v3/files"
SLUG_RE   = re.compile(r"^maqueta-([a-z0-9]+(?:-[a-z0-9]+)*)\.html$")

def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()

def list_folder():
    files, token = [], None
    q = f"'{FOLDER_ID}' in parents and trashed = false and mimeType = 'text/html'"
    while True:
        params = {"q": q, "fields": "nextPageToken,files(id,name,modifiedTime,size)",
                  "pageSize": 200, "key": API_KEY}
        if token:
            params["pageToken"] = token
        data = json.loads(get(BASE + "?" + urllib.parse.urlencode(params)))
        files += data.get("files", [])
        token = data.get("nextPageToken")
        if not token:
            return files

def main():
    files = list_folder()
    print(f"{len(files)} archivo(s) HTML en la carpeta de Drive")
    written, skipped, ignored = [], [], []
    for f in files:
        m = SLUG_RE.match(f["name"])
        if not m:
            ignored.append(f["name"]); continue
        slug = m.group(1)
        dest_dir = os.path.join("propuestas", slug)
        dest = os.path.join(dest_dir, "index.html")
        body = get(f"{BASE}/{f['id']}?alt=media&key={API_KEY}")
        if len(body) < 500 or b"<html" not in body[:2000].lower():
            ignored.append(f"{f['name']} (no parece HTML completo)"); continue
        if os.path.exists(dest) and open(dest, "rb").read() == body:
            skipped.append(slug); continue
        os.makedirs(dest_dir, exist_ok=True)
        with open(dest, "wb") as out:
            out.write(body)
        written.append(slug)
    print("Nuevas/actualizadas:", written or "ninguna")
    print("Sin cambios:", len(skipped))
    if ignored:
        print("Ignoradas:", ignored)
    # Para el paso siguiente del workflow
    with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a") as go:
        go.write(f"changed={'true' if written else 'false'}\n")
        go.write(f"slugs={' '.join(written)}\n")

if __name__ == "__main__":
    main()
