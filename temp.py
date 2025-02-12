
# programming language = set of structured statements


# human interaction

# programming language

# computer = gate, IC, ... = hardware

# school bus teacher shoes
# print(37 + 400 + 5, 100)

a_age = 18
b_age = 18
c_age = 18
d_age = 18
e_age = 19
f_age = 19
g_age = 20
h_age = 20
i_age = 20
j_age = 22
k_age = 23

# print(k_age, 19, 18, 20, 20, 20, 18, 18, 18, 19, 22)

# print((a_age+...+k_age) / 11)

# print(18, 18, 18, 18, 19, 19, 20, 20, 20, 22, k_age) # int: integer

presenter_age = 64

presenter_name = 'hossein' # str: string

math_score = 19.0 # 19.0 # float

asdf = True

# print(True and True) # bool: boolean  -> logic
# print(False and (False or True)) #   1 ------- ### ------- ### -------- ### ---------- 2

#      ----- ### -------
#  1 ------- ### ---------   2
#      ----- ### -------

is_adult = presenter_age > 18 #  >,  <,  <=,  >=,  ==,  !=

# if presenter_age < 18:  # len: length
#     print('presenter is a teenager')
# elif presenter_age < 60:  #   18 <= presenter_age < 60
#     print('presenter is an adult')
# else:
#     print("presenter is old")


# loop, iteration

# for i in range(1000):  # 0, 1, 2, ..., 1000-1
#     print(i * 2)

# for i in range(19, 54):
#     print(i)

# list

a = []
class_ages = [18, 19, 23, 22, 19, 18, 20, 18, 18, 20, 20]

provinces = ["Hamedan", "Gorgan", "Markazi", "Bushehr"]

chaos = [19, 'hossein', 19.0, True]

# chaos[0] = '23'
# print(class_ages[11])
# print(provinces[2])
# for i in chaos:
#     i = str(i)
#     print(i, type(i))

#set
# b = {18, 20, 18, 18, 20, 18}
# print('length of this set:', len(b))


#tuple
# c = (18, 29, 20)
# for i in c:
#     print(i)


#dict: dictionary
d = {'presenter_name': presenter_name, 'presenter_age': presenter_age, 'presenter_address': 'Tehran', 'presenter_country': 'Iran'}

# print(d['presenter_country'])


def score_average(scores):
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    return average


class_scores = [19, 18, 17, 16, 17.5, 18.25]
print(score_average(class_scores))
# print(scores)




