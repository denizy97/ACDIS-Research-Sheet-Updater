# ACDIS-Research-Sheet-Updater
PROCEDURE:

To simply update each research with that researcher's latest security related research:

(0-) If there are no csv files in the "research sheet updater" folder copy the latest ones under the originals folder and paste them in "research sheet updater"
1- Open terminal, type "python research_sheet_updater.py" and press enter, enter the API key and press enter again.
(the key is in the file named "the key", otherwise contact experts-help@illinois.edu to get a new one, more info on publish.illinois.edu/researchconnections/?page_id=67)
2- Login to ACDIS and go to the WordPress page
3- On the right menu, under TablePress, click Import a Table
4- Click browse and choose one of the csv files in this "research sheet updater" folder
5- Click on "Replace existing table" and find the table with the same or similar name to the one you are uploading, select it.
6- Press Import
7- Go back to step 3 and repeat until every file is uploaded and replaced
8- If you are paranoid (which you probably should be because our keywords list sucks) you should double check and make sure that every research is security related
9- COPY the latest generated and updated files under the originals file in a folder named after the current month and year

To add a new researcher:

1- Simply open the related file, add the person and the information to a new row
2- That is it, the program will now search for that person's latest security related publication automatically. Please store the files in the originals folder

What to do if there is a research you want to add to the list but the program isn't finding it:

1- Go to the experts.illinois.edu page of that research and read its abstract
2- Find word(s) that make this paper security related. THINK THIS CAREFULLY IF YOU ADD A VAGUE KEYWORD NON-SECURITY RELATED PAPERS WILL ALSO BE FOUND
3- Open the keywords file under the keywords folder
4- Add the keyword both with a small and capital first letter, if it is multiple words think if they could be written with a "-" instead etc.


Good Luck :)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


COPYRIGHT:

Copyright © 2000 Deniz Yıldırım <denizy@protonmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.

WARRANTY:

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details. */

LICENCE:

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

