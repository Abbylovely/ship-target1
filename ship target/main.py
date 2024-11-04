from random import randint
import pgzrun
#itertools helps us cycle through a set of items repeatedly
import itertools

WIDTH=400
HEIGHT=400



block_pos=[
    (350,50),(350,350),(50,350),(50,50)
]
b_pos=itertools.cycle(block_pos)

block1=Actor("block",center=(50,50))
robot1=Actor("robot",center=(200,200))

def draw():
    screen.clear()
    block1.draw()
    robot1.draw()

def move_block():
    animate(block1,"bounce_end",duration=1,pos=next(b_pos))

def update():
    pass

move_block()
clock.schedule_interval(move_block,1)
pgzrun.go()
