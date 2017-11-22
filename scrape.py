
def extract_Player_Data_Only(pagetext,scrape1,scrape2):

    start = pagetext.find(scrape1)
    end = pagetext.rfind(scrape2)
    pagetext = pagetext[start:end]
   
    #   strip html markup between beg and end
    inside = 0
    text = '' 
    for char in pagetext:
 
        if char == '<':
            inside = 1          
        elif (inside == 1 and char == '>'):
            inside = 0
            text += ','
        elif inside == 1:
            continue
        else:
            text += char
     
    return text