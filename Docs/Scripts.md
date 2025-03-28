### Para correr pruebas unitarias :
Windows: ``` pytest .\tests\  ```
Linux: ```pytest tests```
para simplificacion de salida: ```-v```

### Para correr covertura de pruebas:
Windows: ```coverage run --omit=tests/* -m pytest .\tests\ ; coverage report```
Linux: ```coverage run --omit=tests/* -m pytest && coverage report ```