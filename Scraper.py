from splinter import Browser
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import logging
import multiprocessing

logging.basicConfig(format='%(message)s', filename='data_splinter.json', level=logging.WARNING)

class MynimoScraper:
	def __init__(self):
		self.url = 'http://cebu.mynimo.com'
		self.proxy = [
						'--proxy=23.27.197.200:24801',
						'--proxy=23.27.197.201:24801',
						'--proxy=23.27.197.202:24801',
						'--proxy=23.27.197.203:24801',
						'--proxy=23.27.197.204:24801',
						'--proxy=23.27.197.205:24801',
						'--proxy-type=http',
					 ]

	def __visit_url(self, browser, keyword):
		self.q = keyword
		browser.visit(self.url)
		browser.fill('q' , keyword)
		browser.find_by_name('gosearch').first.click()
		data = browser.html
		soup = BeautifulSoup(data)
		return soup

	def get_job_information(self, keyword, writer):
		count = 0
		browser = Browser('phantomjs', service_args= self.proxy)
		soup = self.__visit_url(browser, keyword)
		jobs = soup.find_all('tr', attrs = {'class':'aJobS'})
		count += self.__parse_data(jobs, keyword, writer)
		
		while soup.find('li', attrs = {'class':'next'}):
			browser.click_link_by_text('Next')
			data = browser.html
			soup = BeautifulSoup(data)
			jobs = soup.find_all('tr', attrs = {'class':'aJobS'})
			count += self.__parse_data(jobs, keyword, writer)
		print count
		print keyword
			
		browser.quit()

	def __parse_data(self, jobs, keyword, writer):
		output = OrderedDict()
		count = 0
		
		for job in jobs:
			output['keyword'] = self.q
			output['Job Title'] = job.find_all('td')[0].find(attrs = 'jobTitleLink').text.encode('utf-8')
			try:
				output['Location'] = job.find_all('td')[1].find(attrs = 'address').text
			except AttributeError:
				output['Location'] = job.find_all('td')[1].text.strip()
			output['Company'] = job.find_all('td')[2].text.strip()
			descri = job.find_next('tr').find(attrs = 'searchContent')
			try:
				output['Description'] = descri.text.encode('utf-8').strip()
			except AttributeError:
				output['Description'] = 'No description available!'
			count += 1
		
			writer.data.put(output)

		return count

class Worker(multiprocessing.Process):
	def __init__(self, queued_keyword, id, writer):
		multiprocessing.Process.__init__(self)
		self.scraper = MynimoScraper()
		self.queue = queued_keyword
		self.id = id
		self.writer = writer

	def run(self):
		item = self.queue

		while True:
			if item.empty() == False:
				keyword = item.get() 
				self.scraper.get_job_information(keyword.value, self.writer)
				print 'process %s' % self.id
			else:
				break

class Writer(multiprocessing.Process):
	def __init__(self):
		multiprocessing.Process.__init__(self)
		self.data = multiprocessing.Queue()
		
	def run(self):
		while True:
			output = self.data.get()
			if output == 'poison':
				break
			else:
				logging.warning(json.dumps(output, indent = 4))
		
class Keyword:
	def __init__(self, value):
		self.value = value

class MynimoScraper_Process:
	def __init__(self):
		self.item = multiprocessing.Queue()

	def start_working(self, keyword):
		list_workers = []
		count = multiprocessing.cpu_count()

		for i in keyword:
			self.item.put(Keyword(i))

		writer = Writer()

		for j in range(count):
			workers = Worker(self.item, j+1, writer)
			list_workers.append(workers)
			workers.start()

		writer.start()

		for j in list_workers:
			j.join()

		writer.data.put('poison')
			
if __name__ == '__main__':
	process = MynimoScraper_Process()
	keyword = ['Math', 'Java', 'PHP', 'Python']
	process.start_working(keyword)


			
