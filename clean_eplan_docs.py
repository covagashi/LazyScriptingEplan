#!/usr/bin/env python3
"""
Script para limpiar la documentación de EPLAN.
Elimina:
1. Secciones "See Also" y todo lo que viene después
2. Opcionalmente, enlaces de imágenes rotos
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
    # Buscar "See Also" con diferentes variaciones (puede tener espacios, saltos de línea, etc.)
    pattern = r'\n\s*See Also\s*\n.*'

    if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
        cleaned_content = re.sub(pattern, '\n', content, flags=re.IGNORECASE | re.DOTALL)
        return cleaned_content.rstrip() + '\n', True

    return content, False


def remove_broken_image_links(content: str, base_path: Path) -> Tuple[str, bool]:
    """
    Elimina enlaces de imágenes que no existen en el sistema de archivos.

    Args:
        content: Contenido del archivo markdown
        base_path: Ruta base del archivo actual para resolver rutas relativas

    Returns:
        Tupla de (contenido limpio, fue_modificado)
    """
    modified = False

    # Patrón para encontrar enlaces de imágenes markdown
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'

    def check_image(match):
        nonlocal modified
        alt_text = match.group(1)
        image_path = match.group(2)

        # Si es una URL, la dejamos
        if image_path.startswith(('http://', 'https://', '//')):
            return match.group(0)

        # Resolver la ruta relativa
        full_path = (base_path.parent / image_path).resolve()

        # Si la imagen no existe, eliminar el enlace
        if not full_path.exists():
            modified = True
            return ''  # Eliminar el enlace completamente

        return match.group(0)

    cleaned_content = re.sub(image_pattern, check_image, content)

    return cleaned_content, modified


def process_file(file_path: Path, remove_images: bool = False) -> dict:
    """
    Procesa un archivo markdown individual.

    Args:
        file_path: Ruta al archivo
        remove_images: Si True, también elimina enlaces de imágenes rotos

    Returns:
        Diccionario con estadísticas del procesamiento
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        content = original_content
        see_also_removed = False
        images_removed = False

        # Limpiar sección "See Also"
        content, see_also_removed = clean_see_also_section(content)

        # Opcionalmente eliminar imágenes rotas
        if remove_images:
            content, images_removed = remove_broken_image_links(content, file_path)

        # Solo escribir si hubo cambios
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                'processed': True,
                'see_also_removed': see_also_removed,
                'images_removed': images_removed
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
        '--remove-images',
        action='store_true',
        help='También eliminar enlaces de imágenes rotos'
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
        'images_removed': 0,
        'errors': 0
    }

    for i, file_path in enumerate(md_files, 1):
        if i % 100 == 0:
            print(f"Procesando: {i}/{len(md_files)} archivos...")

        if args.dry_run:
            # En dry-run, solo leer y analizar
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                _, see_also_found = clean_see_also_section(content)

                if see_also_found:
                    stats['modified'] += 1
                    stats['see_also_removed'] += 1
                    print(f"  [DRY-RUN] Modificaría: {file_path.relative_to(base_path)}")

            except Exception as e:
                stats['errors'] += 1
                print(f"  [ERROR] {file_path.relative_to(base_path)}: {e}")
        else:
            result = process_file(file_path, remove_images=args.remove_images)

            if result.get('error'):
                stats['errors'] += 1
                print(f"  [ERROR] {file_path.relative_to(base_path)}: {result['error']}")
            elif result.get('processed'):
                stats['modified'] += 1
                if result.get('see_also_removed'):
                    stats['see_also_removed'] += 1
                if result.get('images_removed'):
                    stats['images_removed'] += 1

    # Mostrar resumen
    print()
    print("=" * 60)
    print("RESUMEN")
    print("=" * 60)
    print(f"Total de archivos procesados: {stats['total']}")
    print(f"Archivos modificados: {stats['modified']}")
    print(f"  - Con 'See Also' eliminado: {stats['see_also_removed']}")
    if args.remove_images:
        print(f"  - Con imágenes eliminadas: {stats['images_removed']}")
    print(f"Errores: {stats['errors']}")
    print()

    if args.dry_run:
        print("NOTA: Esto fue una ejecución de prueba. Ejecuta sin --dry-run para aplicar los cambios.")

    return 0


if __name__ == '__main__':
    exit(main())
