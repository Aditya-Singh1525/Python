print('If don\'t know the number give 0.')

def STDfinder():
    try:
        a = float(input('Enter the distance in km:'))
        b = float(input('Enter the time in h:'))
        c = float(input('Enter the speed in km/h:'))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    s = 's'
    t = 't'
    d = 'd'

    print('What to find?\n')
    
    y = input('If distance:d,time:t,speed:s:').lower().strip()

    if y == s:
        if b == 0:
            print("Error: Time cannot be zero when calculating speed.")
        else:
            print(a/b,'km/h is your speed.')
    elif y == t:
        if c == 0:
            print("Error: Speed cannot be zero when calculating time.")
        else:
            print(a/c,'h is your time.')
    elif y == d:
        print(b*c,'km is your distance.')
    else:
        print("Invalid choice.")

print('If don\'t known value give it "0"\n')

if __name__ == '__main__':
    STDfinder()

