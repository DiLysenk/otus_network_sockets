import random

LOCALHOST = "127.0.0.1"


def random_port():
    """возвращает рандомный порт"""
    return random.randint(20000, 30000)