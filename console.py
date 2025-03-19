#!/usr/bin/python3
""" Console module for interacting with PillPocket"""
import cmd
import sys
import models
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.medication import Medication
from models.order import Order


class PILLPOCKETCommand(cmd.Cmd):
    """ PillPocket command interpreter."""
    prompt = "(PillPocket) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Medication": Medication,
        "Order": Order
    }
    types = {
            "string": str,
            "integer": int,
            "float": float
            }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """ Empty line + ENTER shouldn't execute anything."""
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in PILLPOCKETCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = PILLPOCKETCommand.classes[args[0]]()
        for parameter in args[1:]:
            if "=" not in parameter:
                continue
            key, value = parameter.split("=", 1)
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace("_", " ").replace('\\"', '"')
            else:
                try:
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                except ValueError:
                    continue
            if key in PILLPOCKETCommand.types:
                try:
                    value = PILLPOCKETCommand.types[key](value)
                except ValueError:
                    continue
            setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        "Print all string representation of all instances"
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([
                str(obj) for obj in objects.values()
                if type(obj).__name__ == args[0]
                ])
        # print([
        #    str(obj) for obj, key in storage.all().items()
            #   if obj.__class__.__name__ == args[0]
    # ])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            obj = storage.all()[f"{args[0]}.{args[1]}"]
            setattr(obj, args[2], args[3])
            obj.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if type(obj).__name__ == args[0]:
                    count += 1
            print(count)


if __name__ == '__main__':
    PILLPOCKETCommand().cmdloop()
