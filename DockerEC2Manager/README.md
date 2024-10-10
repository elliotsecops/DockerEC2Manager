# DockerEC2Manager

This project provides a Docker container to list AWS EC2 instances securely using environment variables for credentials. It's suitable for both novice and experienced Docker and AWS users.

## Features

* **Security:** Avoids storing credentials within the container image by using environment variables.
* **Flexibility:** Allows specifying the AWS region when running the container.
* **Simplicity:** Easy to build and run.
* **Lightweight:** Uses an optimized base image to minimize size.
* **Multi-stage builds (optional):** Further reduces the final image size.
* **Health checks (optional):** Verifies the container's health.

## Requirements

* Docker installed and running.
* An AWS account with valid credentials.

## Usage

### 1. Clone the repository:

```bash
git clone https://github.com/elliotsecops/DockerEC2Manager.git
cd DockerEC2Manager
```

### 2. Build the Docker image:

```bash
docker build -t docker-ec2-manager .
```

### 3. Run the container:

Replace `<YOUR_ACCESS_KEY_ID>`, `<YOUR_SECRET_ACCESS_KEY>`, and `<YOUR_SESSION_TOKEN>` (if applicable) with your AWS credentials. Replace `us-west-2` with your desired region.

```bash
docker run --rm \
    -e AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID> \
    -e AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY> \
    -e AWS_SESSION_TOKEN=<YOUR_SESSION_TOKEN> \  # Optional, if using temporary authentication
    docker-ec2-manager <region> # Example: us-west-2
```

**For novice users:** This command runs the container, lists the EC2 instances in the specified region, and then removes it.  Environment variables provide AWS credentials securely without storing them in the image.

**For advanced users:** You can customize the Dockerfile to use multi-stage builds, health checks, and a `requirements.txt` file to manage Python dependencies, as described in the "Optional Enhancements" section.  You can also explore using more minimalist base images like `alpine` or `distroless`.

## Optional Enhancements (for advanced users)

The Dockerfile includes options for multi-stage builds and health checks, which are commented out by default. You can uncomment these lines to enable them. You can also use a `requirements.txt` file to manage Python dependencies.  See the Dockerfile for details.

## Contributing

Contributions are welcome! Please open a pull request with your changes.

## License

MIT

---

# DockerEC2Manager

Este proyecto proporciona un contenedor Docker para listar instancias EC2 de AWS de forma segura utilizando variables de entorno para las credenciales. Es adecuado tanto para usuarios principiantes como avanzados de Docker y AWS.

## Características

* **Seguridad:** Evita almacenar credenciales dentro de la imagen del contenedor utilizando variables de entorno.
* **Flexibilidad:** Permite especificar la región de AWS al ejecutar el contenedor.
* **Simplicidad:** Fácil de construir y ejecutar.
* **Ligero:** Utiliza una imagen base optimizada para minimizar el tamaño.
* **Multi-stage builds (opcional):** Reduce aún más el tamaño de la imagen final.
* **Health checks (opcional):** Verifica el estado del contenedor.

## Requisitos

* Docker instalado y en funcionamiento.
* Una cuenta de AWS con credenciales válidas.

## Uso

### 1. Clonar el repositorio:

```bash
git clone https://github.com/elliotsecops/DockerEC2Manager.git
cd DockerEC2Manager
```

### 2. Construir la imagen Docker:

```bash
docker build -t docker-ec2-manager .
```

### 3. Ejecutar el contenedor:

Reemplaza `<YOUR_ACCESS_KEY_ID>`, `<YOUR_SECRET_ACCESS_KEY>` y `<YOUR_SESSION_TOKEN>` (si aplica) con tus credenciales de AWS. Reemplaza `us-west-2` con la región deseada.

```bash
docker run --rm \
    -e AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID> \
    -e AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY> \
    -e AWS_SESSION_TOKEN=<YOUR_SESSION_TOKEN> \  # Opcional, si usas autenticación temporal
    docker-ec2-manager <region> # Ejemplo: us-west-2
```

**Para usuarios novatos:** Este comando ejecuta el contenedor, lista las instancias EC2 en la región especificada y luego lo elimina. Las variables de entorno proporcionan las credenciales de AWS de forma segura sin almacenarlas en la imagen.

**Para usuarios avanzados:** Puedes personalizar el Dockerfile para usar *multi-stage builds*, *health checks* y un archivo `requirements.txt` para gestionar las dependencias de Python, como se describe en la sección "Mejoras Opcionales". También puedes explorar el uso de imágenes base más minimalistas como `alpine` o `distroless`.

## Mejoras Opcionales (para usuarios avanzados)

El Dockerfile incluye opciones para *multi-stage builds* y *health checks*, que están comentadas por defecto. Puedes descomentar estas líneas para activarlas. También puedes usar un archivo `requirements.txt` para gestionar las dependencias de Python. Consulta el Dockerfile para más detalles.

## Contribuciones

Las contribuciones son bienvenidas! Por favor, abre un *pull request* con tus cambios.

## Licencia

MIT