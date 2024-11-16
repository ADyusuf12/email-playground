import smtplib
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Template
from pathlib import Path 
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Access the variables
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to add attachment
def add_attachment(email, file_path):
    with open(file_path, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {file_path}')
        email.attach(part)

# Read and render email template
template = Template(Path('index.html').read_text())
email_body = template.render(name='A D')

# Set up email message
email = EmailMessage()
email['from'] = 'A D'
email['to'] = 'adanbatta@yahoo.com'
email['subject'] = 'ASOIF'
email.set_content(email_body, 'html')

# Add an attachment (optional)
# add_attachment(email, 'path_to_attachment_file.pdf')

# List of recipients
recipients = ['recipient1@example.com', 'recipient2@example.com']

# Send email to each recipient
for recipient in recipients:
    email['to'] = recipient
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        try:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(email)
            logging.info(f'Email sent to {recipient}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {e}')
