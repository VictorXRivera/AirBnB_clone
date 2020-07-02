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
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_quit(self, inp):
        """ Quit command """
        return True

    def do_EOF(self, inp):
        """ Actual exiting """
        return True
    
    def emptyline(self):
        """ Empty line edgecase? """
        pass

    def preloop(self):
        """ Setup for json serialization and search by uid for deletion
        """
        return

    def postloop(self):
        """ Closes program and saves to JSON storage
        """
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
        """ Commandsn """
        if inp == 'quit':
            return self.do_quit(inp)
        if inp == 'create':
            return self.do_create
        if new_instance == 'show':
            return self.do_show

if __name__ == '__main__':
    HBNBCommand().cmdloop()
