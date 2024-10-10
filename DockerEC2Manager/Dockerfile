FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

# Instalar AWS CLI y Python3
RUN apt-get update && apt-get install -y awscli python3 && rm -rf /var/lib/apt/lists/*

# Copiar el script Python
COPY list_instances.py /app/

# Crear un grupo y usuario sin privilegios
RUN groupadd -r appgroup && useradd -r -ms /bin/bash -g appgroup appuser

# Cambiar propietario del script Python
RUN chown appuser:appgroup /app/list_instances.py

# Cambiar al usuario sin privilegios
USER appuser

# Establecer el directorio de trabajo
WORKDIR /home/appuser

# Usar ENTRYPOINT para ejecutar el script Python
ENTRYPOINT ["/bin/sh", "-c", "su -l appuser -c 'python3 /app/list_instances.py'"]