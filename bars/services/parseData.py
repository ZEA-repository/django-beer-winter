from bs4 import BeautifulSoup as BS
import requests


class Parse:
	""" take data from website """

	def __init__(self, url, selector):
		self.url = requests.get(url, verify=False)
		self.html = BS(self.url.content, "html.parser")
		self.data = self.html.select(selector)

	def lambic(self):
		""" parsing addresses lambic

		Incorrect coordinates by addresses:
			ул. Долгоруковская, 19с7
			ул. Неверовского 10с6
			Проспект Мира, 26с7
			ул. Большая Ордынка, 65
			Страстной бульвар, 7с1
			ул. Верхняя Радищевская, 15с1
			Гоголевский б-р, 33/1
			Большой Черкасский пер., 15/17с1 """

		correct_addresses = [
			"ул. Долгоруковская, 19 с7",
			"ул. Неверовского 10 с6",
			"Москва, Проспект Мира, 26 с7",
			"Москва, Пятнитская улица, 74 с3",
			"Страстной бульвар, 7 с1",
			"Верхняя Радищевская, 15 с1",
			"Гоголевский бульвар, 33/1",
			"Большой Черкасский переулок, 17" 
		]

		addresses = [self.data[count].text for count in range(19) if count % 2 == 0]
		addresses[2] = correct_addresses[0]
		addresses[3] = correct_addresses[1]
		addresses[4] = correct_addresses[2]
		addresses[5] = correct_addresses[3]
		addresses[6] = correct_addresses[4]
		addresses[7] = correct_addresses[5]
		addresses[8] = correct_addresses[6]
		addresses[9] = correct_addresses[7]
		return addresses

	def manneken_pis(self):
		""" parsing addresses manneken_pis """

		petrovka = self.data[2].text
		return petrovka

	def __str__(self):
		return "{} {}".format(lambic=lambic, manneken_pis=manneken_pis)
