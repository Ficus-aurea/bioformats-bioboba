import click
from pathlib import Path
from analyze_fastq import analyze_fastq


@click.command()
@click.argument(
    'file_path',
    type=click.Path(exists=True, path_type=Path, readable=True)
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Выводить подробную информацию о процессе анализа'
)
@click.version_option(version='1.0.0', prog_name='FASTQ Analyzer')
def main(file_path: Path, verbose: bool) -> None:
    """
    Демонстрационный скрипт для анализа FASTQ-файлов.
    
    Выполняет визуальный и статистический анализ FASTQ-файла FILE_PATH
    (возможно, сжатого в формате .gz).
    
    Примеры:
    
    \b
        python run_fastq.py example.fastq
        python run_fastq.py example.fastq.gz --verbose
    """
    if verbose:
        click.echo(f"Начинаем анализ файла: {file_path}")
        click.echo(f"Размер файла: {file_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    click.echo(f"Анализ файла: {file_path}")
    click.echo("-" * 40)
    
    try:
        analyze_fastq(file_path)
        if verbose:
            click.echo("Анализ завершен успешно!")
    except Exception as e:
        click.echo(f Ошибка при анализе файла: {e}", err=True)
        raise click.Abort()


if __name__ == "__main__":
    main()
