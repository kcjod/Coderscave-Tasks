import smtplib
import csv

def send_email(sender_email, sender_password, email, receivers):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, sender_password)
    print("Logged in Successful into", sender_email)
    for receiver in receivers:
        server.sendmail(sender_email, receiver, email)
        print("Message sent successfully to", receiver)
    
    print("Emails sent successfully to all the recipients.")

def read_receivers(file):
    reader = csv.reader(file)
    recipients = [row[0] for row in reader] # if all the email ids are in first column
    return recipients

def main():
    sender_email = input("Sender's Email: ")
    sender_password = input("Enter the password: ")

    subject = input("Subject: ")
    message = input("Message:\n\n")

    receivers = read_receivers("recipients.csv")
    print("Receivers gathered successfully.")

    text = f"Subject: {subject}\n Message:\n\n {message}"
    print("Logging in to your account......")
    send_email(sender_email, sender_password, text, receivers)


if __name__ == "__main__":
    main()