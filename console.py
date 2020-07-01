#!/usr/bin/python3
""" Custom hbnb console """
import cmd, sys

class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
    prompt = '(hbnb) '

    def do_quit(self, inp):
        """ Quit command"""
        return True

    def help_quit(self):
        """ Description of cmd """
        print('Quit command to exit the program')
    
    def default(self, inp):
        """ Quit function """
        if inp == 'quit':
            return self.do_quit(inp)

    do_EOF = do_quit
    help_EOF = help_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
