from django.shortcuts import render
import time
import rsa
import base64
import json
# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def form(request, esc, player):
	sign = ""
	teacher = "user"
	player = player
	timereq = int(time.time())
	esc = int(esc)
	private_key = rsa.PrivateKey(1, 2, 3, 4, 5)

	data = {'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc}
	firma = rsa.sign( json.dumps(data, sort_keys=True) , private_key, 'SHA-1' )
	firma64 = base64.urlsafe_b64encode(firma)

	return render(request, 'form.html', {'sign':firma64, 'teacher':teacher, 'player':player, 'time':timereq, 'esc':esc})