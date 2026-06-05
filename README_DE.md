# Prompt-generation 🎨 Kurzanleitung

Prompt-generation ist ein leichtgewichtiges Desktop-Tool für KI-Bildgeneratoren wie Stable Diffusion, Midjourney, FLUX und ähnliche Plattformen.

Statt unübersichtlicher Textdateien oder Tabellen bietet es eine intuitive Benutzeroberfläche zum Verwalten, Organisieren und Erstellen von Prompts – ganz ohne Programmierkenntnisse.

## 🚀 Erste Schritte

### Schritt 1: Herunterladen und Starten

**Für die meisten Nutzer**

Laden Sie das aktuelle `.zip`-Paket von der GitHub-Releases-Seite herunter, entpacken Sie es und starten Sie `PromptGenerator.exe`.

**Für Entwickler**

Python 3.8+ erforderlich.

```bash
pip install PyQt6
python main.py
```

### Schritt 2: Tags auswählen und Gewichte anpassen

* Standardbibliothek ist bereits enthalten.
* Eigene JSON-Bibliotheken können über `File → Load Library...` geladen werden.
* Tags per Mausklick auswählen.
* Über das ⚙-Symbol Gewichtungen anpassen.

Beispiel:

```text
(masterpiece:1.3)
```

* Zusätzliche Begriffe können im Feld „Custom Prompts“ eingetragen werden.

### Schritt 3: Inspirationsmodus

Klicken Sie auf:

🎲 Global Random

Eine zufällige Kombination wird in einer separaten Inspirationsbox erzeugt, ohne Ihre aktuelle Auswahl zu verändern.

Gefällt Ihnen das Ergebnis, klicken Sie auf:

✨ Apply Inspiration

um es zu übernehmen.

### Schritt 4: Prompt generieren

Klicken Sie auf:

🚀 Generate Prompt

Anschließend werden angezeigt:

* Eine Vorschau in Ihrer Sprache
* Der englische Prompt für die KI

Mit:

📋 Copy English

können Sie den Prompt direkt kopieren.

## 💡 Tipps

### Visueller Bibliothekseditor

Mit:

```text
Ctrl + E
```

öffnen Sie den visuellen Editor.

Bibliotheken, Kategorien und Prompts lassen sich komfortabel bearbeiten, ohne JSON-Dateien manuell anzupassen.

### Anpassung

Unterstützt:

* Mehrsprachige Benutzeroberfläche
* Sofortigen Sprachwechsel
* Drei integrierte Designs:

  * Dark Cyber
  * Light Minimal
  * Dracula Purple
