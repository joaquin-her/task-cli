# Usa una imagen base de Ubuntu
FROM python:3.14-rc-alpine3.20

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /task-cli

# Copia los archivos de tu proyecto al contenedor
COPY requirements.txt /task-cli/
COPY /src /task-cli/src
COPY /tests /task-cli/tests
COPY /scripts /task-cli/scripts

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

CMD ["/bin/sh"]

