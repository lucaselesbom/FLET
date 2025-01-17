import flet as ft
import pyttsx3
import speech_recognition as sr


def main(page: ft.Page):
    # Inicializar o mecanismo TTS
    engine = pyttsx3.init()

    # Configuração do título da página
    page.title = "Conversor de Texto e Áudio"

    # Função para executar o TTS
    def text_to_speech(e):
        text = input_box.value.strip()
        if text:
            engine.say(text)
            engine.runAndWait()
            result_label.value = "Texto convertido em áudio com sucesso!"
        else:
            result_label.value = "Por favor, digite algum texto."
        page.update()

    # Função para transcrever áudio
    def transcribe_audio(e):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            result_label.value = "Ouvindo... Fale algo."
            page.update()
            try:
                audio = recognizer.listen(source, timeout=5)
                result_label.value = "Processando áudio..."
                page.update()
                text = recognizer.recognize_google(audio, language="pt-BR")
                input_box.value = text
                result_label.value = "Áudio transcrito com sucesso!"
            except sr.UnknownValueError:
                result_label.value = "Não foi possível entender o áudio."
            except sr.RequestError:
                result_label.value = "Erro ao acessar o serviço de reconhecimento."
            page.update()

    # Elementos da interface
    input_box = ft.TextField(label="Digite o texto ou use o microfone", multiline=True, width=400, height=150)
    convert_button = ft.ElevatedButton("Converter para Áudio", on_click=text_to_speech)
    transcribe_button = ft.ElevatedButton("Transcrever Áudio", on_click=transcribe_audio)
    result_label = ft.Text(value="", color="green")

    # Adicionando elementos à página
    page.add(
        ft.Column(
            [
                ft.Text("Conversor de Texto e Áudio", size=24, weight="bold"),
                input_box,
                ft.Row([convert_button, transcribe_button], alignment=ft.MainAxisAlignment.CENTER),
                result_label,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executar o aplicativo
ft.app(target=main)
