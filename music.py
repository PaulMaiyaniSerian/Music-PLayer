import pygame
from tkinter import Tk, Button
import sys
import math
import os
from mutagen.mp3 import MP3
from pygame import color
from random import randrange, randint

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0, 255,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
OLIVE = (128,128,0)
BLUE = (0,0,255)
MAROON = (128,0,0)
OVER =(255,12, 12)
GRAY = (167, 148, 148)
REDDISH = (255, 2, 2)
colors = [WHITE, GREEN, RED, YELLOW, OLIVE, BLUE, MAROON, OVER, GRAY, REDDISH]
pygame.init()

SIZE = (700, 500)

MAIN_WINDOW = pygame.display.set_mode(SIZE)


pygame.display.set_caption("PAUL'S Music Player")

# loop untill user clicks false
done = False





# balance framerate
clock = pygame.time.Clock()

def draw_music_timer(time, color_r, x, y):
    font3 = pygame.font.SysFont('Calibri', 30, True, False)
    time = font3.render(time, True, color_r)
    MAIN_WINDOW.blit(time, [x, y])


# def get_music_time():
# time_sec = pygame.mixer.music.get_pos() * 0.001 
# minutes = int(time_sec // 60) * -1
# seconds = int(time_sec % 60)
# font3 = pygame.font.SysFont('Calibri', 50, True, False)   
# time_st = font3.render(f"{minutes} : {seconds}", True, GREEN)


index = 0


list_music = []

if list_music:
    song_path = list_music[index]
else:
    current_title = "Drag Music"



def play(music_name):
    global current_title, song_path
    pygame.mixer.music.load(music_name)
    current_title = os.path.basename(str(music_name))
    song_path = music_name
    pygame.mixer.music.play()
    
  


if list_music:
    current_title = os.path.basename(str(list_music[index]))
else:
    current_title = "PAUL'S Music Player>> Drag Music HERE!!"



paused = False
playing = False
stoped = False
started = True

def busy():
    return pygame.mixer.music.get_busy()


def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()


triangle = {
    "point1": [SIZE[0] - 350, SIZE[1] - 100],
    "point2": [SIZE[0] - 350, SIZE[1] - 70],
    "point3": [380, 415]
}
go_next = True
controls = False
at_end = False

def next():
    global list_music, index, started, playing, go_next
    if list_music:
        if index == len(list_music) - 1:
            index += -(len(list_music))

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

        else:
            go_next = True
            started = False
            playing = True
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        
            
            # play(list_music[index])
another_index = 0
def prev():
    global list_music, index, started, playing, go_next
    if list_music:
        if index == 0:
            index += 1
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        elif index < 0:
            index = 1
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        else:
            go_next = False
            started = False
            playing = True
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        
            # play(list_music[index])

clicked=False

def draw_prev( ):
    # pygame.draw.rect(MAIN_WINDOW, RED,  [SIZE[0] - 450, SIZE[1] - 100,30, 30]
    font_title = pygame.font.SysFont('Calibri', 40, True, False)   
    music_title = font_title.render("I<", True, GRAY)
    MAIN_WINDOW.blit(music_title, [SIZE[0] - 452, SIZE[1] - 103])

def draw_next():
    # pygame.draw.rect(MAIN_WINDOW, RED,  [SIZE[0] - 250, SIZE[1] - 100,30, 30])
    font_title = pygame.font.SysFont('Calibri', 40, True, False)   
    music_title = font_title.render(">I", True, GRAY)
    MAIN_WINDOW.blit(music_title, [SIZE[0] - 250, SIZE[1] - 103])

def draw_play():
    pygame.draw.rect(MAIN_WINDOW, WHITE,  [SIZE[0] - 350, SIZE[1] - 100,30, 30])
    pygame.draw.rect(MAIN_WINDOW,  OLIVE,  [SIZE[0] - 346, SIZE[1] - 95,7, 20])
    pygame.draw.rect(MAIN_WINDOW,  OLIVE,  [SIZE[0] - 332, SIZE[1] - 95,7, 20])
def draw_pause():
    pygame.draw.polygon(MAIN_WINDOW, (200, 107, 107),  [triangle["point1"], triangle["point2"], triangle["point3"]])

