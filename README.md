# SodaPop_API_Client

## Modify:

2. file ```iframe/views.py```
  + ```:9``` change ```teacher = "user given"```
  + ```:10``` change ```url = "https://[server]/api/esc/?teacher="+teacher``` replacing [server] with given server
  + ```:16``` change ```url = "https://[server]/api/newalone/"``` replacing [server] with given server
  + ```:18``` change ```teacher = "user given"```
  + ```:22``` change ```private_key = rsa.PrivateKey( key given )```

## Run:

1. Run ```python manage.py runserver```
2. Open ```localhost:8000```
