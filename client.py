import socket
import curses

from consts import PI_IP_ADDRESS, SERVER_PORT

messages = {
    # http://sticksandstones.kstrom.com/appen.html
    119: 'f', # w
    115: 'b', # s
    97:  'l', # a
    100: 'r', # d
    120: 's'  # x 
}

if __name__=="__main__":
    s = socket.socket()
    s.connect((PI_IP_ADDRESS, SERVER_PORT))

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    try:
        while True:
            c = screen.getch()
            message = messages.get(c)
            if message is not None:
                s.send(message.encode())
            
    finally:
        s.close()
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()