# SodaPop_API_Client

## Modify:

1. file ```iframe/templates/form.html```
  + ```:1``` change ```action="https://[server]/api/newalone/"``` replacing **[server]** with the given server (posibly sp.gamelab.cl)

2. file ```iframe/views.py```
  + ```:12``` change ```teacher = "user given"```
  + ```:16``` change ```private_key = rsa.PrivateKey( key given )```

## Run:

1. Run ```python manage.py runserver```
2. Open ```localhost:8000/form/[esc]/[player name]/```
