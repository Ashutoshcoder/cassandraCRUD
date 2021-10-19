"""
Author : Ashutosh Kumar
Version : 1.1
Description : Insert Patient Data Using Python
Email : ashutoshkumardbms@gmail.com
"""


def insertBulkData():
    try:

        # The secrets module is used for generating cryptographically strong random numbers suitable for,
        # managing data such as passwords, account authentication, security tokens, and related secrets.
        import secrets

        # This module implements pseudo-random number generators for various distributions.
        # Python offers a function that can generate random numbers from a specified range
        # and also allowing rooms for steps to be included, called randrange() in random module.
        from random import randrange

        # This module holds classes for working with prepared statements and
        # specifying consistency levels and retry policies for individual
        # queries.

        from cassandra.query import SimpleStatement

        # The main class to use when interacting with a Cassandra cluster. Typically,
        # one instance of this class will be created for each separate Cassandra cluster
        # that your application interacts with

        from cassandra.cluster import Cluster

        # Faker is a Python package that generates fake data for you.
        # Whether you need to bootstrap your database, create good-looking XML documents,
        # fill-in your persistence to stress test it, or anonymize data taken from a production service,
        # Faker is for you.

        from faker import Faker

        # Connecting with Cassandra
        cluster = Cluster()

        # health_sector is name of the keyspace, in this case the database
        session = cluster.connect('health_sector')
        print("Connected ")

        # Faker module for Fake Data Generation
        fake = Faker()

        # List of Hospital Names
        hospitals = ['Hospital A', 'Hospital B', "Hospital C", 'Hospital AA', 'Hospital BB', "Hospital CC"]
        hospitals = ['A', 'B', "C", 'AA', 'BB', "CC"]

        # creating a prepaid statement
        queryForPatient = SimpleStatement(
            "INSERT INTO patients(p_id,p_name,p_age,p_gender,p_admission_date,p_discharge_date,p_disease,p_treatment,p_hospital_name)"
            " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")

        # List of diseases noted in the Hospital
        diseases = ["Autoimmune Diseases", "Allergies & Asthma", "COVID-19", "Cancer", "Celiac Disease",
                    "Crohn's & Colitis",
                    "Heart Disease", "Infectious Diseases", "Liver Disease", "Lupus", "Multiple Sclerosis",
                    "Relapsing Polychondritis", "Rheumatoid Arthritis", "Scleroderma", "Type 1 Diabetes"]

        # List of treatments noted in the Hospital
        treatments = ["Back surgery (spinal surgery)", "Bad breath", "Baker's cyst", "Balloon kyphoplasty",
                      "Balloon sinuplasty for chronic sinusitis", "Bariatric surgery", "Barium enema",
                      "Barium swallow and barium meal", "Benign prostate treatments", "Birthmarks",
                      "Bladder cancer", "Bladder investigations(cystoscopy)", "Bladder lesion removal",
                      "Blood clot or thrombosis test", "Blood disorder test", "heart disease risk (cardiac testing)",
                      "Blood type or blood group test", "Blurred vision", "Body Movement Therapy", "Bone density scan",
                      "Cancer investigations and treatments", "Cancer tests", "Capsule endoscopy",
                      "Cardiac catheterisation",
                      "Cardiac CT scan (heart CT)", "Cardiac electrophysiology", "Cardiac MRI scan (heart MRI)",
                      "Cardiomemo recording",
                      ]

        # List of Gender
        gender = ['Male', 'Female', 'Other']

        '''
        Following few lines of code is to generate the dates for admission and discharge of patients 
        This will give discharge dates which is greater than admit dates 
        '''

        from random import randrange

        def random_date(start, end):
            """
            This function will return a random datetime between two datetime
            objects.
            """
            delta = end - start
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = randrange(int_delta)
            return start + timedelta(seconds=random_second)

        """
        Taking a date and time range for admit date and discharge date
        """
        from datetime import datetime, timedelta

        d1 = datetime.strptime('10/10/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('10/31/2021 11:59 PM', '%m/%d/%Y %I:%M %p')

        # For Number of records
        for counter in range(1, 5001):

            # generating Dates
            admitDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")
            dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

            # Discharge Date Should always be ahead of admit date so this loop
            while dischargeDate < admitDate:
                dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

            # insert statement for records
            session.execute(queryForPatient, (counter, fake.name(), randrange(20, 100), secrets.choice(gender),
                                              admitDate, dischargeDate, secrets.choice(diseases),
                                              secrets.choice(treatments), secrets.choice(hospitals)))

    except Exception as exceptions:
        print("Exception occured during Execution of the Program", exceptions)
    finally:
        print("Program Completed ! Check for results")
