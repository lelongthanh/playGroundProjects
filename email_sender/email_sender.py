import smtplib  # allow to create what we call an SMTP server
# if want to send emails, need SMTP server
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())  # read file html
email = EmailMessage()
email['from'] = 'Thomas Le'
email['to'] = 'mynamestorm2000@gmail.com'
email['subject'] = 'You won a new Vinfast VF9 car'

# thêm 'html' sẽ giúp định dạng file
email.set_content(html.substitute({'name': 'Thomas'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('lelongthanh289@gmail.com', 'glat zswh ptqh aeib')
    smtp.send_message(email)
    print('all good boss!')
