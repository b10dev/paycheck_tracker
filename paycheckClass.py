import mysql.connector


class PayCheck(object):
    # Opening DB and Defining the cursor
    cnx = mysql.connector.connect(user='b10', password='li27co07', host='127.0.0.1', database='paychecks')
    cursor = cnx.cursor()
    # Common sql commands
    insert_command_select_all_from_table = "SELECT * FROM paycheck"

    def __init__(self, date, gross, our_cut, workers_comp, misc, total, hometime, notes):
        self.date = date
        self.gross = gross
        self.our_cut = our_cut
        self.workers_comp = workers_comp
        self.misc = misc
        self.total = total
        self.hometime = hometime
        self.notes = notes
        self.id = id

    # repr for debug and conformation.
    # @property
    def __repr__(self):
        return "Date {} : Gross ${} Our Cut ${} WA ${} Misc ${} Total ${} Hometime ? {} Notes : {}".format(
            self.date,
            self.gross,
            self.our_cut,
            self.workers_comp,
            self.misc,
            self.total,
            self.hometime,
            self.notes)

    # Close the cursor and DB when exiting the program.
    @classmethod
    def close_cursor(cls):
        PayCheck.cursor.close()
        PayCheck.cnx.close()

    # Commit the cursor after any command
    @classmethod
    def commit_cursor(cls):
        PayCheck.cnx.commit()

    # Make a simple query
    @classmethod
    def simple_query(cls, x):
        insert_command = x
        PayCheck.cursor.execute(insert_command)
        PayCheck.commit_cursor()

    # Format the output of querys
    @classmethod
    def paycheck_summary(cls, insert_command):
        PayCheck.cursor.execute(insert_command)
        paycheck_history = PayCheck.cursor.fetchall()
        print("The total number of paychecks are : ", PayCheck.cursor.rowcount)
        print("____________________________________________\n")
        for i in paycheck_history:
            print("|ID :     ", i[8])
            print("|Date :   ", i[0])
            print("|Gross :  ", i[1])
            print("|40% :    ", i[2])
            print("|WA :     ", i[3])
            print("|Misc :   ", i[4])
            print("|Total :  ", i[5])
            print("________________________\n")

    # UI for paycheck constructor.
    @classmethod
    def new_paycheck(cls):
        # Take input for the constructor.
        date = input("Enter the date yyyy-mm-dd : ")
        gross = input("Enter the gross '0.00' : ")
        our_cut = input("Enter the 43% '0.00' : ")
        workers_comp = input("Enter the WA '0.00' :  ")
        misc = input("Enter any misc charges '0.00' : ")
        total = input("Enter the total '0.00' : ")
        hometime = input("Was this a hometime week? 0 = no, 1 = yes : ")
        notes = input("Enter any Notes, up to 300 char : ")
        # Populate paycheck instance.
        paycheck = PayCheck(date, gross, our_cut, workers_comp, misc, total, hometime, notes)
        # Call repr for conformation.
        print("\n" + str(paycheck))
        confirm = input("\nInsert this new paycheck?\n0 = Yes\n1 = Reenter\n2 = Return to Main Menu:\n ")
        if confirm == "0":
            try:
                insert_command = """INSERT INTO paycheck(date, gross, our_cut,
                                    workers_comp, misc, total, hometime, notes)
                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
                insert_values = [paycheck.date, paycheck.gross, paycheck.our_cut,
                                 paycheck.workers_comp, paycheck.misc, paycheck.total, paycheck.hometime,
                                 paycheck.notes]
                PayCheck.cursor.execute(insert_command, insert_values)
                PayCheck.commit_cursor()
                print("\nPaycheck entered successfully!!!")
            except mysql.connector.errors.DataError:
                print("\nPlease enter data with appropriate format\nDate YYYY-MM-DD\nNumeric Values 0.00\n")
                PayCheck.new_paycheck()
            except mysql.connector.errors.DatabaseError:
                print("Database error, Please try again.")
                PayCheck.new_paycheck()
        elif confirm == "1":
            PayCheck.new_paycheck()
        else:
            pass

    # Query for viewing all paychecks
    @classmethod
    def view_paycheck_history(cls):
        PayCheck.paycheck_summary(PayCheck.insert_command_select_all_from_table)

    # Query for viewing paychecks by month
    @classmethod
    def view_paycheck_by_month(cls):
        month = input("Enter the two digit month to filter paychecks by month: ")
        insert_command = "select * from paycheck where date like '%2019-" + month + "%';"
        PayCheck.paycheck_summary(insert_command)

    @classmethod
    def delete_paycheck(cls):
        insert_command = "SELECT * FROM paycheck"
        PayCheck.paycheck_summary(insert_command)
        entry_to_delete = input("Enter an id to delete the entry: ")
        try:
            commands = "DELETE FROM paycheck WHERE id=" + entry_to_delete + ";"
            PayCheck.simple_query(commands)
            insert_command = "SELECT * FROM paycheck"
            PayCheck.paycheck_summary(insert_command)
            PayCheck.commit_cursor()
        # Bare exception used for the time being.
        except:
            print("Unknown Error")
            PayCheck.start_of_program()

    @classmethod
    def get_totals(cls):
        x = 0
        while x <= 0:
            interface_choices = ["1 : Year to date Totals ",
                                 "2 : Year to date Averages",
                                 "3 : Monthly Totals",
                                 "4 : Monthly Averages",
                                 "9 : Quit"]
            for i in interface_choices:
                print(i)
            start_of_choices = input("\nPlease make a selection, and press Enter: \n")
            if start_of_choices == "1":
                insert_command = "select round(sum(gross),2), round(sum(our_cut),2), " \
                                 "round(sum(total),2) from paycheck where date like '%2019%';"
                PayCheck.cursor.execute(insert_command)
                db_response = PayCheck.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross total : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("Total deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
            if start_of_choices == "2":
                insert_command = "select round(avg(gross),2), round(avg(our_cut),2), " \
                                 "round(avg(total),2) from paycheck where date like '%2019%';"
                PayCheck.cursor.execute(insert_command)
                db_response = PayCheck.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross total : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("Total deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
            if start_of_choices == "3":
                month = input("Enter the two digit month to filter paychecks by month: ")
                insert_command = "select round(sum(gross),2), round(sum(our_cut),2), " \
                                 "round(sum(total),2) from paycheck where date like '%2019-" + month + "%';"
                PayCheck.cursor.execute(insert_command)
                db_response = PayCheck.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross total : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("Total deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
                    pass
            if start_of_choices == "4":
                month = input("Enter the two digit month to filter paychecks by month: ")
                insert_command = "select round(avg(gross),2), round(avg(our_cut),2), " \
                                 "round(avg(total),2) from paycheck where date like '%2019-" + month + "%';"
                PayCheck.cursor.execute(insert_command)
                db_response = PayCheck.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross AVG : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("AVG deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
                    pass
            if start_of_choices == "9":
                x = 1

    @classmethod
    def start_of_program(cls):
        x = 0
        while x <= 0:
            print("---------------------Main Menu---------------------\n")
            interface_choices = ["1 : Enter a New Paycheck ",
                                 "2 : View all Paychecks ",
                                 "3 : View Paychecks by month",
                                 "4 : Delete entry",
                                 "5 : Totals",
                                 # "8 : Testing",
                                 "9 : Quit"]
            for i in interface_choices:
                print(i)
            start_of_choices = input("\nPlease make a selection, and press Enter: \n")
            if start_of_choices == "1":
                PayCheck.new_paycheck()
            if start_of_choices == "2":
                PayCheck.view_paycheck_history()
            if start_of_choices == "3":
                PayCheck.view_paycheck_by_month()
            if start_of_choices == "4":
                PayCheck.delete_paycheck()
            if start_of_choices == "5":
                PayCheck.get_totals()
            # Uncomment for testing and adding a new module.
            '''    
            if start_of_choices == "8":
                pass
            '''
            if start_of_choices == "9":
                x = 1
                PayCheck.close_cursor()
                print("Goodbye")
