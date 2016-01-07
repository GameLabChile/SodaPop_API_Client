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

def form(request, esc, player):
	url = "https://[server]/api/newalone/"
	sign = ""
	teacher = "user given"
	player = player
	timereq = int(time.time())
	esc = int(esc)
	private_key = rsa.PrivateKey() #key given
	data = {'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc}
	firma = rsa.sign( json.dumps(data, sort_keys=True) , private_key, 'SHA-1' )
	firma64 = base64.urlsafe_b64encode(firma)

	return render(request, 'form.html', {'sign':firma64, 'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc, 'url':url})