
# Qpysl4a Test

QPySL4A is the Script Layer for Android (SL4A) Library for QPython. It allows you to program to drive Android to work.

Install <a href = "https://github.com/qpython-android/qpython3/releases">QPython 3S</a>

Documentation <a href = "https://kylelk.github.io/html-examples/androidhelper.html">androidhelper documentation</a>

For more info check <a href = "https://github.com/qpython-android/qpysl4a">QPySL4A</a>

```bash
    import androidhelper
```

#### create an android object 
```bash
    androidobj = androidhelper.Android()
```

#### make a toast
```bash
    androidobj.makeToast("hello world")
```

#### get clipboard content
```bash
    clipboard = androidobj.getClipboard().result
    print(clipboard)
```

#### print clipboard data as toast
```bash
    androidobj.makeToast(clipboard)
```

#### check, turn on/off bluetooth
```bash
    checkbt = androidobj.checkBluetoothState().result
    print(checkbt)
```

#### writing an if condition to turn on bluetooth 
```bash
    if checkbt != True:
        androidobj.toggleBluetoothState(True)
        print("Bluetooth turned ON")
    else:
        androidobj.toggleBluetoothState(False)
        print("Bluetooth turned OFF")
```

#### check wifi 
```bash
    checkwifi = androidobj.checkWifiState().result 
    print(checkwifi)
```

#### turning on/off wifi is same as of turning on bluetooth 

#### check aeroplane mode on/off 
```bash
    checkaeroplanemode = androidobj.toggleAeroplaneMode().result
    print(checkaeroplanemode)
```

#### text to speak 
```bash
    androidobj.ttsSpeak("hello world")
```

#### speech recognition
```bash
    print(androidobj.recognizeSpeech())
```

#### take picture
```bash
    path = '/storage/emulated/0/Pictures/cam.jpg' # full file path
    androidobj.cameraCapturePicture(path)
```

#### get last know location
```bash
    location = androidobj.getLastKnownLocation()
    print(location)
    lat = location[1]['passive']['latitude']
    lon = location[1]['passive']['longitude']
    print(lat,lon)
```

#### geocoding latitude and longitude
```bash
    print (androidobj.geocode(lat, lon))
```

#### play audio
```bash
    path = '/storage/emulated/0/sunflower_instrument.mp3'
    print (androidobj.mediaIsPlaying())
    androidobj.mediaPlay(path)
```

#### stop playing audio 
```bash
    androidobj.mediaPlayClose()
```

#### print count of contacts
```bash
    print(androidobj.contactsGetCount())
```

#### print contact names
```bash
    print(androidobj.contactsGet())
```

#### print contact by id
```bash
    print(androidobj.contactsGetById(2))
```

#### make a phone call
```bash
    phone_number = 'XXXXXXXXXX'
    androidobj.phoneCallNumber(phone_number)
```

#### read/count SMS
###### count SMS (False-total SMS, True-unread SMS)
```bash
    print(androidobj.smsGetMessageCount(True))
```

#### print SMS
```bash
    print (androidobj.smsGetMessages(True))
```

#### delete an SMS 
```bash
    print (androidobj.smsDeleteMessage(Id))
    # this will return true/false 
```

#### send SMS
```bash
    phone_number = 'XXXXXXXXXX'
    androidobj.smsSend(phone_number, "message")
```

#### send email
###### if we want to send mail to multiple persons, write the mail id in list ['','','']
```bash
    to = 'name@gmail.com'
    subject = 'test mail'
    body = 'hai, this is a test mail'
    attachment = None
    # attachment should be an absolute path 
    androidobj.sendEmail(to, subject, body)
```

#### vibrate phone
```bash
    androidobj.vibrate(1000)
    # 1000 = 1 sec
```

#### create dialogue box
```bash
    inp = androidobj.dialogGetInput('question', 'Enter your name')
    print(inp)
    androidobj.makeToast(f'hello {inp[1]}')
```
