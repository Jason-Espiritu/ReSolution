# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label start:

    ## INTRO OF SELECTING A GENDER AND PLAYER NAME ##

    # Choosing a Gender
    window hide
    $ quick_menu = False
    scene black
    with Dissolve(1.5)
    pause(2.5)
    window show
    
    $ renpy.notify("Character Selection and Naming")
    
    "...hnnnngg..."
    #insert sound effect of cloth rustling

    "You woke up in the middle of the night."
    scene home_night with Dissolve(1.5)
    "Ow!" with vpunch
    "Why am I having a headache?"
    #insert sound effect of empty can tumbling

    """
    Oh yeah... Alfred came here and celebrated my employment...

    I drank a bit but, I can't recall what happened after that.
    
    Ugh... I guess that drink was strong enough to knock me over.

    Anyway... what am I again?
    
    You looked down to know your gender.
    """

    # Gender Choice
    menu:
        "I am a Male":
            pass
        "I am a Female":
            # change to female pronouns
            $ sex = "Female"
            $ he = "she"
            $ He = "She"
            $ his = "her"
            $ His = "Her"
            $ him = "her"
            $ Sir = "Ma\'am"
            $ sir = "ma\'am"
            $ Mr = "Ms."
            $ guy = "girl"
            $ player = female_name
    
    if sex == "Male":
        """
        You noticed that there's a bulge underneath your pants.

        You touched it and you felt a pleasuring sensation 

        Oh yeah... I'm a man. Why did I forgot that.
        """
    else: #Female Selected 
        """
        You noticed that you have two mounds on your chest.

        You touched one of it and you felt a pleasuring sensation 

        Oh yeah... I'm a woman. Why did I forgot that.
        """

    """
    Frustrated, you lay back on the bed and looked at the ceiling rembering what you've forgoten.

    Hmm... what was my name again?
    """

    call screen name_input

label pro_back_1:    
    "Ugh... this headache is making it hard for me to remember anything." with vpunch

    "{i}*sigh*{/i} I guess there's nothing I can do but to take a rest and hope that this headache is gone."

    # insert sound effect rustling cloth here

    "You grabbed your blanket, shut your eyes and went into deep sleep."

    window hide
    scene black
    with dissolve

    pause(2.0)

    ## PROLOGUE: RE:AWAKEN ## 
    window show
    $quick_menu = True
    with dissolve
    
    # INSERT ALARM CLOCK SFX
    "*Alarm rings*" with hpunch

    "..."

    "*Alarm rings*" with hpunch

    "(annoyed) hnggh…"

    "Still half asleep, I tapped my alarm clock to make it stop."

    # Insert Alarm Tap sound.
    "*tap*"

    "I woke up, sitting on the side of my bed; I clasped my hands and stretched up as high as it can go, making my blood rushed enough to make me awake."
    
    $renpy.notify("Prologue: RE:AWAKEN")

    scene home with Dissolve(2.0)
    # Insert calm bg music

    mc "hnnnngghhh…"

    mc "*sigh*"

    "I stood up and looked at the calendar to see what day is it."

    mc "Oh… It’s Monday"

    "As I look closely on my calendar, there was something written on the box of Monday."

    "\“My 1st Day Teaching\”"

    """
    After reading it, I grinned, and went to the window.
    
    I opened the curtain window, and took a nice deep breath of fresh air as I was greeted with a lovely view of the sea-reflecting skies and the energy brimming rays of the morning sun.
    """

    mc "Looks like it’s going to be a fine day."

    "Reassured and Excited, I went into the kitchen to make the best breakfast that I could make."
    
    # insert sizzling sound effect

    "*sizzle*"
    
    """
    After cooking, I put my breakfast on the table and also prepared a brewed hot coffee.
    
    The strong aroma of brewed coffee and the beautiful smell of my breakfast makes me happy and relaxed.
    
    While having my breakfast, I looked into my phone to read some news articles and laugh at some jokes that pops up on social media.
    
    After eating breakfast, I went and took a bath, then wore my casual clothes.
    
    I looked into the dressing mirror to see if my clothes are matching.
    """
    if sex == "Male":
        jump male_dress
    else:
        jump female_dress

