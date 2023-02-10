import os
import zipfile


def __cambiar_lineas(archivo, linea_a_cambiar, nueva_linea):
    with open(archivo, "r+") as file:
        lines = file.readlines()

        # Mover el cursor hasta la posición correcta
        file.seek(0)
        for i, line in enumerate(lines):
            if i + 1 == linea_a_cambiar:
                file.write(nueva_linea + "\n")
            else:
                file.write(line)

        # Truncar el archivo para eliminar líneas extra
        file.truncate()


def modificacion_de_archivos(path, nombre_proyecto):
    # cambiar el nombre de archivos
    os.rename(path + "/Nombre_Base.uvoptx", path + f"/{nombre_proyecto}.uvoptx")
    os.rename(path + "/Nombre_Base.uvprojx", path + f"/{nombre_proyecto}.uvprojx")
    os.rename(path + "/Nombre_Base.uvguix.humbe", path + f"/{nombre_proyecto}.uvguix.humbe")

    # Cambiar líneas de codigo
    __cambiar_lineas(path + f"/{nombre_proyecto}.uvprojx", 51, f"          <OutputName>{nombre_proyecto}</OutputName>")
    __cambiar_lineas(path + "/CMakeLists.txt", 2, f"project({nombre_proyecto})")
    __cambiar_lineas(path + "/CMakeLists.txt", 12, f"        {nombre_proyecto}")


def extraer(path):
    zip_file = zipfile.ZipFile('Base.zip', 'r')
    zip_file.extractall(path)
    zip_file.close()
