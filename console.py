"""console modules"""
import cmd

class HBNBCommand(cmd.Cmd):
    """functionality of the HBNB console"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Exit the program."""
        return True

    def do_EOF(self, args):
        """Exit the program."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
