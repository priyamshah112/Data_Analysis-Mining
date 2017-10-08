import csv
with open("C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user_data.csv") as fd:
  reader = csv.reader(fd)
  me=[row for idx,row in enumerate(reader) if idx is (2)]
  
  
print(me)

    
def main():
    v=0
    s=input("Enter the video app name for now-YouTube  VLC for Android  MX Player ")
    apps(s,v)


def apps(s,v):
    #Android_Wear=((1,'Golf GPS & Scorecard-Hole19'),(2,'Cheap hotel deals'),(3,'Seven-7 Minute'),(4,'365Scores:Sports'),(5,'Kornoot-Cycling & Hiking Maps'),(6,'Runtastic Pro'),(7,'Onefootball-Football scores'),(8,'SofaScore Live Score'),(9,'StrongLifts 5x5'),(10,'Citymapper'),(11,'Fluenty'),(12,'Weather Live Free'),(13,'video call & chat ICQ'),(14,'Any.do:To-do list,Calendar,Reminders & Tasks'),(15,'Sleep as Android'),(16,'Android Wear-Smartwatch'),(17,'Water Drink'),(18,'Endomond o-Running & Walking'),(19,'Calculator'),(20,'Heart Rate Monitor & Tracker'),(21,'RunKeeper-GPS'),(22,'Calculator for Android Wear'),(23,'Google Fit-Fitness Tracking'),(24,'PixtoCam for Android Wear'),(25,'PaperCraft'))
    chk=1;
    if(chk):
        with open ('Communication.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
                
    if(chk):
        with open ('GAMES.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break

    if(chk):
         
         with open ('Productivity.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
                
    if(chk):
         with open ('SOCIAL.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
                    
    if(chk):
         with open ('EDUCATION.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
    if(chk):
        with open ('Photography.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
                
    if(chk):
        with open ('VIDEO.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                
            
                for i in line:
                    
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in s):
                        print("Word ",i)
                
                        v=v+1
                        chk=0
                        break
                
    if(chk):
        with open ('DATING.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
    if(chk):
        with open ('ANDROID_WEAR.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
                
    if(chk):
        with open ('BOOKS.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break
                
    if(chk):
        with open ('Travel.txt','r') as inf:
        
            for line in inf:
                line=line.split("  ")
                for i in line:
                
            #if  ('MX Playerver'.find(line) >=0) :
                    if(i in 'MX Playerver6.0'):
                
                        print("F")
                        chk=0
                        break

    print("Video: ",v);          

main();

