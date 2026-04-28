from pathlib import Path
from pygame import mixer

class CaixaSom:
    _instance = None

    def __new__(cls, *args, **kwargs):
        nova_instancia = super().__new__(cls)
        cls._instance = nova_instancia
        
        return nova_instancia
    
    def __init__(self, musicas: str = 'medias/sons/musicas', efeitos: str = 'medias/sons/efeitos'):
        self.musicas = Path(__file__).parent.parent / musicas
        self.efeitos = Path(__file__).parent.parent / efeitos

        self.musica_atual = None
    
    def init(self):
        if not mixer.get_init():
            mixer.init()
    
    def tocar_efeito(self, nome_efeito: str, volume: float = 1):
        efeito = mixer.Sound(Path(self.efeitos / nome_efeito))
        efeito.play()
        efeito.set_volume(volume)

    def tocar_musica(self, nome_musica: str, volume: float = 1, loop: int = -1, fadeout: float = 0):
        self.musica_atual = str(Path(nome_musica).stem)
        mixer.music.load(Path(self.musicas / nome_musica))
        mixer.music.play(loop)
        mixer.music.set_volume(volume)

        if fadeout:
            mixer.music.fadeout(fadeout)

    def pausar_musica(self):
        mixer.music.stop()

if __name__ == '__main__':
    caixa_som = CaixaSom()
    caixa_som.init()
    caixa_som.tocar_efeito('error.ogg.mp3')
