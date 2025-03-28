### Para correr pruebas unitarias :
Windows: ``` pytest .\tests\  ```
Linux: ```pytest tests```
para simplificacion de salida: ```-v```

### Para correr covertura de pruebas:
Windows: ```coverage run -q -m pytest .\tests\ ; coverage report```
Linux: ```coverage run -q -m pytest && coverage report ```