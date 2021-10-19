"""
Author : Ashutosh Kumar
Version : 1.0
Description : Delete Patient Data from Cassandra
Email : ashutoshkumardbms@gmail.com
"""

from cassandra.query import SimpleStatement
from cassandra.cluster import Cluster

def connectToDatabase():
    try:
        # Connecting with Cassandra
        cluster = Cluster()
        # health_sector is name of the keyspace, in this case the database
        session = cluster.connect('health_sector')
        return session
    except Exception as exceptions:
        print("Exception Occured", exceptions)


def deleteSingleData():
    try:
        session = connectToDatabase()
        print("Connected ")
        dataToBeDeleted = int(input("Enter ID number to be deleted"))  # getting ID for data to be deleted
        query = "DELETE FROM patients where p_id = " + str(dataToBeDeleted) + " ;"  # Query for Deleting Data
        print(query)  # Having a look at the query being executed
        session.execute(query)  # Executing query

    except Exception as exceptions:
        print("Exception occured during Execution of the Program", exceptions)
    finally:
        print("Program Completed ! Check for results")


def deleteAllData():
    try:
        session = connectToDatabase()
        query = "truncate patients;"
        session.execute(query)
    except Exception as exceptions:
        print("Exception occured during Execution of the Program", exceptions)
    finally:
        print("Program Completed ! Check for results")
