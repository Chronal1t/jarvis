import pygame
import time

# Инициализация pygame mixer
pygame.mixer.init()

def play_audio(file_path):
    """Универсальная функция воспроизведения аудио"""
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # Ждем окончания воспроизведения
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
    except pygame.error as e:
        print(f"Ошибка загрузки файла: {e}")
    except Exception as e:
        print(f"Ошибка воспроизведения: {e}")

def Activation_system_jarvis():
    """Активация системы JARVIS"""
    play_audio("D:\\programming\\JARVIS\\JARVIS_voice\\app_sound_jarvis-og_run.wav")

def start_download():
    """Звук загрузки/старта"""
    play_audio("D:\\programming\\JARVIS\\JARVIS_voice\\app_sound_jarvis-og_ok4.wav")

def activation_jarvis():
    """Приветствие JARVIS"""
    play_audio("D:\\programming\\JARVIS\\JARVIS_voice\\app_sound_jarvis-og_greet1.wav")
