# Microservicio de Star Wars

Este repositorio contiene un microservicio en Python que consume la API (People) de Star Wars (SWAPI) ordena los datos por nombre y los expone en un endpoint. El microservicio está contenerizado con Docker y se despliega en Kubernetes.

## Requisitos

* Docker
* Docker Compose
* kubectl
* Minikube

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/dacega/swapi-microservice.git

2. Construye la imagen de Docker:

```bash
docker build -t <nombre-imagen>:<tag> .

3. (Opcional) Ejecuta el microservicio localmente con Docker Compose

El docker-compose.yml contiene el comando para construir el Dockerfile directamente si la imagen no está creada anteriormente

```bash
docker-compose up -d

4. Subir la imagen a Docker Hub:

```bash
docker tag <nombre-imagen>:<tag> <tu_usuario_de_docker_hub>/<nombre-imagen>:<tag>
docker login
docker push <tu_usuario_de_docker_hub>/<nombre-imagen>:<tag>

5. Despliega el microservicio en Kubernetes

En mi caso, hice uso de Minikube

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

6. Exponiendo el microservicio

Para ello, comprobamos que el microservicio está levantando y obtenemos su nombre:
```bash
kubectl get pods

Luego, ya que no tengo acceso a Minikube externamente, hice uso de un port-forward para redirigir el tráfico y poder acceder externamente en local:
```bash
kubectl port-forward <nombre_del_pod> 8080:5000

## Prueba del microservicio

Para hacer uso y verificar que el microservicio funciona correctamente, hacemos una petición curl al puerto expuesto a través del port-forward
```bash
curl http://localhost:8080/people

esto te devolverá la lista de People ordenada por el campo nombre:
![image](https://github.com/user-attachments/assets/52e275dd-607c-4c04-9716-1f550eca031e)

## Puntos extra

1. Se ha configurado un HPA para escalar automáticamente el microservicio en función de la utilización de CPU.

Para aplicar el HPA:
```bash
kubectl apply -f hpa.yaml

2. Pruebas de rendimiento
Se ha creado un script de prueba de rendimiento con ab (test.sh).

Para ejecutar la prueba:
Asegúrate de que el port-forward esté activo:
```bash
kubectl port-forward <nombre_del_pod> 8080:5000

Dale permisos de ejecución al script:
```bash
chmod +x test.sh

Ejecuta el script:
```bash
./test.sh
