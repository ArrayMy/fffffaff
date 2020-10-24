from app.characters import Characters
from app.window import Window
from app.enemies import Entities
from app.base import Base

import random
 
#Create window
app = Window()
app.setSize(800,600)
app.setName('fffffaff')

#Create entities
mainCharacter = Characters()
mainCharacter.set(
  sizeHeight = 30,
  sizeWidth = 30,
  positionX = 140,
  positionY = 390,
  color = (0,0,255))

enemy =  Entities()
enemy.set(
  sizeHeight = 30,
  sizeWidth = 30,
  positionX = 580,
  positionY = random.randint(20, 780),
  color = (255,0,0)
)

mainCharacterBase = Base(mainCharacter)
mainCharacterBase.set(
  sizeHeight = 40,
  sizeWidth = 40,
  positionX = 20,
  positionY = 0,
  color = (0,255,0)
)

program_status = True

#Start program
while program_status:
  #Exit?
  program_status = app.window_close_cross()
  #Reset screen
  app.window_fill((0,0,0))
  #Render entities
    #character
  app.window_show_character(mainCharacter)
    #base
  app.window_show_character_base(mainCharacterBase)
  #Update entities
  mainCharacter.move(app.window_listen_keyboard())
  #Render updates
  app.window_update()
