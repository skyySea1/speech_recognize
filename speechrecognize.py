import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = listener.listen(source, timeout=5, phrase_time_limit=5)
            comando = listener.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            return comando
    except sr.WaitTimeoutError:
        print("Não detectei nenhum comando de voz. Tentando novamente...")
        return None
    except Exception as e:
        print(f"Erro ao ouvir: {e}")
        return None

def run_jarvis():
    while True:
        comando = ouvir()
        if comando:
            if 'bom dia' in comando:
                falar("Bom dia, como posso ajudar?")
            elif 'tchau' in comando:
                falar("Até mais!")
                break
            elif 'olá' in comando:
                falar("Olá! Como posso ajudar você hoje?")
            elif 'como vai' in comando:
                falar("Estou indo bem, obrigado por perguntar! E você?")
            elif 'marseu' or 'marcéu' or 'maceu' or 'macel' in comando:
                falar("Marcell, o homem mais épico que já existiu depois de Jesus e José.")
            # Adicione mais comandos e respostas aqui
        else:
            falar("Desculpe, não entendi. Pode repetir?")

# Executa o assistente
if __name__ == "__main__":
    run_jarvis()