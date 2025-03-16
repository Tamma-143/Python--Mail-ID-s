import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate a random CAPTCHA
def generate_captcha(length=6):
    chars = string.ascii_letters + string.digits  # Letters (a-z, A-Z) and numbers (0-9)
    captcha = ''.join(random.choices(chars, k=length))
    return captcha

# Function to send an email with CAPTCHA
def send_email(to_email, captcha):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_app_password"  # Use an App Password instead of your real password

    subject = "Your CAPTCHA Code"
    message = f"Hello,\n\nYour CAPTCHA code is: {captcha}\n\nPlease use this code to proceed.\n\nBest Regards,\nYour Team"

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print(f"CAPTCHA sent successfully to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# Function to send CAPTCHA to multiple email addresses
def send_captcha_to_users(email_list):
    for email in email_list:
        captcha = generate_captcha()  # Generate a unique CAPTCHA for each user
        send_email(email, captcha)

# List of email recipients
email_recipients = ["subhu1@example.com", "rudra2@example.com", "bala3@example.com"]  # Replace with actual emails

# Send CAPTCHA to all users
send_captcha_to_users(email_recipients)