class Bar:
    def __init__(self):
        self.init_dist = 20
        self.seek_dist = 660

    def draw(self):
        pygame.draw.rect(MAIN_WINDOW, WHITE,[self.init_dist, 350,660, 10])
    
    def seek(self, length,  elapsed):
        if length != 0:
            self.seek_pos = (self.seek_dist - (((length - elapsed) / length) * self.seek_dist)) + self.init_dist
            pygame.draw.rect(MAIN_WINDOW, REDDISH,[self.init_dist, 350,self.seek_pos-30, 10])
            pygame.draw.circle(MAIN_WINDOW, RED, [self.seek_pos, 355], 10)
        else:
            pygame.draw.circle(MAIN_WINDOW, BLUE, [self.init_dist + 10, 355], 10)
  
song_length = 0
time_sec = 0

vol = 1
pygame.mixer.music.set_volume(round(vol,1))

class Volume:
    def __init__(self):
        self.initial = 0

    def draw(self):
        pygame.draw.rect(MAIN_WINDOW, WHITE,[650, 150,10, 150])
        # pygame.draw.rect(MAIN_WINDOW, GREEN,[640, 150,30, 10])

    def adjust_volume(self, distance, direction="up"):
        pygame.draw.rect(MAIN_WINDOW, GREEN,[640, distance,30, 10])
        # pygame.draw.rect(MAIN_WINDOW, GREEN,[650, distance,10, 150-15])
        pass

vol_dist = 150
seek_bar = Bar()
volume_bar = Volume()

MUSIC_END = pygame.USEREVENT + 1
# draw snow
snow_cord_list = []

for i in range(500):
    x = randrange(0,SIZE[0])
    y = randrange(0,SIZE[1])
    snow_cord_list.append([x,y])

def draw_snow():
     for i in range(len(snow_cord_list)-1):
        pygame.draw.circle(MAIN_WINDOW, colors[randint(0,5)], snow_cord_list[i], 2)

        snow_cord_list[i][1] += 1

        if snow_cord_list[i][1] > SIZE[1]:
            snow_cord_list[i][1] = 1


