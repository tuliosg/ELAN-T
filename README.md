# ELAN-T
 O ELAN-T (EUDICO Linguistic Annotator - Tagger) é uma ferramenta que permite a etiquetagem (_Part-Of-Speech Tagging_) de arquivos _.txt_ exportados do software [ELAN](https://archive.mpi.nl/tla/elan).
 A etiquetagem é realizada através do modelo pré-treinado para Português Brasileiro da biblioteca [spaCy](https://archive.mpi.nl/tla/elan), o [_pt_core_news_lg_](https://spacy.io/models/pt#pt_core_news_lg).

 ## Como utilizar?
 ### Instalando as dependências
Inicialmente, é necessária a instalação das dependências do projeto:
```shell
pip install -r requirements.txt
```
Nessa etapa serão instalados os componentes necessários para a execução correta do código.
_Observação:_ O procedimento pode demorar um pouco pois o modelo utilizado possui um tamanho considerável.
### Organizando o diretório
O uso do script depende da organização dos arquivos em uma pasta única. Assim, armazene todos os arquivos _.txt_ que foram exportados do ELAN em uma pasta que contenha apenas isso.

Um **exemplo** de caminho organizado:
```shell
C:\User\Desktop\Arquivos_ELAN
```
A nomenclatura acima é apenas um exemplo. Uma dica que pode evitar transtornos é criar a pasta em um caminho que não possua acentos, caracteres especiais ou espaços em branco nos nomes das pastas.
### Executando o código
A ferramenta permite a etiquetagem de uma ou mais entrevistas presentes em uma pasta. Para a execução do código:
```shell
py elan-t.py caminho\pasta_dos_arquivos
```
