# app/Dockerfile

# Usar una imagen base de Python oficial
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos primero para aprovechar el caché de Docker
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que corre la aplicación Flask
EXPOSE 5000

# El comando para ejecutar la aplicación cuando se inicie el contenedor
# Usamos 'flask run' que es la forma moderna de ejecutar una app de desarrollo
CMD ["flask", "run", "--host=0.0.0.0"]