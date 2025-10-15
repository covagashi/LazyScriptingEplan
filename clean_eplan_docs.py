#!/usr/bin/env python3
"""
Script para limpiar la documentación de EPLAN.
Limpia:
1. Tablas de código innecesarias (formato "| C# | Copy Code |")
2. Líneas de separación vacías redundantes
3. Bloques de código vacíos
"""

import os
import re
from pathlib import Path
from typing import Tuple


def clean_see_also_section(content: str) -> Tuple[str, bool]:
    """
    Elimina la sección "See Also" y todo lo que viene después.

    Args:
        content: Contenido del archivo markdown

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    # Buscar "See Also" con diferentes variaciones
    pattern = r'\n\s*See Also\s*\n.*'

    if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
        cleaned_content = re.sub(pattern, '\n', content, flags=re.IGNORECASE | re.DOTALL)
        return cleaned_content.rstrip() + '\n', True

    return content, False


def clean_code_tables(content: str) -> Tuple[str, bool]:
    """
    Convierte tablas de código en bloques de código normales.

    Detecta patrones como:
    | C# | Copy Code |
    | --- | --- |
    | ``` code ``` | |

    Y los convierte a:
    ```csharp
    code
    ```

    Args:
        content: Contenido del archivo markdown

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    modified = False

    # Patrón para detectar tablas de código
    # Captura: | Language | Copy Code |
    #          | --- | --- |
    #          | ``` código ``` | |
    pattern = r'\|\s*(C#|C\+\+/CLI|VB|Python|JavaScript)\s*\|\s*Copy Code\s*\|\s*\n\|\s*---\s*\|\s*---\s*\|\s*\n\|\s*```\s*(.*?)\s*```\s*\|\s*\|'

    def replace_table(match):
        nonlocal modified
        modified = True
        language = match.group(1).strip()
        code = match.group(2).strip()

        # Mapear lenguajes a identificadores de código
        lang_map = {
            'C#': 'csharp',
            'C++/CLI': 'cpp',
            'VB': 'vb',
            'Python': 'python',
            'JavaScript': 'javascript'
        }

        lang_id = lang_map.get(language, language.lower())

        # Retornar bloque de código limpio
        return f'```{lang_id}\n{code}\n```'

    cleaned_content = re.sub(pattern, replace_table, content, flags=re.DOTALL)

    return cleaned_content, modified


def clean_empty_code_blocks(content: str) -> Tuple[str, bool]:
    """
    Elimina bloques de código vacíos o que solo contienen espacios.

    Args:
        content: Contenido del archivo markdown

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    modified = False

    # Patrón para bloques de código vacíos: ``` ``` (con o sin lenguaje)
    pattern = r'```[a-z]*\s*```'

    if re.search(pattern, content, re.IGNORECASE):
        cleaned_content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        modified = True
        return cleaned_content, modified

    return content, False


def clean_redundant_empty_lines(content: str) -> Tuple[str, bool]:
    """
    Reduce múltiples líneas vacías consecutivas a máximo 2.

    Args:
        content: Contenido del archivo markdown

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    original_content = content

    # Reemplazar 3 o más líneas vacías consecutivas por 2
    cleaned_content = re.sub(r'\n\s*\n\s*\n(\s*\n)+', '\n\n', content)

    modified = cleaned_content != original_content
    return cleaned_content, modified


