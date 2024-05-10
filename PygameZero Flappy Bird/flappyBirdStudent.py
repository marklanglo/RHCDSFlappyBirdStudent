# Program Name	: Pygame Zero Flappy Bird v2


#simple code to change window position
x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

import pgzrun
import pygame
import time
from random import randint


#=====================Constants======================
#	What are constants?
#		Constants are variables that never change
#	throughout the project's runtime.  Use-cases for
#	constants are somewhat limited, but in this game
#	we used constants for the game window size and
#	a few of the messages that appear on screen.
#
#	#===Numbers===#
#	WIDTH 	= game window width
#	HEIGHT 	= game window height
#
#	#===Messages===#
#	START_MESSAGE 			= message for beginning game
#	RESTART_MESSAGE 		= message for resetting game
#	CURRENT_SCORE_MESSAGE 	= message to help display the score
#	HIGH_SCORE_MESSAGE 		= message to help display the high score
#	NEW_HIGH_SCORE_MESSAGE 	= displays when new high score is reached
#
#====================================================


#Coordinate System for Pygame
#  (0,0)                      (800,0)
#    +--------------------------+
#    |                          |
#    |                          |
#    |                          |
#    |                          |
#    |                          |
#    |                          |
#    |                          |
#    |                          |
#    |                          |
#    +--------------------------+
#  (0,900)                   (800,900)

#Numbers
WIDTH 					= 800
HEIGHT 					= 900

#Text (strings)
START_MESSAGE 			= "Press JUMP to Start!"
RESTART_MESSAGE 		= "Press R to Play Again!"
CURRENT_SCORE_MESSAGE	= "Current Score: "
HIGH_SCORE_MESSAGE 		= "High-score: "
NEW_HIGH_SCORE_MESSAGE	= "HIGH SCORE!"

#END of constants


#======================Variables=====================
#	What are variables?
#		Variables are values stored in the program that
#	can change.  There are many types of variables, and
#	the simplest ones include strings for words and
#	ints/floats for numbers.  Constants also use these "data-types"
#
#	#===Objects===#
#	player = this variable will hold our player object
#	pipes[] = this variable will store a list of our pipe objects
#	
#	#===Numbers===#
#	score = stores the current score for the game
#	high_score = stores the high score for the current instance of the game
#
#	#===Booleans===#
#	scene_initialized 	= used to initialize the scene for the first run of the
#                         game and for every time the game resets.
#	player_ready 		= used to determine if the player object is ready for inputs
#	spawner_started 	= used to start spawning pipes
#
#====================================================

#Objects
player 				= None
pipes 				= []

#Numbers
score 				= 0
high_score 			= 0

#Booleans
scene_initialized 	= False
player_ready 		= False
spawner_started 	= False

#END of variables


#==================Pipe Class========================
# Short Description:
#		This is the class used to initialize pipe objects
#	in our game.
#====================================================
class Pipe:
    global score
    
    #initializes pipe object
    def __init__(self):
        
        #Actors
        self.actor_top 			= Actor("pipe")
        self.actor_bot 			= Actor("pipe")
        
        #Numbers
        self.actor_height 		= randint(-150, 250)
        self.actor_top.pos 		= (WIDTH + 200, self.actor_height)
        self.actor_bot.pos 		= (WIDTH + 200, self.actor_height + 800)
        self.actor_bot.angle 	= 180
        self.speed 				= 3
        
        #Booleans
        self.has_scored 		= False

    #used to draw pipe object on screen
    def draw(self):
        self.actor_top.draw()
        self.actor_bot.draw()

    #updates the pipe object in the game
    def update(self, speed):
        
        #1. We want to update the actors position using the speed variable we
        #	pass into our update function.  We need to figure out how to update
        #	our x position with the speed.
        #
        #   HINT:
        #         You can access and change the x position of the actor
        #         for the pipe with the following code:
        #             self.actor_top.x AND self.actor_bot.x
        
        pass #delete the pass when you think you have your solution
        
        #self.			 -= 		    #update the top pipe's x
        #self.			 -= 		    #update the bottom pipe's x

    #returns the top pipe's hitbox
    def top_hitbox(self):
        return self.actor_top._rect

    #returns the bottom pipe's hitbox
    def bot_hitbox(self):
        return self.actor_bot._rect
    
    #checks if the pipe is eligible to add a point to the score
    def check_add_point(self, other_x):
        global score
        
        if self.actor_top.x < other_x and self.has_scored == False:
            sounds.sfx_point.play()
            score += 1
            self.has_scored = True
            
