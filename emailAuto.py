import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    """
    Send an automated email with optional attachment
    
    Args:
        sender_email: Your email address
        sender_password: Your email password or app password
        recipient_email: Recipient's email address
        subject: Email subject
        body: Email body content
        attachment_path: Optional path to file attachment
    """
    
    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Add body to email
        message.attach(MIMEText(body, 'plain'))
        
        # Add attachment if provided
        if attachment_path:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {attachment_path.split("/")[-1]}'
                )
                message.attach(part)
        
        # Create SMTP session
        # For Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        
        # Login to email account
        server.login(sender_email, sender_password)
        
        # Send email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"Email sent successfully to {recipient_email}!")
        return True
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False


# Example usage
if __name__ == "__main__":
    # Configuration
    SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email
    SENDER_PASSWORD = "your_app_password"   # Replace with your app password
    RECIPIENT_EMAIL = "sablaygaming@gmail.com"
    
    # Email content
    subject = "Automated Email Test"
    body = """Hello,

This is an automated email sent using Python.

Best regards,
Your Name"""
    
    # Send email (without attachment)
    send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body)
    
    # Send email with attachment (uncomment to use)
    # send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body, "path/to/file.pdf")


# For scheduling emails, you can use these approaches:

# Option 1: Using schedule library
"""
import schedule
import time

def job():
    send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body)

# Schedule email to send daily at 9:00 AM
schedule.every().day.at("09:00").do(job)

# Schedule email every hour
schedule.every().hour.do(job)

# Keep script running
while True:
    schedule.run_pending()
    time.sleep(60)
"""

# Option 2: Using time.sleep for delay
"""
import time

# Send email after 10 seconds
time.sleep(10)
send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, subject, body)
"""