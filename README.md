# VoiceControlledNoticeBoard

How to Start:

Components Required:
1. Download Android App From PlayStore: Blue term
2. Bluetooth Speaker

Packages to Install

1. Install Bluetooth module on raspberry PI:
	a. sudo apt-get install pi-bluetooth
	b. sudo apt-get install BlueZ
	c. sudo apt-get install blueman 

2. Install Espeak (Text to Speech Module):
	a.sudo apt-get install espeak python-espeak

3. Install Sqlite3 and Python drivers:
	a. sudo apt-get install sqlite3
    b. sudo apt-get install python-sqlite


Steps To run:
1. Copy the files inside the templates Folder at location : /usr/lib/python2.7/dist-packages/django/contrib/admin/templates
2. navigate to django/mysite and run command: python manage.py runserver
3. Hit the Localhost Url in browser and Connect device via Bluetooth once successfully connected open Google Voice Typing speak the message the wait for message to be displayed on web Interface


Experiments Implemented:
1. Relay Activation using voice
2. Displaying voice converted text message on LCD Panel 

Applications:
1. Can be used for making public announcements e.g. flight announcements, public announcements, etc. using Kiosks and electronic bulletin boards
2. In case of emergency to send SOS signals if no other means of communication is available.

Limitations:
1. Web interfaces are not best suitable for event driven applications because they are not ss intuitive as a mobile interdface.
2. Accuracy of voice to text conversion.

References :
1. A Voice-Controlled Web Browser to Navigate Hierarchical Hidden Menus of Web Pages in a Smart-TV Environment
   by Sungjae Han ,Geunseong Jung , Minsoo Ryu,Byung-Uk Choi and Jaehyuk Cha

2. A Comparison of Voice Controlled and Mouse Controlled Web Browsing
   by Kevin Christian,Bill Kules,Ben Shneiderman,Adel Youssef
   