#END of pipe class


#================Player Class========================
# Short Description:
#		This is the class used to initialize the player
#	object in our game.
#====================================================
class Player:
    
    #initializes player object
    def __init__(self):
        
        #Strings
        self.actor_name			 = "bird"
        
        #Actors
        self.actor               = Actor(self.actor_name)
        
        #Numbers
        self.actor.pos           = (WIDTH/2, HEIGHT/2)
        self.fly_speed           = -9
        self.gravity             = 0.3
        self.gravity_fast        = 1
        self.velocity            = 0
        self.angle               = 0
        self.min_angle           = -80
        self.max_angle           = 20
        self.rotation_speed      = 3
        self.rotation_speed_fast = 7
        
        #Booleans
        self.has_lost            = False

    #used to draw player on the screen
    def draw(self):
        self.actor.draw()

    #used to update the position of the player on the screen
    def update(self):
        
        #update the velocity of the bird using gravity
        #add the velocity to the actor
        if self.actor.y < HEIGHT - 35:
            
            #if player has lost the gravity is more
            if self.has_lost:
                
                if self.velocity < 0:
                    
                    self.velocity = 0
                    
                self.velocity += self.gravity_fast
                self.actor.y += self.velocity
                
            else:
                
                #2. The above code is how the bird falls during the losing condition, below you need to
                #write the code for how the bird normally falls.  Uncomment by removing the '#'s

                # HINT–You will need the following:
                # self.velocity, self.gravity, self.actor.y
                
                pass #delete the pass when you think you have your solution
                
                #			 += 			    #update the velocity
                #			 += 			    #update the actor y position

        #update the rotation of the bird
        if self.velocity > 0 and self.actor.angle > self.min_angle:
            
            self.actor.angle -= self.rotation_speed
            
        elif self.has_lost and self.actor.angle > self.min_angle:
            
            self.actor.angle -= self.rotation_speed_fast


    #used to make the player object fly
    def fly(self):

        #checks if the player has lost
        if not self.has_lost:
            sounds.sfx_wing.play()
            #reset velocity to be the flying speed
            self.velocity = self.fly_speed
            #reset the angle to max
            self.actor.angle = self.max_angle

    #used to check if the player hits another object
    def check_collision(self, otherActor):
        if self.actor.colliderect(otherActor):
            return True
        else:
            return False

    #used to change the state of whether the player has lost
    def set_has_lost(self, _has_lost):
        self.has_lost = _has_lost
        
    #used to reset the player to its initial state
    def reset(self):
        self.actor               = Actor(self.actor_name)
        self.actor.pos           = (WIDTH/2, HEIGHT/2)
        self.velocity            = 0
        self.angle               = 0
        self.has_lost            = False

#END of player class


