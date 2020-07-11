#!/usr/bin/python3
""" Custom hbnb console """
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import re

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

    def do_help(self, args):
        """ Doc to display all commands """
        cmd.Cmd.do_help(self, args)

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
    def do_destroy(self, args):
        """
        Deletes an instance of the class name and id
        saves the changes inside JSON file
        """
        tokens = args.split()
        stored_keys = storage.all()
        if tokens:
            if tokens[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            if len(tokens) < 1:
                print("** class name missing **")
                return
            key = tokens[0] + "." + tokens[1]
            if key in stored_keys.keys():
                stored_keys.pop(key)
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class name missing **")
            return

    def do_create(self, args):
        """
        Creates a new instance of BaseModel and saves it inside JSON flie
        """
        tokens = args.split()
        if len(tokens) < 1:
            print("** class name missing **")
            return
        if tokens[0] in HBNBCommand.all_classes:
            new_model = HBNBCommand.all_classes[tokens[0]]()
            storage.new(new_model)
            storage.save()
            print(new_model.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        """
        token = args.split()
        all_instances = []
        if len(token) < 1:
            for x in storage.all().values():
                all_instances.append(str(x))
            print(all_instances)
        else:
            classes = HBNBCommand.all_classes
            if token[0] not in classes:
                print("** class doesn't exist **")
                return
            for x in storage.all().keys():
                if x[0:len(token[0])] == token[0]:
                    all_instances.append(str(storage.all()[x]))
            print(all_instances)

    def do_count(self, args):
        """ Counts number of instances of a class """
        count_help = 0
        class_list = args.split()
        if class_list[0] not in self.all_classes:
            print("** class doesn't exist **")
        obj = storage.all()
        for key in obj:
            key_help = key.split('.')
            if key_help[0] == class_list[0]:
                count_help += 1
        print(count_help)

    def do_update(self, args):
        """ Update an instance based on the class name and id by adding
        or updating object """
        tokens = shlex.split(args)
        class_list = args.split()
        if class_list:
            if class_list[0] not in self.all_classes:
                print("** class doesn't exist **")
                return
            if len(class_list) < 2:
                print("** instance id missing **")
            obj = storage.all()
            if len(class_list) == 2:
                print("** attribute name missing **")
                return
            if len(class_list) == 3:
                print("** value missing **")
                return
            if len(class_list) > 2:
                key = class_list[0] + '.' + class_list[1]
                if key not in obj:
                    print("** no instance found **")
                if key in obj:
                    if len(class_list) < 3:
                        print("** attribute name missing **")
                    if len(class_list) < 4:
                        print("** value missing **")
                    if tokens[2]\
                            in storage.all()[key].to_dict().keys():
                        setattr(storage.all()[key], tokens[2],
                                type(getattr(storage.all()
                                             [key], tokens[2]))(tokens[3]))
                    else:
                        setattr(storage.all()[key], tokens[2], tokens[3])
                    storage.all()[key].save()
        else:
            print("** class name missing **")

    def do_show(self, args):
        """ show string representation of an instance"""
        tokens = args.split()
        stored_keys = storage.all()
        if len(tokens) < 1:
            print("** class name missing **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        if tokens[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(tokens) >= 2:
            key = tokens[0] + "." + tokens[1]
            if key in stored_keys:
                show_output = stored_keys[key]
            try:
                print(show_output)
            except UnboundLocalError:
                pass
            if key not in stored_keys:
                print("** no instance found **")
        else:
            return

    def default(self, args):
        """
        default method to use with command()
        """
        spaces = (args.replace('.', ' ').replace('(', ' ')
                  .replace(')', ' ').replace('"', ''))
        print(spaces)
        tokens = spaces.split()
        second = tokens[0]
        first = tokens[1]
        tokens[0] = first
        tokens[1] = second
        if len(tokens) > 4:
            new_args = tokens[1] + ' ' + tokens[2]
            + ' ' + tokens[3] + ' ' + tokens[4]
            if tokens[0] == 'update':
                self.do_update(new_args)
        if len(tokens) > 2:
            new_args = tokens[1] + ' ' + tokens[2]
            if tokens[0] == 'all':
                self.do_all(new_args)
            elif tokens[0] == 'destroy':
                self.do_destroy(new_args)
            if tokens[0] == 'create':
                self.do_create(new_args)
            if tokens[0] == 'show':
                self.do_show(new_args)
            if tokens[0] == 'update':
                self.do_update(new_args)
        else:
            new_args = tokens[1]
            if tokens[0] == 'all':
                self.do_all(new_args)
            elif tokens[0] == 'destroy':
                self.do_destroy(new_args)
            if tokens[0] == 'create':
                self.do_create(new_args)
            if tokens[0] == 'show':
                self.do_show(new_args)
            if tokens[0] == 'update':
                self.do_update(new_args)
            if tokens[0] == 'count':
                self.do_count(new_args)
            if tokens[0] == 'quit':
                self.do_quit(inp)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
