def fill_the_box(height, length, width, *args):
    free_volume = height*length*width
    i=0
    while args[i] != "Finish":
        if free_volume >= args[i]:
            free_volume-=args[i]
            i+=1
        else:

            return f"No more free space! You have {sum(args[i+1:len(args)-1])+args[i]-free_volume} more cubes."
    return f"There is free space in the box. You could put {free_volume} more cubes."

print(fill_the_box(2, 8,2, 2, 1, 7, 3, 1, 5,"Finish"))