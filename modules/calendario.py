from console import console, erro, aviso, limpar_tela

from rich.panel import Panel

from art import text2art
import calendar
from rich.table import Table
from datetime import datetime

MESES = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
    'jan', 'fev', 'mar', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'
]

def obter_ano_valido():
    while True:
        try:
            ano = int(console.input("Digite um ano: "))

            if ano > 0:
                break
            else:
                aviso('Digite um ano não negativo.')

        except ValueError:
            erro('Digite um ano válido.')

def obter_mes_valido():
    console.print()

    while True:
        try:
            mes_input = console.input("Digite um mês (nome ou número): ").lower()

            if mes_input.isdigit():
                mes = int(mes_input)

            elif mes_input in MESES:
                mes = MESES.index(mes_input) + 1

            else:
                erro('Digite um mês válido.')
                continue

            if (1 <= mes <= 12) or (mes in MESES):
                break

        except:
            erro('Digite um mês válido.')

def obter_dia_valido():
    console.print()

    _, ultimo_dia = calendar.monthrange(ano, mes)
    while True:
        try:
            dia = int(console.input(f"Dia (1-{ultimo_dia}): "))

            if 1 <= dia <= ultimo_dia:
                return ano, mes, dia
            else:
                aviso('Digite um dia válido.')

        except ValueError:
            erro('Digite apenas números.')

def exibir_calendario(ano, mes, dia_escolhido):
    cal = calendar.monthcalendar(ano, mes)
    titulo = f"\n[bold green3]{MESES[mes-1].upper()} {ano}[/bold green3]"
    tabela = Table(title=titulo, show_lines=True, header_style="bold green3")

    for d in ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]:
        tabela.add_column(d, justify="center")

    for semana in cal:
        linha = [
            f"[bold green1][{dia}][/]" if dia == dia_escolhido else (str(dia) if dia != 0 else "")
            for dia in semana
        ]

        tabela.add_row(*linha)

    limpar_tela()

    console.print(Panel(text2art('CALENDARIO'), style='bold green', expand=False))

    console.print(tabela)

def ir_para_data_especifica():
    try:
        console.print()
        ano = int(console.input("Digite o ano: "))

        if ano < 0:
            aviso('Digite um ano não negativo.')
            return None, None, None

        console.print()
        mes_input = console.input("Digite o mês (Nome ou número): ").lower()

        if mes_input.isdigit():
            mes = int(mes_input)

        elif mes_input in MESES:
            mes = MESES.index(mes_input) + 1

        else:
            erro('Digite um mês válido.')
            return None, None, None

        if not (1 <= mes <= 12):
            erro('Digite um mês válido.')
            return None, None, None

        _, ultimo_dia = calendar.monthrange(ano, mes)

        try:
            console.print()
            dia = int(console.input(f"Digite o dia (1-{ultimo_dia}): "))

        except ValueError:
            erro('Digite um dia válido.')
            return None, None, None

        if not (1 <= dia <= ultimo_dia):
            erro('Digite um dia válido.')
            return None, None, None

        return ano, mes, dia

    except ValueError:
        erro('Ocorreu um erro.')
        return None, None, None

def principal():
    agora = datetime.now()
    ano_exibido, mes_exibido, dia_exibido = agora.year, agora.month, agora.day

    while True:
        exibir_calendario(ano_exibido, mes_exibido, dia_exibido)
        console.print("\n[A] Anterior | [D] Próximo | [G] Ir para | [Q] Sair\n")

        while True:
            comando = console.input(">>> ").lower().strip()

            match comando:
                case 'd':
                    mes_exibido += 1

                    if mes_exibido > 12:
                        mes_exibido = 1
                        ano_exibido += 1
                    break

                case 'a':
                    mes_exibido -= 1

                    if mes_exibido < 1:
                        mes_exibido = 12
                        ano_exibido -= 1
                    break

                case 'g':
                    while True:
                        console.print()
                        novo_ano = obter_ano_valido()
                        novo_mes = obter_mes_valido()
                        novo_dia = obter_dia_valido()

                        if novo_ano:
                            ano_exibido, mes_exibido, dia_exibido = novo_ano, novo_mes, novo_dia
                            break
                    break

                case 'q':
                    break

                case _:
                    erro('Digite um comando válido.')

        if comando == 'q':
            break

if __name__ == "__main__":
    principal()
