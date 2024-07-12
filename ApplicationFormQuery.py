import sqlite3 

# Connect to the database
conn = sqlite3.connect('Database/CAS.db')
cursor = conn.cursor()
print("input id")
id = 23
# Query the database for the entered email and password
cursor.execute('''
SELECT
    User_Info.infoID,
    User_Info.accountID,
    Economic_Status.economicID,
    Grades.gradeID,
    Guardian_Info.guardianID,
    School.schoolID
FROM
    User_Info
    INNER JOIN Economic_Status ON User_Info.infoID = Economic_Status.infoID
    INNER JOIN School ON User_Info.infoID = School.infoID
    INNER JOIN Guardian_Info ON Guardian_Info.infoID = User_Info.infoID
    INNER JOIN Grades ON User_Info.accountID = Grades.accountID
WHERE
    User_Info.accountID = ?
''',(23,)
)

user = cursor.fetchone()
print(user)


# Close the connection
conn.close()
