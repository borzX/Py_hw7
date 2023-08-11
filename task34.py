song = 'пара-ра-рам рам-пам-папам па-ра-па-да'


def rythm_detect(song):
    sp = song.split()
    f = lambda x: sum(1 for i in x if i in 'а')
    temp = f(sp[0])
    if all([f(i) == temp for i in sp]):
        return 'Парам пам-пам'
    return 'Пам парам'

print(rythm_detect(song))

# Вариант 2
# ----------------------------------------------
# def rythm_detect(song):
#     frazu = song.split()
#     a_list = [] # список с количеством а
#     temp_a = 0
#     for i in frazu:
#         temp_a = 0
#         for j in range(1, len(i)):
#             if j == len(i)-1:
#                 if i[j] == "а"and i[j-1]=="а":
#                     temp_a = temp_a
#                     a_list.append(temp_a)
                
#                 elif i[j] == "а":
#                     temp_a = temp_a+1
#                     a_list.append(temp_a)

#             else:
#                 if i[j] == "а"and i[j-1]=="а":
#                     temp_a = temp_a
                
#                 elif i[j] == "а":
#                     temp_a = temp_a+1
    
#     for i in a_list:
#         if i == i-1 or len(a_list)==1: 
#             return print("Парам пам-пам")
#         else:
#             return print("Пам парам")
        
# print(rythm_detect(song))