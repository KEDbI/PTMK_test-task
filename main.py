import sys
import script

if int(sys.argv[1]) == 1:
    script.task_1()

elif int(sys.argv[1]) == 2:
    if len(sys.argv) > 5:
        print('Too many arguments.')
    if len(sys.argv) < 5:
        print('Not enough arguments.')
    else:
        script.task_2(full_name=sys.argv[2], birthdate=sys.argv[3], sex=sys.argv[4])

elif int(sys.argv[1]) == 3:
    script.task_3()

elif int(sys.argv[1]) == 4:
    script.task_4()

elif int(sys.argv[1]) == 5:
    script.task_5()

elif int(sys.argv[1]) == 6:
    script.task_6()