import smtplib
from email.message import EmailMessage
import schedule
import time

# Email account details
sender_email = 'yourgmail@gmail.com'
receiver_email = 'yourfriend@example.com'
app_password = 'your_app_password_here'

# Function to send email
def send_email():
    subject = 'Daily Reminder!'
    body = '''Hi friend,
Just sending you a daily reminder as planned.
Have a great day!
– Deepa'''

    # Create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    # Send email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
            print("Email sent successfully at 10 AM!")
    except Exception as e:
        print("Error sending email:", e)

# Schedule the email every day at 10:00 AM
schedule.every().day.at("10:00").do(send_email)

print("Scheduler started... Will send email every day at 10 AM.")

# Keep running the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # check every 60 seconds
