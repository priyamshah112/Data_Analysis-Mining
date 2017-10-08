#ANALYSIS STEP-1 (To get user data and count them category wise in our database)
"""Problem Definition:To get a users personality based on number of app of particular category he uses.
   Abstract:The following code is analysis of a persons android app list ,the apps of user are category wise arranged and counted to get the users personality
            based on maximum apps being available on his app list.The study is resulted in a bar graph as well as pie chart for better supervision using matplotlib.
   Description:The csv module helps to read and operate functions on csv file of user data.The pandas library helps in using dataframes of users_data.csv
               to operate.Numpy library to operate numpy functions and matplotlib to  use graphs functions of library to plot user data analysed graphically.
   Future Scope: The further analysis accuracy would be based on users particular app usage time."""
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator
import os
import errno

#import re
user=1
count=[0] *14
class prj:

    
        
    #count=[0] *10 is global variable
    
    name=['Communication','GAMES','Productivity','SOCIAL','EDUCATION','Photography','VIDEO','DATING','ANDROID_WEAR','BOOKS','Travel','Online_Shopping','MUSIC','Launcher']
    #list of playstore categories being searched 
    
        
            
        
   
    def apps(s):
        #Android_Wear=((1,'Golf GPS & Scorecard-Hole19'),(2,'Cheap hotel deals'),(3,'Seven-7 Minute'),(4,'365Scores:Sports'),(5,'Kornoot-Cycling & Hiking Maps'),(6,'Runtastic Pro'),(7,'Onefootball-Football scores'),(8,'SofaScore Live Score'),(9,'StrongLifts 5x5'),(10,'Citymapper'),(11,'Fluenty'),(12,'Weather Live Free'),(13,'video call & chat ICQ'),(14,'Any.do:To-do list,Calendar,Reminders & Tasks'),(15,'Sleep as Android'),(16,'Android Wear-Smartwatch'),(17,'Water Drink'),(18,'Endomond o-Running & Walking'),(19,'Calculator'),(20,'Heart Rate Monitor & Tracker'),(21,'RunKeeper-GPS'),(22,'Calculator for Android Wear'),(23,'Google Fit-Fitness Tracking'),(24,'PixtoCam for Android Wear'),(25,'PaperCraft'))
        global count
        global user
        chk=1;
        if(chk):
            with open ('Communication.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    #line[0].lower()
                    if(line[0].lower() in s):
                            print(line[0])
                            #print(i) 
                            count[0]=count[0]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                            print(line[0])
                            #print(i) 
                            count[0]=count[0]+1
                            chk=0
                            break
                    elif(line[0] in s):
                            print(line[0])
                            #print(i) 
                            count[0]=count[0]+1
                            chk=0
                            break
                    
                        
                    
        if(chk):
            with open ('GAMES.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                            print(line[0])
                            #print(i) 
                            count[1]=count[1]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                            print(line[0])
                            #print(i) 
                            count[1]=count[1]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                            print(line[0])
                            #print(i) 
                            count[1]=count[1]+1
                            chk=0
                            break

        if(chk):
            with open ('Online_Shopping.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                            print(line[0])
                            #print(i) 
                            count[11]=count[11]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                            print(line[0])
                            #print(i) 
                            count[11]=count[11]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                            print(line[0])
                            #print(i) 
                            count[11]=count[11]+1
                            chk=0
                            break
        if(chk):
            with open ('Music.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                            print(line[0])
                            #print(i) 
                            count[12]=count[12]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                            print(line[0])
                            #print(i) 
                            count[12]=count[12]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                            print(line[0])
                            #print(i) 
                            count[12]=count[12]+1
                            chk=0
                            break

        if(chk):
             
             with open ('Productivity.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0])
                            count[2]=count[2]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                    
                            print(line[0])
                            count[2]=count[2]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                    
                            print(line[0])
                            count[2]=count[2]+1
                            chk=0
                            break
                    
        if(chk):
             with open ('SOCIAL.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                            print(line[0])
                            #print(i) 
                            count[3]=count[3]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                            print(line[0])
                            #print(i) 
                            count[3]=count[3]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                            print(line[0])
                            #print(i) 
                            count[3]=count[3]+1
                            chk=0
                            break
                        
        if(chk):
             with open ('EDUCATION.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0])
                            count[4]=count[4]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                    
                            print(line[0])
                            count[4]=count[4]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                    
                            print(line[0])
                            count[4]=count[4]+1
                            chk=0
                            break
        if(chk):
            with open ('Photography.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0])
                            count[5]=count[5]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                    
                            print(line[0])
                            count[5]=count[5]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                    
                            print(line[0])
                            count[5]=count[5]+1
                            chk=0
                            break
                    
        if(chk):
            with open ('VIDEO.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    
                
                    #for i in line:
                        
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                            print(line[0])
                            #print(i)
                            count[6]=count[6]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                            print(line[0])
                            #print(i)
                            count[6]=count[6]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                            print(line[0])
                            #print(i)
                            count[6]=count[6]+1
                            chk=0
                            break
                    
        if(chk):
            with open ('DATING.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0])
                            count[7]=count[7]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                    
                            print(line[0])
                            count[7]=count[7]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                    
                            print(line[0])
                            count[7]=count[7]+1
                            chk=0
                            break
        if(chk):
            with open ('ANDROID_WEAR.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0])
                            count[8]=count[8]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                    
                            print(line[0])
                            count[8]=count[8]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                    
                            print(line[0])
                            count[8]=count[8]+1
                            chk=0
                            break
                    
        if(chk):
            with open ('BOOKS.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0])
                            count[9]=count[9]+1
                            chk=0
                            break
                    
        if(chk):
            with open ('Travel.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0]) 
                            count[10]=count[10]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                    
                            print(line[0]) 
                            count[10]=count[10]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                    
                            print(line[0]) 
                            count[10]=count[10]+1
                            chk=0
                            break
        if(chk):
            with open ('Launcher.txt','r') as inf:
            
                for line in inf:
                    line=line.split("  ")
                    #for i in line:
                    
                #if  ('MX Playerver'.find(line) >=0) :
                    if(line[0] in s):
                    
                            print(line[0]) 
                            count[13]=count[13]+1
                            chk=0
                            break
                    elif(line[0].lower() in s):
                    
                            print(line[0]) 
                            count[13]=count[13]+1
                            chk=0
                            break
                    elif(line[0].upper() in s):
                    
                            print(line[0]) 
                            count[13]=count[13]+1
                            chk=0
                            break

    #s=input("Enter the app name : ")
    #apps(s)
        
   
    #count=[1,2,3,4,5,0,1,0,6,4]
    def analysis():
        global count
        global user
        with open("counter.txt",'r') as c:
            for line in c:
                user=int(line)
            print(user)
            
        k = "user"+str(user)
        print(k)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CODE FOR BAR GRAPH OF ANALYSIS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        frequencies = [count[0],count[1],count[2],count[3],count[4],count[5],count[6],count[7],count[8],count[9],count[10],count[11],count[12],count[13]]   # raw data

        freq_series = pd.Series.from_array(frequencies)   # in my original code I create a series and run on that, so for consistency I create a series from the list.

        x_labels=['Communication','GAMES','Productivity','SOCIAL','EDUCATION','Photography','VIDEO','DATING','ANDROID_WEAR','BOOKS','Travel','Online_Shopping','MUSIC','Launcher']
            

        plt.figure(figsize=(12, 8))
        ax = freq_series.plot(kind='bar')
        ax.set_title("ANALYSIS-1")
        ax.set_xlabel("CATEGORIES")
        ax.set_ylabel("NUMBER OF APPS USED")
        ax.set_xticklabels(x_labels)

        #rects = ax.patches
        """   def xrange(x):
                    return iter(range(x))
        # Now make some labels
            labels = ["label%d" % i for i in xrange(len(rects))]

            for rect, label in zip(rects, labels):
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')
            
        """
        plt.savefig('C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user/'+k+'_bar'+'.png')
        plt.show()
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CODE FOR PIE-CHART OF ANALYSIS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
        #ax1,fig1 = plt.subplots()

        frequencies = [count[0],count[1],count[2],count[3],count[4],count[5],count[6],count[7],count[8],count[9],count[10],count[11],count[12],count[13]]   # bring some raw data
        sorted_frequencies=sorted(count,reverse=True)
        x_labels=['Communication','GAMES','Productivity','SOCIAL','EDUCATION','Photography','VIDEO','DATING','ANDROID_WEAR','BOOKS','Travel','Online_Shopping','MUSIC','Launcher']
        #colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        #slices = [1,2,3] * 4 + [20, 25, 30] * 2
        #cmap = plt.cm.prism
        #colors = cmap(np.linspace(0., 1., len(slices)))
        explode = list()
        for d in x_labels:
            explode.append(0.1)
        pie=plt.pie(sorted_frequencies, labels=None,explode=explode,autopct='%1.1f%%',shadow=True, startangle=90)
        #axes[0].set_title('Analysis 1');
        plt.title('Analysis 1', weight='bold', size=14)
        plt.legend(pie[0], x_labels, loc="best")
        plt.axis('equal')
        plt.savefig('C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user/'+k+'_pie'+'.png')
        plt.show()
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Result of Analysis~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            
            
        max_value = max(frequencies)
        max_index = frequencies.index(max_value)
        min_value = min(frequencies)
        min_index = frequencies.index(min_value)
        total=sum(frequencies)
        print("The user has a MAX usage of: "+str(x_labels[max_index])+" Category"+"\nOut of Total: "+str(total)+" Apps"+"\n"+"The percentage of that category app in overall users app list is "+str((max(frequencies)/total)*100))
        print("The user has a MIN usage of: "+str(x_labels[min_index])+" Category"+"\n"+"The percentage of that category app in overall users app list is "+str((min(frequencies)/total)*100))

        """Category_dict = {}
        for i in range(len(frequencies)):
            Category_dict[frequencies[i]] = x_labels[i]

        #print("Category \n")
        #for i in range(14):
         #   print(str(i)+"] "+x_labels[i]+"\n")
        sorted_d = sorted(Category_dict.items(), key=operator.itemgetter(0))#reverse=True for descending order
        print("[Category : Number Of App] \n")
        print(sorted_d)"""
        #sorted_count=sorted(count,reverse=True)


        a=pd.read_csv('C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user_data.csv')
        #print(a.head(7))
        print(a.loc[0+8*user:6+8*user,:])#loc[0+8*user:6+8*user,:]
        c=a.loc[0:6,:]
        b=a.loc[1,'Unnamed: 1']
        #print(b)
        name=['Communication','GAMES','Productivity','SOCIAL','EDUCATION','Photography','VIDEO','DATING','ANDROID_WEAR','BOOKS','Travel','Online_Shopping','MUSIC','Launcher']
            #fileName  = x+".txt"
        if(frequencies[0]/100==0):
            print(" \n Introvert  \n");
        elif(frequencies[0]/100<=0.5):
            print(" \n Thought Spreader \n");
        else:
            print(" \n Have lot of free time \n");
        if(frequencies[1]/100==0):
            print(" \n Focussed Person \n");
        elif(frequencies[1]/100<=0.5):
            print(" \n Lazy  \n");
        else:
            print(" \n Gamer \n");
        if(frequencies[2]/100==0):
            print(" \n Productivity:0% \n");
        elif(frequencies[2]/100<=0.5):
            print(" \n Productivity:50% \n");
        else:
            print(" \n Productivity:100% \n");
        if(frequencies[3]/100==0):
            print(" \n Social:0% \n");
        elif(frequencies[3]/100<=0.5):
            print(" \n Social:50% \n");
        else:
            print(" \n Social:100% \n");
        if(frequencies[4]/100==0):
            print(" \n Learning:0% \n");
        elif(frequencies[4]/100<=0.5):
            print(" \n Learning:50% \n");
        else:
            print(" \n Learning:100% \n");
        if(frequencies[5]/100==0):
            print(" \n Photography:0% \n");
        elif(frequencies[5]/100<=0.5):
            print(" \n Photography:50% \n");
        else:
            print(" \n Photography:100% \n");
        if(frequencies[6]/100==0):
            print(" \n Video:0% \n");
        elif(frequencies[6]/100<=0.5):
            print(" \n Video:50% \n");
        else:
            print(" \n Video:100% \n");
        if(frequencies[7]/100==0):
            print(" \n Dating:0% \n");
        elif(frequencies[7]/100<=0.5):
            print(" \n Dating:50% \n");
        else:
            print(" \n Dating:100% \n");
        if(frequencies[8]/100==0):
            print(" \n Android_Wear:0% \n");
        elif(frequencies[8]/100<=0.5):
            print(" \n Android_Wear:50% \n");
        else:
            print(" \n Android_Wear:100% \n");
        if(frequencies[9]/100==0):
            print(" \n Books:0% \n");
        elif(frequencies[9]/100<=0.5):
            print(" \n Books:50% \n");
        else:
            print(" \n Books:100% \n");
        if(frequencies[10]/100==0):
            print(" \n Travel:0% \n");
        elif(frequencies[10]/100<=0.5):
            print(" \n Travel:50% \n");
        else:
            print(" \n Travel:100% \n");
        if(frequencies[11]/100==0):
            print(" \n Online_Shopping:0% \n");
        elif(frequencies[11]/100<=0.5):
            print(" \n Online_Shopping:50% \n");
        else:
            print(" \n Online_Shopping:100% \n");
        if(frequencies[12]/100==0):
            print(" \n Music:0% \n");
        elif(frequencies[12]/100<=0.5):
            print(" \n Music:50% \n");
        else:
            print(" \n Music:100% \n");
        if(frequencies[13]/100==0):
            print(" \n Launcher:0% \n");
        elif(frequencies[13]/100<=0.5):
            print(" \n Launcher:50% \n");
        else:
            print(" \n Launcher:100% \n");
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Directory~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        filename = "C:/PROJECT/user.txt"
        if not os.path.exists(os.path.dirname("C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user/"+k+".txt")):
            try:
                os.makedirs(os.path.dirname("C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user/"+k+".txt"))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~writing result in file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
        with open("C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user/"+k+".txt",'w') as t:
                content = t.write( " The user has a MAX usage of: %s Category \nThe user has a MIN usage of:%s Category \n Total_Apps_installed - %d \n ~User Details: \n  \n  %s \n \n \t \t\t\t ~Apps Installed~ \n  %s \nlist_of_category_wise_data(Number of App,Category)  - \n"  % (str(x_labels[max_index]),str(x_labels[min_index]),total,c,b))
                 
                for i in range (14):
                     m=t.write(" %s : %d "%(name[i],count[i]))
        t.close()
        #print("Number of App based on category used by user ",frequencies)
   
        
        
    row_count = sum(1 for row in csv.reader( open('C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user_data.csv')))
    a=pd.read_csv("C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user_data.csv")
    with open("C:/Python 3.6/DATA ANALYSIS/DASUT/DASUT-Analytics-master/user_data.csv") as fd:
            
        reader = csv.reader(fd)
        
        #print(row_count)
        for z in range(0,row_count//8):
            
            me=a.loc[1+8*z,'Unnamed: 1']
        
            #print(me)
            with open ('inputfromuser.txt','w') as inf:
                inf.write(str(me))
            with open ('inputfromuser.txt','r') as inf:
            
                for line in inf:
                    nm=line.split("\n")
                    print(nm[0])
            
                    apps(str(nm[0]))
            for i in range (14):
                print(name[i]," : ",count[i])
            
            user=user+1
            os.remove("counter.txt")
            with open("counter.txt",'w') as c:
                c.write("%d"%(user))
            print(user)
            analysis()
            
    #~~~~~~~~~~~~~~~~~~~~Personality calculation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
prj;

