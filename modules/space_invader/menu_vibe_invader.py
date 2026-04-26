from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.console import Group
from art import text2art

def draw_menu():
    titulo = Text(text2art("VIBE  INVADERS"), style="bold green")
    
    menu = Text("\n\n[A] Jogar\n\n[Q] Sair\n\n", style="bold green", justify='center')
    
    controles = Align(Text("A: Esquerda  |  D: Direita  |  Backspace: Atirar", style="bold green"), vertical='bottom', align='center')

    conteudo = Group(titulo, menu, controles)

    panel = Panel(conteudo, border_style="green", height=20)

    return Align.center(panel, vertical="middle")


def draw_gameover(wave, score, highscore):
    text = Text(justify="center")
    text.append("GAME OVER\n", style="bold red")
    text.append("\n")
    text.append(f"{'WAVE':<12}{wave}\n", style="bold green")
    text.append(f"{'SCORE':<12}{score}\n", style="bold green")
    text.append(f"{'HIGHSCORE':<12}{highscore}\n", style="bold green")

    panel = Panel(
        Align.center(text, vertical="middle"),
        border_style="green",
        width=40,
        height=12,
        expand=False
    )

    return Align.center(panel, vertical="middle")


def handle_menu_input(key):
    if key == b'a':
        return "game"
    elif key == b'q':
        return "exit"

    return "menu"