

# About

El proyecto `BlockCompUVG` que es la extensión de [CompetencySystemApi](https://github.com/paulbelches/CompetencySystemApi.git) de manera que este provea no solo la funcionalidad básica de interactuar con contractos inteligentes directametne con un frontend. 

Si bien el proyecto proveía las capacidades de interactuar con el contrato inteligente y hacer la transferencia de competencias de manera práctica, no contaba con buenas prácticas en cuanto al manejo de los datos haciendo uso de `json-server`. A si mismo no contaba con una persistencia de datos 

# ¿Mono repo?

La organización de este proyecto se basa en la realización de un monorepo como se hace en `Poliltyth` pero con ciertas libertades en la forma en que se usan los directorios. La motivación detrás de imitar este patrón esta en la reutilización de código como lo son los modelos generables con pydantic. A crriterio personal considero que la abstracción de los bloques. 

Respecto a las libertades tomadas es importante mencionar que cambia un poco el uso de los directorios. 

- **bases**: Desaparece por completo y en todo caso cualquier *entrypoint* al proyecto son trasladado a *projects*. 
- **components**: En esencia se mantiene como el directorio con los 
- **deveploment**: Se mantiene igual. 
- **projects**: En el esquema original estas carpetas contienen archivo de configuración `toml`, sin embargo, en este esquema se encuentra el punto de entrada de los distintos servicios (`app.py`, `main.py`, etc.) también encontramos archivos de configuracion y son el espacio en el que encontramos `requirements.txt`, `venv` y  


# Proyectos

# Ganache


# BlockCompUVG - API (Fastapi)


