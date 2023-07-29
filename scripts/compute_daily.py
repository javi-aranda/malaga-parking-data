import datetime
import os

import click
import pandas as pd


@click.command()
@click.option("--year", help="Año de los datos solicitados.")
@click.option("--month", help="Mes solicitado.")
@click.option("--day", help="Día solicitado.")
def compute_daily(year, month, day):
    # Cargamos los datos de un día en un DataFrame
    data_path = os.path.join(os.getcwd(), year, month, day)
    csv_files = [
        name
        for name in os.listdir(data_path)
        if name.endswith(".csv") and name.startswith("parking-data")
    ]
    # Excluir ficheros vacíos
    csv_files = [
        name for name in csv_files if os.stat(os.path.join(data_path, name)).st_size > 0
    ]
    dataframes = []
    for file in csv_files:
        try:
            df = pd.read_csv(os.path.join(data_path, file))
        except pd.errors.EmptyDataError:
            print(f"Warning: {os.path.join(data_path, file)} está vacío, ignorando.")
            continue
        except pd.errors.ParserError:
            print(f"Error leyendo {os.path.join(data_path, file)}, ignorando")
            continue

        # Añadir columna con la hora
        hour, minute = file.split(".")[0].split("-")[-1].split("_")
        df["time"] = datetime.time(hour=int(hour), minute=int(minute))

        dataframes.append(df)

    df = pd.concat(dataframes)

    # Convertir a tipo int varias columnas
    df["capacidad"].replace("None", -1, inplace=True)
    df["capacidad_discapacitados"].replace("None", -1, inplace=True)
    df["libres"].replace("None", -1, inplace=True)
    df["libres_discapacitados"].replace("None", -1, inplace=True)

    df_cols_to_numeric = [
        "capacidad",
        "capacidad_discapacitados",
        "libres",
        "libres_discapacitados",
    ]

    df[df_cols_to_numeric] = df[df_cols_to_numeric].astype(int)

    df_grouped = df.groupby("poiID")

    # Preparar un DataFrame con valores de las columnas agregados
    poiID = df_grouped["poiID"].min()
    nombre = df_grouped["nombre"].min()
    capacidad = df_grouped["capacidad"].min()
    media_libres = df_grouped["libres"].mean().astype(int)
    media_libres_discapacitados = df_grouped["libres_discapacitados"].mean().astype(int)
    max_libres = df_grouped["libres"].max().astype(int)
    max_libres_discapacitados = df_grouped["libres_discapacitados"].max().astype(int)
    min_libres = df_grouped["libres"].min().astype(int)
    min_libres_discapacitados = df_grouped["libres_discapacitados"].min().astype(int)

    # Obtener índices de máximos y mínimos de aparcamientos libres y libres_discapacitados
    max_libres_idx = df_grouped["libres"].idxmax()
    min_libres_idx = df_grouped["libres"].idxmin()
    max_libres_discapacitados_idx = df_grouped["libres_discapacitados"].idxmax()
    min_libres_discapacitados_idx = df_grouped["libres_discapacitados"].idxmin()

    # Usar los índices para obtener las horas de los máximos y mínimos
    default_time = "00:00:00"
    max_time_libres = df.loc[max_libres_idx, "time"].fillna(default_time).values
    min_time_libres = df.loc[min_libres_idx, "time"].fillna(default_time).values
    max_time_libres_discapacitados = (
        df.loc[max_libres_discapacitados_idx, "time"].fillna(default_time).values
    )
    min_time_libres_discapacitados = (
        df.loc[min_libres_discapacitados_idx, "time"].fillna(default_time).values
    )

    # Crear DataFrame con los datos agregados
    stats_df = pd.DataFrame(
        {
            "poiID": poiID,
            "nombre": nombre,
            "capacidad": capacidad,
            "media_libres": media_libres,
            "media_libres_discapacitados": media_libres_discapacitados,
            "max_libres": max_libres,
            "max_libres_discapacitados": max_libres_discapacitados,
            "max_time_libres": max_time_libres,
            "max_time_libres_discapacitados": max_time_libres_discapacitados,
            "min_libres": min_libres,
            "min_libres_discapacitados": min_libres_discapacitados,
            "min_time_libres": min_time_libres,
            "min_time_libres_discapacitados": min_time_libres_discapacitados,
        }
    )

    # Convert float columns to integers
    stats_df_cols_to_numeric = [
        "poiID",
        "capacidad",
        "media_libres",
        "media_libres_discapacitados",
        "max_libres",
        "max_libres_discapacitados",
        "min_libres",
        "min_libres_discapacitados",
    ]
    stats_df[stats_df_cols_to_numeric] = stats_df[stats_df_cols_to_numeric].astype(int)

    # Guardar el DataFrame en un fichero CSV
    stats_df.to_csv(os.path.join(data_path, "stats.csv"), index=False)


if __name__ == "__main__":
    compute_daily()
