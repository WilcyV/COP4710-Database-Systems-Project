import customtkinter
import tkcalendar
import datetime
import calendar
import main

# Main background screen
mainWindow = customtkinter.CTk()
mainWindow.geometry("500x500")
mainWindow.title("Appointment Booking Login")
mainWindow.resizable(False, False)

# Transitions login screen to booking screen.
def updateToBookingScreen(QueryResult):

      def submitAppointment():

                # Stores date, staff name, location name, and service name.
                appointmentDate = dateCalendarBox.get_date()
                appointmentStaff = staffSelectionDropdown.get()
                appointmentLocation = locationSelectionDropdown.get()
                appointmentService = serviceSelectionDropdown.get()

        # Uses the previous variables set to grab each variable's respective ID from their dictionary in the main file to pass into the "insertIntoBooking" function. Updates upcoming appointments afterwards.
                result = main.insertIntoBooking(appointmentDate, personID, main.listOfServices[appointmentService]["ServiceID"], main.listOfLocations[appointmentLocation]["LocationID"], main.listOfStaff[appointmentStaff]["StaffID"])

        # Displays a prompt showing the booking was successful or unsuccessful. Hides text after 2.5 seconds.
                if(result != None):

                              appointmentBookedTxtLabel.configure(text = "Staff already booked for this day.", text_color = "Red")

