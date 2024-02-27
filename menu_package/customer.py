def menu_board(name,price):
    print("----------------------")
    for i in range(len(name)):
        print(f"{i}.{name[i]}:{price[i]}")
    print("----------------------")
def order_update(last,new,amount):
    cnt=0
    index=-1
    key_list = list(last.keys())
    value_list=list(last.values())
   
    for i in range(len(last)):
        if new!=key_list[i]:
            cnt+=1    
    if cnt <len(last):
        last[new] = value_list[index]+1
    elif cnt ==len(last):
        last[new] = 1

    return last
def pay(order,name,price):
    amount=0
    key_list = list(order.keys())
    value_list=list(order.values())
    print("----------------------------")
    for i in range(len(name)):
        for j in range(len(key_list)):
            if name[i] == key_list[j]:
                print(f"{key_list[j]}x{int(value_list[j])}:{int(price[i])}/{int(value_list[j])*int(price[i])}")
                amount = amount+(int(value_list[j])*int(price[i]))
    print("----------------------------")    
    return amount
def bill_paper(order,name,price):
    key_list = list(order.keys())
    value_list=list(order.values())

    