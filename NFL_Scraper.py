# Importing our NFL library
import Nfl_lib as lib
# Creating a list of years
years = ["2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007"]
# updating the header before head
lib.update_header('nfl_offense.csv',"RK,PLAYER,POS,TEAM,COMP,ATT,PCT,YDS,YDS/A,LONG,TD,INT,SACK,RATE,YDS/G,YEAR")


# Looping for no. of years
for j in range(0,11) :
    value_count = 1
    # looping for the pages
    for i in range(0,3) :
	# As 2017 has only 2 pages skiping after 2
        if (i == 2 and years[j] == "2017"):
            break    
        lib.extract_data_from_web('nfl_offense.csv',['http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/'+years[j]+'/qualified/false/count/'+str(value_count)],['RK','PLAYER','TEAM','COMP','ATT','PCT','YDS','YDS/A','LONG','TD','INT','SACK','RATE','YDS/G'],"RK","</tr>",years[j],1,15)
       	# Incrementing the count for the pages
	value_count = value_count + 40

lib.update_header('nfl_defense.csv',"RK,PLAYER,POS,TEAM,AST,TOTAL,COMB,SACK,YDSL,PD,INT,YDS,LONG,TD,FF,REC,TD,YEAR")

for j in range(0,11) :
    value_count = 1
    for i in range(0,40) :
        if (i == 34 and years[j] == "2017"):
           break
        elif (i==37 and (years[j] in ["2007","2009","2011","2012","2014","2015","2016"])):
            break
        elif (i==38 and years[j]=="2013") :
            break
        elif (i==39 and years[j]=="2008") :
            break
        
        lib.extract_data_from_web('nfl_defense.csv',['http://www.espn.com/nfl/statistics/player/_/stat/defense/sort/totalTackles/year/'+years[j]+'/qualified/false/count/'+str(value_count)],['RK','PLAYER','TEAM','AST','TOTAL','COMB','SACK','YDSL','PD','INT','YDS','LONG','TD','FF','REC','TD','TACKLES','SACKS','INTERCEPTIONS','FUMBLES'],"RK","</tr>",years[j],0,17)
        value_count = value_count + 40
      





        
