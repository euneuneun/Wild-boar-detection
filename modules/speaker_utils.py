import pygame

def init_speaker(sound_file):

    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    return sound

def play_sound(sound):

    sound.play(-1)  

def stop_sound(sound):

    sound.stop()