label pro_back_2:
    mc "Alright, Looking good."

    "I double checked my prepared belongings for work to see if everything is in check."

    mc "Hmm… Alright, I’m ready"
    
    "Prepared, ready, and excited; I opened the door to a whole new journey as a Professional Teacher."

    scene black with fade
    """
    ...

    ...
    
    ...
    """
    scene city with fade
    pause (2.0)
    #insert busy city noices
    
    """
    The city is as busy as always; students in their uniforms going to their schools. 
    
    People in casual clothing are either hanging out with their peers, family or by themselves, and lastly people wearing their respective professional clothing going to their work.
    
    It feels surreal to this day that I am now a part of those people after I graduated from university half a year ago.
    
    Walking to work, I saw a university student focused on his notes while walking.
    
    Focused on his notes, it seems that he is not aware of his surroundings and is about to meet me.
    """

    mc "Hey kid, watch out."

    UniStu "Huh? ... What!!?"

    # Thump sound effects

    "*thump*" with vpunch
    
    "It was too late to avoid and we both crashed into each other."
    
    # Paper flying sound effect

    "We both land in our bottoms; and his notes that he was holding, flew and scattered all over the place."

    UniStu "NO!!!..."
    
    "He immediately sprang up, anxiously trying to get his notes."
    
    "Without a word, I also grab the other notes to help him."
    
    #insert paper pick up sound effect

    "Upon getting his notes, I smiled as I read some it. I can see that he is studying hard from the way how concise his notes are."
    
    """
    Every topic was summarized to a point that it was easy to understand, and the way he designed it was well thought and easy to find.
    
    Looking at it, reminds me of my days in university where I was the top of my colleagues. 
    
    But achieving it wasn’t easy; every day and night my eyes are fixated on books, lessons, web studies, and etc. 
    
    Understanding everything to the point that I can fluently explain every topic at any level where even a child can understand.
    
    It was a grueling yet satisfying journey, that I ended up graduating with the highest level of achievements.
    
    And now I’m a certified Teacher.
    
    I gave the rest of notes back to him and he apologized.
    """

    UniStu "I’m really sorry, I wasn’t looking"

    mc "It’s fine, you don’t need to apologize for that."

    mc "But be sure, next time you keep an eye on your surroundings."

    UniStu "I will."
    
    """
    The tense University Student meekly move past me.
    
    But as he walks away from my eyes can see, I shouted.
    """

    mc "Hey!"
    
    "The University Student flinched and looked back at me. Then I continued:"
    
    mc "You’re doing a great job. Keep it up."
    
    "I gave him a thumbs up that quickly shifted his mood from being nervous to being delighted."
    
    UniStu "T-Thank you… and… I-I’ll try my best."
    
    "He waves back and went to begone with the crowd."
    
    "And I also went on my way."

    scene black with dissolve

    """
    ...
    
    ...

    ...
    """
    scene city with dissolve
    pause(2.0)
    # Insert Quiet Suburbs sfx

    "Walking in these streets all the way to the school in which I’ll be teaching was peaceful."
    
    "Here, I can see students with identical uniforms walking the same path as I am, some of them are even looking at me, and some –"

    student "Good morning [Sir]."

    "– are happily greeting and waving at me."

    mc "Good morning to you too"

    "{i}\“So, this is what it feels like to be a Professional\”{/i}"

    "Or I guess it’s because of how I look that gives off a very “Teacher Aura” on myself."
    """
    I was planning to take a break for a year just to relax before finding a job but, 6 months had passed since I graduated, and a week before the New Year; 
    
    My old-time friend came over to my place and suggested that since I’m not doing anything, why not try applying to get a job at Good Life High School since I’m close to it.
    """
    
    "He was right, at that time I was doing nothing but 6 things:\nEat, sleep, play, study, shop, and drink."

    """
    I considered his suggestion and passed my application to the school the day after.
    
    Two days after, I got a phone call from the school saying that, I’ve been accepted, and they sent me an exact date of when I’ll start working.
    
    To be honest I didn’t expect that they would hire me at the 2nd half of the school year. 
    
    Most of the schools that I’ve inquired are opening up their job applications after the end of their school year so that teacher allocation and scheduling can be handled smoothly.
    
    I guess they are really short on staff that they acknowledge my application.
    
    I took a sigh and thought optimistically.
    """

    scene school with Dissolve(1.5)

    "As I get closer, I got to see the gates of my workplace."
    
    "It was fairly a simple sliding gate wide enough to fit two cars."
    
    "The walls surrounding the school are seven feet tall and the building is two-storey tall with a roof access hence the roof fences."

    unk "It seems, you like what you see young lad."

    mc "!!!???"

    "Admiring the Overall appearance of the School, I startled when someone in front of me talked."

    principal "Seems, you like what you see young lad."

    principal "And. You must be our new hire I believe?"

    mc "Ah, yes. It’s a pleasure to meet you sir."

    mc "I humbly apologize that you seem to have waited for me in the gate."

    principal "Oh don’t worry, it’s an old-habit of mine greeting the new commers into our school"

    principal "In fact, I think I should be the one to apologize for the sudden hiring."

    mc "Oh not at all. I’m actually glad and fortunate enough to get hired immediately after graduating."

    principal "I’m also glad. Well then, let me show you around the campus before you start your day."

    
    "I followed the principal inside the campus and introduced me to their facilities."
    
    scene hallway with dissolve

    "The school was large and open. The Main building was at the center this whole land. Even it was a two-storey building, it was big enough to accomodate this many students."

    "The school hallway was tidy and well decorated to lighten up the mood."
    
    scene school_back with dissolve

    "And at the back of it was an open ground filled with leisure spots for students and teachers to relax."
    
    scene hallway with dissolve
    
    "But most of all, the school also has vending machines strategically placed around the campus."

    mc "It feels like this school really is focused on comfort."

    principal "Why yes,"

    extend " yes it is."

    principal "This school was designed with comfort in mind."

    principal "And if students and Teachers are comfortable, they can give their full potential studying, and teaching. Don’t you think so?"

    mc "I can agree to that."
    
    """
    The principal has a point. If you aren’t comfortable to the environment or the nature of the school, you can’t give your best because you are stressed.
    
    After the tour, we went to the faculty where I will be preparing my things for today.
    """
    
    principal "Oh… I forgot to tell you."

    principal "You are now a part of the Senior High Division of this School and this is their Faculty Room."

    mc "So, I’ll be teaching students who are now one or two steps away from college or university, It’s close to my line of work."

    principal "Hoh… I like your confidence lad. Well, let’s introduce you to your seniors."

    scene black with dissolve
    # Insert door open sound effect

    "*Door Opens*"

    scene faculty with dissolve
    
    """
    The principal opened the door and inside are my seniors preparing their lessons for this day.
    
    The room was well organized and comfortable to work with. And the overall feel of this room can be summarized in one word: enthusiastic.
    
    I was quite nervous when it came to my mind that my seniors will be in their late 30’s or something but, looking at them now, it seems that they are at least either 2-5 years older than me.
    """

    principal "*ahem*"

    "The principal cough and all of my seniors stopped and look at our direction."
    
    principal "As you may have knew, last month one of our professors transferred to a different school and now we are short of manpower to teach our students."

    principal "And here where this lad comes in. [He] just got recently hired a week ago. Be nice to [him]."

    "The Principal whispered at me."

    principal "Come on lad, Introduce yourself to everyone."

    "I nodded and inhaled deeply."

    mc "Good Morning! My name is [player], I’m currently 22 years old and I’m happy that I could work with you."

    # Insert formal clapping sound effect

    "I bowed as a sign of respect to my seniors then, a formal applause came down to my seniors."
    
    "One by one they introduced themselves to me and promised to help me out in case I got problems."

    jump Alfred_Came

