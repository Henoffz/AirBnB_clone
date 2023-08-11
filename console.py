#!/usr/bin/python3
"""
This is the command line interpreter for 
managing the Airbnb files
"""
import cmd
import cmd
from models import storage, allclasses
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command line interpreter.
    """
    prompt = '(hbnb)'
    classes = allclasses
    
    def do_quit(self, args):
        """
        method that exit interpreter on entering 'quit'
        """
        return True

    def do_EOF(self, args):
        """
        method that exit the interpreter using EOF(CTRL + D)
        """
        print()
        return True

    def do_help(self, arg):
        """
        provide help details for each available command
        """
        super().do_help(arg)

    def emptyline(self):
        """
        returns the prompt because
        only 'Enter key' was pressed
        without typing nothing
        """
        return

    def do_create(self, arg):
        """
        Create instances based on command argument from user.
        """
        if len(arg) == 0:
            print('** class name missing **')
        elif arg[0] in self.classes:
            new_instance = eval(arg[0])()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        
        objects = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arg) > 1:
            id = arg[0] + "." + arg[1]
            if id in objects:
                instance = objects[id]
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        and save the change into the JSON file
        """
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arg) > 1:
            id = arg[0] + "." + arg[1]
            if id in objects:
                instance = objects[id]
                del instance
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        prints all instances of the Base class.
        """
        objects = storage.all
        obj_list = []
        if len(args) == 0:
            for obj_key in objects:
                obj_list.append(objects[obj_key])
            print(obj_list)
        elif arg[0] in self.classes:
            if obj_key[:len(args[0])] == args[0]:
                obj_list.append(objects[obj_key])
                print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """
        objects = storage.all()
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1 and tokens[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tokens) == 1 and tokens[0] in self.classes:
            print("** instance id missing **")
        elif len(tokens) == 2:
            instance_key = tokens[0] + "." + tokens[1]
            if instance_key not in objects:
                print("** no instance found **")
            else:
                instance = objects[instance_key]
                immutable_attrs = ["id", "created_at", "updated_at"]
                if len(tokens) >= 3:
                    if len(tokens) == 3:
                        print("** attribute name missing **")
                    elif len(tokens) == 4:
                        print("** value missing **")
                    elif tokens[2] not in immutable_attrs:
                        instance.__dict__[tokens[2]] = tokens[3]
                        instance.updated_at = datetime.now()
                        storage.save()






if __name__ == '__main__':
    HBNBCommand().cmdloop()
