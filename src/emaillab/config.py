from getpass import getpass
from ruamel.yaml import YAML

def load_file(filename):
  yaml = YAML()
  #---------------
  # Read from file
  with open(filename, 'r') as file:
    yml_return = yaml.load(file)
  return yml_return

def input_multi_line_str(prompt):
  lines = []
  line = input(prompt)
  if line == "|":
    while True:
      line = input("  Line " + str(len(lines)+1) + " (leave empty to end): " )
      if not line: 
        break
      lines.append(line)
    ret_str = '\n'.join(lines)
  else:
    ret_str = line
  return ret_str

def create_file(filename):
  yaml = YAML()
  init = ("""
    user:
      name: ""
      email: ""
      password: ""
    smtp:
      url: ""
      port: ""
    addressee:
      to: ""
      subject: ""
      body: ""
      attachment: ""
      pixel: ""
  """)
  data = yaml.load(init)

  data["user"]["name"]            = input("Enter your name (required): ")
  data["user"]["email"]           = input("Enter your email address (required): ")
  data["user"]["password"]        = getpass("Enter your email password (required): ")
  data["smtp"]["url"]             = input("Enter smtp url (leave empty for default): ") or 'smtp.gmail.com'
  data["smtp"]["port"]            = input("Enter smtp port (leave empty for default): ")  or '465'
  data["addressee"]["to"]         = input("Enter addressee email (required): ")
  data["addressee"]["subject"]    = input("Enter addressee subject (required): ")
  data["addressee"]["body"]       = input_multi_line_str("Enter addressee body (required type '|' for multi line): ")
  data['addressee']['attachment'] = input("Enter addressee attachment (optional): ")
  data["addressee"]["pixel"]      = input("Enter addressee pixel (optional): ")

  with open(filename, 'w') as file:
    yaml.dump(data, file)