# _*_ coding:utf-8 _*_
# Author:liu

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0, 0, 100))

    # draw circle
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)

    # draw the clock number 1-12
    for n in range(1, 13):
        angle = math.radians(n * (360 / 12) - 90)
        x = math.cos(angle) * (radius - 20) - 10
        y = math.sin(angle) * (radius - 20) - 10
        print_text(font, pos_x + x, pos_y + y, str(n))

    # get the time of day
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    # draw the hours hand
    hour_angle = wrap_angle(hours * (360 / 12) - 90)
    hour_angle = math.radians(hour_angle)
    hour_x = math.cos(hour_angle) * (radius - 80)
    hour_y = math.sin(hour_angle) * (radius - 80)
    target = (pos_x + hour_x, pos_y + hour_y)
    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 12)

    # draw the minutes hand
    min_angle = wrap_angle(minutes * (360 / 60) - 90)
    min_angle = math.radians(min_angle)
    min_x = math.cos(min_angle) * (radius - 60)
    min_y = math.sin(min_angle) * (radius - 60)
    target = (pos_x + min_x, pos_y + min_y)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 12)

    # draw the seconds hand
    sec_angle = wrap_angle(seconds * (360 / 60) - 90)
    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius - 40)
    sec_y = math.sin(sec_angle) * (radius - 40)
    target = (pos_x + sec_x, pos_y + sec_y)
    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 12)

    # draw the center
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20)

    print_text(font, 0, 0, str(hours) + ":" + str(minutes) + ":" + str(seconds))
    pygame.display.update()
