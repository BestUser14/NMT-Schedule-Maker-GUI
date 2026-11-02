# NMT-Schedule-Maker
This program automatically makes schedules for New Mexico Institute of Mining and Technology classes. These schedules can be organized in a few ways based on how the user wants their schedule to be organized, including evenly spreading out classes or minimizing classes on a certain day, as well as preferred professors for classes.

To use this program install python (and possible pip)

On windows:
	go to python.org and install the newewest verison of python3
	go to the command line and type this command

		py -m pip -r install requirements.txt

	#then you can run the program by running this in the command line in the program folder
		py main.py
On linux (debian):
	run this
		sudo apt install python3
		sudo apt install pip
		python3 -m pip install pytz, ics, datetime, requests, matplotlib
	or
		python3 -m pip -r install requirements.txt
	to run the program run this
		python3 gui.py
none of the above was proofread or tested, if it doesnt work, look at the python error and install whatever library it says is missing

```console
	pip install -r requirements.txt
	py gui.py
```

Calendar
	This program export the schedule into an ics file which can be read by basically any calendar app.
	when you import the calendar, it is probably a good idea to make a new calendar in the calendar, which can be done in at least: apple calendar, google calendar, ubuntu calendar.
	you can use this new calendar to see the schedule, and if you dont like it you can just delete that calendar instead of manually deleting hundreds of classes from your personal events.
	to use the calendar you can open the ics file in your calendar app and save it to your temporary calendar.
