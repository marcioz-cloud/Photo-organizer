Photo Organizer

Este projeto em Python foi desenvolvido para facilitar esse processo, categorizando automaticamente os arquivos em pastas baseadas no ano e no mês de criação, utilizando os metadados dos arquivos. A ferramenta é simples, eficiente e fácil de usar.


Como Funciona
O script analisa os arquivos em uma pasta fornecida pelo usuário.
Verifica se os arquivos possuem extensões suportadas.
Para imagens, tenta extrair a data de criação dos metadados EXIF. Para vídeos ou arquivos sem metadados, utiliza a data de modificação.
Cria pastas organizadas por ano e mês e move os arquivos para as respectivas pastas.
Arquivos sem metadados válidos são movidos para uma pasta especial chamada no-meta-data.

Observações
Extensões não suportadas: Arquivos com extensões não suportadas são ignorados e registrados no arquivo de log.
Logs detalhados: Todas as ações e possíveis erros são documentados no arquivo organizer_log.txt.
