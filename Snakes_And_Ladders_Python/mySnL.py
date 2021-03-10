"""
Snakes&Ladders|Vaikuntapalli|Paramapadam Game by Jay - 13/03/20
Github: mr-circuit
"""

import pygame
from random import randint

timer = pygame.time.Clock()

# #---Initializations

pygame.init()
width = 1280
height = 720
favicon = pygame.image.load("favicon.png")
displaySettings = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Vaikuntapalli | Paramapadam | S&L")
pygame.display.set_icon(favicon)
pygame.display.update()

# #---Colour Schemes

# #-RGB

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# #-Black & White

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# #-Other Colours

yellow = (255, 255, 0)
purple = (127, 0, 255)
maroon = (195, 73, 32)
aqua = (0, 255, 255)
pink = (215, 72, 148)

# #---Game Looks

# #-Onscreen

board = pygame.image.load("board.png")
startPage = pygame.image.load("startpage.png")
gamePage = pygame.image.load("gamepage.png")
loadingPage = pygame.image.load("loadingpage.png")
loadingPage1 = pygame.image.load("loadingpage1.png")
loadingPage2 = pygame.image.load("loadingpage2.png")
loadingPage3 = pygame.image.load("loadingpage3.png")
loadingPage4 = pygame.image.load("loadingpage4.png")
loadingPage5 = pygame.image.load("loadingpage5.png")
loadingPage6 = pygame.image.load("loadingpage6.png")
loadingPage7 = pygame.image.load("loadingpage7.png")
loadingPage8 = pygame.image.load("loadingpage8.png")
loadingPage9 = pygame.image.load("loadingpage9.png")
loadingPage10 = pygame.image.load("loadingpage10.png")
loadingPage11 = pygame.image.load("loadingpage11.png")
creditsPage = pygame.image.load("creditspage.png")

# #-Dice

side1 = pygame.image.load("side1.png")
side2 = pygame.image.load("side2.png")
side3 = pygame.image.load("side3.png")
side4 = pygame.image.load("side4.png")
side5 = pygame.image.load("side5.png")
side6 = pygame.image.load("side6.png")

# #-Players

redPlayer = pygame.image.load("redcoin.png")
yellowPlayer = pygame.image.load("yellowcoin.png")
greenPlayer = pygame.image.load("greencoin.png")
bluePlayer = pygame.image.load("bluecoin.png")

# #---Music

# #-Audio Files

pygame.mixer.music.load("background.wav")
loser = pygame.mixer.Sound("looser.wav")
snakehiss = pygame.mixer.Sound("snakehiss.wav")
ladder = pygame.mixer.Sound("ladder.wav")
winner = pygame.mixer.Sound("winner.wav")


