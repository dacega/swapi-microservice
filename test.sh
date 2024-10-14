#!/bin/bash

# URL del microservicio (reemplaza con la IP y puerto del port-forward)
URL="http://localhost:8080/people"  

# Número de peticiones
NUM_REQUESTS=1000

# Concurrencia
CONCURRENCY=10

# Ejecutar la prueba con ab
ab -n $NUM_REQUESTS -c $CONCURRENCY $URL
