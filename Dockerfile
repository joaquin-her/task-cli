# Usa una imagen base de Ubuntu
FROM python:3.14-rc-alpine3.20

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /task-cli

# Copia los archivos de tu proyecto al contenedor
COPY requirements.txt /task-cli/
COPY /src /task-cli/src
COPY /task_cli.py /task-cli/
COPY cli_wrapper.sh /task-cli/
# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Crea un enlace simbólico para que 'task-cli' apunte a tu script
RUN ln -s /task-cli/cli_wrapper.sh /usr/local/bin/task-cli
CMD ["/bin/sh"]

