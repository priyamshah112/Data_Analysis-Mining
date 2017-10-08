
import sqlite3 as a
import sys #system
Android_Wear=((1,'Golf GPS & Scorecard-Hole19'),(2,'Cheap hotel deals'),(3,'Seven-7 Minute'),(4,'365Scores:Sports'),(5,'Kornoot-Cycling & Hiking Maps'),(6,'Runtastic Pro'),(7,'Onefootball-Football scores'),(8,'SofaScore Live Score'),(9,'StrongLifts 5x5'),(10,'Citymapper'),(11,'Fluenty'),(12,'Weather Live Free'),(13,'video call & chat ICQ'),(14,'Any.do:To-do list,Calendar,Reminders & Tasks'),(15,'Sleep as Android'),(16,'Android Wear-Smartwatch'),(17,'Water Drink'),(18,'Endomond o-Running & Walking'),(19,'Calculator'),(20,'Heart Rate Monitor & Tracker'),(21,'RunKeeper-GPS'),(22,'Calculator for Android Wear'),(23,'Google Fit-Fitness Tracking'),(24,'PixtoCam for Android Wear'),(25,'PaperCraft'))
Education=((1,'TED'),(2,'Pictoword:Word'),(3,"BYJU'S-The Learning App"),(4,'Elevate-Brain Training Games'),(5,'Lumosity-Brain Training'),(6,'Paheli'),(7,'Coursera:Online'),(8,'Khan Academy'),(9,'Udemy Online'),(10,'Fit Brains Trainer'),(11,'EdX-Online'),(12,'KOGNITIVO-Brain Training'),(13,'ABC For Kids - Education App'),(14,'Math Challenge'),(15,'Math Tricks'),(16,'Brain it On! - Physics'),(17,'4 Pics 1 Word'),(18,'Memory Gaames:Brain Training'),(19,'Grammar Practice'),(20,'Complete Biology'),(21,'How to Draw Tattos'),(22,'myHomework'),(23,'Next Gen Science'),(24,'SMTT TOEFL Speaking'),(25,"Teacher's Gradebook"),(26,'Meritnation-CBSE'),(27,'Pocket Mathematics'),(28,'Google Classroom'),(29,'Virtual Teacher'),(30,'MBA Skool'),(31,'CamScanner-Phone PDF Creator'),(32,'Google Slides'),(33,'English Grammar'),(34,'Daily GK & Online Test SSC IAS PSC IBPS Govt Exams'),(35,'Bank Exam'),(36,'English Synonym'),(37,'Exam Prep(Eng/Hindi) SSC CGL,IBPS,Bank PO,GATE'),(38,'IELTS Vocabularies-ILVOC'),(39,'GMAT Math'),(40,'SAT Test'),(41,'Painless GRE'),(42,'GRE Vocabulary Expert'),(43,'Law-CLAT Exam Guide'),(44,'GRE Tests'),(45,'HashLearn JEE Main,NEET,CBSE,BITSAT Preparation'),(46,'ACT Test'),(47,'Pocket Verbal'),(48,'GRE Prep & Practice by Magoosh'),(49,'play2prep:ACT,SAT prep'),(50,'Ready4 SAT(Prep4SAT)'),(51,'OCAS'))
Programming=((1,'C++ Programming'),(2,'C Programming'),(3,'Learn Java'),(4,'100+ Java'),(5,'Learn C++'),(6,'Programming Hub,Learn to code'),(7,'Learn HTML'),(8,'Learn PHP'),(9,'Learn SQL'),(10,'LearnC# .NET'),(11,'C++ Tutorials'),(12,'SoloLearn:Learn to Code for Free'),(13,'Learn JavaScript'),(14,'Learn CSS'),(15,'CppDroid-C/C++ IDE'),(16,'Udacity Lifelong Learning'),(17,'GeeksforGeeks'),(18,'Hacked'),(19,"Programmer's Dictionary"),(20,'Code Monk'),(21,'Dcoder,Mobile Compiler IDE:Now code on Mobile'),(22,'Object Oriented Programming'))
Social=((1,'Waplog Chat & Free Dating'),(2,'Walkie:Talk to Strangers,Chat'),(3,'Instagram'),(4,'Facebook'),(5,'Twitter'),(6,'Snapchat'),(7,'LINE:Free Calls & Messages'),(8,'WeChat'),(9,'Telegram'),(10,'hike messenger'),(11,'LinkedIn'),(12,'Pinterest'),(14,'Tumblr'),(15,'Whatsapp'),(16,'Facebook Lite'),(17,'Google+'),(18,'Kik'),(19,'Hike'),(20,'Messenger'),(21,'Skype-free IM & video calls'),(22,'Reddit'))
Dating=((1,'Waplog Chat & Free Dating'),(2,'Walkie:Talk to Strangers,Chat'),(3,'Tonight-chat,meet,dating apps'),(4,'Perfect Hookup App-Adult Dating for Meetup & NSA'),(5,'JAUMO Flirt Chat & Dating'),(6,'happn-Local dating app'),(7,'Tinder-Match.Chat.Meet.'),(8,'Badoo-Free Chat&Dating App'),(9,'OkCupid Dating'),(10,'TryDate-Free Online Dating App'),(11,'TrulyMadly'),(12,'SayHi Chat,Love,Meet,Dating'))
Games=((1,'Adventures of Mana'),
(2,'After Burner Climax'),
(3,'Alpha Betty Saga'),
(4,'Angry Birds'),
(5,'Angry Birds 2 [a]'),
(6,'Angry Birds Epic'),
(7,'Angry Birds Friends'),
(8,'Angry Birds Go!'),
(9,'Angry Birds Rio'),
(10,'Angry Birds Seasons'),
(11,'Angry Birds Space'),
(12,'Angry Birds Star Wars'),
(13,'Angry Birds Star Wars II'),
(14,'Angry Birds Stella'),
(15,'Angry Birds Transformers'),
(16,'Apollo Justice: Ace Attorney'),
(17,'Art of Conquest'),
(18,'Asphalt 8: Airborne'),
(19,'Asphalt Xtreme'),
(20,'Backbreaker'),
(21,'Blitz Brigade'),
(22,'Blossom Blast Saga'),
(23,'Boom Beach'),
(24,'Bubble Witch 2 Saga'),
 (25,'Bubble Witch 3 Saga'),
(26,'Bubble Witch Saga'),
(27,'Call of Duty: Heroes'),
(28,'Camp Pokémon'),
(29,'Candy Crush Jelly Saga'),
(30,'Candy Crush Saga'),
(31,'Candy Crush Soda Saga'),
(32,'Chaos Rings III'),
(33,'Clash of Clans'),
(34,'Clash Royale'),
(35,'Clumsy Ninja'),
(36,'Crusaders of Light'),
(37,'CSR Classics'),
(38,'CSR Racing'),
(39,'CSR Racing 2'),
(40,'Dead Trigger'),
(41,'Dead Trigger 2'),
(42,'Diamond Digger Saga'),
(43,'Dragon Quest VIII'),
(44,'Dungeon Hunter 5'),
(45,'Earn to Die 2'),
(46,'Emily Wants to Play'),
(47,'Farm Heroes Saga'),
(48,'Farm Heroes Super Saga'),
(49,'FIFA 10'),
(50,'FIFA 11'),
(51,'FIFA 12'),
(52,'FIFA 13'),
(53,'FIFA 14 Mobile'),
(54,'FIFA 15'),
(55,'FIFA 16'),
(56,'FIFA Mobile'),
(57,'Final Fantasy Grandmasters'),
(58,'Final Fantasy IX'),
(59,'Final Fantasy Tactics: The War of the Lions'),
(60,'Final Fantasy XV: A New Empire'),
(61,'Final Fantasy: Brave Exvius'),
(62,'Fire Emblem Heroes'),
(63,'Futurama: Worlds of Tomorrow'),
(64,'Gangstar Vegas'),
(65,'Grand Theft Auto III'),
(66,'Grand Theft Auto: San Andreas'),
(67,'Grand Theft Auto: Vice City'),
(68,'Hearthstone'),
(69,'Hit It Rich!'),
(70,'Hitman Go'),
(71,'Hitman: Sniper'),
(72,'Horizon Chase'),
(73,'Injustice 2'),
(74,'Injustice: Gods Among Us'),
(75,'Just Dance Now'),
(76,'Lara Croft Go'),
(77,'Lara Croft: Relic Run'),
(78,"Layton's Mystery Journey"),
(79,'Lego Batman 3: Beyond Gotham'),
(80,'Logres: Japanese RPG'),
(81,'Marvel: Contest of Champions'),
(82,'Marvel: Future Fight'),
(83,'Mega Man Mobile'),
(84,'Mega Man Mobile 2'),
(85,'Mega Man Mobile 3'),
(86,'Mega Man Mobile 4'),
(87,'Mega Man Mobile 5'),
(88,'Mega Man Mobile 6'),
(89,'Miitomo'),
(90,'Mobius Final Fantasy'),
(91,'Modern Combat 5: Blackout'),
(92,'Modern Combat Versus'),
(93,'Monster Hunter Explore'),
(94,'Monster Strike'),
(95,'Nortal Kombat X'),
(96,'N.O.V.A. 3'),
(97,'Need for Speed: No Limits'),
(98,'Nintendo Switch Online'),
(99,'One Piece Treasure Cruise'),
(100,'Open Sorcery'),
(101,'Order & Chaos 2: Redemption'),
(102,'Order & Chaos Online'),
(103,'Oz: Broken Kingdom'),
(104,'Papa Pear Saga'),
(105,'Paradise Bay'),
(106,'Pepper Panic Saga'),
(107,'Pet Rescue Saga'),
(108,'Phantasy Star Online 2es'),
(109,'Pictoword'),
(110,'Pocket Master'),
(111,'Pokémon Duel'),
(112,'Pokémon Go'),
(113,'Pokémon Photo Booth'),
(114,'Pokémon Shuffle'),
(115,'Pokémon TV'),
(116,'Pokémon: Magikarp Jump'),
(117,'Power Rangers: Legacy Wars'),
(118,'Pyramid Solitaire Saga'),
(119,'Real Racing 2'),
(120,'Real Racing 3'),
(121,'Scrubby Dubby Saga'),
(122,'Shadowgun'),
(123,'Shuffle Cats'),
(124,'Space Marshals'),
(125,'Star Wars: Commander'),
(126,'Star Wars: Galaxy of Heroes'),
(127,'Star Wars: Uprising'),
(128,'Super Mario Run'),
(129,'Super Meat Boy'),
(130,'Sword Art Online Code Resister'),
(131,'Sword Art Online: Memory Defrag'),
(132,'Terminator Genisys: Future War'),
(133,'Terraria'),
(134,'Tetris'),
(135,'Tetris Blitz'),
(136,'The Cave'),
(137,'The Simpsons: Tapped Out'),
(138,'The Sims FreePlay'),
(139,	'Tiny Troopers'),
(140,'Unkilled'),
(141,'Untitled Animal Crossing game'),
(142,'Vainglory'),
(143,'Vikings: War of Clans'),
(144,'Voez'),
(145,'Yo-kai Watch: Wibble Wobble'),
(146,'YouTube Gaming'),
(147,'Yu-Gi-Oh! Duel Links'),
(148,'Google Play Games')	
	
)
Music=((1,'Google Play Music'),(2,'Gaana:Bollywood Music & Radio'),(3,'Saavn Music & Radio'),(4,'Wynk Music:MP3 & Hindi songs'),(5,'Music Player'))
Media_Video=((1,'YouTube'),(2,'VLC for Android'),(3,'MX Player'),(4,'Retrica'),(5,'VivaVideo:Free Video Editor'),(6,'321 Media Player'),(7,'Media Clip Video Downloader'),(8,'Music Video Editor'),(9,'Social Media Video Downloader'),(10,'MAX Player - HD Video Player'),(11,'Google Play Movies & TV')
)
Communication=((1,'Gmail'),(2,'WhatsApp Messenger'),(3,'FB Messenger'),(4,'Google Hangouts'),(5,'Google Chrome'),(6,'Samsung Push Service'),(7,'imo free calls and chat'),(8,'Truecaller:CallerID & Dialer'),(9,'UC Browser:Fast download Private & Secure'),(10,'Google Duo'),(11,'Google Allo'),(12,'Opera Mini-fast web browser') )
Books_Reference=((1,'Google Play Books'),(2,'Oxford Dictionary of English Free'),(3,'English Hindi Dictionary'),(4,'Amazon Kindle'),(5,'Solved 15 Years Jee main paper'),(6,'JEE MAINs,AIEEE & JEE Advance'),(7,'Toppr-JEE Main,NEET,CBSE'),(8,'PrepLane-IIT JEE,NEET/AIPMT'),(9,'infinite IIT JEE'),(10,'ALLEN Test My Prep'))
News=((1,'Google Play Newsstand'),(2,'UC News-Latest News,Live Cricket Scores,Videos'),(3,'NewsDog-India News,Local News,Hindi News'),(3,'Dailyhunt(Newshunt)News'),(4,'AajTak'),(5,'ABP LIVE News'),(6,'JioExpressNews-Live India News'),(7,'NDTV News-India'))
Photography=((1,'Google Photos'),(2,'PicsArt Photo Studio:Collage Maker & Pic Editor'),(3,'B612-Selfegenic Camera'),(4,'Slow motion camera and video'),(5,'Photo Editor Pro'),(6,'Photo Editor:Effects&Filters'),(7,'Holo-Holograms for Videos in Augmented Reality'),(8,'PicMix-Photos in Collages'),(9,'Prisma'),(9,'Pixlr-Free Photo Editor'),(10,'Candy Camera-Selfie,beauty camera,photo editor'))
Productivity=((1,'Google Drive'),(2,'Google Slides'),(3,'Google Sheets'),(4,'OneNote'),(5,'Evernote'),(6,'Google Calendar'),(7,'Google PDF Viewer'),(8,'Microsoft Word'),(9,'Microsoft Office Mobile'),(10,'HP ePrint Enterprise Service'),(11,'Microsoft OneDrive'),(12,'Adobe Reader'),(13,'ES file Explorer File Manager'),(14,'HTC File Manager'),(15,'File Manager HD(File Transfer)'))
Travel=((1,'Google Maps'),(2,'MakeMyTrip-Flights Hotels Cabs'),(3,'trivago-Hotels & Travel'),(4,'redBus-Bus and Hotel Booking'),(5,'TripAdvisor Hotels Restaurant'),(7,'Cleartrip-Flights,Hotels,Activities,Dineout'),(8,'Yatra-Flights Hotels Bus IRCTC/Trains & Ola/Uber'),(9,'Ola Cabs'),(9,'Uber'),(10,'Meru Cabs'),(11,'ZoomCar'),(12,'ZipCar'))



