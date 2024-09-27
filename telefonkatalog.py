
import mysql.connector

def printMeny():
    print("------------------- Telefonkatalog -------------------")
    print("| 1. Legg til ny person                              |")
    print("| 2. Søk opp person eller telefonnummer              |")
    print("| 3. Vis alle personer                               |")
    print("| 4. Avslutt                                         |")
    print("------------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge fra menyen:")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall):
    if(valgtTall == "1"):
        registrerPerson()
    elif(valgtTall == "2"):
        sokPerson()
        printMeny()
    elif(valgtTall == "3"):
        visAllePersoner()
    elif(valgtTall == "4"):
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N")
        if(bekreftelse == "J" or bekreftelse == "j"):
            exit()
        else:
            printMeny()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-4.")
        utfoerMenyvalg(nyttForsoek)

def registrerPerson():
    fornavn = input("Skriv inn fornavn:")
    etternavn = input("Skriv inn etternavn:")
    telefonnummer = input("Skriv inn telefonnummer:")

    lagreIDatabase(fornavn, etternavn, telefonnummer)
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

def visAllePersoner():
    mydb = mysql.connector.connect(
        host="localhost",  # replace with actual host if needed
        user="telefonbruker",  # replace with actual user
        password="passord",  # replace with actual password
        database="telefonkatalog"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM person")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()
    printMeny()

def sokPerson():
    print("1. Søk på fornavn")
    print("2. Søk på etternavn")
    print("3. Søk på telefonnummer")
    print("4. Tilbake til hovedmeny")
    sokefelt = input("Skriv inn ønsket søk 1-3, eller 4 for å gå tilbake:")
    if(sokefelt == "1"):
        navn = input("Fornavn:")
        finnPerson("fornavn", navn)
    elif(sokefelt == "2"):
        navn = input("Etternavn:")
        finnPerson("etternavn", navn)
    elif(sokefelt == "3"):
        tlfnummer = input("Telefonnummer:")
        finnPerson("telefonnummer", tlfnummer)
    elif(sokefelt == "4"):
        printMeny()
    else:
        print("Ugyldig valg. Velg et tall mellom 1-4.")
        sokPerson()

def finnPerson(typeSok, sokeTekst):
    mydb = mysql.connector.connect(
        host="localhost",  # replace with actual host if needed
        user="telefonbruker",  # replace with actual user
        password="passord",  # replace with actual password
        database="telefonkatalog"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM person WHERE " + typeSok + " = '" + sokeTekst + "'")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()

def lagreIDatabase(fornavn, etternavn, telefonnummer):
    mydb = mysql.connector.connect(
        host="localhost",  # replace with actual host if needed
        user="telefonbruker",  # replace with actual user
        password="passord",  # replace with actual password
        database="telefonkatalog"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO person (fornavn, etternavn, telefonnummer) VALUES (%s, %s, %s)"
    val = (fornavn, etternavn, telefonnummer)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

# Test connection script
def test_connection():
    mydb = mysql.connector.connect(
        host="localhost",  # replace with actual host if needed
        user="telefonbruker",  # replace with actual user
        password="passord",  # replace with actual password
        database="telefonkatalog"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM person")
    resultater = cursor.fetchall()

    for dings in resultater:
        print(dings)

# Run the program
printMeny()  # Starts the program by displaying the menu for the first time
