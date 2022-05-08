# Whatsapp_scripts
Just a naive whatsapp web reader &amp; sender.

Properties & Features :

- Will always need mobile whastapp scanner to log in.
- Finds a contact which has been recently(see limitations) contacted and sends message to them and also reads last few messages from them.
- Tested in Linux + Firefox only.
- Uses selenium Library mostly.

Limitation :

- Most xpaths and class names in web.whatsapp will change in future, so yeah this code definitely won't stand the test of time.
- It's strange but when finding for recent contacts, the first 13 contacts are numbered/referenced between o-12 but after that it changes drastically like the contact immediately aft 12th last contacted is indexed at 50th, didn't try to understand the numbering scheme much though, only coded for the first 13.(it maybe the case, it will be numbered different or more orderly in some other browser etc)
- Used a lot of time.sleep() because browser opening up, whatsapp connections took some time.

Sources & Thoughts :

- How to obtain xpaths, class names : https://medium.com/@jihargifari/how-to-send-multiple-whatsapp-message-using-python-3f1f19c5976b
- Another source but yeah severly outdated, like this code will be from now : https://apoorvtyagi.tech/how-i-automated-my-whatsapp-chats
- I tried to tresspass the QR scanning but all of the methods failed, Stackoverflow answers mostly suggested to take use my firefox profile and use it to open the browser, in theory it wouldn't need QR scanning, tried this in various ways (see Autologging_trials.py) but ddidn't work out, Also for this you would need an executable gecko file, most answers i refered in Autologging_trials.py, you would find it.
- Most Articles/Sources have the answers for chrome though, haven't tried there though.