con = a.connect('PLAYSTORE.db')
with  con:
   cur = con.cursor()
   cur.execute("DROP TABLE ANDROID_WEAR")
   cur.execute("CREATE TABLE ANDROID_WEAR (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO ANDROID_WEAR VALUES(?,?)",Android_Wear)

   

   
   cur.execute("SELECT * FROM ANDROID_WEAR")
   ROW =cur.fetchall()
   for row in ROW:
      print("ANDROID_WEAR")
      print(row)

   cur.execute("DROP TABLE EDUCATION")
   cur.execute("CREATE TABLE EDUCATION (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO EDUCATION VALUES(?,?)",Education)
   cur.execute("SELECT * FROM EDUCATION")
   ROW =cur.fetchall()
   for row in ROW:
      print("EDUCATION")
      print(row)
   cur.execute("DROP TABLE PROGRAMMING")
   cur.execute("CREATE TABLE PROGRAMMING (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO PROGRAMMING VALUES(?,?)",Programming)
   cur.execute("SELECT * FROM PROGRAMMING")
   ROW =cur.fetchall()
   for row in ROW:
      print("PROGRAMMING")
      print(row)
   cur.execute("DROP TABLE SOCIAL")
   cur.execute("CREATE TABLE SOCIAL (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO SOCIAL VALUES(?,?)",Social)
   cur.execute("SELECT * FROM SOCIAL")
   ROW =cur.fetchall()
   for row in ROW:
      print("SOCIAL")
      print(row)
   cur.execute("DROP TABLE DATING")    
   cur.execute("CREATE TABLE DATING (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO DATING VALUES(?,?)",Dating)
   cur.execute("SELECT * FROM DATING")
   ROW =cur.fetchall()
   for row in ROW:
      print("DATING")
      print(row)
   cur.execute("DROP TABLE GAMES")
   cur.execute("CREATE TABLE GAMES (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO GAMES VALUES(?,?)",Games)
   cur.execute("SELECT * FROM GAMES")
   ROW =cur.fetchall()
   for row in ROW:
      print("GAMES")
      print(row)
  # cur.execute("DROP TABLE MUSIC")
   cur.execute("CREATE TABLE MUSIC (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO MUSIC VALUES(?,?)",Music)
   cur.execute("SELECT * FROM MUSIC")
   ROW =cur.fetchall()
   for row in ROW:
      print("MUSIC")
      print(row)
 #  cur.execute("DROP TABLE VIDEO")
   cur.execute("CREATE TABLE VIDEO (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO VIDEO VALUES(?,?)",Media_Video)
   cur.execute("SELECT * FROM VIDEO")
   ROW =cur.fetchall()
   for row in ROW:
      print("VIDEO")
      print(row)
  # cur.execute("DROP TABLE Communication")
   cur.execute("CREATE TABLE Communication (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO Communication VALUES(?,?)",Communication)
   cur.execute("SELECT * FROM Communication")
   ROW =cur.fetchall()
   for row in ROW:
      print("Communication")
      print(row)
  # cur.execute("DROP TABLE BOOKS")
   cur.execute("CREATE TABLE BOOKS (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO BOOKS VALUES(?,?)",Books_Reference)
   cur.execute("SELECT * FROM BOOKS")
   ROW =cur.fetchall()
   for row in ROW:
      print("BOOKS")
      print(row)
  # cur.execute("DROP TABLE NEWS")
   cur.execute("CREATE TABLE NEWS (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO NEWS VALUES(?,?)",News)
   cur.execute("SELECT * FROM NEWS")
   ROW =cur.fetchall()
   for row in ROW:
      print("NEWS")
      print(row)
  # cur.execute("DROP TABLE Photography")
   cur.execute("CREATE TABLE Photography (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO Photography VALUES(?,?)",Photography)
   cur.execute("SELECT * FROM Photography")
   ROW =cur.fetchall()
   for row in ROW:
      print("Photography")
      print(row)
  # cur.execute("DROP TABLE Productivity")
   cur.execute("CREATE TABLE Productivity (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO Productivity VALUES(?,?)",Productivity)
   cur.execute("SELECT * FROM Productivity")
   ROW =cur.fetchall()
   for row in ROW:
      print("Productivity")
      print(row)
   #cur.execute("DROP TABLE Travel")
   cur.execute("CREATE TABLE Travel (ID INT, APP_NAME TEXT)")
   cur.executemany("INSERT INTO Travel VALUES(?,?)",Travel)
   cur.execute("SELECT * FROM Travel")
   ROW =cur.fetchall()
   for row in ROW:
      print("Travel")
      print(row)
