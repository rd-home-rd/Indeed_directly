# coding: utf8
import lxml.html
import string
import xlsxwriter
import pandas
import codecs
import sys
import urllib.parse
import numpy
from time import sleep   
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

class has_next_window():
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self):
  	pass

  def __call__(self, driver):
    windows = driver.window_handles   # Finding the referenced element
    if len(windows)>1:
        return True
    else:
        return False

argvs = sys.argv
worker_number=int(argvs[2])
#一覧ページ

for worker_number_sub in range(worker_number,26,5):
	profile = webdriver.FirefoxProfile()
	profile.set_preference('browser.download.folderList',2) # custom location
	profile.set_preference('browser.download.manager.showWhenStarting', False)
	profile.set_preference('browser.download.dir', 'C:\\Users\\tai.RD-WOODS\\Desktop\\csv_indeed')
	profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
	driver = webdriver.Firefox(profile)
	wait=WebDriverWait(driver,20)
	alljobarray=[]
	for pagenum in range((worker_number_sub-1)*4000,worker_number_sub*4000,10):
		list_page="https://jp.indeed.com/jobs?q=&l="+str(urllib.parse.quote(argvs[1]))+'&start='+str(pagenum)
		driver.get(list_page)
		wait.until(ec.presence_of_all_elements_located)
	#	sponsor	
		sjobs=driver.find_elements_by_xpath("//div[contains(@class,'iaP')]/parent::div[@class='sjCapt']/preceding-sibling::a")
		for sjob in sjobs:
			main_window = driver.current_window_handle
			sjob.send_keys(Keys.CONTROL+Keys.RETURN)
			wait.until(has_next_window())
			windows = driver.window_handles
			driver.switch_to.window(windows[1])
			try:
				wait.until(ec.presence_of_element_located((By.ID,'branding')))
			except:
				driver.find_element_by_tag_name("body").send_keys(Keys.F5)
				wait.until(ec.presence_of_all_elements_located)
			jobarray=[]
			if lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][2]/div[@class='jdSectionBody']/text()") !=[]:
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][1]/h1/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][2]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][3]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][4]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][5]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
			else: 
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][1]/h1/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][2]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][3]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')	
				try:	
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][4]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][5]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
			if jobarray in alljobarray:
				print(jobarray)
			else: 
				alljobarray.append(jobarray)
			del jobarray
			driver.close()
			driver.switch_to_window(main_window)
		del sjobs
	# 	organic
		jobs=driver.find_elements_by_xpath("//div[contains(@class,'iaP')]/ancestor::table/preceding-sibling::h2[@class='jobtitle']/a")
		for job in jobs:
			main_window = driver.current_window_handle
			job.send_keys(Keys.CONTROL+Keys.RETURN)
			wait.until(has_next_window())
			windows = driver.window_handles
			driver.switch_to.window(windows[1])
			try:
				wait.until(ec.presence_of_element_located((By.ID,'branding')))
			except:
				driver.find_element_by_tag_name("body").send_keys(Keys.F5)
				wait.until(ec.presence_of_all_elements_located)
			jobarray=[]
			if lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][2]/div[@class='jdSectionBody']/text()") !=[]:
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][1]/h1/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][2]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][3]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][4]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection'][5]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
			else: 
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][1]/h1/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][2]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][3]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')	
				try:	
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][4]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
				try:
					jobarray.append(lxml.html.fromstring(driver.page_source).xpath("//div[@id='job_summary']/div[@class='jdSection grayBar'][5]/div[@class='jdSectionBody']/text()")[0])
				except:
					jobarray.append('0')
			if jobarray in alljobarray:
				print(jobarray)
			else: 
				alljobarray.append(jobarray)
			del jobarray
			driver.close()
			driver.switch_to_window(main_window)
		del jobs
		wait.until(ec.presence_of_all_elements_located)
	d=pandas.DataFrame(data=alljobarray[:][:])
	writer = pandas.ExcelWriter('結果'+str(worker_number_sub)+'.xlsx',engine="xlsxwriter")
	d.to_excel(writer,index=False)
	writer.save()
	del alljobarray,d,writer
	driver.quit()