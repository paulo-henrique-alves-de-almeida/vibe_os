# import Rich
import console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich import box
from rich.align import Align

# outras importações
from time import sleep
import pathlib

def limpar_tela():
    console.clear()

def cabecalho(titulo: str = "VibeOS"):
    limpar_tela()
    console.print(Panel(Align.center(''), border_style="green", box=box.DOUBLE))
    console.print(
        Panel(f"[bold green]{titulo}[/bold green]",
              border_style="green",
              box=box.SIMPLE_HEAD,
              expand=False),
        justify="center"
    )

def animacao_boot():
    """Sequência de boot estilo terminal retrô."""
    limpar_tela()
    console.print("\n")
    etapas = ["Iniciando sistema...",]
    with Progress(
        SpinnerColumn(style="green"),
        TextColumn("[green]{task.description}"),
        BarColumn(bar_width=40, style="green", complete_style="bright_green"),
        console=console,
        transient=True,
    ) as progress:
        tarefa = progress.add_task("Inicializando...", total=len(etapas))
        for etapa in etapas:
            progress.update(tarefa, description=etapa, advance=1)
            sleep(0.6)

    console.print(
        Panel("[bold bright_green]  SISTEMA INICIALIZADO COM SUCESSO  [/bold bright_green]",
              border_style="bright_green", box=box.DOUBLE),
        justify="center"
    )
    sleep(1)