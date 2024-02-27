from menu_package.__init__ import read_data,add_data
from menu_package.customer import menu_board,order_update,pay
#자료들의 리스트화
name = read_data("./menu_package/name.txt")
print("name:",name)
quantity = read_data("./menu_package/quantity.txt")
print("quantity:",quantity)
price = read_data("./menu_package/price.txt")
cnt=0
n_order={"메뉴":"수량"}
#--------------------------------------------
menu_board(name,price)
order = input("원하시는 제품을 골라주세요!(나가기:q)")
while True:
   

                                  
    if order =="q":
        break
    if order =="n":
        
        amount =pay(n_order,name,price)

        print(f"총 금액:{amount}") 
        break   
    if int(order)>=len(name):order=input("다시 주문해 주세요.")
    elif int(order)< len(name) and int(quantity[int(order)])>0:
        quantity[int(order)] = int(quantity[int(order)]) -1
        print(f"수{quantity}")
        order_update(n_order,name[int(order)],quantity)
        print(n_order)
        order=input("더 주문하시나요?(결제하시려면 n을 눌러주세요)")

    elif int(quantity[int(order)])<=0:
        order=input("재고가 없습니다.")



    




