import time
import os


def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')


def move_snake(wait_time, phase, space_before, space_after):
    clear_screen()
    if phase == 1:
        print(space_before, end='')
        print(r"____/\____/\____:)", end='')
        print(space_after, end='')
        print(r"<>--^--<>")
        time.sleep(wait_time)
    if phase == 2:
        print(space_before, end='')
        print(r"_____/\____/\___:)", end='')
        print(space_after, end='')
        print(r"<>--^--<>")
        time.sleep(wait_time)
    if phase == 3:
        print(space_before, end='')
        print(r"_____/\____/\___:o >--^--<>")


def main(STEP):
    PHASE_1, PHASE_2, PHASE_3 = 1, 2, 3
    moving = range(STEP)
    snake_step = practice_yield(STEP)
    for i in moving:
        space_before, space_after = next(snake_step)
        move_snake(0.3, PHASE_1, space_before, space_after)
        if moving.stop != STEP:
            move_snake(0.5, PHASE_2, space_before, space_after)
        else:
            move_snake(0, PHASE_3, space_before, space_after)


def practice_yield(STEP):
    space_before = "   "
    space_after = " " * STEP
    while space_after != "":
        space_before += " "
        space_after = space_after[:-1]
        yield space_before, space_after


if __name__ == "__main__":
    main(8)
