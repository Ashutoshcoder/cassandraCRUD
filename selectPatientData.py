"""
Author : Ashutosh Kumar
Version : 1.0
Description : To Show Patient Data
Email : ashutoshkumardbms@gmail.com
"""

from cassandra.query import SimpleStatement
from cassandra.cluster import Cluster
from deletePatientData import *


def showSingleData():
    try:
        session = connectToDatabase()
        print("Connected ")
        dataToBeDeleted = int(input("Enter ID number to be selected"))  # getting ID for data to be deleted
        query = "select * from patients where p_id = " + str(dataToBeDeleted) + " ;"  # Query for Deleting Data
        print(query)  # Having a look at the query being executed
        result = session.execute(query)  # Executing query
        print("Name ", result.p_name, "Age", result.p_age)

    except Exception as exceptions:
        print("Exception occured during Execution of the Program", exceptions)
    finally:
        print("Program Completed ! Check for results")


def selectAllData():
    try:
        session = connectToDatabase()
        query = "select * from patients;"
        hugeResult = session.execute(query)
        for rows in hugeResult:
            eachPatient=[]
            eachPatient.append(rows.p_id)
            eachPatient.append(rows.p_name)
            eachPatient.append(rows.p_age)
            file1 = open("outputFile.txt", "a+")
            print(eachPatient)
            file1.write(str(eachPatient)+"\n")

    except Exception as exceptions:
        print("Exception occured during Execution of the Program", exceptions)
    finally:
        print("Program Completed ! Check for results")
