# Bloons-Python

## Visão Geral

Este projeto é um script em Python que utiliza a biblioteca `pyautogui` para automatizar o jogo **Bloons TD 6**. O script foi desenvolvido para farmar XP em um mapa específico, controlando o posicionamento de macacos, atualizando-os e interagindo com a interface do jogo.

---

## Estrutura do Projeto

O projeto consiste nos seguintes arquivos:

- `codigo.py`: O script principal em Python que contém a lógica de automação do jogo.
- `.gitignore`: Arquivo de configuração para o Git, que especifica quais arquivos e diretórios devem ser ignorados.
- `README.md`: Este arquivo, que fornece informações sobre o projeto.

---

## Funcionalidades

O script `codigo.py` realiza as seguintes ações no jogo **Bloons TD 6**:

### Posicionamento de Macacos:

- Coloca um **macaco especial** nas coordenadas `(341, 805)`.
- Coloca um **macaco bumerangue** nas coordenadas `(485, 810)`.
- Coloca um **macaco de gelo** nas coordenadas `(156, 800)`.

### Upgrades de Macacos:

- Após um período de **135 segundos**, realiza upgrades no **macaco bumerangue**, clicando:
  - 3 vezes no botão de upgrade da **direita**.
  - 2 vezes no botão de upgrade de **baixo**.
- Após mais **120 segundos**, realiza upgrades no **macaco de gelo**, clicando:
  - 2 vezes no botão de upgrade da **direita**.
  - 3 vezes no botão de upgrade de **baixo**.

### Controle do Fluxo do Jogo:

- O script também clica no botão de **"play"** do jogo.
- Utiliza pausas (`time.sleep`) para aguardar o progresso do jogo.

---

## Requisitos

Para executar este projeto, é necessário ter a biblioteca `pyautogui` instalada.

Você pode instalá-la com o comando:

```bash
pip install pyautogui
