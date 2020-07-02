#!/usr/bin/python3
""" Custom hbnb console """
from models.user import User
import cmd

class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
    classes = {'BaseModel' : BaseModel, 'User' : User,
               'State' : State
               'City' : City
               'Amenity' : Amenity
               'Place': Place
               'Review' : Review}
    prompt = '(hbnb) '

    def do_quit(self, inp):
        """ Quit command """
        return True

    def do_EOF(self, inp):
        """ Actual exiting """
        return True

    def emptyline(self):
        """ Empty line edgecase? """
        pass

    def help_quit(self):
        """ Description of cmd """
        print('Quit command to exit the program\n')
    
    def default(self, inp):
        """ Quit function """
        if inp == 'quit':
            return self.do_quit(inp)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
