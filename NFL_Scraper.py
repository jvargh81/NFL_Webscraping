import Nfl_lib as lib

url_offense = ['http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2017/seasontype/2',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2016/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2016/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2016/qualified/false/count/81'
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2015/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2015/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2015/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2014/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2014/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2014/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2013/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2013/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2013/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2012/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2012/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2012/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2011/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2011/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2011/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2010/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2010/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2010/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2009/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2009/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2009/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2008/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2008/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2008/qualified/false/count/81',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2007/qualified/false',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2007/qualified/false/count/41',\
       'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/year/2007/qualified/false/count/81']


year = ["2017","2017","2016","2016","2016","2015","2015","2015","2014","2014","2014","2013","2013","2013","2012","2012","2012","2011","2011","2011","2010","2010","2010","2009","2009","2009","2008","2008","2008","2007","2007","2007"]

lib.update_header('nfl_offense.csv',"RK,PLAYER,POS,TEAM,COMP,ATT,PCT,YDS,YDS/A,LONG,TD,INT,SACK,RATE,YDS/G,YEAR")
lib.extract_data_from_web('nfl_offense.csv',url_offense,['RK','PLAYER','TEAM','COMP','ATT','PCT','YDS','YDS/A','LONG','TD','INT','SACK','RATE','YDS/G'],"RK","</tr>",year,1,15)


lib.update_header('nfl_defense.csv',"RK,PLAYER,POS,TEAM,AST,TOTAL,COMB,SACK,YDSL,PD,INT,YDS,LONG,TD,FF,REC,TD,YEAR")
j = 0
value_count = 1
years = ["2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007"]


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
      





        