def clean_duplicate_tab_links(content: str) -> Tuple[str, bool]:
    """
    Elimina los enlaces de navegación de tabs de código, manteniendo solo el texto.

    Convierte:
    - [C#](#i-tab-content-xxx)
    - [VB](#i-tab-content-yyy)

    En:
    **C#**
    **VB**

    Args:
        content: Contenido del archivo markdown

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    modified = False

    # Patrón para detectar líneas con enlaces de tab-content
    # Captura el nombre del lenguaje
    pattern = r'^-\s*\[(C#|C\+\+/CLI|VB|Python|JavaScript|\.NET)\]\(#i-(?:tab-content|syntax)-[A-Za-z0-9-]+\)\s*$'

    lines = content.split('\n')
    cleaned_lines = []

    for line in lines:
        match = re.match(pattern, line)
        if match:
            modified = True
            # Reemplazar con el nombre del lenguaje en negrita
            language = match.group(1)
            cleaned_lines.append(f'**{language}**')
        else:
            cleaned_lines.append(line)

    cleaned_content = '\n'.join(cleaned_lines)

    return cleaned_content, modified


def remove_vb_keep_csharp(content: str) -> Tuple[str, bool]:
    """
    Elimina código VB de bloques mixtos C#/VB, manteniendo solo C#.

    Detecta patrones como:
    **C#**
    **VB**
    ```
    código mezclado C# y VB
    ```

    Y los convierte a:
    **C#**
    ```csharp
    solo código C#
    ```

    Args:
        content: Contenido del archivo markdown

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    modified = False

    # Patrón para detectar bloques mixtos: **C#** seguido de **VB** y luego un bloque de código
    pattern = r'\*\*C#\*\*\s*\n\*\*VB\*\*\s*\n\s*```\s*\n(.*?)\n```'

    def extract_csharp_only(match):
        nonlocal modified
        modified = True

        mixed_code = match.group(1)
        lines = mixed_code.split('\n')

        csharp_lines = []
        in_vb_section = False

        for line in lines:
            # Detectar líneas VB que deben eliminarse siempre
            if any([
                line.strip().startswith('Dim '),
                line.strip().startswith('Private Sub '),
                line.strip().startswith('Public Sub '),
                line.strip().startswith('Function '),
                line.strip().startswith('End Sub'),
                line.strip().startswith('End Function'),
                line.strip().startswith('End If'),
                line.strip().startswith('End Class \''),  # Comentario VB al final
                line.strip().startswith('End '),
                ((' As ' in line or ' as ' in line) and
                 (line.strip().startswith('Dim ') or 'ByVal ' in line or 'ByRef ' in line)),
                'ByVal ' in line and '(' in line,
                'Handles ' in line,
                line.strip().startswith('If Not ') and ' Is Nothing Then' in line,
                line.strip().endswith(' Then'),
                line.strip().startswith("'") and not line.strip().startswith("'//"),
                ' & vbCrLf' in line,
                'Is Nothing' in line,
                line.strip().startswith('Catch ') and ' As ' in line and not '{' in line,
            ]):
                in_vb_section = True
                continue  # Saltar esta línea VB

            # Si estamos en VB, saltar hasta encontrar línea vacía o código C#
            if in_vb_section:
                # Detectar si volvemos a C# (línea vacía seguida de código C# o claramente C#)
                if line.strip() == '':
                    # Línea vacía, posible cambio a C#
                    in_vb_section = False
                    continue
                elif any([
                    line.strip().startswith('//'),
                    '{' in line or '}' in line,
                    line.strip().endswith(';'),
                    ' new ' in line and '(' in line,
                ]):
                    in_vb_section = False
                    # No continuar, procesar esta línea como C#
                else:
                    continue  # Seguimos en VB, saltar línea

            # Agregar línea C# (si no está vacía o es relevante)
            if not in_vb_section:
                csharp_lines.append(line)

        # Limpiar líneas vacías del inicio y final
        csharp_code = '\n'.join(csharp_lines).strip()

        # Si hay código C#, crear bloque
        if csharp_code:
            return f'**C#**\n```csharp\n{csharp_code}\n```'
        else:
            return '**C#**\n```csharp\n// Code removed\n```'

    cleaned_content = re.sub(pattern, extract_csharp_only, content, flags=re.DOTALL)

    return cleaned_content, modified


def clean_corrupted_characters(content: str) -> Tuple[str, bool]:
    """
    Elimina o reemplaza caracteres especiales corruptos.

    Reemplaza:
    - â → - (guion largo corrupto)
    - â¢ → (elimina bullet corrupto)
    - Â → (elimina espacio no-break corrupto)
    - € → (elimina)
    - œ → (elimina)
    - â → " (comillas)
    - â → " (comillas)

    Args:
        content: Contenido del archivo markdown

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    original_content = content

    # Diccionario de reemplazos
    replacements = {
        'â': '-',        # Guion largo corrupto
        'â¢': '',        # Bullet point corrupto
        'Â®': '®',       # Símbolo registered
        'Â': '',         # Espacio no-break corrupto
        '€': '',         # Euro corrupto
        'œ': '',         # Ligadura corrupta
        'â': '"',       # Comilla izquierda
        'â': '"',       # Comilla derecha
        'â': "'",       # Apóstrofe
        'Â°': '°',       # Símbolo de grado
        'Â·': '·',       # Middle dot
        'Ã©': 'é',       # e con acento
        'Ã¡': 'á',       # a con acento
        'Ã³': 'ó',       # o con acento
        'Ãº': 'ú',       # u con acento
        'Ã­': 'í',       # i con acento
        'Ã±': 'ñ',       # ñ
    }

    cleaned_content = content
    for old_char, new_char in replacements.items():
        cleaned_content = cleaned_content.replace(old_char, new_char)

    modified = cleaned_content != original_content
    return cleaned_content, modified


def process_file(file_path: Path) -> dict:
    """
    Procesa un archivo markdown individual.

    Args:
        file_path: Ruta al archivo

    Returns:
        Diccionario con estadísticas del procesamiento
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        content = original_content
        stats = {
            'see_also_removed': False,
            'code_tables_cleaned': False,
            'empty_blocks_removed': False,
            'empty_lines_cleaned': False,
            'tab_links_cleaned': False,
            'vb_code_removed': False,
            'corrupted_chars_fixed': False
        }

        # Limpiar sección "See Also"
        content, stats['see_also_removed'] = clean_see_also_section(content)

        # Limpiar tablas de código
        content, stats['code_tables_cleaned'] = clean_code_tables(content)

        # Eliminar bloques de código vacíos
        content, stats['empty_blocks_removed'] = clean_empty_code_blocks(content)

        # Limpiar líneas vacías redundantes
        content, stats['empty_lines_cleaned'] = clean_redundant_empty_lines(content)

        # Limpiar enlaces de tabs duplicados
        content, stats['tab_links_cleaned'] = clean_duplicate_tab_links(content)

        # Eliminar código VB, mantener solo C#
        content, stats['vb_code_removed'] = remove_vb_keep_csharp(content)

        # Limpiar caracteres corruptos
        content, stats['corrupted_chars_fixed'] = clean_corrupted_characters(content)

        # Solo escribir si hubo cambios
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                'processed': True,
                **stats
            }

        return {'processed': False}

    except Exception as e:
        return {'error': str(e)}


