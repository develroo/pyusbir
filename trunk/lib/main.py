#!/usr/bin/python
# -*- coding: utf-8 -*-
#Programmed by Kaan AKŞİT

try:
  import pygame,pygame.camera,sys,time,os,time,threading,usbir
  from pygame.locals import *
except ImportError, err:
  print "couldn't load module. %s" % (err)
  sys.exit()

global_color      = (200, 0, 0)

class window:
  def __init__(self):
    localtime = time.asctime(time.localtime(time.time()))
    print "\x1b\x5b1;33;32m" + localtime + ', Kaan AKŞİT, 2010' + "\x1b[0m"
    print "\x1b\x5b1;31;40m" + 'Pygame version: '+ "\x1b[0m" + str(pygame.version.ver)
    pygame.init()
    window.screen     = pygame.display.set_mode((320, 240),pygame.DOUBLEBUF)
    print "\x1b\x5b1;31;40m" + 'Video info: '+ "\x1b[0m",
    print "\x1b\x5b1;33;20m", pygame.display.Info(), "\x1b[0m"
    self.background = pygame.Surface(window.screen.get_size())
    self.background.set_colorkey((250, 250, 250))
    pygame.display.set_caption(('caption'))
  def image_load(self,image_name):
    image = pygame.image.load(self.filepath(image_name))
    return image
  def image_blit(self,image,posx,posy,angle=0):
    image            = pygame.transform.rotate(image, angle)
    imagepos         = image.get_rect()
    imagepos.centerx = posx
    imagepos.centery = posy
    self.background.blit(image,imagepos)
    return imagepos
  def text_blit(self,script,color,posx,posy,font_type,font_size):
    font            = pygame.font.Font(self.filepath(font_type),font_size)
    text            = font.render(unicode(script), 0, color)
    textpos         = text.get_rect()
    textpos.centerx = posx
    textpos.centery = posy
    self.background.blit(text,textpos)
    return textpos, script
  def filepath(self,filename):
    data_py  = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.normpath(os.path.join(data_py, '..', 'datas'))
    return os.path.join(data_dir, filename)
  def refresh(self):
    window.screen.blit(self.background, (0, 0))
    pygame.display.flip()
    return True
  def blit(self,image,rect):
    self.background.fill((100, 100, 100))
    self.background.blit(image,rect)
    return True
  def draw_rectangle(self,rect,color):
    pygame.draw.rect(self.background, color, (rect[0],rect[1],rect[2],rect[3]),2)
    return True
  def cache_images(self):
    return True
def main():
   screen = window()
   clock  = pygame.time.Clock()
   images = [screen.image_load('green.jpeg'),screen.image_load('red.jpeg')]
   case   = 0
   rate   = 120
   delay  = 1./rate
   glass = usbir.shutterglass(0x0955,0x0007)
   glass.set_rate(rate)
   while True:
     t1 = time.time()
     events = pygame.event.get()
     #for e in events:
       if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
         sys.exit()
     glass.swap_eye()
     clock.tick()
     if case == 1:
       screen.image_blit(images[0],160,120)
       case = 0
     elif case == 0:
       screen.image_blit(images[1],160,120)
       case = 1
     screen.text_blit(('FPS: '+ str(int(clock.get_fps()))),global_color,50,230,"fonts/ka1.ttf",10)
     screen.refresh()
     tlast = delay-(time.time()-t1)
     time.sleep(tlast)
   return
      
if __name__ == "__main__":
  sys.exit(main())