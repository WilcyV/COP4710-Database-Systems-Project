import SQLHandler

# Dictionaries used to hold all the information for staff, locations, and services. Keys are the names of each, while the value is the rest of the information.
listOfStaff = {}
listOfLocations = {}
listOfServices = {}

# Querying the database to check if the provided username and password exists in the "Booking_Account" table.
def userLogin(username, password):

      return SQLHandler.executeSQLQuery("SELECT person_id FROM Booking_Account WHERE accountUsername = %s AND accountPassword = %s;", True, username, password)

# Return's a user's full name to display on the appointment screen.
def getPersonName(personID):

      personName = SQLHandler.executeSQLQuery("SELECT * FROM Person WHERE person_id = %s;", True, personID)
      return personName[1] + " " + personName[2]

# Returns all rows of a specific user's bookings to display on the upcoming appointments screen.
def upcomingAppointments(personID):

      return SQLHandler.executeSQLQuery("SELECT * FROM listUpcomingAppointments WHERE person_id = %s ORDER BY BookingDate ASC;", False, personID)

# Handles data insertion into database.
def insertIntoBooking(appointmentDate, personID, serviceID, locationID, staffID):

      try:

                SQLHandler.executeSQLQuery("INSERT INTO Booking(BookingDate, person_id, ServiceID, location_id, StaffID) VALUES(%s, %s, %s, %s, %s);", True, appointmentDate, personID, serviceID, locationID, staffID)

      except Exception as err:

                return str(err)

  # Sets up the "listOfStaff", "listOfLocations", and "listOfServices" dictionaries in order to make it much more easily accessible for the UI.
  try:

        # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Querying database and storing each staff's respective information in a dictionary.
        dataReturned = SQLHandler.executeSQLQuery("SELECT * FROM Staff", False)

    for dataRow in (dataReturned):

              staffName = None

        dataReturned = SQLHandler.executeSQLQuery("SELECT * FROM Person WHERE person_id = %s;", True, dataRow[2])
        staffName = dataReturned[1] + " " + dataReturned[2]

        listOfStaff[staffName] = {

            "YearsOfExperience": dataRow[1],
                      "StaffID": dataRow[0],
                      "PersonID": dataRow[2],

        }

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Querying database and storing each location's respective information in a dictionary.
    dataReturned = SQLHandler.executeSQLQuery("SELECT * FROM Location;", False)

    for dataRow in (dataReturned):

              listOfLocations[dataRow[2]] = {

                  "LocationID": dataRow[0],
                            "State": dataRow[3],
                            "PostalCode": dataRow[4],
                            "Address": dataRow[1]

              }

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Querying database and storing each service's respective information in a dictionary.
    dataReturned = SQLHandler.executeSQLQuery("SELECT * FROM Service;", False)

    for dataRow in (dataReturned):

              listOfServices[dataRow[1]] = {

                  "ServiceID": dataRow[0],
                            "ServiceDurationInSeconds": dataRow[2]

              }

except Exception as err:

    print(f"Error: {err}")
