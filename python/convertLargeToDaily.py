eventDiv = '''
<div>
	<article>
		<a href="#schedule-content-container" onclick="showDetails('{{startTime}}-{{endTime}}', '{{eventName}}', '{{eventNickname}}')"><div class="container">
			<img data-lazy="images/pic01.jpg" style="width:100%;">
			<div class="time">{{startTime}}-{{endTime}}</div>
			<div class="activity">{{eventName}}</div>
		  </div></a>
	</article>
</div>
'''
def getData(keypair):
	return keypair[keypair.find('="')+2:][:-1]
def convertTimeToAmPm(time):
	hr, min = time.split(":")
	if (int(hr) < 9 or int(hr) == 12):
		return time + "pm"
	return time + "am"
outputString = ""
with open('largeSchedule.txt') as f:
	lines = f.readlines()
	eventLine = 0
	startNewEvent = False
	tmpOutput = ""
	for line in lines:
		line = line.rstrip()
		if ('''<li class="cd-schedule__event"><!--event start-->''' in line):
			eventLine = 0
			startNewEvent = True
		elif ('''</li><!-- end event-->''' in line):
			startNewEvent = False
			outputString += tmpOutput
			tmpOutput = ""
		if (startNewEvent):
			if (eventLine == 1):
				info = line.split()
				tmpOutput = eventDiv.replace("{{startTime}}", getData(info[1])).replace("{{endTime}}", getData(info[2]))
				tmpOutput = tmpOutput.replace("{{eventNickname}}", getData(info[3]))
			elif (eventLine == 2):
				tmpOutput = tmpOutput.replace("{{eventName}}", line[line.find('">')+2:])	
		eventLine += 1

print(outputString)