def main():
    """Función principal."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Limpia archivos markdown de la documentación de EPLAN'
    )
    parser.add_argument(
        'path',
        type=str,
        default=r'D:\LazyScriptingEplan\src\ai\Knowledge\eplan_docs\Eplan API',
        nargs='?',
        help='Ruta al directorio con los archivos (default: directorio de EPLAN API)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Mostrar qué archivos se modificarían sin hacer cambios'
    )

    args = parser.parse_args()

    base_path = Path(args.path)

    if not base_path.exists():
        print(f"Error: La ruta {base_path} no existe")
        return 1

    # Encontrar todos los archivos .md
    md_files = list(base_path.rglob('*.md'))

    print(f"Encontrados {len(md_files)} archivos markdown")
    print(f"Iniciando limpieza...")
    if args.dry_run:
        print("(MODO DRY-RUN: No se harán cambios)")
    print()

    stats = {
        'total': len(md_files),
        'modified': 0,
        'see_also_removed': 0,
        'code_tables_cleaned': 0,
        'empty_blocks_removed': 0,
        'empty_lines_cleaned': 0,
        'tab_links_cleaned': 0,
        'vb_code_removed': 0,
        'corrupted_chars_fixed': 0,
        'errors': 0
    }

    for i, file_path in enumerate(md_files, 1):
        if i % 500 == 0:
            print(f"Procesando: {i}/{len(md_files)} archivos...")

        if args.dry_run:
            # En dry-run, solo leer y analizar
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                _, code_tables_found = clean_code_tables(content)

                if code_tables_found:
                    stats['modified'] += 1
                    stats['code_tables_cleaned'] += 1
                    print(f"  [DRY-RUN] Modificaría: {file_path.relative_to(base_path)}")

            except Exception as e:
                stats['errors'] += 1
                print(f"  [ERROR] {file_path.relative_to(base_path)}: {e}")
        else:
            result = process_file(file_path)

            if result.get('error'):
                stats['errors'] += 1
                print(f"  [ERROR] {file_path.relative_to(base_path)}: {result['error']}")
            elif result.get('processed'):
                stats['modified'] += 1
                if result.get('see_also_removed'):
                    stats['see_also_removed'] += 1
                if result.get('code_tables_cleaned'):
                    stats['code_tables_cleaned'] += 1
                if result.get('empty_blocks_removed'):
                    stats['empty_blocks_removed'] += 1
                if result.get('empty_lines_cleaned'):
                    stats['empty_lines_cleaned'] += 1
                if result.get('tab_links_cleaned'):
                    stats['tab_links_cleaned'] += 1
                if result.get('vb_code_removed'):
                    stats['vb_code_removed'] += 1
                if result.get('corrupted_chars_fixed'):
                    stats['corrupted_chars_fixed'] += 1

    # Mostrar resumen
    print()
    print("=" * 60)
    print("RESUMEN")
    print("=" * 60)
    print(f"Total de archivos procesados: {stats['total']}")
    print(f"Archivos modificados: {stats['modified']}")
    print(f"  - Secciones 'See Also' eliminadas: {stats['see_also_removed']}")
    print(f"  - Tablas de código limpiadas: {stats['code_tables_cleaned']}")
    print(f"  - Bloques vacíos eliminados: {stats['empty_blocks_removed']}")
    print(f"  - Líneas vacías limpiadas: {stats['empty_lines_cleaned']}")
    print(f"  - Enlaces de tabs convertidos a títulos: {stats['tab_links_cleaned']}")
    print(f"  - Código VB eliminado (solo C#): {stats['vb_code_removed']}")
    print(f"  - Caracteres corruptos corregidos: {stats['corrupted_chars_fixed']}")
    print(f"Errores: {stats['errors']}")
    print()

    if args.dry_run:
        print("NOTA: Esto fue una ejecución de prueba. Ejecuta sin --dry-run para aplicar los cambios.")

    return 0


if __name__ == '__main__':
    exit(main())
