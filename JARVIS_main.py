import speech_recognition as sr
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
import time

from JARVIS_speak import *
# Инициализация стеммера
stemmer = SnowballStemmer("russian")

def listen():
    """Прослушивание и распознавание речи со стеммингом"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
        
        # Применяем стемминг
        text = text.lower()
        tokens = word_tokenize(text)
        stemmed_words = [stemmer.stem(word) for word in tokens]
        stemmed_text = ' '.join(stemmed_words)
        
        return stemmed_text
        
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def main():
    """Основная функция с базовой логикой активации"""
    jarvis_active = False

    while True:
        command = listen()

        if jarvis_active == False:
            continue
        
        # Активация по ключевому слову
        if 'джарвис' in command:
            Activation_system_jarvis()
            jarvis_active = True

        if jarvis_active:
            print(f"Команда: {command}")
            
            # Деактивация
            if any(stop_word in command for stop_word in ["стоп", "выход", "законч"]):
                print("JARVIS: Деактивирован!")
                jarvis_active = False
                break

            # Таймаут неактивности (15 секунд)
            if not command:
                start_time = time.time()
                while time.time() - start_time < 15:
                    command = listen()
                    if command:
                        print(f"Команда: {command}")
                        break
                else:
                    jarvis_active = False
                    print("JARVIS: Таймаут неактивности")

if __name__ == "__main__":
    main()