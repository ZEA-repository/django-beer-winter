from faker import Faker


def random_description_db(num):
	""" Create random data for description db field 
		num - number of sentenses """

	fake = Faker()
	my_word_list = [
	'beer','cheesecake','sugar',
	'special','wafer','dessert',
	'sesame','stout','beans',
	'pie','bar','Ice','oat', 'drink' ]

	if num == 1:
		sentense = fake.sentence(ext_word_list=my_word_list)
		sentense = " ".join(sentense)

	sentense = [fake.sentence(ext_word_list=my_word_list) for bar in range(num)]
	sentense = " ".join(sentense)
	
	return sentense