import pygame, sys, subprocess, json
pygame.init()
NEGRO, GRIS, BLANCO = (0, 0, 0), (192, 192, 192), (255, 255, 255)
AZUL, AMARILLO, ROJO, VERDE = (0, 0, 255), (255, 255, 0), (255, 0, 0), (0, 255, 0)
ANCHO, ALTO, TAM = 800, 600, 50
FILAS, COLUMNAS = ALTO // TAM, ANCHO // TAM
MAINSPACE = pygame.display.set_mode((ANCHO, ALTO))
almacenajetxt = {}
almacenajecarpetas = {}
almacenajeterminal = []
almacenajebuscaminas = []
almacenajesnake = []
almacenajepong = []

def renderizar_marcador(seleccionado):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) == seleccionado:
                pygame.draw.rect(MAINSPACE, GRIS, pygame.Rect(columna * TAM, fila * TAM, TAM, TAM), 3)
seleccion = (0, 0)
def renderizar_carpetas(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if str((fila, columna)) in almacenaje:
                pygame.draw.rect(MAINSPACE, AMARILLO, pygame.Rect(columna * TAM+10, fila * TAM+10, TAM-20, TAM-20))

def renderizar_txt(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if str([fila, columna]) in almacenaje:
                pygame.draw.rect(MAINSPACE, BLANCO, pygame.Rect(columna * TAM+10, fila * TAM+10, TAM-20, TAM-20))

def renderizar_terminal(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) in almacenaje:
                pygame.draw.rect(MAINSPACE, AZUL, pygame.Rect(columna * TAM+10, fila * TAM+10, TAM-20, TAM-20))

def renderizar_buscaminas(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) in almacenaje:
                pygame.draw.rect(MAINSPACE, ROJO, pygame.Rect(columna * TAM+10, fila * TAM+10, TAM-20, TAM-20))

def renderizar_snake(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) in almacenaje:
                pygame.draw.rect(MAINSPACE, VERDE, pygame.Rect(columna * TAM+10, fila * TAM+10, TAM-20, TAM-20))

def renderizar_pong(almacenaje):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if (fila, columna) in almacenaje:
                pygame.draw.rect(MAINSPACE, GRIS, pygame.Rect(columna * TAM+10, fila * TAM+10, TAM-20, TAM-20))

while True:
    MAINSPACE.fill(NEGRO)
    try:
        with open("ids.json", "r") as json_file:
            ids = json.load(json_file)
        with open("almacenaje.json", "r") as json_file:
            almacenaje = json.load(json_file)
        almacenajecarpetas[str(ids).replace("[", "(").replace("]", ")")] = almacenaje
        with open("almacenajedetexto.json", "r") as json_file:
            text_dict = json.load(json_file)
        almacenajetxt |= text_dict
    except: pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("almacenajedetexto2.json", "w") as json_file:
                json.dump("", json_file)
            with open("almacenajedetexto.json", "w") as json_file:
                json.dump("", json_file)
            with open("almacenaje2.json", "w") as json_file:
                json.dump("", json_file)
            with open("almacenaje.json", "w") as json_file:
                json.dump("", json_file)
            with open("ids.json", "w") as json_file:
                json.dump("", json_file)
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
            elif event.key == pygame.K_c:
                if (str(seleccion) not in almacenajecarpetas) and (str([seleccion[0], seleccion[1]]) not in almacenajetxt) and (seleccion not in almacenajeterminal):
                    almacenajecarpetas[str(seleccion)] = [[],[]]
            elif event.key == pygame.K_t:
                if (str(seleccion) not in almacenajecarpetas) and (str([seleccion[0], seleccion[1]]) not in almacenajetxt) and (seleccion not in almacenajeterminal):
                    almacenajetxt[str([seleccion[0], seleccion[1]])] = ""
            elif event.key == pygame.K_s:
                if (str(seleccion) not in almacenajecarpetas) and (str([seleccion[0], seleccion[1]]) not in almacenajetxt) and (seleccion not in almacenajeterminal):
                    almacenajeterminal.append(seleccion)
            elif event.key == pygame.K_b:
                if (str(seleccion) not in almacenajecarpetas) and (str([seleccion[0], seleccion[1]]) not in almacenajetxt) and (seleccion not in almacenajeterminal):
                    almacenajebuscaminas.append(seleccion)
            elif event.key == pygame.K_k:
                if (str(seleccion) not in almacenajecarpetas) and (str([seleccion[0], seleccion[1]]) not in almacenajetxt) and (seleccion not in almacenajeterminal):
                    almacenajesnake.append(seleccion)
            elif event.key == pygame.K_p:
                if (str(seleccion) not in almacenajecarpetas) and (str([seleccion[0], seleccion[1]]) not in almacenajetxt) and (seleccion not in almacenajeterminal):
                    almacenajepong.append(seleccion)
            elif event.key == pygame.K_BACKSPACE:
                try:
                    with open("almacenaje2.json", "w") as json_file:
                        json.dump("", json_file)
                    with open("almacenaje.json", "w") as json_file:
                        json.dump("", json_file)
                    with open("ids.json", "w") as json_file:
                        json.dump("", json_file)
                    del almacenajecarpetas[str(seleccion)]
                except:
                    try:
                        with open("ids.json", "w") as json_file:
                            json.dump("", json_file)
                        del almacenajetxt[str(seleccion).replace("(", "[").replace(")", "]")]
                        with open("almacenajedetexto.json", "w") as json_file:
                            json.dump(almacenajetxt, json_file)
                    except:
                        try:
                            almacenajeterminal.remove(seleccion)
                        except:
                            try:
                                almacenajebuscaminas.remove(seleccion)
                            except:
                                try:
                                    almacenajepong.remove(seleccion)
                                except:
                                    try:
                                        almacenajesnake.remove(seleccion)
                                    except:
                                        pass
            elif event.key == pygame.K_RETURN:
                if seleccion in almacenajeterminal: subprocess.run('python main2.py')
                elif str(seleccion) in almacenajecarpetas:
                    with open("ids.json", "w") as json_file:
                        json.dump(seleccion, json_file)
                    with open("almacenaje2.json", "w") as json_file:
                        json.dump(almacenajecarpetas, json_file)
                    subprocess.run('python main3.py')
                elif str([seleccion[0],seleccion[1]]) in almacenajetxt:
                    with open("ids2.json", "w") as json_file:
                        json.dump(seleccion, json_file)
                    with open("almacenajedetexto2.json", "w") as json_file:
                        json.dump(almacenajetxt, json_file)
                    subprocess.run('python main4.py')
                elif seleccion in almacenajebuscaminas: subprocess.run('python main6.py')
                elif seleccion in almacenajesnake: subprocess.run('python main7.py')
                elif seleccion in almacenajepong: subprocess.run('python main8.py')

    MAINSPACE.fill(NEGRO)
    renderizar_carpetas(almacenajecarpetas)
    renderizar_txt(almacenajetxt)
    renderizar_terminal(almacenajeterminal)
    renderizar_pong(almacenajepong)
    renderizar_snake(almacenajesnake)
    renderizar_buscaminas(almacenajebuscaminas)
    renderizar_marcador(seleccion)
    pygame.display.flip()