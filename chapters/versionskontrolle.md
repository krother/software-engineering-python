# Versionskontrolle

## Was ist Versionskontrolle?

Ein System zur Versionskontrolle protokolliert automatisch *Änderungen* in Deinem Programmcode und anderen Dateien im Projekt. Du kannst dadurch:

* Ideen ausprobieren, ohne das Programm kaputt zu machen.
* Zu früheren Versionen und wieder zurück springen.
* Das gleiche Programm auf mehreren Computern editieren.
* Mit mehreren Leuten parallel an einem Projekt arbeiten.
* Dein Projekt im Netz veröffentlichen.

Versionskontrolle ist der erste Schritt, um professionell Programme zu entwickeln. Sobald Du mit Versionskontrolle anfängst, ist es schwer, damit wieder aufzuhören.

## Welche Versionskontrollsysteme gibt es?

Heute sind vor allem drei Systeme zur Versionskontrolle üblich:

* [git](https://git-scm.com/) – Das mit Abstand beste und am weitesten verbreite dezentrale System. Wurde von Linus Torvalds entwickelt. Praktisch alle großen Open-Source-Projekte laufen unter `git`.
* [Mercurial (hg)](http://hginit.com/) – Weniger komplexes und einfacher zu lernendes dezentrales System.
* [Subversion (SVN)](https://subversion.apache.org) – Ein sehr gutes, zentralisiertes System. Wird vor allem in Softwarefirmen verwendet.

Für kleinere Projekte (Doktorarbeiten und kleiner) sind alle drei Systeme bestens geeignet.

## Installation

Git ist ein Programm für die **Kommandozeile**.

Unter Windows findest Du die Installationsdateien unter [https://book.git-scm.com/downloads](https://book.git-scm.com/downloads).

Unter Ubuntu Linux ist `git` sehr leicht zu installieren:

    sudo apt install git

Es gibt mehrere [graphische Oberflächen](https://book.git-scm.com/downloads/guis) für `git`. Diese sind aus meiner Sicht aber nicht unbedingt notwendig.

## Aufgaben

### 1. Erstelle ein Repository

* Erstelle ein leeres Verzeichnis für Dein Projekt
* Öffne ein Windows-Terminal (`cmd` im Startmenü eingeben)
* Wechsle in das Verzeichnis (mit `cd VERZEICHNISNAME`)
* Gib ein `git init`

### 2. Dateien hinzufügen

Nun speichern wir Quelltext im 

* Schreibe ein **Hello World**-Programm im Projektverzeichnis
* Gib `git status` ein.
* Füge eine Datei mit `git add DATEINAME` hinzu.
* Gib `git status` ein.
* Speichere die Änderungen im Repository mit `git commit`
* Gib `git status` ein.

### 3. Änderungen hinzufügen

* Ändere den Quelltext Deines Programms
* Gib `git status` ein.
* Gib `git diff DATEINAME` ein.
* Füge die Änderungen mit `git add` und `git commit` wie oben hinzu.
* Zeige mit `git log` die Geschichte des Projekts an.

### 4. Dateien ignorieren

Automatisch generierte Dateien haben in der Regel im Repository nichts zu suchen. `git` soll diese ignorieren.

* Erstelle im Texteditor die Datei `.gitignore` im Projektverzeichnis
* Schreibe den Namen einer compilierten oder anderen automatisch generierten Datei in  `.gitignore` (ein Dateiname pro Zeile).
* Du kannst auch mit dem Eintrag `VERZEICHNISNAME/*` ein Verzeichnis komplett ignorieren lassen.
* Füge `.gitignore` dem Repository hinzu.

### 5. GitHub

Nun veröffentlichen wir unser Projekt.

* Lege Dir ein Konto auf [GitHub](https://github.com/) an.
* Erstelle dort ein neues Repository.
* Folge den Anweisungen auf dem Bildschirm, um das existierende Repository im Netz zu veröffenlichen.
* Erstelle eine `README.md`-Datei mit grundsätzlichen Infos zum Projekt.
* Wähle eine Lizenz für Dein Programm aus.
* Weitere Änderungen kannst Du mit `git push` veröffentlichen.

### 6. Kollaboration

Entwickelt ein Projekt im Zweierteam weiter.

* Füge einen zweiten Contributor zu Deinem Projekt hinzu.
* Mit `git clone URL` kann dieser sich eine Kopie des Projekts besorgen.
* Mit `git pull` könnt Ihr beide die aktuellste Version anfordern und so den Code der anderen Contributors erhalten.
* Versucht beide, unterschiedliche Dateien zu editieren die Änderungen ins Repository zu übertragen. Was passiert?
* Versucht beide, die gleiche Datei parallel zu ändern und diese Änderungen ins Repository zu übertragen. Was passiert?


## Links

* [Git Dokumentation](https://book.git-scm.com/doc)
* [Try GitHub - online-Tutorial](https://try.github.io/)
* [GitHub - öffentliches Repository](https://github.com/)
