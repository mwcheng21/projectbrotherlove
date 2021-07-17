

eventString = '''
<li class="cd-schedule__event"><!--event start-->
<a data-start="{{timeStart}}" data-end="{{timeEnd}}" data-content="event-{{eventNickname}}" data-event="event-{{eventColor}}" href="#0">
<em class="cd-schedule__name">{{eventName}}</em>
</a>
</li><!-- end event-->
'''

dayStartString = '''
<!--start {{dayOfWeek}}-->
<li class="cd-schedule__group">
<div class="cd-schedule__top-info"><span>{{dayOfWeek}} ({{date}})</span></div>

<ul>
'''

dayEndString = '''
</ul>
</li><!-- end day-->
'''
outputString = ""

def convertTo24Hr(time):
	hr, min = time.split(":")
	if (int(hr) < 9):
		return str(int(hr)+12) + ":" + min
	return time



with open('schedule.txt') as f:
	lines = f.readlines()
	ind = 0
	for line in lines:
		if (ind==0):
			outputString+=dayStartString.replace("{{dayOfWeek}}", line.split()[1]).replace("{{date}}", line.split()[0])
		else:
			info = line.split()
			timeStart, timeEnd = info[0].split("-")
			timeStart = convertTo24Hr(timeStart)
			timeEnd = convertTo24Hr(timeEnd)
			tmpOutput = eventString.replace("{{timeStart}}", timeStart).replace("{{timeEnd}}", timeEnd)
			tmpOutput = tmpOutput.replace("{{eventName}}", line[line.find("\t")+1:])
			tmpOutput = tmpOutput.replace("{{eventNickname}}", info[1])
			tmpOutput = tmpOutput.replace("{{eventColor}}", str(ind%4 + 1))
			outputString += tmpOutput
		ind += 1
outputString += dayEndString
print(outputString)








