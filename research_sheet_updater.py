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
import sys
keywords_file = "keywords/KeySecurityWords.txt"
keywords = {"this", "is", "a","set"}
with open(keywords_file) as f:
	keywords.clear()
	for line in f:
		word = line[0:len(line)-1]
		keywords.add(word)

#string_input: "<p>stuff stuff.</p>"
def securityRelated(string_input):
	translator = str.maketrans('', '', string.punctuation) #maps punctuations to None
	string_clean = string_input.translate(translator)	#deletes punctuations
	string_clean = string_clean[1:len(string_clean)-1] #deletes the letter p from beginning and end of string
	word_list = string_clean.split() #turns string into a list of words
	return (keywords.isdisjoint(word_list) == False) #checks if any keyword is in the input text

api_key = input("Please write/paste the API key: ")
csv_names = ["physical.csv", "chemical.csv", "cybersecurity.csv", "energy.csv", "waterfoodclimate.csv"]
csv_names_new = ["physical_new.csv", "chemical_new.csv", "cybersecurity_new.csv", "energy_new.csv", "waterfoodclimate_new.csv"]
email_column = 1
date_column = 4
title_column = 3
page_size = "200"

headers = {
    'Accept': 'application/json',
    'api-key': api_key,
}

params = (
    ('fields', 'title.*,subTitle.*,publicationStatuses.*,info.*,abstract.*'),
    ('apiKey', api_key),
	('size', page_size),
	('order', 'publicationYear'),
	('orderBy', 'descending')
)
for i in range(len(csv_names)):
	row_changed = False
	with open(csv_names[i], encoding='utf-8') as csv_file, open(csv_names_new[i], 'w', encoding='utf-8', newline='') as csv_file_new:
		row_changed = False
		file_changed = False
		csv_reader = csv.reader(csv_file)
		csv_writer = csv.writer(csv_file_new)
		line = 0
		for row in csv_reader:
			row_changed = False #reset this flag at the beginning of each row
			#first row contains titles of columns
			if line == 0:
				line += 1
			else:
				current_person = row[email_column] #email is in second column
				r = requests.get("https://experts.illinois.edu/ws/api/518/persons/" + current_person + "/research-outputs", headers=headers, params=params)
				#if r.status_code != 200:
					#print("Person " + current_person + " couldn't be found!")
					#print("Status code: " + str(r.status_code))

				if r.status_code == 200: #if there is such a person
					json_list = r.json() #parse json
					#write date to column in row
					new_row = row.copy()
					item = 0
					#find the most recent security related
					is_security_related = False
					while item < len(json_list.get("items")) - 1:
						if(json_list.get("items")[item].get("abstract") != None):
							abstract = json_list.get("items")[item].get("abstract").get("text")[0].get("value")
							if(securityRelated(abstract) == True):
								is_security_related = True
								#print("found keyword in item " + str(item))
								break
						item += 1
					if is_security_related == True:
						#write its date
						publications = json_list.get("items")[item].get("publicationStatuses")
						publication_index = 0
						for publication in publications:
							if publication.get("current") == True:
								break;
							publication_index += 1
						date = json_list.get("items")[item].get("publicationStatuses")[publication_index].get("publicationDate")
						new_row[date_column] =  ""
						new_row[title_column] = ""
						if(date.get("year") != None and (row[date_column][0:4].isdigit() == False or int(date.get("year")) >= int(row[date_column][0:4]))):
							new_row[date_column] += str(date.get("year"))
							if(date.get("month") != None):
								new_row[date_column] += "-" + str(date.get("month"))
								if(date.get("day") != None):
									new_row[date_column] += "-" + str(date.get("day"))
						#write title to column in row
						research_name = json_list.get("items")[item].get("title").get("value")
						if(json_list.get("items")[item].get("subTitle")):
							research_subName = json_list.get("items")[item].get("subTitle").get("value")
						research_link = json_list.get("items")[item].get("info").get("portalUrl")
						#if we find the name of the research but not its link, just write the title
						if(research_name != None and research_link == None):
							new_row[title_column] = str(research_name)
							if(research_subName != None):
								new_row[title_column] += ': ' + str(research_subName)
						#if we find the link as well as the title then write title as hyperlink
						elif research_link != None:
							new_row[title_column] = "<a href= \"" + str(research_link) + "\">" + str(research_name)
							if(research_subName != None):
								new_row[title_column] += ': ' + str(research_subName)
							new_row[title_column] += "</a>"
						#if no column missing then update the row with the new one
						if(research_name != None and date.get("year") != None and new_row[date_column] != "" and new_row[title_column] != row[title_column]):
							csv_writer.writerow(new_row) #overwrite row with new one
							row_changed = True
							file_changed = True
			#if at the end we made no change copy row directly
			if row_changed == False:
				csv_writer.writerow(row)
	if file_changed == True:
		print("there is a change in " + csv_names[i])
		os.remove(csv_names[i])
		os.rename(csv_names_new[i], csv_names[i])
	else:
		print("there isn\'t any change in " + csv_names[i])
		os.remove(csv_names_new[i])
