
def main():
    address_book={} #공백 딕셔너리 생성
    while True:
        user = display_menu();
        if user ==1: #이름과 번호를 추가
            name,number=get_contact()
            address_book[name]=number
            print("key",name)
            print("value",address_book[name])

        elif user==2: #이름으로 항목 삭제
            name,number=get_contact()
            address_book.pop(name) #팝 날린다.
        elif user==3:
            s=input("input name : ")
            try:
                print(f'{s}의 전화번호 {address_book[s]}')
            except:
                print("fail")
        elif user==4:
           for key in sorted(address_book):
               print(key," number : ",address_book[key])
        elif user == 5:
            f=open('123.txt','rb')
            s=f.readlines()
            print(s)
            f.close()
        else:
            break
def get_contact():
    name=input("name : ")
    number=input("number : ")
    return name,number      #튜플로 반환

#메뉴를 화면에 출력
def display_menu():
    print("1. add number")
    print("2. delete number")
    print("3. search number")
    print("4. print number")
    print("5. open number")
    #print("7. end")
    select = int(input("pick menu: "))
    return select
#실
main()