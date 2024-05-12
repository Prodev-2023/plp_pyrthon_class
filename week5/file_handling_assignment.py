try:
    with open('my_file.txt', 'w') as note:
        my_note = note.write(" what a world \n what a day \n what a life")

except FileExistsError as e:
    print(e)

    with open('my_file.txt', 'a') as read_note:
        my_note = read_note.write(' \n The deep thoughts of a man')
except PermissionError as e:
    print(e)

else:

    with open('my_file.txt', 'r') as read_note:
        my_note = read_note.read()
        print(my_note)
finally:
    print('code successfully ran ...')