# main program loop
while not done:
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            if index == len(list_music)-1:
                at_end = True
                index += -(len(list_music))
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                play(list_music[index])
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                

            else:
                at_end = False
                if index < len(list_music)-1 and go_next and not at_end:
                    index += 1
                    play(list_music[index])
                    # print(index)
                elif index < len(list_music)-1 and go_next and at_end:
                    index = 0
                    play(list_music[index])
                    # print(index)
                elif index < len(list_music)-1 and not go_next and not at_end:
                    index -= 1
                    play(list_music[index])
                    # print(index)
                else:
                    index = 0
                    play(list_music[index])
                    # print(index)

            
        elif event.type == pygame.DROPFILE:
            # print(event.file)
            if os.path.isfile(event.file):
                # check extension:
                file = os.path.basename(str(event.file))
                file_ext = os.path.splitext(file)
                if file_ext[1] == ".mp3":
                    if event.file in list_music:
                        index_music = list_music.index(event.file)
                        started = False
                        playing = True
                        pygame.mixer.music.stop()
                        play(list_music[0])
                        

                    else:
                        list_music.append(event.file)
                        index_music = list_music.index(event.file)
                        
                        started = False
                        playing = True
                        pygame.mixer.music.stop()
                        # play
                       
                        play(list_music[0])
     
                else:
                    print("unsupprorted format")
                
            if os.path.isdir(event.file):
                for (path, folder_names, filenames) in os.walk(event.file):
                    if filenames:
                        for filename in filenames:
                            full_path = path + "\\" + filename
                            file = os.path.basename(str(full_path))
                            file_ext = os.path.splitext(file)
                            if file_ext[1] == ".mp3":
                                if filename not in list_music:
                                    list_music.append(full_path)
                                    started = False
                                    playing = True
                                    pygame.mixer.music.stop()
                                    play(list_music[0])
                                else:
                                    started = False
                                    playing = True
                                    pygame.mixer.music.stop()
                                    play(list_music[0])
                                    print("already")
                            # print(full_path)
                    # print(path)

        elif event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if busy() and not paused:
                    pause()
                    paused = True
                    playing = False
                elif busy() and paused:
                    unpause()
                    playing = True
                    paused = False
                elif not busy() and not paused:
                    if list_music:
                        play(list_music[index])
                        started = False
                        playing = True
                     

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False
                paused = False
                stoped = True
            
            if event.key == pygame.K_n:
                controls = True
                next()
            

            if event.key == pygame.K_p:
                controls = True
                prev()

                
                    
            if event.key == pygame.K_UP:
                if vol_dist == 300 or vol_dist > 150:
                    vol += round(0.1,1)
                    pygame.mixer.music.set_volume(vol)
                    # print(vol)
                    vol_dist -= 15
    
            if event.key == pygame.K_DOWN:
                if vol_dist == 150 or vol_dist < 300:
                    vol -= round(0.1,1)
                    pygame.mixer.music.set_volume(vol)
                    # print(vol)
                    vol_dist += 15

            if event.key == pygame.K_RIGHT:
                # buggy

                pass

            if event.key ==pygame.K_LEFT:
                pass

            if event.key == pygame.K_r:
                index  -= 1
                pygame.mixer.music.stop()
                pygame.mixer.music.rewind()
                print(index)
                


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, False ,False):
                # print(pygame.mouse.get_pos())
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1]  >= 381 and mouse_pos[1] <= 428 and mouse_pos[0] >= 240 and mouse_pos[0] <= 280:
                    controls = True
                    prev()
                elif mouse_pos[1]  >= 381 and mouse_pos[1] <= 428 and mouse_pos[0] >= 440 and mouse_pos[0] <= 480:
                    controls = True
                    next()
                
                elif mouse_pos[1]  >= 381 and mouse_pos[1] <= 428 and mouse_pos[0] >= 338 and mouse_pos[0] <= 381:
                    if busy() and not paused:
                        pause()
                        paused = True
                        playing = False
                    elif busy() and paused:
                        unpause()
                        playing = True
                        paused = False
                    elif not busy() and not paused:
                        if list_music:
                            play(list_music[index])
                            started = False
                            playing = True
                    
        
        
        elif event.type == pygame.MOUSEWHEEL:
            # print(pygame.mouse.get_pos())
            if pygame.mouse.get_pos()[1] >= 332 and pygame.mouse.get_pos()[1] <= 359:
                pass

            else:
                if event.y == 1:
                    if vol_dist == 300 or vol_dist > 150:
                        vol += round(0.1,1)
                        pygame.mixer.music.set_volume(vol)
                        # print(vol)
                        vol_dist -= 15
                else:
                    if vol_dist == 150 or vol_dist < 300:
                        vol -= round(0.1,1)
                        pygame.mixer.music.set_volume(vol)
                        # print(vol)
                        vol_dist += 15

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
    
            if event.key == pygame.K_DOWN:
                pass
        
    # gamelogic

    MAIN_WINDOW.fill(BLACK)
    # draw_snow()
    # update
    # draw  time
    if current_title != "PAUL'S Music Player>> Drag Music HERE!!":
        current_song = MP3(song_path)
        song_length = current_song.info.length
        song_min = int(song_length // 60)
        song_sec = int(song_length % 60)
        draw_music_timer(f"{song_min}:{song_sec}", GREEN, 30, 400)
    else:
        draw_music_timer(f"__ : __", GREEN, 30, 400)
    
    font_title = pygame.font.SysFont('Calibri', 20, True, False)   
    music_title = font_title.render(current_title, True, WHITE)

    MAIN_WINDOW.blit(music_title, [10, 10])


    volume_bar.draw()
    volume_bar.adjust_volume(distance=vol_dist)


    seek_bar.draw()
    seek_bar.seek(song_length, time_sec)

    
    

  
    if started:
        draw_pause()
        time_sec = pygame.mixer.music.get_pos() * 0.001 
        minutes = int(time_sec // 60)
        seconds = int(time_sec % 60)
        draw_music_timer(str(f'__ : __'), GREEN, 590, 400)
  

    elif playing and not started:
        draw_play()
        time_sec = pygame.mixer.music.get_pos() * 0.001 
        minutes = int(time_sec // 60) 
        seconds = int(time_sec % 60)
        draw_music_timer(str(f'{minutes} : {seconds}'), GREEN, 590, 400)

        if not controls:
            pygame.mixer.music.set_endevent(MUSIC_END)
            

        

    elif not playing and paused and not started:
        draw_pause()
        time_sec = pygame.mixer.music.get_pos() * 0.001 
        minutes = int(time_sec // 60)
        seconds = int(time_sec % 60)
        draw_music_timer(str(f'{minutes} : {seconds}'), GREEN, 590, 400)
  

    draw_next()
    draw_prev()
 
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