else:

            populateUpcomingAppointments()
              appointmentBookedTxtLabel.configure(text = "Appointment successfully booked!", text_color = "Green")

        appointmentBookedTxtLabel.after(2500, lambda: appointmentBookedTxtLabel.configure(text = ""))

    def clearUpcomingAppointmentsWidgets():

              # Loops through all children in the upcoming appointments frame and destroys them.
              for appointment in (upcomingAppointmentsScrollFrame.winfo_children()):

                            appointment.destroy()

          def populateUpcomingAppointments():

                    # Clears upcoming appointments.
                    clearUpcomingAppointmentsWidgets()

        # All rows of a specific person from "Booking".
        dataReturned = main.upcomingAppointments(personID)

        # Loops through all rows from "Booking" and creates small windows for each. Displays information such as appointment date, appointment staff, appointment location, and appointment service.
        for appointment in (dataReturned):

                      appointmentDate = str(appointment[1])
                      appointmentDate = f"{calendar.month_name[int(appointmentDate[5:7])]} {appointmentDate[8:10]}, {appointmentDate[0:4]}"

            appointmentStaffName = appointment[3]
            appointmentAddress = appointment[5]
            appointmentLocation = appointment[6]
            appointmentService = appointment[7]

            upcomingAppointment = customtkinter.CTkFrame(master = upcomingAppointmentsScrollFrame, height = 150)
            upcomingAppointment.pack(fill = "x", padx = 10, pady = 10)

            labelOne = customtkinter.CTkLabel(master = upcomingAppointment, text = f"{appointmentDate}", font = ("Times New Roman", 40, "bold"))
            labelTwo = customtkinter.CTkLabel(master = upcomingAppointment, text = f"Staff name: {appointmentStaffName}", font = ("Times New Roman", 18))
            labelThree = customtkinter.CTkLabel(master = upcomingAppointment, text = f"Location: {appointmentLocation} ({appointmentAddress})", font = ("Times New Roman", 18))
            labelFour = customtkinter.CTkLabel(master = upcomingAppointment, text = f"Service: {appointmentService}", font = ("Times New Roman", 18))

            labelOne.pack(padx = 10, pady = 10)
            labelTwo.pack(padx = 10, pady = 10)
            labelThree.pack(padx = 10, pady = 10)
            labelFour.pack(padx = 10, pady = 10)

    # "QueryResult" contains row information from the "Person" table tied to the login account.
    personID = QueryResult
    personName = "N/A"

    personName = main.getPersonName(personID)

    # Remove old window and create new ones for booking screen
    for childWindow in (mainWindow.winfo_children()):

              childWindow.destroy()

    # New window variable
    mainWindow.geometry("1280x1000")
    mainWindow.title("Appointment Booking Window")
    mainWindow.grid_columnconfigure(1, weight = 1)
    mainWindow.grid_rowconfigure(0, weight = 1)

    # Upcoming appointments setup (left side)
    upcomingAppointmentsFrame = customtkinter.CTkFrame(master = mainWindow, width = 400)
    upcomingAppointmentsFrame.pack(side = "left", fill = "y", padx = 10, pady = 10)

    upcomingAppointmentsTxtLabel = customtkinter.CTkLabel(master = upcomingAppointmentsFrame, text = "Upcoming Appointments", font = ("Times New Roman", 30, "bold"))
    upcomingAppointmentsTxtLabel.pack(pady = 10, padx = 10)

    upcomingAppointmentsScrollFrame = customtkinter.CTkScrollableFrame(master = upcomingAppointmentsFrame, width = 400, corner_radius = 0)
    upcomingAppointmentsScrollFrame.pack(side = "left", fill = "y", padx = 10, pady = 10)

    # Appointments setup (right side)
    appointmentBookingFrame = customtkinter.CTkFrame(master = mainWindow)
    appointmentBookingFrame.pack(side = "right", fill = "both", expand = True, padx = 10, pady = 10)
    appointmentBookingFrame.grid_columnconfigure(1, weight = 1)
    appointmentBookingFrame.grid_rowconfigure(0, weight = 1)

    appointmentBookingTxtLabel = customtkinter.CTkLabel(master = appointmentBookingFrame, text = f"Welcome, {personName}!", font = ("Times New Roman", 40, "bold"))
    appointmentBookingTxtLabel.pack(padx = 10, pady = 10)

    appointmentBookingOptionsFrame = customtkinter.CTkFrame(master = appointmentBookingFrame, border_width = 2)
    appointmentBookingOptionsFrame.pack(fill = "both", expand = True, padx = 50, pady = 5)
    appointmentBookingOptionsFrame.grid_columnconfigure(1, weight = 1)
    appointmentBookingOptionsFrame.grid_rowconfigure(0, weight = 1)

    bookNewAppointmentTxtLabel = customtkinter.CTkLabel(master = appointmentBookingOptionsFrame, text = "Book a new appointment?", font = ("Times New Roman", 30))
    bookNewAppointmentTxtLabel.pack(padx = 10, pady = 10)

    # Setup for date selection
    dateRowFrame = customtkinter.CTkFrame(master = appointmentBookingOptionsFrame, fg_color = "transparent", height = 150)
    dateRowFrame.pack(fill = "x", padx = 5, pady = 40)

    dateTxtLabel = customtkinter.CTkLabel(master = dateRowFrame, text = "Date:", font = ("Times New Roman", 40))
    dateTxtLabel.pack(side = "left", padx = 5, pady = 5)

    dateCalendarBox = tkcalendar.Calendar(master = dateRowFrame, height = 100, date_pattern="yyyy-mm-dd", mindate = datetime.date.today(), weekendbackground = "white", weekendforeground = "black", normalbackground = "white", normalforeground = "black")
    dateCalendarBox.pack(side = "right", padx = 5, pady = 5)

    # Setup for staff selection
    staffSelectionRowFrame = customtkinter.CTkFrame(master = appointmentBookingOptionsFrame, fg_color = "transparent", height = 150)
    staffSelectionRowFrame.pack(fill = "x", padx = 5, pady = 40)

    staffSelectionTxtLabel = customtkinter.CTkLabel(master = staffSelectionRowFrame, text = "Staff for Service:", font = ("Times New Roman", 40))
    staffSelectionTxtLabel.pack(side = "left", padx = 5, pady = 5)

    staffSelectionDropdown = customtkinter.CTkOptionMenu(master = staffSelectionRowFrame, values = list(main.listOfStaff.keys()))
    staffSelectionDropdown.pack(side = "right", padx = 5, pady = 5)

    # Setup for location selection
    locationSelectionRowFrame = customtkinter.CTkFrame(master = appointmentBookingOptionsFrame, fg_color = "transparent", height = 150)
    locationSelectionRowFrame.pack(fill = "x", padx = 5, pady = 40)

    locationSelectionTxtLabel = customtkinter.CTkLabel(master = locationSelectionRowFrame, text = "Location:", font = ("Times New Roman", 40))
    locationSelectionTxtLabel.pack(side = "left", padx = 5, pady = 5)

    locationSelectionDropdown = customtkinter.CTkOptionMenu(master = locationSelectionRowFrame, values = list(main.listOfLocations.keys()))
    locationSelectionDropdown.pack(side = "right", padx = 5, pady = 5)

    # Setup for service
    serviceSelectionRowFrame = customtkinter.CTkFrame(master = appointmentBookingOptionsFrame, fg_color = "transparent", height = 150)
    serviceSelectionRowFrame.pack(fill = "x", padx = 5, pady = 40)

    serviceSelectionTxtLabel = customtkinter.CTkLabel(master = serviceSelectionRowFrame, text = "Service:", font = ("Times New Roman", 40))
    serviceSelectionTxtLabel.pack(side = "left", padx = 5, pady = 5)

    serviceSelectionDropdown = customtkinter.CTkOptionMenu(master = serviceSelectionRowFrame, values = list(main.listOfServices.keys()))
    serviceSelectionDropdown.pack(side = "right", padx = 5, pady = 5)

    # Submit button
    submitAppointmentButtonFrame = customtkinter.CTkFrame(master = appointmentBookingOptionsFrame, fg_color = "transparent", height = 150)
    submitAppointmentButtonFrame.pack(fill = "x", padx = 5, pady = 5)

    submitAppointmentButton = customtkinter.CTkButton(master = submitAppointmentButtonFrame, text = "SUBMIT", width = 250, command = submitAppointment, font = ("Times New Roman", 20))
    submitAppointmentButton.pack(fill = "y", padx = 5, pady = 5)

    # Notification text below the submit button to display successful booking. An empty string is passed in order to make it invisible.
    appointmentBookedTxtLabel = customtkinter.CTkLabel(master = appointmentBookingFrame, text = "", font = ("Times New Roman", 20), text_color = "Green")
    appointmentBookedTxtLabel.pack(padx = 10, pady = 20)

    # Gets and displays upcoming appointments.
    populateUpcomingAppointments()

