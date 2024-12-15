# Málaga Parking Data
[![Últimos datos recogidos satisfactoriamente](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/update_data.yml/badge.svg)](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/update_data.yml)
[![Estadísticas diarias calculadas](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/compute_daily.yml/badge.svg)](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/compute_daily.yml)
[![Ejecutar limpieza semanal](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/cleanup_weekly.yml/badge.svg)](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/cleanup_weekly.yml)

El propósito de este proyecto es tener un scraper automatizado mediante GitHub Actions que recoja
la información de aparcamientos públicos disponibles en tiempo semi-real, utilizando para ello
el portal de Datos Abiertos de Málaga.

## Últimos datos recopilados
Los datos recopilados más actualizados se encuentran en el fichero [latest.csv](https://github.com/javi-aranda/malaga-parking-data/blob/main/latest.csv).

La referencia de los códigos utilizados para identificar los distintos aparcamientos está recogida
en [catalogo.csv](https://github.com/javi-aranda/malaga-parking-data/blob/main/catalogo.csv).

## Potenciales aplicaciones
Con una serie importante de datos se pueden realizar análisis estadísticos sobre el uso de los
aparcamientos públicos a lo largo del tiempo, cruzando datos como puedan ser factores meteorológicos,
festivos locales o eventos de interés general.

## Scripts
El proyecto cuenta con una serie de scripts en Python que utilizan la biblioteca `pandas` para procesar 
los datos recogidos y calcular ciertas estadísticas. También cuenta con utilidades para limpiar los 
datos que no son válidos de forma periódica, ayudando a mantener una consistencia a lo largo del repositorio.

## Dashboard
Para facilitar la consulta de los datos existe el proyecto [Málaga Parking Dashboard](https://malaga-parking.streamlit.app),
que permite explorar los últimos resultados obtenidos directamente en el mapa para conocer el estado
de los aparcamientos, y además incluye un buscador temporal para poder desgranar la información
en periodos de tiempo concretos. El código de este proyecto se encuentra en [malaga-parking-dashboard](https://github.com/javi-aranda/malaga-parking-dashboard).
