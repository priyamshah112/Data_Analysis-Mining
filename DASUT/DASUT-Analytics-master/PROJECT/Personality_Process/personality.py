personality_type=['Conscientiousness','Extrovert','Agreeable','Open_Minded','Emotional']
#Conscientiousness: कर्त्तव्य निष्ठां
category=['Communication','GAMES','Productivity','SOCIAL','EDUCATION','Photography','VIDEO','DATING','ANDROID_WEAR','BOOKS','Travel','Online_Shopping','MUSIC','Launcher']
"""Agreeableness is a person's tendency to be compassionate and cooperative toward others. Characteristics: Image-1
   Conscientiousness is a person's tendency to act in an organized or thoughtful way.  Characteristics: Image-2
   Extraversion is a person's tendency to seek stimulation in the company of others.   Characteristics: Image-3
   Emotional range, also referred to as Neuroticism or Natural reactions, is the extent to which a person's emotions are sensitive to the individual's environment.Characteristics: Image-4
   Openness, or Open to Experience, is the extent to which a person is open to experiencing a variety of activities. Characteristics: Image-5
   """
Needs_Percentiles=['need_liberty','need_ideal','need_love' ,'need_practicality','need_self_expression' ,'need_stability','need_structure','need_challenge','need_closeness','need_curiosity','need_excitement' ,'need_harmony']
"""
The second model, Needs, describes at a high level which aspects of a product are likely to resonate with the data.
The model includes twelve categories of needs based on  work in marketing.
Image-6
"""
Values=['value_conservation','value_hedonism','value_openness_to_change','value_self_enhancement','value_self_transcendence']
"""
The third model, Values, describes motivating factors that influence the user decision-making.
The model has five dimensions of human values based on work in psychology.
Image-7
"""
#~~~~~~~~~~~~~~Solutions ~~~~~~~~~~
Purchasing_preferences=[
'consumption_preferences_spur_of_moment'#Likely to indulge in spur of the moment purchases 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_credit_card_payment'#Likely to prefer using credit cards for shopping 0.0 (unlikely)1.0 (likely)
,'consumption_preferences_influence_brand_name' #Likely to be influenced by brand name when making product purchases 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_influence_utility '#Likely to be influenced by product utility when making product purchases 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_online_ads '#Likely to be influenced by online ads when making product purchases 0.0 (unlikely)1.0 (likely)
,'consumption_preferences_social_media'# Likely to be influenced by social media when making product purchases 0.0 (unlikely)1.0 (likely)
,'consumption_preferences_family_members'# Likely to be influenced by family when making product purchases 0.0 (unlikely)1.0 (likely)
,'consumption_preferences_clothes_quality' #Likely to prefer quality when buying clothes	0.0 (unlikely)1.0 (likely)
,'consumption_preferences_clothes_style' #Likely to prefer style when buying clothes            0.0 (unlikely)1.0 (likely)
,'consumption_preferences_clothes_comfort' #Likely to prefer comfort when buying clothes        0.0 (unlikely)1.0 (likely)
,'consumption_preferences_automobile_ownership_cost' #Likely to be sensitive to ownership cost when buying automobiles	0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_automobile_safety']#Likely to prefer safety when buying automobiles	0.0 (unlikely)0.5 (neutral)1.0 (likely)

Music_preferences=[
'consumption_preferences_music_rap'#Likely to like rap music       0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_country'# Likely to like rap music 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_r_b '#Likely to like rap music     0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_hip_hop '#Likely to like rap music 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_live_event'# Likely to like rap music 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_playing' #Likely to like rap music 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_latin '#Likely to like rap music   0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_rock '#Likely to like rap music     0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_music_classical']#Likely to like rap music 0.0 (unlikely)0.5 (neutral)1.0 (likely)

Health_activity_preferences=[
'consumption_preferences_gym_membership'#Likely to have a gym membership 0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_outdoor' #Likely to like outdoor activities    0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_eat_out']#Likely to eat out frequently         0.0 (unlikely)0.5 (neutral)1.0 (likely)

Movie_preferences=[
'consumption_preferences_movie_romance'#Likely to like romance movies                     0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_adventure'#Likely to like adventure movies                0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_horror' #Likely to like horror movies                     0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_musical' #Likely to like musical movies                   0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_historical'# Likely to like historical movies             0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_science_fiction' #Likely to like science_ficition movies  0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_war' #Likely to like war movies                           0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_drama'# Likely to like drama movies                       0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_action'# Likely to like action movies                     0.0 (unlikely)1.0 (likely)
,'consumption_preferences_movie_documentary']#Likely to like documentaary movies          0.0 (unlikely)1.0 (likely)                   

Reading_preferences=[
'consumption_preferences_read_frequency'#Likely to read often                                    0.0 (unlikely)0.5 (neutral)1.0 (likely)
,'consumption_preferences_books_entertainment_magazines' #Likely to read entertainment magazines 0.0 (unlikely)1.0 (likely)  
,'consumption_preferences_books_non_fiction' #Likely to read non-fiction books                   0.0 (unlikely)1.0 (likely)  
,'consumption_preferences_books_financial_investing'# Likely to read financial investment books  0.0 (unlikely)1.0 (likely)  
,'consumption_preferences_books_autobiographies']#Likely to read autobiographical books           0.0 (unlikely)1.0 (likely)  

Volunteering_preferences=[
'consumption_preferences_volunteer']#Likely to volunteer for social causes 0.0 (unlikely)0.5 (neutral)1.0 (likely)

Environmental_concern_preferences=[
'consumption_preferences_concerned_environment']#Likely to be concerned about the environment 0.0 (unlikely)0.5 (neutral)1.0 (likely)

Entrepreneurship_preferences=[
'consumption_preferences_start_business']#Likely to consider starting a business in next few years 0.0 (unlikely)0.5 (neutral)1.0 (likely)

"""p1={"Communication":1} #'Open_Minded'
p2={"GAMES":1} #Obsessive,Introvert
p3={"Productivity":1}#Conscientiousness
p4={"SOCIAL":1}#Novelty_Seeking,Extrovert,'Open_Minded'
p5={"EDUCATION":1}#Perfectioner,'Conscientiousness','Agreeable'
p6={"Photography":1}
p7={"VIDEO":1}
p8={"DATING":1}
p9={"ANDROID_WEAR":1}
p10={"BOOKS":1}
p11={"Travel":1}
p12={"Online_Shopping":1}#Novelty_Seeking
p13={"MUSIC":1}#Empathetic
p14={"Launcher":1}#Psycopath"""
Conscientious={"Communication":0.12,"Games":0.01,"Productivity":0.5,"Social":0.2,"EDUCATION":0.1,"Photography":0.1,"VIDEO":0.1,"DATING":0.1,"ANDROID_WEAR":0.1,"BOOKS":0.1,"Travel":0.1,"Online_Shopping":0.1,"MUSIC":0.1,"Launcher":0.01}
Extrovert={"Communication":0.3,"Games":0.01,"Productivity":0.1,"Social":0.4,"EDUCATION":0.1,"Photography":0.2,"VIDEO":0.2,"Dating":0.1,"ANDROID_WEAR":0.2,"BOOKS":0.01,"Travel":0.2,"Online_Shopping":0.01,"MUSIC":0.2,"Launcher":0.01}
Agreeable={"Communication":0.3,"Games":0.1,"Productivity":0.3,"Social":0.4,"EDUCATION":0.2,"Photography":0.2,"VIDEO":0.2,"Dating":0.1,"ANDROID_WEAR":0.2,"BOOKS":0.01,"Travel":0.2,"Online_Shopping":0.01,"MUSIC":0.2,"Launcher":0.01}
Open_Minded={"Communication":0.3,"Games":0.1,"Productivity":0.3,"Social":0.4,"EDUCATION":0.2,"Photography":0.2,"VIDEO":0.2,"Dating":0.1,"ANDROID_WEAR":0.2,"BOOKS":0.1,"Travel":0.2,"Online_Shopping":0.1,"MUSIC":0.2,"Launcher":0.1}
Emotional={"Communication":0.2,"Games":0.1,"Productivity":0.3,"Social":0.2,"EDUCATION":0.2,"Photography":0.2,"VIDEO":0.2,"Dating":0.1,"ANDROID_WEAR":0.2,"BOOKS":0.1,"Travel":0.2,"Online_Shopping":0.1,"MUSIC":0.2,"Launcher":0.1}
