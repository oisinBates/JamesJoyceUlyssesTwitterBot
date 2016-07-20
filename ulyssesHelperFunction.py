
def getChapter(x):
	part="Part I: The Telemachiad"
	episode="Episode 1, Telemachus"

	if 389 <= x <= 607:
	    episode="Episode 2, Nestor" 

	elif 608 <= x <= 718:
	    episode="Episode 3, Proteus" 

	elif 719 <= x <= 902:
		part="Part II: The Odyssey"
		episode="Episode 4, Calypso" 

	elif 903 <= x <= 1064:
		part="Part II: The Odyssey"
		episode="Episode 5, Lotus Eaters" 

	elif 1065 <= x <= 1469:
		part="Part II: The Odyssey"
		episode="Episode 6, Hades" 

	elif 1470 <= x <= 2018:
		part="Part II: The Odyssey"
		episode="Episode 7, Aeolus" 

	elif 2019 <= x <= 2407:
		part="Part II: The Odyssey"
		episode="Episode 8, Aeolus" 

	elif 2408 <= x <= 2944:
		part="Part II: The Odyssey"
		episode="Episode 9, Aeolus"

	elif 2945 <= x <= 3478:
		part="Part II: The Odyssey"
		episode="Episode 10, Wandering Rocks"

	elif 3479 <= x <= 4123:
		part="Part II: The Odyssey"
		episode="Episode 11, Sirens"

	elif 4124 <= x <= 4701:
		part="Part II: The Odyssey"
		episode="Episode 12, Cyclops"

	elif 4702 <= x <= 4842:
		part="Part II: The Odyssey"
		episode="Episode 13, Nausicaa"

	elif 4843 <= x <= 4910:
		part="Part II: The Odyssey"
		episode="Episode 14, Oxen of the Sun"

	elif 4911 <= x <= 6436:
		part="Part II: The Odyssey"
		episode="Episode 15, Circe"

	elif 6437 <= x <= 6734:
		part="Part III: The Nostos"
		episode="Episode 16, Eumaeus"

	elif 6735 <= x <= 7443:
		part="Part III: The Nostos"
		episode="Episode 17, Ithaca"

	elif 7444 <= x <= 7454:
		part="Part III: The Nostos"
		episode="Episode 18, Penelope"

	return {'part': part, 'episode': episode}



















#import random
# from pyswitch import Switch   # pyswitch can be found on PyPI
# myswitch = Switch()

# part="Part I: The Telemachiad"
# episode="Episode 1, Telemachus"
# @myswitch.case(range(0,389))
# def case1(value):
# 	episode="Episode 1, Telemachus"

# @myswitch.case(range(389,608))
# def case2(value):
#     episode="Episode 2, Nestor" 

# @myswitch.case(range(608,719))
# def case3(value):
#     episode="Episode 3, Proteus" 

# @myswitch.case(range(719, 903))
# def case4(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 4, Calypso" 

# @myswitch.case(range(903, 1065))
# def case5(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 5, Lotus Eaters" 

# @myswitch.case(range(1065, 1470))
# def case6(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 6, Hades" 

# @myswitch.case(range(1470, 2019))
# def case7(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 7, Aeolus" 

# @myswitch.case(range(2019, 2408))
# def case8(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 8, Aeolus" 

# @myswitch.case(range(2408, 2945))
# def case9(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 9, Aeolus"

# @myswitch.case(range(2945, 3479))
# def case10(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 10, Wandering Rocks"

# @myswitch.case(range(3479, 4124))
# def case11(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 11, Sirens"

# @myswitch.case(range(4124, 4702))
# def case12(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 12, Cyclops"

# @myswitch.case(range(4702, 4843))
# def case13(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 13, Nausicaa"

# @myswitch.case(range(4843 ,4911))
# def case14(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 14, Oxen of the Sun"

# @myswitch.case(range(4911, 6437))
# def case15(value):
# 	part="Part II: The Odyssey"
# 	episode="Episode 15, Circe"

# @myswitch.case(range(6437, 6735))
# def case16(value):
# 	part="Part III: The Nostos"
# 	episode="Episode 16, Eumaeus"

# @myswitch.case(range(6735,7444))
# def case17(value):
# 	part="Part III: The Nostos"
# 	episode="Episode 17, Ithaca"

# @myswitch.case(range(7444, 7455))
# def case18(value):
# 	part="Part III: The Nostos"
# 	episode="Episode 18, Penelope"

	

# myswitch(488)
# print('part: ', part)
# print('episode: ', episode)

# for i in range(15):
# 	print random.randrange(0,7455)

# startPoint=random.randrange(0,7455)
# print('start:', startPoint)



# 2.1.1	Episode 1, Telemachus
# 2.1.2	Episode 2, Nestor
# 2.1.3	Episode 3, Proteus
# 2.2	Part II: The Odyssey
# 2.2.1	Episode 4, Calypso
# 2.2.2	Episode 5, Lotus Eaters
# 2.2.3	Episode 6, Hades
# 2.2.4	Episode 7, Aeolus
# 2.2.5	Episode 8, Lestrygonians
# 2.2.6	Episode 9, Scylla and Charybdis
# 2.2.7	Episode 10, Wandering Rocks
# 2.2.8	Episode 11, Sirens
# 2.2.9	Episode 12, Cyclops
# 2.2.10	Episode 13, Nausicaa
# 2.2.11	Episode 14, Oxen of the Sun
# 2.2.12	Episode 15, Circe
# 2.3	Part III: The Nostos
# 2.3.1	Episode 16, Eumaeus
# 2.3.2	Episode 17, Ithaca
# 2.3.3	Episode 18, Penelope
# 3	