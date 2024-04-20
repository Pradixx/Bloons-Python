import pyautogui as py
import time

py.PAUSE = 0.5

# #abrir win
# py.press('win', 1, 1)

# #escrever blons e dar enter
# py.write('bloons', 0.5)
# py.press('enter')

# #esperar abrir 25s
# time.sleep(13)

# #botao iniciar
# py.click(984,979, 1, 0.5)

# #esperar animação 5s
# time.sleep(4)

# #play
# py.click(819,917, 1, 0.5)

# #clicar no mapa
# py.click(922,235, 1, 0.5)

# #clicar na dificuldade
# py.click(1277,521, 1, 0.5)

# #clicar em padrão
# py.click(634,572, 1, 0.5)

# #clicar me ok
# py.click(1136,703, 1, 0.5)

##**Só para voltar para jogo enquanto não está todo o código
py.click(1092,1049)

# time.sleep(3)

#colocando macaco especial no jogo
py.click(1711,217, 1, 0.5)
py.click(341,805, 1, 0.5)

#dando play no jogo
py.click(1825,1002, 2, 0.5)

#esperar 15s
time.sleep(20)

#colocando macaco bumerang no jogo
py.click(1715,347, 1, 0.5)
py.click(485,810, 1, 0.5)

#esperar para upar macaco bumerang
time.sleep(135)

#upando macaco bumerang
py.click(485,810, 1, 0.5)
py.click(1547,621, 3, 0.5)
py.click(1565,787, 2, 0.5)

#colocando macaco gelo
py.click(1807,482, 1, 0.5)
py.click(156,800, 1, 0.5)

#esperar para upar macaco gelo
time.sleep(120)

#upando macaco gelo
py.click(156,800, 1, 0.5)
py.click(1547,621, 2, 0.5)
py.click(1565,787, 3, 0.5)