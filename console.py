#!/usr/bin/python3
"""Module with the entry point of the command interpreter."""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Defines the entry point of the command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def help_quit(self, arg):
        """Help information for the quit command."""
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        to the JSON file and prints the id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)
    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if '.' in args[0]:
            args[0], args[1] = args[0].split('.')
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()
    def do_all(self,arg):
        """Prints all string representation of all instances."""
        args = shlex.split(arg)
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(obj) for obj in storage.all().values()
                   if type(obj) == storage.classes[args[0]]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        arg_list = shlex.split(arg)
        if not arg_list:
            print("** class name missing **")
            return
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        obj_id = arg_list[1]

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        attribute_name = arg_list[2]

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attribute_value = " ".join(arg_list[3:])


        key = class_name + "." + obj_id
        obj = storage.all().get(key)

        if not obj:
            print("** no instance found **")
        else:
            setattr(obj, attribute_name, attribute_value)
            obj.save()
    @staticmethod
    def do_count(class_name):
        """Count the number of instances of a class."""
        instance_count = sum(1 for instance in storage.all().values()
                             if instance.__class__.__name__ == class_name)
        return instance_count
    def default(self, line):
        """Overwrite the default method to handle more cases."""
        # split the command with 1st instance of "." [User, all()]
        class_list = line.split(".", 1)
        if len(class_list) < 2:
            print("Unknown syntax: {}".format(line))
            return False
        # split the second command in class_list [all, )]
        command = class_list[1].split("(", 1)
        if len(command) < 2:
            print("Unknown syntax: {}".format(line))
            return False
        # split the second command in command list with of "("
        class_id = command[1].split(")", 1)

        # handle the update method
        class_name = class_list[0]
        method = command[0]
        args = command[1][:-1]
        args_list = [arg.strip('\'" ') for arg in args.split(",")]

        if class_name not in self.classes and method not in self.cmd_list:
            print("Unknown syntax:{}".format(line))
            return False
        if method in self.no_id_list and not command[1].startswith(")"):
            print("Unknown syntax:{}".format(line))
            return False
        if method in self.id_list and not command[1].endswith(")"):
            print("Unknown syntax: {}".format(line))
            return False

        elif method == self.cmd_list[0]:  # all
            self.do_all(class_list[0])

        elif method == self.cmd_list[2]:  # count
            print(self.class_count(class_list[0]))

        elif method == self.cmd_list[4]:  # show
            self.do_show(class_list[0] + " " + class_id[0])

        elif method == self.cmd_list[3]:  # destroy
            self.do_destroy(class_list[0] + " " + class_id[0])

        elif method == self.cmd_list[5]:
            self.handle_update(class_name, args_list)
            self.do_update(class_name + " " + " ".join(args_list))
        else:
            print("Unknown syntax: {}".format(line))

if __name__=="__main__":
    HBNBCommand().cmdloop()
