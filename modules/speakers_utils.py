import pygame


def init_speaker(sound_file):
    """
    스피커 초기화 및 사운드 파일 로드
    """
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    return sound


def play_sound(sound):
    """
    경고음 재생 (무한 반복)
    """
    sound.play(-1)


def stop_sound(sound):
    """
    경고음 정지
    """
    sound.stop()