# Setup for the login screen
def initializeLoginScreen():

      # Event function for when the login button is clicked.
      def loginButtonEvent():

                # Grabs string input in the input boxes for the username and password.
                providedUsername = usernameEntry.get()
                providedPassword = passwordEntry.get()

        # Returns the "person_id" column of an account, if one was found with the given username and password.
                result = main.userLogin(providedUsername, providedPassword)

        # If "result" has something, then there exists an account with the provided username and password in the database.
        if(result != None):

                      # Shows the successful login text to user. Waits a while before closing the main window.
                      loginSuccessOrErrorTxtLabel.configure(text = "Successfully logged in! Logging in..", text_color = "Green")

            mainWindow.after(500, updateToBookingScreen, result[0])

else:

            # User provided invalid login details; no account exists with the given username and password.
              loginSuccessOrErrorTxtLabel.configure(text = "Invalid login.", text_color = "Red")

    # Main frame
    windowFrame = customtkinter.CTkFrame(master = mainWindow)
    windowFrame.pack(pady = 20, padx = 60, fill = "both", expand = True)

    # Frame to center all buttons/labels
    windowFrameTwo = customtkinter.CTkFrame(master = windowFrame, fg_color = "transparent")
    windowFrameTwo.pack(expand = True)

    # Login label
    loginTxtLabel = customtkinter.CTkLabel(master = windowFrameTwo, text = "Login", font = ("Times New Roman", 50))
    loginTxtLabel.pack(pady = 12, padx = 10)

    # Username text entry
    usernameEntry = customtkinter.CTkEntry(master = windowFrameTwo, placeholder_text = "Username", width = 200, height = 30)
    usernameEntry.pack(pady = 12, padx = 10)

    # Password text entry
    passwordEntry = customtkinter.CTkEntry(master = windowFrameTwo, placeholder_text = "Password", show="*", width = 200, height = 30)
    passwordEntry.pack(pady = 12, padx = 10)

    # Login button
    loginButtonLabel = customtkinter.CTkButton(master = windowFrameTwo, text = "Login", command = loginButtonEvent)
    loginButtonLabel.pack(pady = 12, padx = 10)

    # Invisible text to indicate a successful or unsuccessful login through text and color.
    loginSuccessOrErrorTxtLabel = customtkinter.CTkLabel(master = windowFrameTwo, text = "", font = ("Times new Roman", 16), text_color = "Red")
    loginSuccessOrErrorTxtLabel.pack(pady = 12, padx = 10)

    mainWindow.mainloop()

initializeLoginScreen()
