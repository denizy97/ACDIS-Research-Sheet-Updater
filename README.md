# ACDIS-Research-Sheet-Updater

This is a program that updates the already existing csv files that contain information about security related researchers and their papers.
It uses the API of Elsevier Pure at https://experts.illinois.edu/ws/ which powers Illinois Experts. It grabs the researches of every
researcher that already exists on the spreadsheet and updates their most recent security related paper with a simple keyword search. The
whole program was written in a day so don't expect it to work perfectly.

Written in 2019 by Deniz YILDIRIM <denizy@protonmail.com>

I wrote this while working for ACDIS in Illinois. I received approval from ACDIS to make this open source BUT this program is PROBABLY still owned by the University of Illinois. Consult UofI before changing, distributing, sharing etc. just in case.  
See https://www.bot.uillinois.edu/governance/general_rules for more information.  
As far as I'm concerned you can do whatever you want with it but like I said I am probably not the legal owner of this program.  
Especially don't share the spreadsheets without asking the university as the data is from experts.illinois.edu which is probably licensed

## Procedure If You Work At ACDIS UIUC:

#### To simply update each research with that researcher's latest security related research:

0. *If there are no csv files in the "research sheet updater" folder copy the latest ones under the originals folder and paste them in "research sheet updater"*
1. Open terminal, type "python research_sheet_updater.py" and press enter, enter the API key and press enter again.
(the key is in the file named "the key", otherwise contact experts-help@illinois.edu to get a new one, more info on publish.illinois.edu/researchconnections/?page_id=67)
2- Login to ACDIS and go to the WordPress page
3. On the right menu, under TablePress, click Import a Table
4. Click browse and choose one of the csv files in this "research sheet updater" folder
5. Click on "Replace existing table" and find the table with the same or similar name to the one you are uploading, select it.
6. Press Import
7. Go back to step 3 and repeat until every file is uploaded and replaced
8. If you are paranoid (which you probably should be because our keywords list sucks) you should double check and make sure that every research is security related
9. COPY the latest generated and updated files under the originals file in a folder named after the current month and year

#### To add a new researcher:

1. Simply open the related file, add the person and the information to a new row
2. That is it, the program will now search for that person's latest security related publication automatically. Please store the files in the originals folder

#### What to do if there is a research you want to add to the list but the program isn't finding it:

1. Go to the experts.illinois.edu page of that research and read its abstract
2. Find word(s) that make this paper security related. THINK THIS CAREFULLY IF YOU ADD A VAGUE KEYWORD NON-SECURITY RELATED PAPERS WILL ALSO BE FOUND
3. Open the keywords file under the keywords folder
4. Add the keyword both with a small and capital first letter, if it is multiple words think if they could be written with a "-" instead etc.

Good Luck :)

## Todo:

* Use Fingerprints and Concepts instead of keywords. Each article has a Fingerprint which is a set of Concepts with weights. Each new article will have a new fingerprint probably so you have to go through every article in the database, check their fingerprints and choose those whose fingerprints have security related concepts with high weights.
* Make it a list of all security related articles and add a choice to only keep a number of most recent ones, or articles published after a given date
* Find a way to update the list on the website automatically (RSS Feeds?)
* If you find a way to update the website automatically then find a way to make it run automatically every month or week.