label pro_back_3:
    principal "Ahem… Let’s get back to our main topic."

    "The light conversation took a serious tone that the whole nature of the whole room has been turned upside down."

    principal "The reason why we hired you, is not just because we’re understaffed."

    principal "As I’ve told you earlier; a month ago, one of our teachers transferred schools"

    principal "And you’re his replacement."

    mc "Can you give me the reason why he transferred?"

    show alfred gloom at correct_pos_alfred with dis

    every "..."

    "No one answered and the whole environment turned to worse, like they were reminded of a bad memory."

    alfred "A-actually… he left because, he couldn’t handle it."

    mc "Pardon?"

    show alfred serious at correct_pos_alfred with dis

    alfred "You see, there’s this certain class that’s been… quite… problematic to deal with for some time now."

    principal "Frankly speaking, no one can handle class 12-F."
    
    "So, the problematic class is 12-F."

    mc "How about splitting them up and dissolving the class."

    principal "Well we’ve tried that but, every senior-high school student signed a petition on not letting any student from class 12-F go to their class."

    alfred "It’s either they are hated or they’re afraid of what will happen if one of them became their classmates."

    mc "This is very troubling indeed."

    principal "And that’s why we’re asking you if you can handle class 12-F."

    "Oh… It makes sense now."

    show alfred happy at correct_pos_alfred with dis
    
    "Alfred set me up into applying to this school in order to help him with his problem."

    "I glared at Alfred and it seems he knows why."

    show alfred gloom at correct_pos_alfred with dis
    """
    His apology to me was written all over his face, so I just let out a heavy sigh and assess my situation.
    
    Thinking about it, this might be an opportune moment. If I manage to fix this class, it would be my greatest achievement. 
    
    I would quickly gain their trust and secure my position. Heck, even a promotion might be imminent if I manage to pull this off.
    
    But then again, it’s a huge gamble. It’s a high-risk, high-reward scenario where every decision I will take may result in heavy consequences.
    
    Thinking thoroughly, I’ve made my decision.
    """

    mc "I'll do it"

    show alfred sigh at correct_pos_alfred with dis

    "Everyone was perturbed of what I said and started to question me."
    
    principal "W-wait… are you sure?"

    "He was doubting my decision, I reassure everyone:"

    mc """
    I mean, there’s no other option. Every student in the school was against the dissolvement.

    All of you tried to assess their situation but failed.

    So let me take a crack at it. My experience that I gained during my university days will now be put to the test.
    """
    mc "And besides..."

    extend "I’m not someone who backs down from a challenge."

    show alfred happy at correct_pos_alfred with dis

    "Everyone was astonished from what I said, even Alfred is smiling."
    
    alfred "Looks like I wasn’t wrong recommending you to this school."

    mc "Shut it, you owe me one after this."

    alfred "Yeah-yeah… I’ll treat you to some beer next time."

    hide alfred with dis
    # Insert School Bell sound effect

    "*Bell Ring*"

    principal "Well, that’s settles it. [Mr] [player], you are now the adviser of class 12-F, may you have a wonderful time teaching."

    mc "Thank you."

    "And with that, I went to my desk and prepare my materials for today’s class."

    scene black with Dissolve(1.0)

    """
    ...
    
    ...

    ...
    """
    $quick_menu = False
    window hide
    with Dissolve(1.5)
    pause (2.0)

    jump chapter_1 # Jumps to Chapter 1



