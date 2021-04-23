from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

def auth_client(data):
  #-------------
  # authenticate
  smtp = smtplib.SMTP_SSL(
    data["smtp"]["url"],
    data["smtp"]["port"]
  )
  smtp.login(
    data["user"]["email"],
    data["user"]["password"]
  )
  return smtp

def compose_msg(data):
  msg = MIMEMultipart()
  msg['From']         = data["user"]["name"]
  msg['To']           = data["addressee"]["to"]
  msg['Subject']      = data["addressee"]["subject"]
  msg.attach( MIMEText( data["addressee"]["body"] ) )

  #--------------------
  # optional attachment
  to_file = data["addressee"]["attachment"]
  if to_file:
    with open(to_file, 'rb') as attach:
      img = MIMEImage(attach.read())
    img.add_header('Content-ID', '<{}>'.format(to_file))
    msg.attach(img)

  return msg