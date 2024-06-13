import clipboard
menu = 0
while menu == 0:
    aumentar = input('Transformar em miúsculo:\n').upper()
    clipboard.copy(aumentar)
    menu = int(input('Deseja continuar? Sim - Digite 0, Não - Digite 1.\n'))