#call dialouges
label cont:
    
    ## CHECKS IF NAME IS BLANK
    $ check_name = player.strip()

    if check_name == "":
        if sex == "Male":
            $ player = male_name
        else:
            $ player = female_name
    else:
        pass

    "You grabbed your wallet from the nightstand and picked up your identification card."
    "Oh yeah, my name is [player]"

    jump pro_back_1

label male_dress:
    """
    My top is a Baby pink, elbow length long-sleeved Polo shirt, with the contrast of vertical braiding giving off a very mature demeanor.
    
    And it was tucked in a Black Chinos Style trousers with a leather strapped belt with gold painted buckle expressing professionalism and passion with your line of work.

    """
    jump pro_back_2
label female_dress:
    """
    My top is a White Polo shirt with a Dodger Blue Blazer on top of it, giving off the professional vibe.
    
    And the Polo Shirt was tucked in a black mini-skirt to match with the nice weather.

    """
    jump pro_back_2
label Alfred_Came:
    # check player's Gender
    if sex == "Male":
        unk "Oh… seems like the \"Bully\" came."
        
        jump background_alfred

        label came_m:
            mc "Well… I didn’t expect that you are working here Alfred"

            mc "But I still recall that I won in our battle last week"

            show alfred smug at correct_pos_alfred with dis

            alfred "Come on now, you just won by one game… And besides, do you really want to insult your boss on your 1st day of the job."

            "Wait... Really?!"

            show alfred happy at correct_pos_alfred with dis

            "I looked at the principal that is chuckling beside me and nodded."

            mc "Well, I do apologize for insulting you."

            "I came closer to him and said in a smug tone."

            mc "You’re just still salty that I beat you without breaking a sweat."
        
            show alfred smug at correct_pos_alfred with dis

            alfred "Hoh… picking a fight are we. Just so you know It was lag that made me lost last week."

            mc "Oh… so you want a rematch huh."

            alfred "Let\'s Rock! Just say the time and place. We already know the smell of the game."

            "We both grinned to our hearts content but the principal butt in."

    else:
        unk "Oh… the “shorty” has arrived."
        
        jump background_alfred

        label came_f:
            mc "I didn’t know that you work here Alfred."

            mc "And don’t call me “shorty”, I’m not that short."

            show alfred smug at correct_pos_alfred with dis

            alfred "You’re always shorty in my eyes."

            mc "Why you…! I’ll get you next time."

            alfred "Oooohhh… Scary…"

            mc "Grrrrrr…"
            
            hide alfred with dis

            principal "Ahahaha… it seems like you two know each other."

            show alfred happy at correct_pos_alfred with dis

            alfred "Well we’ve been friends since forever. And she’s always sticks to me wherever I go."

            mc "What?! Why would you bring that up right now?"

            hide alfred with dis

            principal "Ahahaha… well, this makes things simpler."

            mc "What do you mean Sir?"

            principal "Well, from now on He’s going to be your Boss in this Division."

            mc "HAH?! You!? You’ve got to be kidding me."

            show alfred smug at correct_pos_alfred with dis

            alfred "What… you don’t like it?"

            "It’s not that I dislike him being my boss."
            
            "The only thing that gets in my nerves is that smug face of his whenever he’s scheming something."
            
            mc "Hmph"

    jump pro_back_3

label background_alfred:
    "Wait I know that voice"
        
    show alfred happy at correct_pos_alfred with dis
        
    "I looked to the right where the Head of this Department sits and then I saw a familiar face."

    # Alfred's short Background
    "Alfred... A long time friend of mine."
    
    "He's six years older than me, but still acts like a university student if we're together."
    
    "He was my neighbor but, I moved to a dorm after I graduated from Highschool to pursue my degree."
    
    "And during my studies in University, He got married to a well known singer and got a kid."
    
    "But even if we're apart, we're still in contact with each other. He sometimes comes to my place whenever he has time."

    if sex == "Male":
        jump came_m
    else:
        jump came_f