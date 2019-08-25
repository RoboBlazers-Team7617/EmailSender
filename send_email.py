# Initialization
MY_ADDRESS = input("Enter your email address: ")
PASSWORD = input("Enter your password: ")
NAME = input("Enter your name: ")

# Read in the file
with open('message.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('[name]', NAME)

# Write the file out again
with open('message.txt', 'w') as file:
  file.write(filedata)

# Function to read the contacts from contacts.txt and return a
# list of names and email addresses
def get_contacts(filename):
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])
    #returns two seperate arrays with all the names and emails
    return emails

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

emails = get_contacts('contacts.txt')  # read contacts
message_template = read_template('message.txt')

# Actually send email
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# For each contact, send the email:
for email in emails:
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute()

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="Robotics Team #7617 Sponsorship"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    pdfpart = MIMEApplication(open('Second Year Fundraising Plan.pdf', 'rb').read())
    pdfpart.add_header('Content-Disposition', 'attachment', filename='Second Year Fundraising Plan.pdf')
    msg.attach(pdfpart)

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
