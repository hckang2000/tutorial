import sys
import csv
import os
import time
import urllib
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
serviceurl = 'https://www.amazon.com/s/ref=sr_pg_1?'
num=5720;
# now = datetime.datetime.now()
files = "dataset_link_1.txt"
if not os.path.exists(files):
	file(files, 'w').close()
enter = open(files,'w');
for j in range(1,399):

	count = 3;
	page = j;
	url = serviceurl + urllib.urlencode({ 'rh':'n:133140011','page':page,'sort': 'salesrank' , 'unfiltered':'1', 'ie':'UTF8' });
	driver = webdriver.Chrome();
	driver.maximize_window() #For maximizing window
	driver.get(url);
	driver.implicitly_wait(3) #gives an implicit wait for 10 seconds
	while driver.execute_script("return document.readyState") != 'complete':
		pass;

	# elem =driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li");

	for i in range(1,17):
		num+=1;

		print "%s" %(num);
		enter.write("%s\n" %(num))

		temp = 0;#temp =0 refers it is best seller;
		variable = 1;
		unlimited = 0;
		# for qs in range(1,10):
		try:
			if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[1]/div/a/span[1]/span"%(i)).text.encode('utf-8') == "Best Seller":
				temp=0;
		except:
			temp = 1;
			# if temp==0:
				# break;
		if temp == 0:
			print "Best Seller :- Yes";
			enter.write("Best Seller :- Yes\n");

			try:
				print "Name of Book :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[1]/a/h2"%(i)).text.encode('utf-8'));
				enter.write("Name of Book :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[1]/a/h2"%(i)).text.encode('utf-8')))
			except:
				pass;
			try:
				print "Release Date :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[1]/span[3]"%(i)).text.encode('utf-8'));
				enter.write("Release Date :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[1]/span[3]"%(i)).text.encode('utf-8')));
			except:
				pass;
			try:
				print "Author :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[2]/span[2]"%(i)).text.encode('utf-8'));
				enter.write("Author :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[2]/span[2]"%(i)).text.encode('utf-8')));
			except:
				pass;
			try:
				print "URL-Page of the book :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[1]/a"%(i)).get_attribute("href"));
				enter.write("URL-Page of the book :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[1]/a"%(i)).get_attribute("href")));
				new_url = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[1]/div[1]/a"%(i)).get_attribute("href")
			except:
				pass;

			try:

				if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/span[1]"%(i)).text.encode('utf-8') == "Read this and over 1 million books with":
					print "Kindle Unlimited Editon :- Yes";
					enter.write("Kindle Unlimited Editon :- Yes\n");

					unlimited = 1;

				else:
					print "Kindle Unlimited Editon :- No";
					enter.write("Kindle Unlimited Editon :- No\n");

			except:
				pass;

			try:
				print "Number of Rating :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[2]/div[2]/div/a"%(i)).text.encode('utf-8'));
				enter.write("Number of Rating :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[2]/div[2]/div/a"%(i)).text.encode('utf-8')));
			except:
				print "No Ratings till now";
				enter.write("No Ratings till now\n");
				variable = 0;

			try:
				if(unlimited==0):
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/span"%(i)).text.encode('utf-8')=="Auto-delivered wirelessly":
						print "Auto-delivered wirelessly :- Yes";
						enter.write("Auto-delivered wirelessly :- Yes\n");
					else:
						print "Auto-delivered wirelessly :- No";
						enter.write("Auto-delivered wirelessly :- No\n");
				else:
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[2]/div[1]/div[5]/span"%(i)).text.encode('utf-8')=="Auto-delivered wirelessly":
						print "Auto-delivered wirelessly :- Yes";
						enter.write("Auto-delivered wirelessly :- Yes\n");
					else:
						print "Auto-delivered wirelessly :- No";
						enter.write("Auto-delivered wirelessly :- No\n");

			except:
				print "Auto-delivered wirelessly :- No";
				enter.write("Auto-delivered wirelessly :- No\n");

			try:
				if(unlimited==0):
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/span"%(i)).text.encode('utf-8')=="Whispersync for Voice-ready":
						print "Whispersync for Voice-ready :- Yes";
						enter.write("Whispersync for Voice-ready :- Yes\n");
					else:
						print "Whispersync for Voice-ready :- No";
						enter.write("Whispersync for Voice-ready :- No\n");
				else:
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div[2]/div/div[2]/div[2]/div[1]/div[5]/span"%(i)).text.encode('utf-8')=="Whispersync for Voice-ready":
						print "Whispersync for Voice-ready :- Yes";
						enter.write("Whispersync for Voice-ready :- Yes\n");
					else:
						print "Whispersync for Voice-ready :- No";
						enter.write("Whispersync for Voice-ready :- No\n");

			except:
				print "Whispersync for Voice-ready :- No";
				enter.write("Whispersync for Voice-ready :- No\n");

			driver.get(new_url);
			while driver.execute_script("return document.readyState") != 'complete':
				pass;
			try:
				for nums in range(1,10):
					if driver.find_element_by_xpath("""//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li[%s]/b"""%(nums)).text == 'ASIN:':
						print driver.find_element_by_xpath("""//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li[%s]"""%(nums)).text.encode('utf-8');
						enter.write("%s\n"%(driver.find_element_by_xpath("""//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li[%s]"""%(nums)).text.encode('utf-8')));
						break;
			except:
				pass;
			try:
				print "Average Rating :- %s"%(driver.find_element_by_xpath("""//*[@id="reviewSummary"]/div[2]/span/a/span""").text.encode('utf-8'));
				enter.write("Average Rating :- %s\n"%(driver.find_element_by_xpath("""//*[@id="reviewSummary"]/div[2]/span/a/span""").text.encode('utf-8')));
			except:
				pass;
			try:
				print "No. of 5 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[1]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 5 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[1]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 5 star ratings :- 0";
				enter.write("No of 5 star ratings :- 0\n");
			try:
				print "No. of 4 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[2]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 4 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[2]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 4 star ratings :- 0";
				enter.write("No of 4 star ratings :- 0\n");
			try:
				print "No. of 3 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[3]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 3 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[3]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 3 star ratings :- 0";
				enter.write("No of 3 star ratings :- 0\n");
			try:
				print "No. of 2 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[4]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 2 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[4]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 2 star ratings :- 0";
				enter.write("No of 2 star ratings :- 0\n");
			try:
				print "No. of 1 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[5]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 1 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[5]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 1 star ratings :- 0";
				enter.write("No of 1 star ratings :- 0\n");

			try:
				print "Price for Kindle Editon :- %s" %(driver.find_element_by_xpath("""//*[@id="a-autoid-1-announce"]/span[2]/span""").text.encode('utf-8'));
				enter.write("Price for Kindle Editon :- %s\n" %(driver.find_element_by_xpath("""//*[@id="a-autoid-1-announce"]/span[2]/span""").text.encode('utf-8')));
			except:
				pass;

			driver.back();

		else:
			# driver = driver.find_element_by_xpath("div/div/div/div[2]")
			print "Best Seller :- No"
			enter.write("Best Seller :- No\n");
			try:
				print "Name of Book :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[1]/a/h2"%(i)).text.encode('utf-8'));
				enter.write("Name of Book :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[1]/a/h2"%(i)).text.encode('utf-8')));
			except:
				pass;
			try:
				print "Release Date :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[1]/span[3]"%(i)).text.encode('utf-8'));
				enter.write("Release Date :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[1]/span[3]"%(i)).text.encode('utf-8')));
			except:
				pass;
			try:
				print "Author :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[2]/span[2]"%(i)).text.encode('utf-8'));
				enter.write("Author :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[2]/span[2]"%(i)).text.encode('utf-8')));
			except:
				pass;
			try:
				print "URL-Page of the book :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[1]/a"%(i)).get_attribute("href"));
				enter.write("URL-Page of the book :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[1]/a"%(i)).get_attribute("href")));
				new_url = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[1]/div[1]/a"%(i)).get_attribute("href")
			except:
				pass;

			try:
				if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[2]/div[1]/div[2]/span[1]"%(i)).text.encode('utf-8') == "Read this and over 1 million books with":
					print "Kindle Unlimited Editon :- Yes";
					enter.write("Kindle Unlimited Editon :- Yes\n");

					unlimited=1;

				else:
					print "Kindle Unlimited Editon :- No";
					enter.write("Kindle Unlimited Editon :- No\n");

			except:
				pass;

			try:
				print "Number of Rating :- %s" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[2]/div[2]/div/a"%(i)).text.encode('utf-8'));
				enter.write("Number of Rating :- %s\n" %(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[2]/div[2]/div/a"%(i)).text.encode('utf-8')));

			except:
				print "No Ratings till now";
				enter.write("No Ratings till now\n");

				variable = 0;

			try:
				if(unlimited==0):
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[2]/div[1]/div[3]/span"%(i)).text.encode('utf-8')=="Auto-delivered wirelessly":
						print "Auto-delivered wirelessly :- Yes";
						enter.write("Auto-delivered wirelessly :- Yes\n");

					else:
						print "Auto-delivered wirelessly :- No";
						enter.write("Auto-delivered wirelessly :- No\n");

				else:
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[2]/div[1]/div[5]/span"%(i)).text.encode('utf-8')=="Auto-delivered wirelessly":
						print "Auto-delivered wirelessly :- Yes";
						enter.write("Auto-delivered wirelessly :- Yes\n");

					else:
						print "Auto-delivered wirelessly :- No";
						enter.write("Auto-delivered wirelessly :- No\n");

			except:
				print "Auto-delivered wirelessly :- No";
				enter.write("Auto-delivered wirelessly :- No\n");


			try:
				if(unlimited==0):
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[2]/div[1]/div[3]/span"%(i)).text.encode('utf-8')=="Whispersync for Voice-ready":
						print "Whispersync for Voice-ready :- Yes";
						enter.write("Whispersync for Voice-ready :- Yes\n");

					else:
						print "Whispersync for Voice-ready :- No";
						enter.write("Whispersync for Voice-ready :- No\n");

				else:
					if driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[%s]/div/div/div/div[2]/div[2]/div[1]/div[5]/span"%(i)).text.encode('utf-8')=="Whispersync for Voice-ready":
						print "Whispersync for Voice-ready :- Yes";
						enter.write("Whispersync for Voice-ready :- Yes\n");

					else:
						print "Whispersync for Voice-ready :- No";
						enter.write("Whispersync for Voice-ready :- No\n");

			except:
				print "Whispersync for Voice-ready :- No";
				enter.write("Whispersync for Voice-ready :- No\n");

			driver.get(new_url);
			while driver.execute_script("return document.readyState") != 'complete':
				pass;
			try:
				for nums in range(1,10):
					if driver.find_element_by_xpath("""//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li[%s]/b"""%(nums)).text.encode('utf-8') == 'ASIN:':
						print driver.find_element_by_xpath("""//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li[%s]"""%(nums)).text.encode('utf-8');
						enter.write("%s\n"%(driver.find_element_by_xpath("""//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li[%s]"""%(nums)).text.encode('utf-8')));
						break;
			except:
				pass;

			try:
				print "Average Rating :- %s"%(driver.find_element_by_xpath("""//*[@id="reviewSummary"]/div[2]/span/a/span""").text.encode('utf-8'));
				enter.write("Average Rating :- %s\n"%(driver.find_element_by_xpath("""//*[@id="reviewSummary"]/div[2]/span/a/span""").text.encode('utf-8')));
			except:
				pass;
			try:
				print "No. of 5 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[1]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 5 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[1]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 5 star ratings :- 0";
				enter.write("No of 5 star ratings :- 0\n");
			try:
				print "No. of 4 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[2]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 4 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[2]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 4 star ratings :- 0";
				enter.write("No of 4 star ratings :- 0\n");
			try:
				print "No. of 3 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[3]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 3 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[3]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 3 star ratings :- 0";
				enter.write("No of 3 star ratings :- 0\n");
			try:
				print "No. of 2 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[4]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 2 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[4]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 2 star ratings :- 0";
				enter.write("No of 2 star ratings :- 0\n");
			try:
				print "No. of 1 star ratings :- %s"%(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[5]/td[3]/a""").text.encode('utf-8'));
				enter.write("No. of 1 star ratings :- %s\n" %(driver.find_element_by_xpath("""//*[@id="histogramTable"]/tbody/tr[5]/td[3]/a""").text.encode('utf-8')));
			except:
				print "No of 1 star ratings :- 0";
				enter.write("No of 1 star ratings :- 0\n");

			try:
				print "Price for Kindle Editon :- %s" %(driver.find_element_by_xpath("""//*[@id="a-autoid-1-announce"]/span[2]/span""").text.encode('utf-8'));
				enter.write("Price for Kindle Editon :- %s\n" %(driver.find_element_by_xpath("""//*[@id="a-autoid-1-announce"]/span[2]/span""").text.encode('utf-8')));
			except:
				pass;

			driver.back();
		# print "My program took", time.time() "to run"
		now = datetime.datetime.now()
		print now.strftime("%Y-%m-%d %H:%M")
		enter.write("%s\n"%(now.strftime("%Y-%m-%d %H:%M")))
		print "\n";
		enter.write("\n");

	driver.quit()
enter.close()
