import pyrebase
import csv

def dataWriter(user_data):
  with open('user_data.csv','w') as fp:
    writer = csv.writer(fp)
    for param,val in user_data.items():
      writer.writerow([param,''])
      for deeper_params,deeper_vals in val.items():
        writer.writerow([deeper_params,deeper_vals])

def authenticator(config):
  global user_data
  firebase = pyrebase.initialize_app(config)
  db = firebase.database()
  user_data = db.child("user_data").get().val()

def cliPrinter(user_data):
  for k,v in user_data.items():
    print ("UNIQUE ID: ",k,"\n")
    print ("RECEIVED DATA: ")
    for param,val in v.items():
      # if len(val) > 1:
      #   print ("\t******",param,": ",val)
      # else:
      #   print ("\t\t",param,": ",val)
      print (param,": ",val)
      # print (type(val))

config = {
    "apiKey": "AIzaSyDPvrIG5sCQF6yzpth0rJ3VLlaeL2rpEGw",
    "authDomain": "dasut-462eb.firebaseapp.com",
    "databaseURL": "https://dasut-462eb.firebaseio.com",
    "storageBucket": "dasut-462eb.appspot.com",
    "serviceAccount": "dasut-ed60a76ed861.json"
  }

authenticator(config)
print (type(user_data))

# Uncomment for printing on cli
cliPrinter(user_data)
      
dataWriter(user_data)

