# Málaga Parking Data
[![Últimos datos recogidos satisfactoriamente](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/update_data.yml/badge.svg)](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/update_data.yml)
[![Estadísticas diarias calculadas](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/compute_daily.yml/badge.svg)](https://github.com/javi-aranda/malaga-parking-data/actions/workflows/compute_daily.yml)


El propósito de este proyecto es tener un scraper automatizado mediante GitHub Actions que recoja
la información de aparcamientos públicos disponibles en tiempo semi-real, utilizando para ello
el portal de Datos Abiertos de Málaga.

## Últimos datos recopilados
Los datos recopilados más actualizados se encuentran en el fichero [latest.csv](https://github.com/javisenberg/malaga-parking-data/blob/master/latest.csv).

## Potenciales aplicaciones
Con una serie importante de datos se pueden realizar análisis estadísticos sobre el uso de los
aparcamientos públicos a lo largo del tiempo, cruzando datos como puedan ser factores meteorológicos,
festivos locales o eventos de interés general.

## Scripts
El proyecto cuenta con una serie de scripts que utilizan la biblioteca `pandas` para procesar los datos
recogidos y calcular ciertas estadísticas.
