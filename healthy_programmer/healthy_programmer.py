import datetime
import pygame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

while True:
    try:
        print('Please Enter the beginning time (only numbers) of your job accordingly;')
        h = int(input('Hour:- '))
        m = int(input('Minute:- '))
        s = int(input('Second:- '))
        print('')
        print('Please Enter the ending time (only numbers) of your job accordingly;')
        h1 = int(input('Hour:- '))
        m1 = int(input('Minute:- '))
        s1 = int(input('Second:- '))
        break
    except:
        print('Wrong Input! Try again.\n')

now = datetime.datetime.now()
time_1 = now.replace(hour=h, minute=m, second=s, microsecond=0)
# time_2 = now.replace(hour=h1, minute=m1, second=s1, microsecond=0)
time_2 = now.replace(hour=h1, minute=m1, second=s1, microsecond=0)
time_3 = datetime.timedelta(minutes=45)
end = time_2 - time_3

if now < end:
    print("\nThat's it! Now you can start or continue your work\n"
          "We will remind you on time, so that you won't forget to\n"
          "take care of your health.\n"
          "------------------------------------------------------------")

    a = "water_time.mp3"
    b = "eye_exercise.mp3"
    c = "stretching_exercise.mp3"


    def drink_water():
        pygame.mixer.init()
        pygame.display.set_mode((80, 50))
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        clock.tick(10)
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)


    def eye_exe():
        pygame.mixer.init()
        pygame.display.set_mode((80, 50))
        pygame.mixer.music.load(b)
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        clock.tick(10)
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)


    def stretching_exercise():
        pygame.mixer.init()
        pygame.display.set_mode((80, 50))
        pygame.mixer.music.load(c)
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        clock.tick(10)
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)


    log_date = datetime.date.today()
    with open('water.txt', 'a') as water:
        water.write(f'Date {log_date} water log:-\n')
        water.close()
    with open('eyeExe.txt', 'a') as eye:
        eye.write(f'Date {log_date} eye exercise log:-\n')
        eye.close()
    with open('stretching_exercise.txt', 'a') as exe:
        exe.write(f'Date {log_date} stretching exercise log:-\n')
        exe.close()

    while time_1 < now < end:
        pygame.time.delay(900000)
        for i in range(2):
            drink_water()
        log = input("To log your water time, just hit the 'Enter' button::")
        if log == "":
            log = 'Drank Water'
            cur_time = datetime.datetime.now()
            log_time = cur_time.strftime('%H:%M:%S')
            with open('water.txt', 'a') as water:
                water.write('[' + str(log_time) + '] ' + log + '\n')
        pygame.time.delay(900000)
        for i in range(2):
            eye_exe()
        log = input("To log your eye exercise time, just hit the 'Enter' button::")
        if log == "":
            log = 'Eye Exercise Done'
            cur_time = datetime.datetime.now()
            log_time = cur_time.strftime('%H:%M:%S')
            with open('eyeExe.txt', 'a') as water:
                water.write('[' + str(log_time) + '] ' + log + '\n')
        pygame.time.delay(900000)
        for i in range(2):
            stretching_exercise()
        log = input("To log your stretching exercise time, just hit the 'Enter' button::")
        if log == "":
            log = 'Stretching Exercise Done'
            cur_time = datetime.datetime.now()
            log_time = cur_time.strftime('%H:%M:%S')
            with open('stretching_exercise.txt', 'a') as water:
                water.write('[' + str(log_time) + '] ' + log + '\n')
else:
    print("\nWrong Input! You should start this software\n"
          "at-least 1 hour prior to your job ending time.")
