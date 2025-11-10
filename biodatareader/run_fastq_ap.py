import argparse
from pathlib import Path
from analyze_fastq import analyze_fastq


def main() -> None:
    """
    Основная функция демонстрационного скрипта для анализа FASTQ-файлов.

    Скрипт принимает путь к FASTQ-файлу (возможно, сжатому в формате .gz) 
    и выполняет визуальный и статистический анализ.

    Example:
        Запуск из командной строки:

        .. code-block:: bash

            python run_fastq.py example.fastq
            python run_fastq.py -f example.fastq.gz
    """
    parser = argparse.ArgumentParser(
        description="Анализ FASTQ-файлов: визуализация и статистика",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python run_fastq.py example.fastq
  python run_fastq.py --file example.fastq.gz
        """
    )
    
    parser.add_argument(
        'file',
        type=Path,
        help='Путь к FASTQ-файлу (может быть сжат в .gz)'
    )
    
    parser.add_argument(
        '-f', '--file',
        dest='file_path',
        type=Path,
        help='Альтернативный способ указания файла',
        metavar='FILE'
    )
    
    args = parser.parse_args()
    
    # Используем file_path если указан, иначе file
    file_path = args.file_path if args.file_path else args.file
    
    if not file_path.exists():
        parser.error(f"Файл не найден: {file_path}")
    
    print(f"Анализ файла: {file_path}")
    print("-" * 40)
    analyze_fastq(file_path)


if __name__ == "__main__":
    main()
