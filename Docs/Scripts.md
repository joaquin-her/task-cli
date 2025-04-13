### Para correr pruebas unitarias :
Windows: ``` pytest .\tests\  ```
Linux: ```pytest tests```
para simplificacion de salida: ```-v```

### Para correr covertura de pruebas:
Windows: ```coverage run -m pytest .\tests\ ; coverage report```
Linux: ```coverage run -m pytest && coverage report ```

### Para corer docker:
Windows: ```docker run -v ${PWD}:/task-cli task-cli-linux ```
Linux: ```docker run -v $(PWD):/task-cli task-cli-linux ```

### docker raise:

```
docker_build:
        docker build -t task-cli-linux .

dev:
        docker_build
        docker run -it \
                -v $(PWD)/src:/task-cli/src \
                -v $(PWD)/tests:/task-cli/tests \
                -v $(PWD)/task-cli.py:/task-cli/task-cli.py \
                -v $(PWD)/makefile:/task-cli/makefile \
                task-cli-linux
```