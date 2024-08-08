import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'A D'
email['to'] = 'adanbatta@yahoo.com'
email['subject'] = 'ASOIF'

# email.set_content('Winter is coming!')
email.set_content(html.substitute({'name': 'A D'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('adyusuf68@gmail.com', 'vlys fxpb enwk vsrw')
  smtp.send_message(email)
  print('sent boss!')