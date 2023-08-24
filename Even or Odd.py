def even_odd (*args):
    if args[-1] == "even":
        args = list(filter(lambda x: x%2==0, args[0:len(args)-1]))

    elif args[-1] == "odd":
        args = list(filter(lambda x: x%2!=0, args[0:len(args)-1]))

    return args




print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))