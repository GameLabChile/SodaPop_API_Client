from django.shortcuts import render
import time
import rsa
import base64
import json
import urllib2
# Create your views here.
def index(request):
	teacher = "user given"
	url = "https://[server]/api/esc/?teacher="+teacher
	
	res = urllib2.urlopen(url).read()
	json_obj = json.loads(res)
	return render(request, 'index.html', {'escs':json_obj})

def form(request, esc, player, classid, playerid):
	
	sign = ""
	
	url = "https://[server]/api/newalone/"
	teacher = "user given"
	private_key = rsa.PrivateKey() #key given

	player = player
	timereq = int(time.time())
	esc = int(esc)

	data = {'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc, 'playerid': int(playerid), 'classid':int(classid)}
	firma = rsa.sign( json.dumps(data, sort_keys=True) , private_key, 'SHA-1' )
	firma64 = base64.urlsafe_b64encode(firma)
	print  json.dumps(data, sort_keys=True)
	return render(request, 'form.html', {'sign':firma64, 'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc, 'url':url, 'playerid':playerid, 'classid':classid})