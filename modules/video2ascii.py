from console import console
import cv2
import numpy as np
from rich.live import Live
from rich.text import Text
from pathlib import Path
import time

class VideoAscii:
    def __init__(self, nome_video):
        self.path = Path(__file__).parent.parent / 'medias' / 'videos' / nome_video
        self.width = console.width
        self.chars = np.array(list(" @#S%?*+;:,."))

    def get_ascii_frame(self, frame):
        # 1. Redimensiona mantendo a proporção (ajuste 0.5 para altura do terminal)
        h, w = frame.shape[:2]
        height = int((h / w) * self.width * 0.5)
        frame_resized = cv2.resize(frame, (self.width, height))
        
        # 2. Converte para cinza para calcular o brilho
        gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
        
        # 3. Mapeamento vetorizado com Numpy (Super rápido)
        indices = (gray / 255 * (len(self.chars) - 1)).astype(int)
        ascii_array = self.chars[indices]
        
        # 4. Junta tudo em uma string
        ascii_str = "\n".join(["".join(row) for row in ascii_array])
        
        # 5. Retorna o texto formatado em verde
        return Text(ascii_str, style="bold green")

    def play(self):
        cap = cv2.VideoCapture(self.path)
        
        # Pega o FPS original do vídeo
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps <= 0: fps = 30
        frame_duration = 1.0 / fps
        
        with Live(console=console, screen=True, auto_refresh=False) as live:
            start_time = time.perf_counter()
            frame_count = 0
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                elapsed = time.perf_counter() - start_time
                expected_time = frame_count * frame_duration
                
                if elapsed < expected_time:
                    time.sleep(expected_time - elapsed)
                
                elif elapsed > expected_time + frame_duration:
                    frame_count += 1
                    continue

                ascii_text = self.get_ascii_frame(frame)
                live.update(ascii_text, refresh=True)
                
                frame_count += 1
        
        cap.release()

if __name__ == '__main__':
    player = VideoAscii('rickroll.mp4')
    player.play()