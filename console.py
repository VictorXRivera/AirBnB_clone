#!/usr/bin/python3
from cmd import Cmd

class HBNBCommand(Cmd):
    prompt = '(hbnb) '

    def do_quit(self, inp):
        return True

    def help_quit(self):
        print('Quit command to exit the program')
    
    def default(self, inp):
        if inp == 'quit':
            return self.do_quit(inp)

    do_EOF = do_quit
    help_EOF = help_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
