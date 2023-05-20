import androidhelper
# create an android object 
androidobj = androidhelper.Android()
# make a toast
androidobj.makeToast("hello world")

# ----------------------------------------

# get clipboard content
clipboard = androidobj.getClipboard().result
print(clipboard)
# print clipboard data as toast 
androidobj.makeToast(clipboard)

#----------------------------------------

# check, turn on/off bluetooth
checkbt = androidobj.checkBluetoothState().result 
print(checkbt)
# writing an if condition to turn on bluetooth 
if checkbt != True:
    androidobj.toggleBluetoothState(True)
    print("Bluetooth turned ON")
else:
    androidobj.toggleBluetoothState(False)
    print("Bluetooth turned OFF")

#----------------------------------------    

# check WiFi
checkwifi = androidobj.checkWifiState().result 
print(checkwifi)

# turning on/off wifi is same as of turning on bluetooth 

#---------------------------------------- 

# check aeroplane mode on/off
checkaeroplanemode = androidobj.toggleAeroplaneMode().result
print(checkaeroplanemode)
#----------------------------------------

# text to speak
androidobj.ttsSpeak("hello world")

#----------------------------------------

# speech recognition
print(androidobj.recognizeSpeech())
#----------------------------------------

# take picture
path = '/storage/emulated/0/Pictures/cam.jpg'
androidobj.cameraCapturePicture(path)

#----------------------------------------

# get last know location
location = androidobj.getLastKnownLocation()
print(location)
lat = location[1]['passive']['latitude']
lon = location[1]['passive']['longitude']
print(lat,lon)
# geocoding latitude and longitude
print (androidobj.geocode(lat, lon))
#----------------------------------------

# play audio
path = '/storage/emulated/0/sunflower_instrument.mp3'
print (androidobj.mediaIsPlaying())
androidobj.mediaPlay(path)
# stop playing audio 
androidobj.mediaPlayClose()

#----------------------------------------

# print count of contacts
print(androidobj.contactsGetCount())
# print contact names
print(androidobj.contactsGet())
# print contact by id
print(androidobj.contactsGetById(2))

#----------------------------------------

# make a phone call
phone_number = '7306333244'
androidobj.phoneCallNumber(phone_number)

#----------------------------------------

# read/count SMS
# count SMS (False-total SMS, True-unread SMS)
print(androidobj.smsGetMessageCount(True))
# print SMS
print (androidobj.smsGetMessages(True))
# delete an SMS 
print (androidobj.smsDeleteMessage(Id))
# this will return true/false 

#----------------------------------------

# send SMS
phone_number = '7306333244'
androidobj.smsSend(phone_number, "hello from milan")

#----------------------------------------

# send email
# if we want to send mail to multiple persons, write the mail id in list ['','','']
to = 'milansony246@gmail.com'
subject = 'test mail'
body = 'hai, this is a test mail'
attachment = None
# attachment should be an absolute path 
androidobj.sendEmail(to, subject, body)

#----------------------------------------

# vibrate phone
androidobj.vibrate(1000)
# 1000 = 1 sec

#----------------------------------------

# create dialogue box
inp = androidobj.dialogGetInput('question', 'Enter your name')
print(inp)
androidobj.makeToast(f'hello {inp[1]}')