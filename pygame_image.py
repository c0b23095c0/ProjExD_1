import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_x = 0
    bg_y = 0
    bg_img = pg.image.load("fig/pg_bg.jpg")
    img = pg.image.load("fig/3.png")
    img = pg.transform.flip(img, True, False)
    enn = pg.Surface((20,20))
    pg.draw.circle(enn, (255, 0, 0), (10,10),10)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [bg_x, bg_y])
        bg_x += -1
        screen.blit(img, [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()