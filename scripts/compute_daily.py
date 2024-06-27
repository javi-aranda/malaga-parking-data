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
    data_path = os.path.join(os.getcwd(), "data", year, month, day)
    csv_files = [
        name
        for name in os.listdir(data_path)
        if name.startswith("parking-data")
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

    df = pd.concat(dataframes).reset_index(drop=True)

    # Convertir a tipo int la columna "libres"
    df["libres"] = df["libres"].fillna(-1).astype(int)

    # Agrupar por ID y calcular estadísticas
    grouped_df = df.groupby("id")
    stats_df = pd.DataFrame(
        {
            "id": grouped_df["id"].min(),
            "media_libres": grouped_df["libres"].mean().astype(int),
            "max_libres": grouped_df["libres"].max(),
            "min_libres": grouped_df["libres"].min(),
            "max_time_libres": grouped_df.apply(
                lambda x: x.loc[x["libres"].idxmax(), "time"]
            ),
            "min_time_libres": grouped_df.apply(
                lambda x: x.loc[x["libres"].idxmin(), "time"]
            ),
        }
    )
    
    # Guardar el DataFrame en un fichero CSV
    stats_df.to_csv(os.path.join(data_path, "stats.csv"), index=False)


if __name__ == "__main__":
    compute_daily()
