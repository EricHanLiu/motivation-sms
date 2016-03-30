#Motivation SMS
Send yourself an SMS every **n** minutes to motivate yourself.

#How to use
First, you must setup a [Twilio] (https://www.twilio.com/) account.

  1. On the homepage, click the **SIGN UP** button in the top right corner.
  2. Create your account and follow the instructions to verify your account.
  3. Under the **Phone Numbers** tab, click on **Verified Caller IDs**.
  4. If your own number is not already listed (it should be if you verified properly), add it now.

Then, edit the conf.py file with the details from your Twilio account (found in the Account tab under API Credentials).

From here, simply running `python send_sms.py "insert message"` in terminal while in the same directory as the file will send a message to your phone!

#Setting up crontab
In order to receive messages on a timed interval (perhaps every day at 5:00PM), you must add parameters to your crontab file. 
Run `crontab -e`, choose your default editor, and insert the following lines.
#####You can change the interval at which the messages send by editing the five parameters
Formatting guide can be found [here] (https://help.ubuntu.com/community/CronHowto)

``` 
0 * * * * /usr/bin/python /directorywhereyou/clonedthisrepo/send_sms.py "INSERT YOUR MESSAGE HERE"
10 * * * * /usr/bin/python /directorywhereyou/clonedthisrepo/send_sms.py "INSERT YOUR MESSAGE HERE"
20 * * * * /usr/bin/python /directorywhereyou/clonedthisrepo/send_sms.py "INSERT YOUR MESSAGE HERE"
30 * * * * /usr/bin/python /directorywhereyou/clonedthisrepo/send_sms.py "INSERT YOUR MESSAGE HERE"
40 * * * * /usr/bin/python /directorywhereyou/clonedthisrepo/send_sms.py "INSERT YOUR MESSAGE HERE"
50 * * * * /usr/bin/python /directorywhereyou/clonedthisrepo/send_sms.py "INSERT YOUR MESSAGE HERE"
```

#That's it! You're done.
Just save your crontab file and watch the motivational messages fly in.