# --Music_Settings--#
def startPage_Sec_Buttons(text, xPos, yPos, x, y, w, h, i, a, fs):
    mPosition = pygame.mouse.get_pos()
    mClick = pygame.mouse.get_pressed()
    if x + w > xPos > x and y + h > yPos > y:
        pygame.draw.rect(displaySettings, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(displaySettings, i, [x, y, w, h])
    buttons_text(text, (x + w + x) / 2, (y + h + y) / 2, fs)


##---Mouse_Events---##
mPosition = pygame.mouse.get_pos()
mClick = pygame.mouse.get_pressed()


##---Font---##
# --Font for Buttons--#
def buttons_text(text, x, y, fs):
    textFont = pygame.font.Font('comicbd.ttf', fs)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = (x, y)
    displaySettings.blit(TextSurf, TextRect)


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


# --Notifications Font--#
def notification_text(text, x, y, fs, c):
    textFont = pygame.font.Font('comicbd.ttf', fs)
    TextSurf, TextRect = new_text_objects(text, textFont)
    TextRect.center = (x, y)
    displaySettings.blit(TextSurf, TextRect)


def new_text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


##---Game Working Conditions---##
# --Player_Movements--#
def player(a):
    l1 = [[906, 606], [66, 658], [132, 658], [198, 658], [264, 658], [328, 658], [391, 658], [457, 658], [523, 658],
          [587, 658], [652, 658], [652, 593], [587, 593], [523, 593], [457, 593], [391, 593], [328, 593], [264, 593],
          [198, 593], [132, 593], [66, 593], [66, 526], [132, 526], [198, 526], [264, 526], [328, 526], [391, 526],
          [457, 526], [523, 526], [587, 526], [652, 526], [652, 461], [587, 461], [523, 461], [457, 461], [391, 461],
          [328, 461], [264, 461], [198, 461], [132, 461], [66, 461], [66, 393], [132, 393], [198, 393], [264, 393],
          [328, 393], [391, 393], [457, 393], [523, 393], [587, 393], [652, 393], [652, 329], [587, 329], [523, 329],
          [457, 329], [391, 329], [328, 329], [264, 329], [198, 329], [132, 329], [66, 329], [66, 263], [132, 263],
          [198, 263], [264, 263], [328, 263], [391, 263], [457, 263], [523, 263], [587, 263], [652, 263], [652, 197],
          [587, 197], [523, 197], [457, 197], [391, 197], [328, 197], [264, 197], [198, 197], [132, 197], [66, 197],
          [66, 132], [132, 132], [198, 132], [264, 132], [328, 132], [391, 132], [457, 132], [523, 132], [587, 132],
          [652, 132], [652, 66], [587, 66], [523, 66], [457, 66], [391, 66], [328, 66], [264, 66], [198, 66],
          [132, 66], [66, 66]]
    l2 = l1[a]
    x = l2[0] - 33
    y = l2[1] - 33
    return x, y


# --Ladders--#
def ladders(x):
    if x == 5:
        return 16
    elif x == 9:
        return 13
    elif x == 21:
        return 23
    elif x == 28:
        return 53
    elif x == 42:
        return 46
    elif x == 56:
        return 85
    elif x == 62:
        return 78
    elif x == 69:
        return 73
    elif x == 94:
        return 96
    else:
        return x


# --Snakes--#
def snakes(x):
    if x == 7:
        return 4
    elif x == 35:
        return 22
    elif x == 60:
        return 40
    elif x == 70:
        return 34
    elif x == 74:
        return 54
    elif x == 84:
        return 71
    elif x == 99:
        return 24
    else:
        return x


# --Dice_Rolling--#
def dice(a):
    if a == 1:
        a = side1
    elif a == 2:
        a = side2
    elif a == 3:
        a = side3
    elif a == 4:
        a = side4
    elif a == 5:
        a = side5
    elif a == 6:
        a = side6

    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 1000:
        displaySettings.blit(a, (717, 327))
        pygame.display.update()


# --Player_Turn_Buttons--#
def player_button(text, xPos, yPos, x, y, w, h, i, a, fs):
    mPosition = pygame.mouse.get_pos()
    mClick = pygame.mouse.get_pressed()
    if x + w > xPos > x and y + h > yPos > y:
        pygame.draw.rect(displaySettings, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(displaySettings, i, [x, y, w, h])
    buttons_text(text, (x + w + x) / 2, (y + h + y) / 2, fs)


# --Who's Turn--#
def turn(score, l, s):
    a = randint(1, 6)  # player dice roll
    if a == 6:
        six = True
    else:
        six = False
    p = dice(a)
    score += a
    if score <= 100:
        # checking for ladders for player
        lad = ladders(score)
        if lad != score:
            l = True
            pygame.mixer.Sound.play(ladder)
            time = pygame.time.get_ticks()
            score = lad
        # checking for snakes for player
        snk = snakes(score)
        if snk != score:
            s = True
            pygame.mixer.Sound.play(snakehiss)
            score = snk
    # checks if player score is not grater than 100
    else:
        score -= a
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 1500:
            notification_text("Can't move!", 991, 214, 35, black)
            pygame.display.update()
    return score, l, s, six


# --Buttons--#
def button(text, xPos, yPos, x, y, w, h, i, a, fs, b):
    if x + w > xPos > x and y + h > yPos > y:
        pygame.draw.rect(displaySettings, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if b == 1 or b == 7:
                noOfPlayers()
            elif b == 5:
                return 5
            elif b == 0:
                endGame()
            elif b == "s" or b == 2 or b == 3 or b == 4:
                return b
            else:
                return True
    else:
        pygame.draw.rect(displaySettings, i, [x, y, w, h])
    buttons_text(text, (x + w + x) / 2, (y + h + y) / 2, fs)


##---Game Pages---##
# --Introduction Page--#
def gameOpening():
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 2500:
        displaySettings.blit(loadingPage, (0, 0))
        pygame.display.update()
    while True:
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage1, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage2, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage3, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage4, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage5, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage6, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage7, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage8, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage9, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage10, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 100:
            displaySettings.blit(loadingPage11, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()


##--Credits Page--##
def creditPage():
    while True:
        displaySettings.blit(creditsPage, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endGame()
        mPosition = pygame.mouse.get_pos()
        mClick = pygame.mouse.get_pressed()
        if button("Back", mPosition[0], mPosition[1], width / 2 - 100, 600, 200, 50, red, pink, 25, 20):
            mainPage()
        pygame.display.update()


# --Main Page--#
def mainPage():
    pygame.mixer.music.play(-1)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endGame()
        mPosition = pygame.mouse.get_pos()
        mClick = pygame.mouse.get_pressed()

        displaySettings.blit(startPage, (0, 0))
        button("Play", mPosition[0], mPosition[1], (width / 4 - 50), height / 2, 200, 100, green, aqua, 60, 1)
        button("Quit", mPosition[0], mPosition[1], (width / 4 + 480), height / 2, 200, 100, red, pink, 60, 0)

        mPosition = pygame.mouse.get_pos()
        if startPage_Sec_Buttons("Mute Audio", mPosition[0], mPosition[1], 214, 505, 200, 50, purple, maroon, 25):
            pygame.mixer.music.pause()
        if startPage_Sec_Buttons("Audio", mPosition[0], mPosition[1], 527, 505, 200, 50, purple, maroon, 25):
            pygame.mixer.music.unpause()
        if startPage_Sec_Buttons("Credits", mPosition[0], mPosition[1], 838, 505, 200, 50, purple, maroon, 25):
            creditPage()
        pygame.display.update()


# --Players Selection Page--#
def noOfPlayers():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endGame()
        mPosition = pygame.mouse.get_pos()
        mClick = pygame.mouse.get_pressed()
        button1 = button2 = button3 = button4 = button5 = -1
        displaySettings.blit(startPage, (0, 0))
        button1 = button("Single Player", mPosition[0], mPosition[1], (width / 2 - 150), 250, 300, 50, green, aqua, 30,
                         "s")
        button2 = button("Two Players", mPosition[0], mPosition[1], (width / 2) - 150, 350, 300, 50, green, aqua, 30, 2)
        button3 = button("Three Players", mPosition[0], mPosition[1], (width / 2) - 150, 450, 300, 50, green, aqua, 30,
                         3)
        button4 = button("Four Players", mPosition[0], mPosition[1], (width / 2) - 150, 550, 300, 50, green, aqua, 30,
                         4)
        button5 = button("Back", mPosition[0], mPosition[1], 0, 650, 200, 50, red, pink, 30, 5)
        if button1 == "s":
            playGame(21)
        if button2 == 2:
            playGame(2)
        if button3 == 3:
            playGame(3)
        if button4 == 4:
            playGame(4)
        if button5 == 5:
            mainPage()
        pygame.display.update()


##---Play and Quit---##
# --Close_Game--#
def endGame():
    pygame.quit()
    quit()


# --Play_Game--#
def playGame(b):
    button6 = -1
    time = 3000
    if button6 == 7:
        noOfPlayers()
    displaySettings.blit(gamePage, (0, 0))
    displaySettings.blit(board, (width / 40, height / 22.5))
    xR = xY = xG = xB = 740 - 33
    yR = yY = yG = yB = 487 - 33
    displaySettings.blit(redPlayer, (xY, yY))
    if 5 > b > 1 or b == 21:
        displaySettings.blit(yellowPlayer, (xY, yY))
    if 5 > b > 2 or b == 21:
        displaySettings.blit(greenPlayer, (xG, yG))
    if 5 > b > 2:
        displaySettings.blit(bluePlayer, (xB, yB))
    p1 = "Player 1"
    p1score = 0
    if b == 21:
        p2 = "Computer"
        p2score = 0
    if 5 > b > 1:
        p2 = "Player 2"
        p2score = 0
    if 5 > b > 2:
        p3 = "Player 3"
        p3score = 0
    if 5 > b > 3:
        p4 = "Player 4"
        p4score = 0
    t = 1
    playGame = True
    while True:
        l = False
        s = False
        time = 3000
        displaySettings.blit(gamePage, (0, 0))
        displaySettings.blit(board, (width / 40, height / 22.5))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endGame()
        if b == 21:
            if player_button("Player 1", mouse[0], mouse[1], 834, 297, 200, 50, red, grey, 30):
                if t == 1:
                    p1score, l, s, six = turn(p1score, l, s)
                    if not six:
                        t += 1
                    xR, yR = player(p1score)
                    if p1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            notification_text("Player 1 Wins", 991, 214, 50, black)
                            pygame.mixer.Sound.play(winner)
                            pygame.display.update()
                        break
            player_button("Computer", mouse[0], mouse[1], 1064, 297, 200, 50, yellow, grey, 30)
            if True:
                if t == 2:
                    p2score, l, s, six = turn(p2score, l, s)
                    xY, yY = player(p2score)
                    if not six:
                        t += 1
                        if b < 3 or b == 21:
                            t = 1
                    if p2score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            notification_text("Computer Wins", 991, 214, 50, black)
                            pygame.mixer.Sound.play(loser)
                            pygame.display.update()
                        break
        if 5 > b > 1:
            if player_button("Player 1", mouse[0], mouse[1], 834, 297, 200, 50, red, grey, 30):
                if t == 1:
                    p1score, l, s, six = turn(p1score, l, s)
                    xR, yR = player(p1score)
                    if not six:
                        t += 1
                    if p1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            notification_text("Player 1 Wins", 991, 214, 50, black)
                            pygame.mixer.Sound.play(winner)
                            pygame.display.update()
                        break
            if player_button("Player 2", mouse[0], mouse[1], 1064, 297, 200, 50, yellow, grey, 30):
                if t == 2:
                    p2score, l, s, six = turn(p2score, l, s)
                    xY, yY = player(p2score)
                    if not six:
                        t += 1
                        if b < 3:
                            t = 1
                    if p2score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            notification_text("Player 2 Wins", 991, 214, 50, black)
                            pygame.mixer.Sound.play(winner)
                            pygame.display.update()
                        break
        if 5 > b > 2:
            if player_button("Player 3", mouse[0], mouse[1], 834, 382, 200, 50, green, grey, 30):
                if t == 3:
                    p3score, l, s, six = turn(p3score, l, s)
                    xG, yG = player(p3score)
                    if not six:
                        t += 1
                        if b < 4:
                            t = 1
                    if p3score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            notification_text("Player 3 Wins", 991, 214, 50, black)
                            pygame.mixer.Sound.play(winner)
                            pygame.display.update()
                        break
        if 5 > b > 3:
            if player_button("Player 4", mouse[0], mouse[1], 1064, 382, 200, 50, blue, grey, 30):
                if t == 4:
                    p4score, l, s, six = turn(p4score, l, s)
                    xB, yB = player(p4score)
                    if not six:
                        t += 1
                        if b < 5:
                            t = 1
                    if p4score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            notification_text("Player 4 Wins", 991, 214, 50, black)
                            pygame.mixer.Sound.play(winner)
                            pygame.display.update()
                        break
        button6 = button("Back", mouse[0], mouse[1], 1080, 670, 200, 50, red, pink, 30, 7)
        displaySettings.blit(redPlayer, (xR, yR))
        if 5 > b > 1 or b == 21:
            displaySettings.blit(yellowPlayer, (xY + 2, yY))
        if 5 > b > 2:
            displaySettings.blit(greenPlayer, (xG + 4, yG))
        if 5 > b > 3:
            displaySettings.blit(bluePlayer, (xB + 6, yB))
        if l:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time < 2000:
                notification_text("There's a Ladder!", 991, 214, 35, black)
                pygame.display.update()
        if s:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time < 2000:
                notification_text("There's a Snake!", 991, 214, 35, black)
                pygame.display.update()
        timer.tick(7)
        pygame.display.update()


gameOpening()
mainPage()
