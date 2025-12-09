import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_SERVER, SMTP_PORT, MY_EMAIL, MY_PASSWORD

def send_simple_email(recipient, subject, body):
    """Sends a basic text email using SMTP."""
    
    if MY_EMAIL == "<YOUR_GMAIL_ADDRESS>" or MY_PASSWORD == "<YOUR_GMAIL_APP_PASSWORD>":
        return (False, "Email credentials are not configured in config.py.")
    
    message = MIMEMultipart()
    message['From'] = MY_EMAIL
    message['To'] = recipient
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to the SMTP server (TLS encryption)
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() 
        server.login(MY_EMAIL, MY_PASSWORD)
        
        server.sendmail(MY_EMAIL, recipient, message.as_string())
        server.quit()
        
        return (True, "Email sent successfully!")
        
    except Exception as e:
        print(f"Email failed: {e}")
        return (False, f"Sorry, I couldn't send the email. Error: {e}")

def set_calendar_reminder(subject, time_str):
    """Placeholder for Calendar API integration."""
    # REAL IMPLEMENTATION: This requires connecting to Google Calendar API (via OAuth 2.0).
    return f"Reminder set for '{subject}' at {time_str}. (Requires Google Calendar API setup)"
