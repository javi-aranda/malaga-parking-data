#!/bin/bash

# Contador de elementos eliminados
deleted_count=0

# Determinar si un archivo debe ser eliminado
should_delete() {
    if [[ -z "$1" || $(head -n 1 "$1") == "<!DOCTYPE html>" ]]; then
        return 0
    fi
    return 1
}

# Procesar directorio de forma recursiva
process_directory() {
    for file in "$1"/*; do
        if [ -f "$file" ]; then
            if should_delete "$file"; then
                rm "$file"
                deleted_count=$((deleted_count + 1))
            fi
        elif [ -d "$file" ]; then
            process_directory "$file"
        fi
    done
}

# Ejecutar el script en los directorios que tengan estructura numérica (años)
for dir in [0-9][0-9][0-9][0-9]; do
    if [ -d "$dir" ]; then
        process_directory "$dir"
    fi
done

echo "Deleted $deleted_count files."




