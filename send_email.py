# Initialization
MY_ADDRESS = "youremail"
PASSWORD = "yourpassword"

# Function to read the contacts from contacts.txt and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    #returns two seperate arrays with all the names and emails
    return names, emails

# We also need a function to read in a template file (like message.txt)
# and return a Template object made from its contents
from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    #Returns email template object
    return Template(template_file_content)

# Set-up
# import the smtplib module. It should be included in Python by default
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

names, emails = get_contacts('contacts.txt')  # read contacts
message_template = read_template('message.txt')

# Actually send email
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="Robotics Team #7617 Sponsorship"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
