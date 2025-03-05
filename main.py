from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

arm = Entity(parent=camera.ui, model='cube', color=color.white, position=(0.75, -0.6), rotation=(150, -10, 6), scale=(0.2, 0.2, 1.5), texture='Рука.png')

boxes = []

for i in range(15):
    for j in range(15):
        box = Button(color=color.white, model='cube', position=(j,0,i), texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                newBox = Button(color=color.white, model='cube', position=box.position+mouse.normal, texture='grass.png', parent=scene, origin_y=0.5)
                boxes.append(newBox)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)

def update():
    if held_keys['left mouse'] or held_keys['rigth mouse']:
        arm.position = (0.6, -0.5)
    else:
        arm.position = (0.75, -0.6)


app.run()