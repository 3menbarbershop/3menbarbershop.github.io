# 3MEN BarberShop – Link-Seite

Statische Link-Seite (Linktree-Ersatz) für 3MEN BarberShop, Eibacher Hauptstraße 94, 90451 Nürnberg.
Live: https://3menbarbershop.github.io/ (kostenlos über GitHub Pages).

| Datei | Zweck |
|---|---|
| `index.html` | Die Link-Seite (5 Buttons) |
| `impressum.html` | Impressum & Datenschutz |
| `logo.svg` / `logo.png` | Original-Logo (aus `src-logo/logo.pdf`), Farben Blau `#447AAD`, Gold `#DCB455` |
| `icon.png`, `apple-touch-icon.png` | Browser-/Homescreen-Icon |
| `qr-3men.png` / `qr-3men.svg` | QR-Code zur Seite |
| `make_qr.py` | Erzeugt und prüft den QR-Code: `python3 make_qr.py <URL>` |

Links ändern: in `index.html` den jeweiligen `href="..."` anpassen, speichern, committen – GitHub Pages aktualisiert sich in 1–2 Minuten. Der QR-Code bleibt gleich, solange die Seiten-URL gleich bleibt.
