import os

# Defina o caminho onde as pastas serão criadas
base_path = "E:\\"

# Lista de anos para criar as pastas
years = range(2017, 2026)  # Inclui de 2017 a 2025

# Criar as pastas
for year in years:
    folder_path = os.path.join(base_path, str(year))
    try:
        # Verificar se a pasta já existe
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Pasta criada: {folder_path}")
        else:
            print(f"Pasta já existe: {folder_path}")
    except Exception as e:
        print(f"Erro ao criar a pasta {folder_path}: {e}")

print("Processo concluído!")
