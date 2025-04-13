# Usa una imagen base de Ubuntu
FROM python:3.14-rc-alpine3.20

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /task-cli

# Copia los archivos de tu proyecto al contenedor
COPY requirements.txt /task-cli/

# Instala las dependencias de tu proyecto (si las tienes)
# Ejemplo para instalar Python y pip
RUN apk add make
RUN python3 -m venv . 
# Instala las dependencias de tu proyecto desde requirements.txt
# Si no tienes un archivo requirements.txt, puedes omitir esta línea
RUN pip install -r requirements.txt
RUN sh 

CMD ["/bin/sh"]

