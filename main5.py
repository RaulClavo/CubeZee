import pygame, sys, json

with open("ids3.json", "r") as json_file:
    ids = json.load(json_file)

with open("almacenajedetexto4.json", "r") as json_file:
    text_dict2 = json.load(json_file)

text_dict = {str(ids): ''}
text = ''
if str(ids) in text_dict2:
    text_dict |= text_dict2
    text = text_dict2[str(ids)]

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bloc de Notas')

font = pygame.font.Font(None, 32)

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)
    rendered_lines = []
    y_offset = 10

    for line in text.split('\n'):
        rendered_line = font.render(line, True, BLACK)
        screen.blit(rendered_line, (10, y_offset))
        y_offset += rendered_line.get_height()
        rendered_lines.append(rendered_line)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("almacenajedetexto3.json", "w") as json_file:
                json.dump(text_dict, json_file)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if y_offset < HEIGHT - 20:
                    text += '\n'
                    text_dict[str(ids)] = text
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
                text_dict[str(ids)] = text
            else:
                new_text = text + event.unicode
                rendered_new_line = font.render(new_text.split('\n')[-1], True, BLACK)
                if rendered_new_line.get_width() < WIDTH - 20:
                    text += event.unicode
                    text_dict[str(ids)] = text

    clock.tick(60)
