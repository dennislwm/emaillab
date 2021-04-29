import os
import pytest
import re
import smtplib

from emaillab import config, emaillab
from validate_email import validate_email

test_file = "test.yml"
smtp_url  = "dbdev.myftp.org"
smtp_port = 1025

@pytest.fixture
def smtp():
  return smtplib.SMTP(
    smtp_url,
    smtp_port
  )

@pytest.fixture
def data():
  #----------------------------
  # create config if not exists
  new_file = test_file
  if not os.path.exists(new_file):
    new_file = input("Create a config file (leave empty for default): ") or new_file
    config.create_file(new_file)
  #------------
  # load config
  return config.load_file(new_file)

def test_validate_data_smtp_port(data):
  port = int(data["smtp"]["port"])
  assert port >= 0 and port <= 65535

def test_validate_data_smtp_url(data):
  assert re.search(r"([a-z0-9A-Z]+\.)+([a-z0-9A-Z]+)", data["smtp"]["url"])

def test_validate_data_user_email(data):
  assert validate_email(data["user"]["email"])

def test_validate_data_addressee_to(data):
  assert validate_email(data["addressee"]["to"])

def test_validate_data_addressee_pixel(data):
  #
  # optional field
  pixel = data["addressee"]["pixel"]
  if pixel:
    assert re.search(r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", pixel)

def test_compose_msg(smtp, data):
  msg = emaillab.compose_msg(data)
  smtp.send_message(msg)
  smtp.close()
