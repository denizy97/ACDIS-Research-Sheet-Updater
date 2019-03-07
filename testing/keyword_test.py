#Written in 2019 by Deniz YILDIRIM <denizy@protonmail.com>
#This program is PROBABLY owned by the University of Illinois, as I wrote it while
#working for ACDIS in Illinois. Consult UofI before changing, distributing, sharing,
#making it open source etc.
#See https://www.bot.uillinois.edu/governance/general_rules for more information.

import requests
import csv
import json
import os
import string
keywords_file = "../keywords/KeySecurityWords.txt"
keywords = []
with open(keywords_file) as f:
	for line in f:
		word = " " + line[0:len(line)-1] + " "
		keywords.append(word)

#string_input: "<p>stuff stuff.</p>"
def securityRelated(string_input):
	translator = str.maketrans('', '', string.punctuation) #maps punctuations to None
	string_clean = string_input.translate(translator)	#deletes punctuations
	string_clean = string_clean[1:len(string_clean)-1] #deletes the letter p from beginning and end of string
	#word_list = string_clean.split() #turns string into a list of words
	for word in keywords:
		if word in string_clean:
			return True #checks if any keyword is in the input text
	return False

api_key = input("Please write/paste the API key: ")
csv_names = ["../physical.csv", "../chemical.csv", "../cybersecurity.csv", "../energy.csv", "../waterfoodclimate.csv"]
csv_names_new = ["../physical_new.csv", "../chemical_new.csv", "../cybersecurity_new.csv", "../energy_new.csv", "../waterfoodclimate_new.csv"]
email_column = 1
date_column = 4
title_column = 3
page_size = "200"

headers = {
    'Accept': 'application/json',
    'api-key': api_key,
}

params = (
    ('fields', 'title,subTitle,publicationStatuses.*,info.*,abstract.*'),
    ('apiKey', api_key),
	('size', page_size),
	('order', 'publicationYearOnly'),
	('orderBy', 'descending')
)
not_in_API = 0
no_abstract = 0
no_keyword = 0
successful = 0
research_name_full = ""
for i in range(len(csv_names)):
	with open(csv_names[i]) as csv_file:
		found = False
		csv_reader = csv.reader(csv_file)
		line = 0
		print("LOOKING AT " + csv_names[i])
		print("")
		for row in csv_reader:
			row_changed = False #reset this flag at the beginning of each row
			#first row contains titles of columns
			if line == 0:
				line += 1
			else:
				current_person = row[email_column] #email is in second column
				r = requests.get("https://experts.illinois.edu/ws/api/513/persons/" + current_person + "/research-outputs", headers=headers, params=params)
				found = False
				if r.status_code == 200: #if there is such a person
					json_list = r.json() #parse json
					item = 0
					while item < len(json_list.get("items")) - 1:
						publications = json_list.get("items")[item].get("publicationStatuses")
						publication_index = 0
						while publication_index < len(publications):
							if json_list.get("items")[item].get("publicationStatuses")[publication_index].get("current") == True:
								break;
							publication_index += 1
						date = json_list.get("items")[item].get("publicationStatuses")[publication_index].get("publicationDate")
						date_string =  ""
						if(date.get("year") != None and (row[date_column][0:4].isdigit() == False or int(date.get("year")) >= int(row[date_column][0:4]))):
							date_string += str(date.get("year"))
							if(date.get("month") != None):
								date_string += "-" + str(date.get("month"))
								if(date.get("day") != None):
									date_string += "-" + str(date.get("day"))
						if date_string == row[date_column]:
							research_name = json_list.get("items")[item].get("title")
							research_subName = json_list.get("items")[item].get("subTitle")
							research_name_full = str(research_name)
							if research_subName != None:
								research_name_full += ': ' + str(research_subName)
							if (research_name_full in row[title_column]):
								found = True
								if json_list.get("items")[item].get("abstract") != None:
									abstract = json_list.get("items")[item].get("abstract")[0].get("value")
									if(securityRelated(abstract) == True):
										successful += 1
										break
									else:
										no_keyword += 1
										print("Couldn't find keyword in row " + str(line) + ": " + str(row[title_column]))
										print("")
										break
								else:
									no_abstract += 1
									print("There is no Abstract of row " + str(line) + ": " + str(row[title_column]))
									print("")
									break
						item += 1
				else:
					print("STATUS CODE NOT 200")
				if found == False:
					not_in_API += 1
					print("Following row does not exist in API or has the wrong date. Row " + str(line) + ": " + str(row[title_column]))
				#	if r.status_code == 200:
				#		print("PERSON DATA DUMP:")
				#		item = 0
				#		while item < len(json_list.get("items")) - 1:
				#			print(json_list.get("items")[item].get("title"))
				#			print(json_list.get("items")[item].get("subTitle"))
				#			print(json_list.get("items")[item].get("publicationStatuses")[0].get("publicationDate"))
				#			print("*")
				#			item += 1
					print("")
				#else:
				#	print("MATCHED: " + str(row[title_column]))
				#	print("WITH: " + research_name_full)
				#	print ("")
				line += 1

print("IN TOTAL")
print(str(not_in_API) + " entries weren't even in the API or had wrong dates.")
print(str(no_abstract) + " entries didn't have abstracts to search keywords in.")
print(str(no_keyword) + " entries had no keywords in their abstracts.")
print(str(successful) + " entries had were successfully catched with keywords.")
