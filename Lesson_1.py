maxsulotlar = []

while True:
    print("""
***************************************************
**                                               **
**        MINI MARKETGA XUSH KELIBSIZ            **
**                                               **
***************************************************
  """)
    print('1. Maxsulotlarni ko`rish\n2. Maxsulot qo`shish\n3. Sotib olish\n4. Qidirish\n5. Chiqish\n')
    tanlov=input('Yuqoridagi buyruqlardan biriga mos sonni kiriting:')


    if tanlov=='1':
        print("--------------Bizda bor maxulotlar-----------------------\n\n")
        print('Mini marketda bor maxsulotlar soni: ',len(maxsulotlar))
        while len(maxsulotlar) != 0:
            print('Maxsulotlar ro`yxati:')
            for maxsulot in maxsulotlar:
                for key, value in maxsulot.items():
                    print(key, ':', value)
            break
  
    elif tanlov=='2':
        print('------------------Maxsulot qo`shish----------------------')
        maxsulot_nomi=str(input('Maxsulot nomi:'))
        maxsulot_narxi=int(input('Maxsulot_narxi:'))
        maxsulot_miqdori=int(input('Maxsulot miqdori:'))
    
        maxsulotlar.append({'maxsulot_nomi':maxsulot_nomi, 'maxsulot_narxi':maxsulot_narxi, 'maxsulot_miqdori':maxsulot_miqdori})
        print(f'Maxsulot: {maxsulot_nomi}, narxi: {maxsulot_narxi}, maxsulot midqori: {maxsulot_miqdori} qayd etildi.  ')


    elif tanlov=='3':
        print('-------------------Sotib olish----------------------')
        for maxsulot in maxsulotlar:
            for key, value in maxsulot.items():
                print(key, ':', value)
        sotib_olish_uchun_maxsulot = input('Yuqoridagi qaysi maxsulotni sotib oldingiz? ')
        for maxsulot in maxsulotlar:
            if sotib_olish_uchun_maxsulot.lower() == maxsulot['maxsulot_nomi'].lower():
                if maxsulot['maxsulot_miqdori'] != 0:
                    print( maxsulot['maxsulot_narxi']  , ' so`m  kassaga to`lang, iltimos.')
                    maxsulot['maxsulot_miqdori'] -= 1
                else:
                    print('Bizda bu maxsulotdan qolmagan')


    elif tanlov == '4' :
        print('------------------Maxsulotni qidirish------------------')
        qidiruvdagi_maxsulot = input('Qidirishni xohlagan maxsulotingizni nomini kiriting : ')
        for maxsulot in maxsulotlar:
            if maxsulot['maxsulot_nomi'].lower() == qidiruvdagi_maxsulot.lower():
                print('Ushbu maxsulot ' + qidiruvdagi_maxsulot + ' haqidagi ma`lumotlar:')
                print(maxsulot)
            else:
                print('Bizda bunaqa maxsulot topilmadi')

    elif tanlov == '5':
        print('------------------Chiqish------------------')
        print("Thank you for your purchase")
        print("See you")
        break

    else:
        print('Siz noto`gri raqam kiritdingiz. ')    