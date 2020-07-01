#!/usr/bin/python3
""" Custom hbnb console """
import cmd

class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
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

    def help_create(self):
        """ Description on create """
        print('Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id\n')

    def help_show(self):
        """ Desc. on show """
        print('Prints the string representation of an instance based on the class name and id\n')

    def help_destroy(self):
        """ Desc. on destroy """
        print('Deletes an instance based on the class name and id (save the change into the JSON file\n')

    def help_all(self):
        """ Desc. on all """
        print('Prints all string representation of all instances based or not on the class name.\n')

    def help_update(self):
        """ Desc. on update """
        print('Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)\n')
    
    def default(self, inp):
        """ Quit function """
        if inp == 'quit':
            return self.do_quit(inp)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
