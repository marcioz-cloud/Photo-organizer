Photo Organizer

Este projeto em Python foi desenvolvido para facilitar esse processo, categorizando automaticamente os arquivos em pastas baseadas no ano e no mês de criação, utilizando os metadados dos arquivos. A ferramenta é simples, eficiente e fácil de usar.

Funcionalidades:
Extração de Metadados: O script utiliza os dados EXIF de imagens para identificar a data em que a foto foi tirada.
Data Alternativa: Caso os metadados não estejam disponíveis, o script usa a data de modificação do arquivo como referência.
Compatibilidade com Diversos Formatos: Suporte para formatos populares, como .jpg, .jpeg, .png, .mp4, .mov, .avi e .heic.
Criação Automática de Pastas: As fotos e vídeos são organizados em pastas nomeadas pelo ano e mês (ex.: 2025/JAN).
Log de Operações: Todas as ações são registradas em um arquivo de log, incluindo arquivos ignorados, erros e arquivos organizados com sucesso.
Requisitos

Módulos embutidos do Python: os, shutil, datetime.

Como Funciona
O script analisa os arquivos em uma pasta fornecida pelo usuário.
Verifica se os arquivos possuem extensões suportadas.
Para imagens, tenta extrair a data de criação dos metadados EXIF. Para vídeos ou arquivos sem metadados, utiliza a data de modificação.
Cria pastas organizadas por ano e mês e move os arquivos para as respectivas pastas.
Arquivos sem metadados válidos são movidos para uma pasta especial chamada no-meta-data.

Observações
Extensões não suportadas: Arquivos com extensões não suportadas são ignorados e registrados no arquivo de log.
Logs detalhados: Todas as ações e possíveis erros são documentados no arquivo organizer_log.txt.
