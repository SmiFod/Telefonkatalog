# Creating markdown content from the provided text
markdown_content = """
# Linux Setup Guide

## 1. Åpne terminalen
Trykk **CTRL + ALT + T** (her skriver du kommandoene under).

## 2. Se etter og installer oppdateringer til all programvare som er installert
- `sudo apt update` (finner oppdateringer)
- `sudo apt upgrade` (installerer oppdateringer)

## 3. Sett opp brannmur med UFW (Uncomplicated Firewall)
- `sudo apt install ufw` (installerer UFW)
- `sudo ufw enable` (aktiverer brannmuren ved oppstart)
- `sudo ufw allow ssh` (tillater SSH-tilkoblinger gjennom brannmuren)
- Sjekk statusen på brannmuren ved å skrive: `sudo ufw status`

## 4. Skru på SSH
- `sudo apt install openssh-server` (installerer SSH-serveren)
- `sudo systemctl enable ssh` (slår på SSH ved oppstart)
- `sudo systemctl start ssh` (starter SSH her og nå)

## 5. Finn IP-adressen din
- Skriv `ip a`
- Hvis du har kablet nettverk, vil IP vises ved `eth0:` linjen. Hvis du kun har trådløst, vil IP vises ved `wlan0:` linjen. IP-adresse er vanligvis noe som `10.2.3.x`, hvor `x` er et tall mellom 2 og 254.

## 6. Installer Git, Python og MariaDB
- `sudo apt install python3-pip`
- `sudo apt install git`
- `sudo apt install mariadb-server`
- `sudo mysql_secure_installation`

## 7. Lag en ny databasebruker og sett riktige rettigheter
1. Logg inn i MariaDB:
   - `sudo mariadb -u root`
2. Lag ny bruker:
   - `CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';`
3. Gi ny bruker rettigheter:
   - `GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';`
4. Oppdater rettigheter:
   - `FLUSH PRIVILEGES;`

## 8. Installer annen programvare
Installer annen programvare du ønsker, for eksempel VS Code, en annen nettleser, Wireshark, Nmap, osv.
- Hvis du får trøbbel med å installere VS Code:
  1. Last ned `.deb`-filen for `arm64` fra [Visual Studio Code Linux Setup](https://code.visualstudio.com/docs/setup/linux).
  2. Naviger til mappen der du lastet ned filen.
  3. Kjør `sudo apt install ./code`, trykk på `Tab` og deretter `Enter`.

## 9. Kjør oppdatering igjen
- `sudo apt update`
- `sudo apt upgrade`
"""

# Writing the content to a markdown file
file_path = '/mnt/data/linux_setup_guide.md'
with open(file_path, 'w') as file:
    file.write(markdown_content)

file_path  # Returning the file path of the markdown file

# Creating markdown content for the tutorial

markdown_tutorial = """
# Telefonkatalog Setup Guide for Ubuntu

## Trinn 1: Last ned koden fra GitHub

1. Åpne terminalen (Ctrl + Alt + T).
2. Naviger til ønsket mappe hvor du vil klone repoet:

    ```bash
    cd /sti/til/ønsket/mappe
    ```

3. Klon GitHub-repoet:

    ```bash
    git clone https://github.com/LektorRichvoldsen/telefonkatalog_og_database.git
    ```

4. Gå inn i prosjektmappen:

    ```bash
    cd telefonkatalog_og_database
    ```

---

## Trinn 2: Installer nødvendige pakker

1. Oppdater pakker og installer nødvendige avhengigheter:

    ```bash
    sudo apt update
    sudo apt upgrade
    sudo apt install python3-pip mariadb-server git
    ```

2. Installer MySQL-connector for Python:

    ```bash
    pip3 install mysql-connector-python
    ```

---

## Trinn 3: Sett opp MariaDB

1. Start MariaDB-serveren:

    ```bash
    sudo systemctl start mariadb
    ```

2. Sikker konfigurasjon av MariaDB:

    ```bash
    sudo mysql_secure_installation
    ```

    Følg instruksjonene for å sette et root-passord og fjerne uønskede standardinnstillinger.

3. Logg inn i MariaDB:

    ```bash
    sudo mariadb -u root -p
    ```

4. Opprett en database for telefonkatalogen:

    ```sql
    CREATE DATABASE telefonkatalog;
    ```

5. Gå til telefonkatalog-databasen:

    ```sql
    USE telefonkatalog;
    ```

6. Opprett tabellen for å lagre personer:

    ```sql
    CREATE TABLE person (
        id int NOT NULL AUTO_INCREMENT,
        fornavn VARCHAR(255) NOT NULL,
        etternavn VARCHAR(255) NOT NULL,
        telefonnummer CHAR(8),
        PRIMARY KEY (id)
    );
    ```

---

## Trinn 4: Sett opp databasebruker

1. Lag en ny bruker for applikasjonen med passende rettigheter:

    ```sql
    CREATE USER 'telefonbruker'@'localhost' IDENTIFIED BY 'passord';
    GRANT ALL PRIVILEGES ON telefonkatalog.* TO 'telefonbruker'@'localhost';
    FLUSH PRIVILEGES;
    ```

---

## Trinn 5: Kjør Python-applikasjonen

1. Åpne `telefonkatalog.py` (eller hovedfilen i prosjektet) og sørg for at databasekonfigurasjonen stemmer overens med det du har satt opp. Her er et eksempel:

    ```python
    mydb = mysql.connector.connect(
        host="localhost",
        user="telefonbruker",
        password="passord",
        database="telefonkatalog"
    )
    ```

2. Kjør Python-filen:

    ```bash
    python3 telefonkatalog.py
    ```

3. Følg instruksjonene i programmet for å legge til personer, søke, eller vise katalogen.

---

## Trinn 6: Test databasekoblingen

Du kan teste om Python-applikasjonen din kobler seg til databasen ved å kjøre en enkel testkobling:

```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="telefonbruker",
    password="passord",
    database="telefonkatalog"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM person")
resultater = cursor.fetchall()

for dings in resultater:
    print(dings)


