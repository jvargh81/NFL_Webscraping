# Importing Libraries/Packages
import requests
import scrape
import convert_to_list

# Adds the header in the file
def update_header(file_name,header):

    # Writing the header into the file
    csv_file = open(file_name,'a')
    csv_file.write(header)
    csv_file.write("\n")
    csv_file.close()


# Extracts and stores the scraped data from the web into the file.
def extract_data_from_web(file_name,url,header,scrape_start,scrape_end,year,check,value) :
    
	# gets the url and extracts it data drom the web

        page_text = requests.get(url)
	# Initialising variables
        count = 0
        inside = 1
        nfl_data = ""
	# opening the csv file
        csv_file = open(file_name,'a')
        csv_file.write("\n")
        csv_file.close()
        with open(file_name,'a') as csv_file :

            # Extracting data from web        
            page = scrape.extract_Player_Data_Only(page_text.text,scrape_start,scrape_end)
            # cleaning the data
            page = page.replace(",,",",")
            page = page.replace(",,",",")
            page = page.replace(",,",",")
            page = page.strip()
            
            
            # spliting the data to arrange in required format
            nfl = page.split(',')
            count = 0
            for data in range(len(nfl)) :
		# check required only for ofense, to get prper data
                if (check) :
                    if (count == 7) and (nfl[data] in ['1','2','3','4','5','6','7','8','9']):
                            csv_file.write(nfl[data])                    
                            continue
                    
                if (not (nfl[data] in header)) :
		    # in case of NAs we get a unwanted char, so skiping it.
                    if not (nfl[data] == "&nbsp;") :
                        csv_file.write(nfl[data] + ",")
                        count = count + 1
                    else :
                        if (check) :
                           csv_file.write(year) 
                        if(count != 0):
                            csv_file.write("\n")
                        csv_file.write("NA"+ ",")
                        if (check) :
                            count = 0
                        else :
                            count = 1
                # entering new line.    
                if (count == value) :
                         csv_file.write(year + "\n")  
                         count = 0
	# Closing the File
        csv_file.close()                 

