#!/usr/bin/python3
""" Custom hbnb console """
from models.user import User
import cmd
import inspect
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
import shlex
from models.engine.file_storage import FileStorage
import json


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """

    classes = {'BaseModel': BaseModel, 'User': User,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Place': Place,
               'Review': Review}
    prompt = '(hbnb) '

    def do_quit(self, inp):
        """ Quit command """
        return True

    def do_EOF(self, inp):
        """ Actual exiting """
        return True

    def do_create(self, inp):
        """ Create command that creates new instance
        of BaseModel, save to JSON and print id
        """
        i = inp.split()
        args = len(i)
        if args < 1:
            print("** class name missing **")
            return

        if i[0] in HBNBCommand.classes:
            obj = HBNBCommand.classes[i[0]]()
            print(obj.id)
            storage.new(obj)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, inp):
        """ Show Prints the string representation of an instance
        based on the class name and id
        """
        instance = HBNBCommands.classes
        i = inp.split()
        args = len(i)
        if args < 1:
            print("** class name missing **")
            return

        if i[0] not in instance:
            print("** class doesn't exist **")
            return

        if args < 2:
            print("** instance id missing **")
            return

        dict_key = i[0] + "." + i[1]
        if dict_key in storage.all().keys():
            print(storage.all()[dict_key])
            return
        else:
            print("** no instance found **")

    def do_destroy(self, inp):
        """ Destroy Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        instance = HBNBCommand.classes
        i = inp.split()
        args = len(i)
        if args < 1:
            print("** class name missing **")
            return

        if i[0] not in instance:
            print("** class doesn't exist **")
            return

        if args < 2:
            print("** instance id missing **")
            return
        dict_key = i[0] + "." + i[1]
        if dict_key in storage.all().keys():
            storage.all().pop(dict_key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, inp):
        """ Prints all string representation of all
        instances based or not on the class name.
        """
        i = inp.split()
        new_list = []
        args = len(i)

        if args < 1:
            for obj in storage.all().values():
                new_list.append(str(obj))
            print(new_list)
        else:
            instance = HBNBCommand.classes
            if i[0] not in instance:
                print("** class doesn't exist **")
                return
            for dict_key in storage.all().keys():
                if dict_key[0:args[0]] == i[0]:
                    new_list.append(str(storage.all()[dict_key]))
            print(new_list)

    def do_update(self, inp):
        """updates an attribute of the object, us in form of
        update <class> <id> <attribute name> <new value>
        """
        i = shlex.split(inp)
        args = len(i)
        instance = HBNBCommand.classes
        if args < 1:
            print("** class name missing **")
            return
        if i[0] not in instance:
            print("** class doesn't exist **")
            return
        if args < 2:
            print("** instance id missing **")
            return
        key = l[0] + "." + l[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if args < 3:
            print("** attribute name missing **")
            return
        if args < 4:
            print("** value missing **")
            return

        if i[2] in storage.all()[key].to_dict().keys():
            setattr(storage.all()[key], i[2],
                    type(getattr(storage.all()[key], i[2]))(i[3]))
        else:
            setattr(storage.all()[key], i[2], i[3])
        storage.all()[key].save()

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
        print('Creates a new instance of BaseModel,\
        saves it (to the JSON file) and prints the id\n')

    def help_show(self):
        """ Desc. on show """
        print('Prints the string representation \
        of an instance based on the class name and id\n')

    def help_destroy(self):
        """ Desc. on destroy """
        print('Deletes an instance based on the \
        class name and id (save the change into the JSON file\n')

    def help_all(self):
        """ Desc. on all """
        print('Prints all string representation \
        of all instances based or not on the class name.\n')

    def help_update(self):
        """ Desc. on update """
        print('Updates an instance based \
        on the class name and id by adding or \
        updating attribute (save the change into the JSON file)\n')

    def default(self, inp):
        """ Commands """
        if inp == 'quit':
            return self.do_quit(inp)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
