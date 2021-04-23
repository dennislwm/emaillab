import pytest
import os

from emaillab import config

filename = "test.yml"

#-------------------------------------------------------------------
# suspend input capture by pytest so user input can be recorded here
@pytest.fixture
def suspend_capture(pytestconfig):
    class suspend_guard:
        def __init__(self):
            self.capmanager = pytestconfig.pluginmanager.getplugin('capturemanager')
        def __enter__(self):
            self.capmanager.suspend_global_capture(in_=True)
        def __exit__(self, _1, _2, _3):
            self.capmanager.resume_global_capture()

    yield suspend_guard()

def test_create(suspend_capture):
  new_file = filename
  if not os.path.exists(new_file):
    with suspend_capture:
      new_file = input("Create a config file (leave empty for default): ") or filename
      config.create_file(new_file)
  assert os.path.exists(new_file)

@pytest.fixture
def yaml():
  return config.load_file(filename)

def test_load_without_user(yaml):
  assert yaml["user"]["name"]
  assert yaml["user"]["email"]
  assert yaml["user"]["password"]

def test_load_without_smtp(yaml):
  assert yaml["smtp"]["url"]
  assert yaml["smtp"]["port"]

def test_load_without_addressee(yaml):
  assert yaml["addressee"]["to"]
  assert yaml["addressee"]["subject"]  
  assert yaml["addressee"]["body"]
