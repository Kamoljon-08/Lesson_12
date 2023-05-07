mashinalar = []

while True:
    print("""
***************************************************
**                                               **
**        AVTOSERVISGA XUSH KELIBSIZ            **
**                                               **
***************************************************
  """)
    print('1. Mashinalarnini ko`rish\n2. Mashina qo`shish\n3. Sotib olish\n4. Qidirish\n5. Chiqish\n')
    tanlov=input('Yuqoridagi buyruqlardan biriga mos sonni kiriting:')


    if tanlov=='1':
        print("--------------Bizda bor mashinalar-----------------------\n\n")
        print('Avtoservisda bor mashinalar soni: ',len(mashinalar))
        while len(mashinalar) != 0:
            print('Mashinalar ro`yxati:')
            for mashina in mashinalar:
                for keys, value in mashina.items():
                    print(keys, ':', value)
            break
  
    elif tanlov=='2':
        print('------------------Mashina qo`shish----------------------')
        mashina_nomi=str(input('Mashina_nomi:'))
        mashina_narxi=int(input('Mashina_narxi:'))
        mashina_miqdori=int(input('Mashina_miqdori:'))
    
        mashinalar.append({'mashina_nomi':mashina_nomi, 'mashina_narxi':mashina_narxi, 'mashina_miqdori':mashina_miqdori})
        print(f'Mashina_nomi: {mashina_nomi}, mashina_narxi: {mashina_narxi}, mashina_midqori: {mashina_miqdori} qayd etildi.  ')


    elif tanlov=='3':
        print('-------------------Sotib olish----------------------')
        for mashina in mashinalar:
            for keys, value in mashina.items():
                print(keys, ':', value)
        sotib_olish_uchun_mashina = input('Yuqoridagi qaysi mashinani sotib oldingiz? ')
        for mashina in mashinalar:
            if sotib_olish_uchun_mashina.lower() == mashina['mashina_nomi'].lower():
                if mashina['mashina_miqdori'] != 0:
                    print( mashina['mashina_narxi']  , ' so`m  bankkaga to`lang, iltimos.')
                    mashina['mashina_miqdori'] -= 1
                else:
                    print('Bizda bu mashinadan qolmagan')


    elif tanlov == '4' :
        print('------------------Mashinani qidirish------------------')
        qidiruvdagi_mashina = input('Sotib olgan mashinangizni nomini kiriting : ')
        for mashina in mashinalar:
            if mashina['mashina_nomi'].lower() == qidiruvdagi_mashina.lower():
                print('Ushbu mashina ' + qidiruvdagi_mashina + ' haqidagi ma`lumotlar:')
                print(mashina)
            else:
                print('Bizda bunaqa mashina mavjud emas')

    elif tanlov == '5':
        print('------------------Chiqish------------------')
        print("Thank you for your purchase")
        print("See yoyu")
        break
    
    else:
        print('Siz noto`gri raqam kiritdingiz. ')