
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from calendar import monthrange, isleap
from datetime import date, timedelta

def gerar_calendario_pdf(ano):
    a4_largura_cm, a4_altura_cm = 29.7, 21.0
    margem_lateral_cm = 3.0
    num_colunas = 25

    total_dias = 366 if isleap(ano) else 365
    linhas_completas = total_dias // num_colunas
    restantes = total_dias % num_colunas
    linhas_totais = linhas_completas + (1 if restantes else 0)

    conteudo_largura_cm = a4_largura_cm - 2 * margem_lateral_cm
    tamanho_quadrado_cm = conteudo_largura_cm / num_colunas
    conteudo_altura_cm = tamanho_quadrado_cm * linhas_totais
    margem_vertical_cm = (a4_altura_cm - conteudo_altura_cm) / 2

    inicio = date(ano, 1, 1)
    dias_por_mes = [monthrange(ano, m)[1] for m in range(1, 13)]

    fig, ax = plt.subplots(figsize=(a4_largura_cm / 2.54, a4_altura_cm / 2.54))
    dia_do_mes = 1
    mes_index = 0

    for n in range(total_dias):
        dia = inicio + timedelta(days=n)
        linha = n // num_colunas
        coluna = n % num_colunas

        x0 = margem_lateral_cm + coluna * tamanho_quadrado_cm
        y0 = margem_vertical_cm + (linhas_totais - 1 - linha) * tamanho_quadrado_cm

        rect = plt.Rectangle((x0, y0), tamanho_quadrado_cm, tamanho_quadrado_cm,
                             edgecolor='black', facecolor='none')
        ax.add_patch(rect)

        if dia.weekday() in [5, 6]:
            margem_x = tamanho_quadrado_cm * 0.15 * 1.3 * 1.4
            ax.plot(
                [x0 + margem_x, x0 + tamanho_quadrado_cm - margem_x],
                [y0 + margem_x, y0 + tamanho_quadrado_cm - margem_x],
                color='#002266', linewidth=1.5
            )
            ax.plot(
                [x0 + margem_x, x0 + tamanho_quadrado_cm - margem_x],
                [y0 + tamanho_quadrado_cm - margem_x, y0 + margem_x],
                color='#002266', linewidth=1.5
            )
        else:
            ax.text(
                x0 + tamanho_quadrado_cm / 2,
                y0 + tamanho_quadrado_cm / 2,
                str(dia_do_mes),
                color='#bbbbbb',
                ha='center',
                va='center',
                fontsize=5
            )

        dia_do_mes += 1
        if dia_do_mes > dias_por_mes[mes_index]:
            dia_do_mes = 1
            mes_index += 1
            linha_sep = linha + 1
            if linha_sep < linhas_totais:
                y_sep = margem_vertical_cm + (linhas_totais - linha_sep) * tamanho_quadrado_cm
                ax.plot(
                    [margem_lateral_cm, margem_lateral_cm + num_colunas * tamanho_quadrado_cm],
                    [y_sep, y_sep],
                    color='black',
                    linewidth=1
                )

    ax.set_xlim(0, a4_largura_cm)
    ax.set_ylim(0, a4_altura_cm)
    ax.set_aspect('equal')
    ax.axis('off')

    nome_arquivo = f"calendario_{ano}_completo.pdf"
    with PdfPages(nome_arquivo) as pdf:
        pdf.savefig(fig, bbox_inches='tight')

    print(f"PDF gerado com sucesso: {nome_arquivo}")

if __name__ == "__main__":
    try:
        ano = int(input("Informe o ano desejado para o calendário (ex: 2026): "))
        gerar_calendario_pdf(ano)
    except ValueError:
        print("Por favor, insira um ano válido (ex: 2026).")
