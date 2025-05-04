# Calendário Matricial

Gera um calendário anual em formato de grade (25 colunas x N linhas) no estilo matricial, exportado como PDF. Finais de semana são destacados com um "X" azul escuro.

> ⚠️ Projeto experimental. Melhorias visuais e funcionais serão adicionadas no futuro.

## Pré-requisitos

- Python 3.7+
- Bibliotecas:
  - `matplotlib`

## Instalação

```bash
pip install matplotlib
```

## Uso

```bash
python calendario_Matricial.py
```

Você será solicitado a inserir um ano (ex: 2026). O arquivo `calendario_2026_completo.pdf` será gerado na mesma pasta.

## Saída

Um arquivo PDF com o calendário completo do ano solicitado, contendo:

- Quadrados organizados em 25 colunas.
- Dias úteis numerados discretamente.
- Finais de semana com marca em X.
