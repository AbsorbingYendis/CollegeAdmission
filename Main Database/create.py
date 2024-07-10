import sqlite3

conn = sqlite3.connect("CAS_CREATE.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE User_Account (
    accountID    INTEGER   PRIMARY KEY AUTOINCREMENT
                           NOT NULL,
    emailAddress TEXT (50) NOT NULL,
    username     TEXT (50) NOT NULL,
    password     TEXT (50) NOT NULL
);
               
''')
conn.commit
cursor.execute('''CREATE TABLE User_Info (
    infoID              INTEGER    PRIMARY KEY AUTOINCREMENT
                                   NOT NULL,
    firstName           TEXT (20)  NOT NULL,
    lastName            TEXT (20)  NOT NULL,
    middleName          TEXT (20),
    suffix              TEXT (5),
    image               BLOB       NOT NULL,
    emailAddress        TEXT (100) NOT NULL,
    sex                 TEXT (10)  NOT NULL,
    civilStatus         TEXT (10)  NOT NULL,
    placeOfBirth        TEXT (30)  NOT NULL,
    birthDate           TEXT       NOT NULL,
    disability          TEXT (20)  NOT NULL,
    ethnicity           TEXT (20)  NOT NULL,
    motherTongue        TEXT (20)  NOT NULL,
    religion            TEXT (50)  NOT NULL,
    heightcm            INTEGER    NOT NULL,
    addressLine1        TEXT (50)  NOT NULL,
    weightkg            INTEGER    NOT NULL,
    addressLine2        TEXT (50),
    addressMunicipality TEXT (20)  NOT NULL,
    addressBarangay     TEXT (20)  NOT NULL,
    accountID                      REFERENCES User_Account (accountID) 
);
''')
conn.commit
cursor.execute('''CREATE TABLE School (
    schoolID      INTEGER   PRIMARY KEY AUTOINCREMENT,
    infoID        INTEGER   REFERENCES User_Info (infoID) 
                            NOT NULL,
    depedID       INTEGER,
    schoolName    TEXT (50) NOT NULL,
    yearStarted   TEXT (10) NOT NULL,
    yearGraduated TEXT (10) NOT NULL,
    gradeLevel    TEXT (10) NOT NULL
);
''')
conn.commit
cursor.execute('''CREATE TABLE Grades (
    gradeID  INTEGER   PRIMARY KEY AUTOINCREMENT
                       NOT NULL,
    schoolID INTEGER   REFERENCES School (schoolID) 
                       NOT NULL,
    grade    INTEGER   NOT NULL,
    course   TEXT (20) NOT NULL,
    semester INTEGER);
''')
conn.commit
cursor.execute('''CREATE TABLE Document (
    documentID INTEGER PRIMARY KEY AUTOINCREMENT
                       NOT NULL,
    accountID  INTEGER REFERENCES User_Account (accountID) 
                       NOT NULL,
    document   BLOB    NOT NULL,
    Type               NOT NULL
);
''')
conn.commit
cursor.execute('''CREATE TABLE Guardian_Info (
    guardianID          INTEGER PRIMARY KEY AUTOINCREMENT,
    infoID              INTEGER REFERENCES User_Info (infoID) 
                                NOT NULL,
    firstName           TEXT    NOT NULL,
    lastName            TEXT    NOT NULL,
    middleName          TEXT,
    occupacy            TEXT    NOT NULL,
    addressLine1        TEXT    NOT NULL,
    addressLine2        TEXT,
    addressMunicipality TEXT    NOT NULL,
    addressBarangay     TEXT    NOT NULL
);
''')
conn.commit
cursor.execute('''CREATE TABLE Economic_Status (
    economicID   INTEGER PRIMARY KEY AUTOINCREMENT,
    infoID       INTEGER NOT NULL
                         REFERENCES User_Info (infoID),
    incomeSource TEXT    NOT NULL,
    incomeMax    INTEGER NOT NULL,
    incomeMin    INTEGER NOT NULL
);
''')
conn.commit