#=================Draw Function======================
# Description:
#		This function is used to draw onto the window
#	of the game.  The order of our code in here is
#	very important.  The higher the code is in this
#	function the earlier it is drawn.  If you want
#	something drawn in the background you draw it first
#	, and if you want something drawn in the foreground
#	you draw it last.  At the start of every draw we
#	clear the screen.
#
#	Below is the draw order of our game:
#
#	1) Background
#	2) Scene Objects
#	3) Player Object
#	4) Text and Messages
#====================================================
def draw():

    #Initialization of variables
    
    high_score_text = HIGH_SCORE_MESSAGE + str(high_score)
    current_score_text = CURRENT_SCORE_MESSAGE + str(score)
    
    start_message_x = (WIDTH // 2) - 110
    start_message_y = (HEIGHT // 2) - 150
    
    #END of variable initialization

    #clears the screen
    screen.clear()
    #END of clear screen
    
    #Draw Background
    screen.fill((91, 168, 166))
    #END of draw background
    
    #Draw Scene Objects (pipes)
    for pipe in pipes:
        pipe.draw()
    #END of draw scene objects
        
    #Draw Player
    player.draw()
    #END of draw player

    #===Draw Messages===
    # Basic Syntax of text function:
    #
    #	pseudo-syntax:
    #		screen.draw.text( text, position, color, background_color, fontsize)
    #
    #	syntax:
    #		screen.draw.text( "My text", (x, y), color = (R, G, B)
    #
    #===================
    
    #3. Experiment with all of the below text functions (from here down to line 383
    #		Note: To edit the messages themselves, look near the top of the file for the project
    #		Constants
    #Link to Text Function Documentation: https://pygame-zero.readthedocs.io/en/stable/ptext.html
    #Use google color picker to help select colors
    # If you have extra time, you may create your own additional text
    
    #Score text
    screen.draw.text(current_score_text, (20, 100),
                     color = (110, 110, 65),
                     background = (4, 56, 1),
                     fontsize = 32,
                     owidth = 1,
                     ocolor = (255, 255, 150))
    
    #High Score text
    screen.draw.text(high_score_text, (WIDTH - 200, 100),
                     color = (110, 110, 65),
                     background = (4, 56, 1),
                     fontsize = 32,
                     owidth = 1,
                     ocolor = (255, 255, 150))
    
    if player.has_lost:
        
        #Restart Game Text
        screen.draw.text(RESTART_MESSAGE, (start_message_x, start_message_y),
                         color = (110, 110, 65),
                         background = (255, 255, 150),
                         fontsize = 32)
        
        if score > 0 and score == high_score:
            
            #High Score Text
            screen.draw.text(NEW_HIGH_SCORE_MESSAGE, (start_message_x + 35, start_message_y + 100),
                         color = (110, 110, 65),
                         background = (255, 255, 150),
                         fontsize = 32)
            
    elif not player_ready:
        
        #Start Gane Text
        screen.draw.text(START_MESSAGE, (start_message_x, start_message_y),
                         color = (110, 110, 65),
                         background = (255, 255, 150),
                         fontsize = 32)
        
#END of draw messages


#==============================Update Function========================================
# Description:
#		This function is used to update the scene of the game.
#
#
#	What is a scene?
#		The scene is basically just the environment our game/gamestate takes place in.
#	Our game just has one scene, but many games have several scenes. Something such as
#	a new level or a seperate menu screen could be considered a scene.
#
#	Update Function Logic:
#		The main thing controlling the state of our scene are booleans that determine
#	what is happening in the game.  Our booleans that are relevant check if the scene
#	is initialized (scene_initialized), if the player is ready (player_ready), if the
#	player has lost (player.has_lost), and if the spawner was started.
#
#	A) Every time we start or restart the game, we reinitialize it with the first if
#		statement.  Within the first if statement we also start the spawner for the
#		duration of the games runtime.
#
#	B) We run the player update function from the class
#
#	C) We update the pipes
#
#	D) Gamestate actions, we check if the player earns points or loses
#
#=====================================================================================
def update():
    #We need to call these global variables whenever we want to modify them
    #In normal programs its best to avoid having too many global variables,
    #however, since this game is a single file the globals are fine for now
    global scene_initialized
    global spawner_started
    global player_ready
    global score
    global pipes

    #A) We check if our scene has been (re)initialized, if not we initialize it
    if not scene_initialized:
        #clear any pipes from a previous run
        pipes.clear()
            
        #start the spawner if it hasn't been started
        if not spawner_started:
            clock.schedule_interval(spawn_pipe, 3.0)
            spawner_started = True
        
        #spawns or resets the player
        if player == None:
            spawn_player()
        else:
            player.reset()
            
        #sets the score to 0        
        score = 0
        
        scene_initialized = True

    #B) We check if a valid boolean for our player update is true, then if it is
    #	then we run the player.update() function from our class
    if player_ready or player.has_lost:
        player.update()
    
    #C) We check for a valid boolean and will update the pipes
    if player_ready:
        move_pipes()
        
    #D) Gamestate actions, we check if a set of pipes can add a point to the player, and
    #	we also check the collision to see if the player hits a pipe and loses
    for pipe in pipes:
        pipe.check_add_point(player.actor.x)
    
    check_collision()
    
#END of update


#=============Check Collision Function===============
# Description:
#		This function checks whether the player has
#	collided with a pipe.  If they have then we
#	change the state inside the player object for
#	our boolean "player.has_lost" to true.  There are
#	extra checks for if the player goes to high, or
#	for if they hit the ground.
#
#		Additionally, there is a check for if the
#	player sets a high score once it's determined
#	they've lost.
#====================================================
def check_collision():
    global player_ready
    global high_score
    
    #We check every pipe to see if it collides with the player
    # and we check if the player goes out of bounds
    for pipe in pipes:
        
        pass #remove this pass once you believe you have a correct answer
    
        #4. Consider all 4 losing conditions and use functions from
        #	the player class to check these conditions in the if statement below
        #	Uncomment the if statement by deleting the #'s, and remove the "if False:"
        #
        #   HINT: You will need to use the check_collision(otherActor) function from the Player class.
        #         To check the player's position you will need to use player.actor.x or player.actor.y
        
#         if player.						
#           or player.						
#           or player.			 < 			
#           or player.			 > 			:
        if False:
            #we set this boolean to 0 so the player
            # can't input any jump actions
            player_ready = False
            
            #simple if statement to control sound effects
            # and to switch "player.has_lost" to True.
            if not player.has_lost:
                sounds.sfx_smack.play()
                
                #this sound is played if the player isn't
                # at the floor height
                if player.actor.y < HEIGHT - 50:
                    time.sleep(0.7)
                    sounds.sfx_fall.play()

                player.set_has_lost(True)
            
            #5. Try to make an if statement to check if our current score
            #	is greater than the high_score, if this is the case we
            #	want to assign ('=') high_score the value of score
            #		Uncomment by deleting the #       
            
#             if 		 > 		:
                #assignment code goes here
                sounds.sfx_high_score.play()        
            
#END of check_collision
            

#============On Key Down Function====================
# Description:
#		This function reads our keyboard inputs and uses
#	then for meaningful actions in the game.  We have 3
#	possible actions:
#
#	A) Set player ready and jump
#	B) Jump
#	C) Reset game
#====================================================
def on_key_down(key):
    global scene_initialized
    global player_ready
    
    #We check if the player has lost so they can't fly during a losing state
    if not player.has_lost:
        
        #A) Set player ready and Jump with 'up arrow', 'space', 'W', or 'J'
        if key in (keys.UP, keys.SPACE, keys.W, keys.J) and not player_ready:
            player.fly()
            player_ready = True
            
        #B) Jump with 'up arrow', 'space', 'W', or 'J'
        elif key in (keys.UP, keys.SPACE, keys.W, keys.J):
            player.fly()
            
    else:
        
        #C) Reset the game with 'R'
        if key == keys.R:
            
            scene_initialized = False
        
#END of on_key_down
        
#===On Mouse Down===
#	This does the same as steps 1 and 2 but just for the mouse
def on_mouse_down():
    global player_ready
    
    if not player.has_lost:
        
        #A) Set player ready and Jump
        if not player_ready:
            
            player.fly()
            player_ready = True
            
        #B) Jump
        else:
            player.fly()

#END of on_mouse_down


#===Spawn Pipe Function===
def spawn_pipe(num_pipes = 1):
    global pipes
    global player_ready
    
    #we spawn a new pipe and add it to the pipes list
    if player_ready:
        pipes += [Pipe() for _ in range(num_pipes)]

#END of spawn_pipe


#===Spawn Player Function===
def spawn_player():
    global player
    
    #initialize player object
    player = Player()
    
#END of spawn_player


#===Move Pipes Function===
def move_pipes():
    global pipes
    
    for pipe in pipes:
        
        #we run the update function from the pipe class
        pipe.update(pipe.speed)

#END of move_pipes


#We run the game
pgzrun.go()


