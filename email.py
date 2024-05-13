# Creating a class Email
class Email: 

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Initializing has_been_read to default False
# Creating a class inbox 
class Inbox:
    # Initialise an empty list to store the email objects.
    def __init__(self):
        self.inbox = []

    '''Creating a function to create email objects with the email address, 
    subject_line and email_content and store them in the inbox list '''
    def populate_inbox(self, email_address, subject_line, email_content):
        new_email = Email(email_address, subject_line, email_content)
        self.inbox.append(new_email)

    ''' Creating a function to loop through the emails and 
    print each email subject_line with corresponding number'''
    def list_emails(self):
        for i, email in enumerate(self.inbox):
            print(f"{i+1}. {email.subject_line}")

    ''' Creating a function to display selected emails 
        together with the email address, subject_line and email_contents'''
    def read_email(self, index):
        if index < 1 or index > len(self.inbox):
            print("Invalid email index.")
            return
        email = self.inbox[index - 1]
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.has_been_read = True  

# Example usage:
inbox = Inbox()
# Creating email object samples
inbox.populate_inbox("hyperion@gmail.com", "Welcome to HyperionDev", "You are officially welcome")
inbox.populate_inbox("hyperiondev@gmail.com", "You are doing great", "This is to inform you of your progress")
inbox.populate_inbox("hyperioninfo@gmail.com", "Congratulations", "Your certificate is ready")

inbox.list_emails()

menu = True
# Creating a loop to ask user for the program they want to perform
while menu:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # Read an email
        index_to_read = int(input("Enter the index of the email you want to read: "))
        inbox.read_email(index_to_read)
            
    elif user_choice == 2:
        # View unread emails
        unread_emails = [email for email in inbox.inbox if not email.has_been_read]
        if not unread_emails:
            print("You have no unread emails.")
        else:
            print("Unread emails:")
            for i, email in enumerate(unread_emails):
                print(f"{i+1}. {email.subject_line}")
    
    elif user_choice == 3:
        # Quit application
        menu = False
        print("Exiting application...")
        break

    else:
        print("Oops - incorrect input.")
