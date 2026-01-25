# Clasificador de Archivos

Una potente utilidad Python multiplataforma para organizar archivos y carpetas automáticamente según sus extensiones, nombres de carpetas o marcas de tiempo.

## Características

- **Múltiples Métodos de Clasificación**:
  - **Basado en Extensiones**: Clasifica archivos en categorías según sus extensiones
  - **Basado en Tiempo**: Organiza archivos por tiempo de creación, modificación o acceso
  - **Clasificación de Carpetas**: Categoriza carpetas según patrones comunes de nomenclatura

- **Categorías de Archivos**:
  - Documentos (PDF, DOC, TXT, etc.)
  - Imágenes (JPG, PNG, GIF, etc.)
  - Audio (MP3, WAV, FLAC, etc.)
  - Videos (MP4, AVI, MKV, etc.)
  - Archivos Comprimidos (ZIP, RAR, 7Z, etc.)
  - Código (PY, JAVA, HTML, etc.)
  - Ejecutables (EXE, MSI, APP, etc.)
  - Otros (para extensiones no incluidas en las categorías anteriores)

- **Categorías de Carpetas**:
  - Projects: Para carpetas de desarrollo y proyectos
  - Backups: Para contenido de respaldo y archivado
  - Documents: Para carpetas de documentos e informes
  - Media: Para carpetas de fotos, videos, música
  - Downloads: Para carpetas de descargas
  - Applications: Para software y aplicaciones
  - Data: Para conjuntos de datos y bases de datos
  - Web: Para contenido relacionado con la web
  - Dated: Para carpetas con patrones de fecha (detectados automáticamente)
  - Versioned: Para carpetas con patrones de versión (detectados automáticamente)
  - Uncategorized: Para carpetas que no coinciden con ningún patrón

- **Modos de Operación**:
  - Mover (predeterminado): Mueve archivos/carpetas a directorios de destino
  - Copiar: Crea copias en lugar de mover
  - Enlace simbólico: Crea enlaces simbólicos a archivos/carpetas originales
  - Simulación: Muestra qué sucedería sin realizar cambios

- **Compatibilidad Multiplataforma**:
  - Funciona en Windows, macOS y Linux

## Requisitos

- Python 3.6 o superior
- No se requieren bibliotecas adicionales (usa solo la biblioteca estándar)

## Instalación

Si tienes el código fuente, puedes ejecutarlo como un módulo:

```bash
python -m fl_classifier [opciones]
```

## Uso

### Uso Básico

```bash
python -m fl_classifier DIR_ORIGEN [DIR_DESTINO]
```

Si no se especifica `DIR_DESTINO`, los archivos se organizarán en un nuevo directorio llamado `./classified`.

### Opciones Comunes

```
-l, --symlinks       Crear enlaces simbólicos en lugar de mover archivos
-c, --copy           Copiar archivos en lugar de moverlos
-d, --dry-run        Mostrar qué se haría sin realizar cambios reales
-f, --folders        Incluir carpetas en la clasificación
```

### Métodos de Clasificación

```
-e, --extensions     Clasificar por extensiones de archivo (comportamiento predeterminado)
-t, --time           Organizar por atributo de tiempo
```

### Opciones de Organización Basada en Tiempo

```
--time-attr {modified,created,accessed}
                     Atributo de tiempo a utilizar (predeterminado: modified)
--time-format FORMATO
                     Formato de tiempo para directorios (predeterminado: '%Y-%m' para año-mes)
```

## Ejemplos

### Organización Basada en Extensiones

```bash
# Clasificar todos los archivos en la carpeta Descargas por extensión
python -m fl_classifier ~/Downloads ~/Organized

# Clasificar archivos y carpetas, crear copias en lugar de moverlos
python -m fl_classifier ~/Documents ~/Organized -f -c

# Crear enlaces simbólicos en lugar de mover archivos
python -m fl_classifier ~/Pictures ~/Organized -l

# Vista previa de lo que sucedería sin realizar cambios
python -m fl_classifier ~/Desktop -d
```

### Organización Basada en Tiempo

```bash
# Organizar archivos por su tiempo de modificación (año-mes)
python -m fl_classifier ~/Documents ~/TimeOrganized -t

# Organizar por fecha de creación con formato año-mes-día
python -m fl_classifier ~/Photos ~/Chronological -t --time-attr created --time-format "%Y-%m-%d"

# Organizar archivos y carpetas por tiempo de acceso
python -m fl_classifier ~/Downloads ~/AccessOrganized -t --time-attr accessed -f
```

## Preguntas Frecuentes

**P: ¿Qué sucede si un archivo o carpeta ya existe en el directorio de destino?**
R: El script lo omitirá y registrará un mensaje de advertencia.

**P: ¿La organización preservará la estructura de directorios?**
R: No, todos los archivos se aplanan a los directorios de categoría correspondientes. Para una organización jerárquica, considera usar la organización basada en tiempo con un formato jerárquico como `%Y/%m/%d`.

**P: ¿Puedo personalizar las categorías de archivos?**
R: Sí, puedes editar el diccionario `FILE_CATEGORIES` en el script para agregar o modificar categorías.

## Licencia

Esta utilidad se publica bajo la Licencia MIT. Siéntete libre de usarla, modificarla y distribuirla.
