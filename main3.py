import pygame, sys, subprocess, json
almacenaje = None
with open("ids.json", "r") as json_file:
    ids = json.load(json_file)
with open("almacenaje2.json", "r") as json_file:
    almacenaje2 = json.load(json_file)
if str(ids).replace("[","(").replace("]",")") in almacenaje2.keys():
    almacenaje = almacenaje2[str(ids).replace("[","(").replace("]",")")]
    almacenaje = [[tuple(i) for i in j] for j in almacenaje]
else: almacenaje = [[],[]]
pygame.init()
NEGRO, GRIS, BLANCO = (50, 50, 50), (192, 192, 192), (255, 255, 255)
AZUL, AMARILLO = (0, 0, 255), (255, 255, 0)
ANCHO, ALTO, TAM = 400, 300, 25
FILAS, COLUMNAS = ALTO // TAM, ANCHO // TAM
MAINSPACE = pygame.display.set_mode((ANCHO, ALTO))
# almacenajecarpetas = []
def renderizar_marcador(seleccionado):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) == seleccionado:
                pygame.draw.rect(MAINSPACE, GRIS, pygame.Rect(columna * TAM, fila * TAM, TAM, TAM), 3)
seleccion = (0, 0)

#def renderizar_carpetas(almacenaje):
 #   for fila in range(FILAS):
  #      for columna in range(COLUMNAS):
   #         if (fila, columna) in almacenaje:
    #            pygame.draw.rect(MAINSPACE, AMARILLO, pygame.Rect(columna * TAM, fila * TAM, TAM, TAM))

def renderizar_txt(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) in almacenaje:
                pygame.draw.rect(MAINSPACE, BLANCO, pygame.Rect(columna * TAM+5, fila * TAM+5, TAM-10, TAM-10))

def renderizar_terminal(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) in almacenaje:
                pygame.draw.rect(MAINSPACE, AZUL, pygame.Rect(columna * TAM+5, fila * TAM+5, TAM-10,TAM-10))

while True:
    MAINSPACE.fill(NEGRO)
    with open("almacenaje.json", "w") as json_file:
        json.dump(almacenaje, json_file)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if seleccion[0] > 0:
                    seleccion = (seleccion[0] - 1, seleccion[1])
            elif event.key == pygame.K_DOWN:
                if seleccion[0] < FILAS - 1:
                    seleccion = (seleccion[0] + 1, seleccion[1])
            elif event.key == pygame.K_LEFT:
                if seleccion[1] > 0:
                    seleccion = (seleccion[0], seleccion[1] - 1)
            elif event.key == pygame.K_RIGHT:
                if seleccion[1] < COLUMNAS - 1:
                    seleccion = (seleccion[0], seleccion[1] + 1)
            #elif event.key == pygame.K_c:
                #if  (seleccion not in almacenajecarpetas) and (seleccion not in almacenajetxt) and (seleccion not in almacenajeterminal):
                    #almacenajecarpetas.append(seleccion)
            elif event.key == pygame.K_t:
                if (seleccion not in almacenaje[0]) and (seleccion not in almacenaje[1]):
                    almacenaje[0].append(seleccion)
            elif event.key == pygame.K_s:
                if (seleccion not in almacenaje[0]) and (seleccion not in almacenaje[1]):
                    almacenaje[1].append(seleccion)
            elif event.key == pygame.K_BACKSPACE:
                try:
                    almacenaje[0].remove(seleccion)
                except:
                    try:
                        almacenaje[1].remove(seleccion)
                    except: pass
            elif event.key == pygame.K_RETURN:
                if seleccion in almacenaje[1]:subprocess.run('python main2.py')
                if seleccion in almacenaje[0]: subprocess.run('python main5.py')
    MAINSPACE.fill(NEGRO)
    #renderizar_carpetas(almacenajecarpetas)
    renderizar_txt(almacenaje[0])
    renderizar_terminal(almacenaje[1])
    renderizar_marcador(seleccion)
    pygame.display.flip()
