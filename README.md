# Conversor de Vídeo em Python
## Este documento descreve dois scripts Python para converter vídeos entre diferentes formatos.

Você pode instalar as dependências com o seguinte comando:

```sh
pip install -r requirements.txt
```

# Script 1: Conversão de Vídeo TS para MP4
Este primeiro script converte arquivos de vídeo TS (Transport Stream) para o formato MP4. Ele usa a biblioteca moviepy para manipular os arquivos de vídeo.

## Funcionamento
O script define uma função chamada convert_ts_to_mp4 que aceita dois argumentos: um arquivo TS de entrada e um arquivo MP4 de saída. Ele então utiliza a classe VideoFileClip da biblioteca moviepy para carregar o arquivo TS, e escreve o arquivo MP4 usando os codecs de vídeo e áudio especificados.

O método main contém a lógica principal do programa, que inclui encontrar arquivos TS no diretório VIDEO_TS de um DVD, e convertê-los para o formato MP4.

# Script 2: Conversor de Vídeo com Interface Gráfica
Este segundo script é um conversor de vídeo com uma interface gráfica de usuário (GUI) construída usando a biblioteca tkinter. Ele permite ao usuário selecionar arquivos de vídeo, escolher um formato de saída e converter os arquivos.

## Funcionamento
A classe App cria uma interface gráfica com vários elementos, como botões, caixas de listagem e campos de entrada, que permitem ao usuário interagir com o aplicativo. A classe também define vários métodos que são chamados quando o usuário interage com esses elementos, como selecionar arquivos, escolher a pasta de saída e iniciar a conversão.

O método convert_videos é responsável pela conversão dos arquivos de vídeo selecionados. Ele utiliza a biblioteca moviepy para carregar e converter os arquivos de vídeo, e atualiza uma barra de progresso na interface gráfica para indicar o progresso da conversão.

A aplicação é iniciada criando um objeto da classe App e chamando o método mainloop do objeto tkinter.Tk.