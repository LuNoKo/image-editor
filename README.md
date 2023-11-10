# Editor de imagem em Python

Trabalho do curso de ciência da computação da disciplina de Processamento Digital de Imagens cursado na Universidade Feevale.

Realizado no segundo semestre de 2023.

---

## O trabalho

### Enunciado do desafio

O desafio consiste em abrir uma imagem de um número, que varia de 0 (zero) a 9 (nove).

Na sequência, abrir um arquivo de símbolos, que podem ser + (soma), - (subtração), X (multiplicação) ou / (divisão).

Após selecionar outra imagem de número de 0 a 9.

Apresentar o resultado da operação do primeiro pelo segundo número.

### Enunciado

Desenvolva um software que permita manipular imagens. Apresente no menu
as opções de:

Esta estrutura deve ter menus na parte superior e duas janelas, uma para mostrar a imagem original e outra que apresente a imagem transformada.

- ARQUIVO:
  - Abrir (permita ao operador abrir uma imagem armazenada no computador)
  - Salvar (permita ao operador salvar uma imagem manipulada em seu computador)
  - Sair (fecha a aplicação)
  - Sobre (informações sobre os autores e qual a versão do software)
- EXTRAÇÃO DE CARACTERÍSTICAS:
  - Desafio
- FILTROS:
  - Brilho (permita ao operador alterar o brilho de uma imagem)
  - Contraste (permita ao operador alterar o contraste de uma imagem)
  - Grayscale (permite ao operador transformar uma imagem colorida em tonalidades de cinza)
  - Passa Alta (Não realizado)
  - Passa Baixa:
    - Média
    - Mediana
    - Moda
    - Gauss
  - Threshold (Não realizado)
- MORFOLOGIA MATEMÁTICA:
  - Abertura (Não realizado)
  - Dilatação
  - Erosão
  - Fechamento (Não realizado)
- TRANSFORMAÇÕES:
  - Ampliação (permita ao operador ampliar uma imagem)
  - Espelhamento (permita ao operador espelhar uma imagem)
  - Redução (permita ao operador reduzir uma imagem)
  - Rotação (permita ao operador rotacionar uma imagem)
  - Translação (permite ao operador transladar uma imagem de um local ao outro)

\* Os parâmetros de brilho, contraste, translação, ampliação, redução e rotação podem ser fixos ou solicitados ao usuário.

---

## Execução do projeto

#### Windows

1. Instale o Python versão 3.7.8

2. Instale o tesseract com o instalador que se encontra na :file_folder: instalador-tesseract na raiz do projeto

3. Altere o valor da variavel `caminho_instalacao_tesseract_windows` com o caminho da instalação do tesseract realizada no item 2

4. Instale as dependencias com o comando: `pip install PySimpleGUI Pillow numpy pytesseract`

5. Execute o projeto com o seguinte comando na raiz do projeto: `python main.py`

#### Demais sistemas operacionais

1. Instale o Python versão 3.7.8

2. Exclua as linhas 8 e 151

3. Instale as dependencias com o comando: `pip install PySimpleGUI Pillow numpy pytesseract`

4. Execute o projeto com o seguinte comando na raiz do projeto: `python main.py`
