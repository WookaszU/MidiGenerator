import os


def is_valid_directory(parser, arg):
    if not os.path.isdir(arg):
        parser.error('The directory {} does not exist!'.format(arg))
    else:
        return arg

def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        if not arg.endswith('.mid'):
            parser.error('The file type must be .mid!'.format(arg))
        parser.error('The file {} does not exist!'.format(arg))
    else:
        return arg

def is_valid_number(parser, arg):
    try:
        arg = int(arg)
    except ValueError:
        parser.error('Numerical arguments must be integers bigger than 0 ! You have inserted {} !'.format(arg))
    if arg <= 0:
        parser.error('Numerical arguments must be integers bigger than 0 ! You have inserted {} !'.format(arg))
    else:
        return arg