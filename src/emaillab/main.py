import config
import emaillab
import os

def main():
  #----------------------------
  # create config if not exists
  new_file = 'emaillab.yml'
  if not os.path.exists(new_file):
    new_file = input("Create a config file (leave empty for default): ") or new_file
    config.create_file(new_file)

  #------------
  # load config
  data = config.load_file(new_file)

  #-------------
  # confirmation
  str_confirm = input(f"Do you want to send this email (only 'yes' will be accepted)? ")
  if not str_confirm.lower() == 'yes':
    return

  #------------
  # auth client
  smtp = emaillab.auth_client(data)

  #---------------------
  # compose and send msg
  msg = emaillab.compose_msg(data)
  smtp.login( 
    data["user"]["email"],
    data["user"]["password"]
  )
  smtp.send_message(msg)

  #-------------
  # close client
  smtp.close()

if __name__ == "__main__":
  main()
