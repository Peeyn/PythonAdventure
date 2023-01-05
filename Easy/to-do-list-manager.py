# A to-do list manager:
# Write a program that allows the user to add, remove, and view items on a to-do list.
# You can use a list data structure to store the items and provide options for the user to add, remove, and view the items on the list.

mylist = ["shopping","cooking", "workout"]

while(True):

        print("1. Show to-do list\n2. Add item to the list\n3. Remove item from the list\n4. Exit program")

        try:
            x = int(input("Choose option: "))

        except ValueError:
            print("\nValueError: An integer must be provided!\n")

        else:

            if(x==1):
                    print("\nShow to-do list.\n")
                    print(mylist,"\n\n")

            elif(x==2):
                print("\nAdd item to the list.\n")
                mylist.append(input("Write the task to add:"))

            elif(x==3):
                while(True):
                    print("\nHow to remove an item from the list?\n1. By name\n2. By index\n\n")

                    try:
                        y = int(input("Choose option: "))

                    except ValueError:
                        print("\nValueError: An integer must be provided!\n")

                    else:
                        if(y==1):
                            print("\nRemoving item by its name.\n")
                            try:
                                tmp = input("\nWrite name of the task you want to remove: ")
                                mylist.remove(tmp)

                            except TypeError:
                                print("\nstringi\n")
                            except ValueError:
                                print("\nTask:",tmp,"is not in the list!\n")
                            else:
                                print("\nTo-do list after removing the task:\n",mylist,"\n\n")
                                break
                            

                        elif(y==2):
                            print("\nRemoving item by its index.")
                            try:
                                tmp = int(input("Write index of the task you want to remove: "))
                                mylist.pop(tmp)

                            except IndexError:
                                print("\nIndexError: pprovided index is out of range of the list!\n")

                            except TypeError:
                                print("\nTypeError: An integer must be provided!\n")
                                
                            except ValueError:
                                print("\n Index",tmp,"is not in the list!\n")

                            else:
                                print("\nTo-do list after removing the task:\n",mylist,"\n\n")
                                break

                        else:
                            print("\nAn integer between 1-2 must be provided!\n")

                        
            elif(x==4):
                print("\nFinishing program.\n")       
                break        

            else:
               print("An integer between 1-4 must be provided!")
