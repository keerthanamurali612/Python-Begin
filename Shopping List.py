shop_list=[]
while True:
    print("Shopping List")
    print("1.Add item")
    print("2.Remove item")
    print("3.View item")
    print("4.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        item=input("Enter the name of item:")
        shop_list.append(item)
    elif choice==2:
        item=input("Enter the name or no of  item to remove:")
        if item.isnumeric() and int(item) <= len(shop_list):
            shop_list.pop(int(item) - 1)
        elif item in shop_list:
            shop_list.remove(item)
        else:
            print("Item not found on the list.")
    elif choice==3:
        print(shop_list)
    elif choice==4:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
