# Telefonkatalog Setup Guide for Ubuntu

Denne veiledningen vil hjelpe deg med å sette opp en telefonkatalogapplikasjon på Ubuntu ved hjelp av Python, MariaDB, og Git. Vi vil bruke GitHub-repoet [SmiFod/Telefonkatalog](https://github.com/SmiFod/Telefonkatalog).

---

## Trinn 1: Last ned og installer oppdateringer

1. Åpne terminalen (bruk **Ctrl + Alt + T** for å åpne terminalen).
2. Oppdater pakkelisten og installer oppdateringer for all programvare som er installert:

    ```bash
    sudo apt update   # Finner oppdateringer
    sudo apt upgrade  # Installerer oppdateringer
    ```

---

## Trinn 2: Sett opp brannmur med UFW

1. Installer UFW (Uncomplicated Firewall):

    ```bash
    sudo apt install ufw
    ```

2. Aktiver brannmuren ved oppstart:

    ```bash
    sudo ufw enable
    ```

3. Tillat SSH-tilkoblinger gjennom brannmuren:

    ```bash
    sudo ufw allow ssh
    ```

4. Sjekk statusen på brannmuren:

    ```bash
    sudo ufw status
    ```

---

## Trinn 3: Skru på SSH

1. Installer SSH-serveren:

    ```bash
    sudo apt install openssh-server
    ```

2. Aktiver SSH ved oppstart:

    ```bash
    sudo systemctl enable ssh
    ```

3. Start SSH umiddelbart:

    ```bash
    sudo systemctl start ssh
    ```

---

## Trinn 4: Finn IP-adressen din

1. For å finne IP-adressen din, skriv følgende kommando i terminalen:

    ```bash
    ip a
    ```

2. Hvis du har kablet nettverk, vil IP-adressen vises under linjen merket med `eth0:`. Hvis du bruker trådløst nettverk, vil IP-adressen vises under linjen merket med `wlan0:`. Din IP-adresse vil normalt se ut som `10.2.3.x`, hvor `x` er et tall mellom 2 og 254.

---

## Trinn 5: Installer nødvendige pakker

For å kunne kjøre applikasjonen, må du installere nødvendige programvarer og Python-biblioteker:

1. Oppdater pakkelisten og installer nødvendige avhengigheter:

    ```bash
    sudo apt install python3-pip mariadb-server git
    ```

2. Installer MySQL-connectoren for Python, som gjør det mulig for Python-applikasjonen å kommunisere med MariaDB:

    ```bash
    pip3 install mysql-connector-python
    ```

---

## Trinn 6: Sett opp MariaDB

Før du kjører applikasjonen, må du sette opp databasen som lagrer informasjonen om personer.

1. Start MariaDB-serveren:

    ```bash
    sudo systemctl start mariadb
    ```

2. Sikre MariaDB-installasjonen ved å kjøre det interaktive sikkerhetsoppsettet:

    ```bash
    sudo mysql_secure_installation
    ```

   Følg instruksjonene for å sette et root-passord og fjerne uønskede standardinnstillinger, som anonyme brukere og testdatabaser.

3. Logg inn på MariaDB som root-bruker:

    ```bash
    sudo mariadb -u root -p
    ```

4. Opprett en ny database for telefonkatalogen:

    ```sql
    CREATE DATABASE telefonkatalog;
    ```

5. Gå inn i den nyopprettede databasen:

    ```sql
    USE telefonkatalog;
    ```

6. Opprett tabellen som skal lagre informasjon om personene:

    ```sql
    CREATE TABLE person (
        id INT NOT NULL AUTO_INCREMENT,
        fornavn VARCHAR(255) NOT NULL,
        etternavn VARCHAR(255) NOT NULL,
        telefonnummer CHAR(8),
        PRIMARY KEY (id)
    );
    ```

---

## Trinn 7: Opprett en ny databasebruker

For å kunne koble Python-applikasjonen til databasen, må du opprette en ny bruker med de riktige rettighetene:

1. Logg inn i MariaDB:

    ```bash
    sudo mariadb -u root
    ```

2. Opprett en ny bruker:

    ```sql
    CREATE USER 'telefonbruker'@'localhost' IDENTIFIED BY 'passord';
    ```

3. Gi brukeren tilgang til `telefonkatalog`-databasen:

    ```sql
    GRANT ALL PRIVILEGES ON telefonkatalog.* TO 'telefonbruker'@'localhost';
    FLUSH PRIVILEGES;
    ```

---

## Trinn 8: Kjør Python-applikasjonen

1. Åpne `telefonkatalog.py` i en teksteditor (som Visual Studio Code eller Nano) og forsikre deg om at databasekonfigurasjonen samsvarer med det du har satt opp. Her er et eksempel på hvordan konfigurasjonen bør se ut:

    ```python
    mydb = mysql.connector.connect(
        host="localhost",
        user="telefonbruker",
        password="passord",
        database="telefonkatalog"
    )
    ```

2. For å kjøre applikasjonen, gå til prosjektmappen og kjør Python-filen:

    ```bash
    python3 telefonkatalog.py
    ```

3. Programmet vil åpne en meny der du kan velge å legge til personer, søke opp personer eller telefonnumre, vise alle personer, eller avslutte.

---

## Trinn 9: Test databasekoblingen

Du kan teste om applikasjonen din er riktig koblet til databasen ved å bruke denne enkle testkoden:

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
