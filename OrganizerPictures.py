import os
import shutil
from datetime import datetime
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS

# Lista de extensões suportadas (incluindo o formato do iPhone)
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".mp4", ".mov", ".avi", ".heic"}

# Caminho do log
log_file = "organizer_log.txt"

def get_exif_date(file_path):
    """
    Tenta obter a data "Date Taken" (DateTimeOriginal) dos metadados EXIF da imagem.
    Retorna None se não encontrar ou se o arquivo não suportar EXIF.
    """
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    if TAGS.get(tag) == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except UnidentifiedImageError:
        pass  # Arquivo não é uma imagem suportada pelo Pillow
    except Exception as e:
        write_log(f"Erro ao acessar EXIF de {file_path}: {e}")
    return None

def get_file_date(file_path):
    """
    Obtém a data de criação do arquivo:
    - Prioriza a data "Date Taken" (DateTimeOriginal) dos metadados EXIF.
    - Se não houver EXIF ou for um vídeo, usa a data de modificação do arquivo.
    - Retorna None se nenhuma data válida for encontrada.
    """
    # Tentar obter a data dos metadados EXIF
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.heic')):
        exif_date = get_exif_date(file_path)
        if exif_date:
            return exif_date

    # Se não houver EXIF, usa a data de modificação do arquivo
    try:
        timestamp = os.path.getmtime(file_path)
        file_date = datetime.fromtimestamp(timestamp)
        # Verifica se a data é plausível (evita anos como 1980)
        if file_date.year > 1990:  # Ajuste o limite inferior se necessário
            return file_date
    except Exception as e:
        write_log(f"Erro ao obter a data do arquivo {file_path}: {e}")
    return None

def write_log(message):
    """Escreve mensagens no arquivo de log."""
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()}: {message}\n")

def organize_files(source_dir):
    """Organiza arquivos com base em ano e mês."""
    # Caminho de saída para os arquivos organizados
    output_dir = os.path.join(source_dir, "Fotos organizadas")
    os.makedirs(output_dir, exist_ok=True)

    # Iterar sobre os arquivos na pasta
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)

        # Ignorar diretórios
        if not os.path.isfile(file_path):
            continue

        # Ignorar arquivos com extensões não suportadas
        if not any(file_name.lower().endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            write_log(f"Ignorado: {file_name} (extensão não suportada)")
            continue

        # Obter a data do arquivo
        file_date = get_file_date(file_path)
        if not file_date or file_date.year == 1980:
            # Quando a data é inválida ou indica metadados ausentes
            year_folder = "no-meta-data"
            month_folder = None
        else:
            # Criar subpastas por ano e ano-mês usando nomes dos meses abreviados
            year_folder = str(file_date.year)
            month_folder = f"{file_date.year}_{file_date.strftime('%b').upper()}"

        # Criar o caminho final baseado no ano e ano-mês
        if month_folder:
            final_folder = os.path.join(output_dir, year_folder, month_folder)
        else:
            final_folder = os.path.join(output_dir, year_folder)

        os.makedirs(final_folder, exist_ok=True)

        # Mover o arquivo para a pasta final
        try:
            shutil.move(file_path, os.path.join(final_folder, file_name))
            write_log(f"Movido: {file_name} para {final_folder}")
            print(f"{file_name} movido para {final_folder}")
        except Exception as e:
            write_log(f"Erro ao mover {file_name}: {e}")
            print(f"Erro ao mover {file_name}: {e}")

if __name__ == "__main__":
    source_dir = input("Digite o caminho da pasta com as fotos e vídeos: ").strip()

    # Verificar se o diretório existe
    if not os.path.exists(source_dir):
        print("Caminho inválido! Verifique e tente novamente.")
    else:
        organize_files(source_dir)
        print("Organização concluída!")
        print(f"Logs gravados em: {os.path.abspath(log_file)}")
