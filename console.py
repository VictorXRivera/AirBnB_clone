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

    def default(self, line):
        """the all printer"""
        l = line.split(".")
        if len(l) != 2:
            super().default(line)
            return
        if l[0] not in HBNBCommand.classes:
            super().default(line)
            return
        if l[1] == "all()":
            ret = []
            printed = 0
            print("[", end="")
            for key in storage.all().keys():
                # if key[0:len(l[0])] == l[0]:
                if isinstance(storage.all()[key], HBNBCommand.classes[l[0]]):
                    if printed == 1:
                        print(", ", end="")
                    ret.append(str(storage.all()[key]))
                    print(storage.all()[key], end="")
                    printed = 1
            print("]")
            return
        if l[1] == "count()":
            ret = 0
            for key in storage.all().keys():
                # if key[0:len(l[0])] == l[0]:
                if isinstance(storage.all()[key], HBNBCommand.classes[l[0]]):
                    ret += 1
            print(ret)
            return
        if l[1][0:4] == "show":
            if len(l[1][4:]) < 3:
                print("** instance id missing **")
                return
            id = l[1][5:-1]
            key = l[0] + "." + id
            if key in storage.all().keys():
                print(storage.all()[key])
                return
            else:
                print("** no instance found **")
                return
        if l[1][0:7] == "destroy":
            if len(l[1][7:]) < 3:
                print("** instance id missing **")
                return
            id = l[1][8:-1]
            key = l[0] + "." + id
            if key in storage.all().keys():
                storage.all().pop(key)
                return
            else:
                print("** no instance found **")
                return
        if l[1][0:6] == "update":
            if '{' in l[1]:
                args = HBNBCommand.split_with_dict(l[1][7:-1])

                if len(args) < 1:
                    print("** instance id missing **")
                    return
                key = l[0] + "." + args[0]
                if key not in storage.all().keys():
                    print("** no instance found **")
                    return
                if len(args) < 2:
                    print("** attribute name missing **")
                    return
                dict_string = ""
                for char in args[1]:
                    if char == "'":
                        dict_string += '"'
                    else:
                        dict_string += char
                attr_dict = json.loads(dict_string)
                print(attr_dict)
                for attr_key, value in attr_dict.items():
                    if attr_key in storage.all()[key].to_dict().keys():
                        setattr(storage.all()[key], attr_key,
                                type(getattr(storage.all()[key],
                                     attr_key))(value))
                    else:
                        setattr(storage.all()[key], attr_key, str(value))
                    storage.all()[key].save()
                return
            else:
                args = l[1][7:-1].split(", ")
                for index in range(0, len(args)):
                    if args[index][0] == '"' and args[index][-1] == '"':
                        args[index] = args[index][1:-1]

                if len(args[0]) == 0:
                    print("** instance id missing **")
                    return
                key = l[0] + "." + args[0]
                if key not in storage.all().keys():
                    print("** no instance found **")
                    return
                if len(args) < 2:
                    print("** attribute name missing **")
                    return
                if len(args) < 3:
                    print("** value missing **")
                    return
                if args[1] in storage.all()[key].to_dict().keys():
                    setattr(storage.all()[key], args[1],
                            type(getattr(storage.all()[key],
                                 args[1]))(args[2]))
                else:
                    setattr(storage.all()[key], args[1], args[2])
                storage.all()[key].save()
                return

        super().default(line)

    def split_with_dict(line):
        """ Breaks a line into arguments using ', ' as a separator
            while keeping a dictionary in one piece
        """
        args = []
        index = 0
        while index < len(line):
            token = ""
            if line[index] == '"':
                while index < len(line):
                    token += line[index]
                    index += 1
                    if line[index] == '"':
                        token += line[index]
                        index += 1
                        args.append(token)
                        break
            elif line[index] == '{':
                while index < len(line):
                    token += line[index]
                    index += 1
                    if line[index] == '}':
                        token += line[index]
                        index += 1
                        args.append(token)
                        break
            elif line[index] == ' ' or line[index] == ',':
                index += 1
            else:
                while index < len(line):
                    token += line[index]
                    index += 1
                    if line[index] == ' ' or line[index] == ',':
                        index += 1
                        args.append(token)
                        break

        for index in range(0, len(args)):
                    if args[index][0] == '"' and args[index][-1] == '"':
                        args[index] = args[index][1:-1]
        return args

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
