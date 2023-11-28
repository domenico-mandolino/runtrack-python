
def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne du rectangle
            print('|' + '-' * (width - 2) + '|')
        else:
            # Lignes intérieures du rectangle
            print('|' + ' ' * (width - 2) + '|')

# Appeler la fonction avec les paramètres (width, height)
draw_rectangle(10, 3)