# dict of words2meow
dict1 = {'a':'喵呜'  ,'b':'呜喵喵喵','c':'呜喵呜喵','d':'呜喵'  ,'e':'喵'   ,
         'f':'喵喵呜喵','g':'呜呜喵' ,'h':'喵喵喵喵','i':'喵喵'  ,'j':'喵呜呜呜',
         'k':'呜喵呜' ,'l':'喵呜喵喵','m':'呜呜'  ,'n':'呜喵'  ,'o':'呜呜呜' ,
         'p':'喵呜呜喵','q':'呜呜喵呜','r':'喵呜喵' ,'s':'喵喵喵' ,'t':'呜'   ,
         'u':'喵喵呜' ,'v':'喵喵喵呜','w':'喵呜呜' ,'x':'呜喵喵呜','y':'呜喵呜呜','z':'呜呜喵喵',
         '0':'呜呜呜呜呜' ,'1':'喵呜呜呜呜' ,'2':'喵喵呜呜呜' ,'3': '喵喵喵呜呜','4': '喵喵喵喵呜' ,
         '5': '喵喵喵喵喵','6': '呜喵喵喵喵','7': '呜呜喵喵喵','8': '呜呜呜喵喵','9': '呜呜呜呜喵' }

# dict of meow2words
dict2 = dict(zip(dict1.values(),dict1.keys()))

def encode():
    words = input("Input a sentence you want to endoce, NO PUNCTUATION: ").strip().lower()
    for letter in words:
        if letter == ' ':
            print('/',end=' ')
        else:
            print(dict1[letter], end=' ')
    print()

def decode():
    codes = input("Input Meow code you want to decode, ONLY MEOW CODE: ").strip().split(" ")
    for sign in codes:
        if sign == '/':
            print(' ',end='')
        else:
            print(dict2[sign], end='')
    print()
    
def main():    
    while 1:
        choice = input("Encode(Words to Meow codes) or Decode(Meow codes to Words). Plase input [0/1]")

        if   choice == '0':
            encode()
        elif choice == '1':
            decode()
        else:
            break

if __name__=="__main__":
    main()
