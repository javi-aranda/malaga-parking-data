import click
import pandas as pd
import os

@click.command()
@click.option("--year", help="Año de los datos solicitados.")
@click.option("--month", help="Mes solicitado.")
@click.option("--day", help="Día solicitado.")
def compute_daily(year, month, day):
    # Cargamos los datos de un día en un DataFrame
    data_path = os.path.join(os.getcwd(), year, month, day)
    csv_files = [name for name in os.listdir(data_path) if name.endswith(".csv") and name.startswith("parking-data")]
    # Excluir ficheros vacíos
    csv_files = [name for name in csv_files if os.stat(os.path.join(data_path, name)).st_size > 0]
    dataframes = []
    for file in csv_files:
        try:
            df = pd.read_csv(os.path.join(data_path, file))
        except pd.errors.EmptyDataError:
            print(f"Warning: {os.path.join(data_path, file)} está vacío o no puede ser parseado, ignorando.")
            continue
        except pd.errors.ParserError as e:
            print(f"Error leyendo {os.path.join(data_path, file)}, ignorando")
            continue
        dataframes.append(df)

    df = pd.concat(dataframes)

    # Convertir a tipo int las columnas capacidad, capacidad_discapacitados, libres y libres_discapacitados
    df["capacidad"] = df["capacidad"].fillna(-1).astype(int)
    df["capacidad_discapacitados"] = df["capacidad_discapacitados"].fillna(-1).astype(int)
    df["libres"] = df["libres"].fillna(-1).astype(int)
    df["libres_discapacitados"] = df["libres_discapacitados"].fillna(-1).astype(int)
    
    # Crear un DataFrame con las columnas poiID, nombre, capacidad, mean_libres, mean_libres_discapacitados, max_libres, max_libres_discapacitados, min_libres, min_libres_discapacitados
    stats_df = pd.DataFrame({"poiID": df.groupby("poiID")["poiID"].min(),
        "nombre": df.groupby("poiID")["nombre"].min(),
        "capacidad": df.groupby("poiID")["capacidad"].min(),
        "media_libres": df.groupby("poiID")["libres"].mean().astype(int),
        "media_libres_discapacitados": df.groupby("poiID")["libres_discapacitados"].mean().astype(int),
        "max_libres": df.groupby("poiID")["libres"].max().astype(int),
        "max_libres_discapacitados": df.groupby("poiID")["libres_discapacitados"].max().astype(int),
        "min_libres": df.groupby("poiID")["libres"].min().astype(int),
        "min_libres_discapacitados": df.groupby("poiID")["libres_discapacitados"].min().astype(int)
    })

    # Guardar el DataFrame en un fichero CSV
    stats_df.to_csv(os.path.join(data_path, "stats.csv"), index=False)

if __name__ == "__main__":
    compute_daily()
