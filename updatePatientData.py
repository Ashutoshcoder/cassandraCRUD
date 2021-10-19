"""
Author : Ashutosh Kumar
Version : 1.0
Description : Update Data for Patients
Email : ashutoshkumardbms@gmail.com
"""

from deletePatientData import *


def updateSingleData():
    try:
        session = connectToDatabase()
        print("Connected ")
        dataToBeUpdated = int(input("Enter ID to be Updated"))
        newName = input("Enter Name to be Updated")  # getting ID for data to be deleted
        query = "update p_name = " + str(newName) + " from patients where p_id = " + str(
            dataToBeUpdated) + " ;"  # Query for Deleting Data
        print(query)  # Having a look at the query being executed
        result = session.execute(query)  # Executing query
        print("Data Updated")

    except Exception as exceptions:
        print("Exception occured during Execution of the Program", exceptions)
    finally:
        print("Program Completed ! Check for results")
