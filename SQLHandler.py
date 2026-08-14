import mysql.connector
import sys

# Database information.
# /// ------------------------- IMPORTANT: CHANGE THE VARIABLES BELOW TO YOUR OWN DATABASE IN ORDER TO RUN THIS PROGRAM!!! ------------------------- \\\
SQLDatabaseConnection = None
databaseHostName = ""
databaseUsername = ""
databasePassword = ""
databaseName = ""
# // ------------------------------------------------------------------------------------------------------------------------------------------------ \\\

# Initializes the database connection.
def initializeDatabaseConnection():

      global SQLDatabaseConnection
      global databaseHostName
      global databaseUsername
      global databasePassword
      global databaseName

    # Exits if the connection already exists.
      if(SQLDatabaseConnection != None): return

      # Database connection.
      try:

                SQLDatabaseConnection = mysql.connector.connect(

                    #SQL Database information
                    host = databaseHostName,
                              username = databaseUsername,
                              password = databasePassword,
                              database = databaseName,
                              autocommit = True

                )

      except mysql.connector.Error as err:

                print(f"\nCould not connect to database. Error message: {err}")
                print("Did you put the correct information for the database variables?\n")
                sys.exit()

  # Function to run a provided SQL command. Returns ONE or ALL rows depending on "returnOneLine".
  def executeSQLQuery(SQLCommand: str, returnOneLine: bool, *SQLQueryArgs):

        global SQLDatabaseConnection

    # Initializes database connection if it wasn't already.
        if(SQLDatabaseConnection == None): initializeDatabaseConnection()

        # Creates cursor and runs the command.
        DBCursor = SQLDatabaseConnection.cursor()
        DBCursor.execute(SQLCommand, (*SQLQueryArgs,))

    # Checks whether to return one or all rows.
        if(returnOneLine):

                  returnedData = DBCursor.fetchone()
                  DBCursor.close()

            return returnedData

else:

        returnedData = DBCursor.fetchall()
        DBCursor.close()

        return returnedData
