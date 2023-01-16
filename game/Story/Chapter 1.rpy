# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label chapter_1:
    
    scene faculty
    window show
    $quick_menu = True
    with dissolve

    $renpy.notify("Chapter 1: RE:AGE")

    """
    While preparing my materials for today; My emotions are running wild.
    
    It’s a mix-bag of excitement, anxiety, and fear.
    
    Excited that it’s going to be my 1st time working as a teacher.
    
    Continuous thought of things messing up making me Anxious.
    
    And fear of what would the students of Class 12-F will do now that I know they have a bad reputation.
    
    Having these mix-bag emotions running in my head I gently slapped my face to forget it and focus on my work.
    """

    show alfred happy at correct_pos_alfred with dis

    alfred "Hey, this will be your schedule for now."

    """
    Alfred came over on my desk and hand me my schedule.
    
    Looking at the schedule I realized something.
    """

    mc "Wait… I’m going to teach only Class 12-F for the whole day, seven times a week?"

    show alfred sigh at correct_pos_alfred with dis

    alfred "As we’ve told you before, no-one really wanted to teach on that class."

    mc "So, I’m their only teacher and I’m going to teach all of their subjects?"

    show alfred happy at correct_pos_alfred with dis

    alfred "Yup!"

    """
    Seriously!?
    
    I looked at Alfred, and he just pulls out a thumbs up and pats me on the back…
    
    I’m slowly regretting my decision now.
    """

    mc "...*sigh*... Once this is over, you’re going to treat me to the fanciest bar in this city."

    alfred "Ahahaha… please go easy on my wallet."

    mc"""
    You dragged me into this.

    ...*sigh*... there’s no crying over spilled milk.

    I don’t mind teaching and preparing the materials for every subject.

    And I still don’t know what kind of students they are that creates them a bad reputation.

    So, I’m just going to meet them and see what’s up.
    """

    hide alfred with dis
    
    "I grabbed my materials and head out."

    show alfred happy at correct_pos_alfred with dis

    alfred "Goodluck."

    show alfred serious at correct_pos_alfred with dis

    "..."

    teacher1 "Hey Alfred… Do you think [he] can do it all by [him]self?"

    show alfred happy at correct_pos_alfred with dis

    alfred """
    Don’t worry. [He]\'s the smartest [guy] I know.
    
    [His] knowledge is nothing to laugh for. When I looked up [his] bio, [he] aced all of the subjects and when I called the University about it.
    
    All they say is that, [he] was able to simplify even the most difficult topics. So, I’m confident with [his] teaching style even if it’s [his] first day.
    """

    show alfred serious at correct_pos_alfred with dis

    alfred "But that ain’t the problem of that class."

    teacher2 "Yeah… It’s not that they are failing. It’s their behavior is the problem."

    alfred "Let’s just hope that [he] can manage to change them."

    alfred "And maybe prove that, it was really our way of lecturing them are at fault that they were like that to us."

    hide alfred
    scene black
    with Dissolve(2.0)

    """
    ...
    
    ...
    
    ...
    """
    scene hallway with fade

    "Walking in the hallway, I was gathering my thoughts on how to introduce myself."

    mc "Okay, just stay calm, smile and introduce yourself. It’s that easy."

    mc "Conduct attendance, laydown your rules then proceed with the lesson."

    """
    I wonder how will they react to it.
    
    As I get closer to the classroom where I’ll be teaching, the whole feeling of the environment went eerie.

    I can already feel the pressure that this class exerts, like it spells like \"No Teacher’s Allowed\" that makes you want to back and not bother them.

    Now I kind of get why the previous teacher transferred.

    But I already signed up for this, It’s now or never.

    I proceed to walk and never looked back.
    """
    # Insert noisy class but low volume

    """
    A faint noise is slowly getting louder as I go closer to the door.

    Judging from the noise, it seems like they’re having… fun?

    I reached the door and took a deep breath.

    """
    #Insert Door Open sfx

    scene classroom with Dissolve(1.5)

    """    
    I opened the door and I was baffled for what I have witnessed.

    Crumpled papers flying left and right, like some sort of a snowball fight.

    Some students are playing with their phones, or handheld consoles.

    And some students also have their uniforms undone.

    This environment feels like they are in grade school but worse.
    """
    # Insert school chairs moving sfx

    """
    Most of them saw me and rapidly notifies everyone, then the rest sprang into their seats and stayed silent.

    Everyone’s eyes are on me, and it gives of a very daunting look, like they were saying, \"here we go again\" without actually saying it.

    Looking at the room; aside from the number of crumpled papers on the floor and their undone uniforms, everything was neat, even their desks have no signs of any vandalism of some sort.

    So, how come they have a bad reputation?

    Without further ado, I went inside and faced them.
    """

    mc "Good Morning Class! My name is [Mr] [player] and I’m going to be your new adviser."

    mc "And on this final half of this school year, I hope we can have a great time together."

    every "..."

    "Silence"

    "Looks like this is going to be a rough one."
    
    "I brought up the class list Alfred gave me and conduct an attendance."

    mc "Well then, let’s start with your attendance."

    mc "First up, Tadao."

    show tadao serious at correct_pos_tadao with dis
    
    tadao "Here"

    """
    Hmm… looks from his physique, he looks like an athlete of some sort.

    Maybe marathoner?
    
    Anyway, let’s proceed with the others.
    """
    hide tadao with dis

    mc "Hideaki"

    show hideaki serious at correct_pos_hideaki with dis

    hideaki "...here..."

    """
    Scruffy hair, looks like this one doesn’t care about his hair style. Or is it the new trend these days?
    
    Argh… doesn’t matter.
    
    And that patch on his face, did he get into an accident?
    
    Anyway, lets continue.
    """

    hide hideaki with dis

    """
    I called their names one by one and I’ve noticed that everyone looks normal at best.
    
    Like there’s nothing wrong with them on the outside.
    """

    mc "Kazumi"
    
    show kazumi happy at correct_pos_kazumi with dis

    kazumi "Present."

    """
    Oh!? She’s cute, an actress maybe?
    
    What am I thinking? snap out of it…
    """

    hide kazumi with dis

    mc "Mamoru"

    "..."

    mc "Mamoru?"

    show mamoru serious at correct_pos_mamoru with dis

    mamoru "Here…"

    "Hm… looking at him, I can already tell that he screams trouble. Is he the source of this bad rep?"

    hide mamoru with dis

    """
    I resumed calling out their names and to my surprise, everyone is present.
    
    If they’re like this, why do the teachers give up on them? I’m starting to get curious.
    """

    mc "Alright, it seems like everyone is here today." 
    
    mc "So, let’s lay down some class rules and it must be obeyed at all cost in order for us to have a good time together."

    every "..."

    "Hm? The air suddenly became tense and they’re eyes and ears are on me, like they’re anticipating something from me."

    mc """
    Well I only have 3 rules so it’s not that hard to follow.

    So, first of all is to follow the school rules and etiquette as much as possible, but as for today I’ll let it slide since it’s our first meeting.

    But the next time I see those uniforms undone you’ll be making your greetings in the detention room, not here.

    Second, in terms of your gadgets; I’m prohibiting it while we’re having lectures. 
    
    Failure to do so, will be immediately confiscated until the final bell rang.

    And lastly, any heavy violations committed by this class, without a doubt will be put in the principal’s office immediately without question.

    These are the rules that are needed to be followed to avoid heavy consequences. 
    
    Doing so we will have no problems and can enjoy our school life peacefully.
    """
    
    """
    After hearing that, their faces turned frown and their glares are filled with disgust.
    
    But I can also tell from some their faces, that they already knew this would be the case.
    """

    mc "Understand?"

    every "..."

    """
    Everyone was still not pleased, but nodded.

    Looks like I stepped on a landmine. I don’t care if you started to hate me, but this is for your future. 
    
    I need to fix this class’ problem and this is the first step to it. 

    I need to be as strict as possible for them to obey or else, things will get out of hand and I’ll be held responsible for it if I’m not careful.
    """

    mc "Well then!"

    "I grabbed my chalked and my Lesson Notes."

    mc "Then we’ll start with our first lesson."

    
    scene black with dissolve
    """
    ...
    
    ...

    ...
    """
    scene classroom with dissolve

    """
    3rd Period: Math

    Everything was going smooth so far but, it didn’t last long.

    While I’m writing on the board, I noticed a number of students fiddling with their phones.

    I finished writing and faced the class and decided to give them a little warning.

    """

    mc "As you can see in this formula –"
    
    """
    I continued to discuss the lesson and some of the students in question noticed it then immediately put their phones down, but one close to me didn’t.
   
    It seems he’s too fixated on it that he didn’t notice.
    
    I guess if they are like that, I might as well have to set an example.
    
    I slowly get closer to that student while discussing.
    """
    
    mc "And if the steps are done correctly, you will have no problem solving it."
    
    student1 "W-What?"
    
    "I purloined the phone from his and looked at him."

    mc "Right, mister?"
    
    student1 "…Y-yeah…"
    
    "I hand him my chalk."

    mc "Good, now would you please go to the board and solve the next problem."
    
    student1 "tch…"
    
    # insert chalk writting

    "He obediently went to the board and solve the problem."
    
    "Yet, my eyes widened when he manages to answer the problem with ease."
    
    student1 "[Sir]… is this correct? I followed your steps as instructed and ended up with this answer."
    
    mc "…"
    
    mc "Impressive… that is correct."
    
    "Is that last sentence really necessary? Or you’re just blatantly insulting me."

    mc "You may take your seat now."
    
    "We crossed paths and carefully put his phone back on his pocket."
    
    student1 "?!"
    
    "He touched his pocket to reassure then I mutter to him –" 
    
    mc "Please refrain from doing it again or you’ll be saying goodbyes to it until the end of the day, got it."
    
    student1 "Yes [sir]."
    
    "I picked up where the discussion ends and rest are as peaceful as it gets."
    
    scene black with dissolve
    """
    … 
    
    … 
    
    …
    """
    
    scene classroom with dissolve
    
    """
    It’s the Final Period.
    
    Since the previous incident, everyone was obediently quiet and it seems to be focused on my lecture.
    
    Or so I thought.
    
    After the 3rd Period, I’ve noticed that they’re passing down a piece of paper on which they inscribe something on it.
    
    And since they’re not making too much noise, I didn’t even bother confiscating it. 
    
    And they are also partaking whenever I called their names so I assumed that it must be some random talk that didn’t even matter for me.
    
    I finished my lesson and coincidentally the last bell rang.
    """
    # insert bell ring sfx


    mc "Well what a coincidence, students remember–"
    
    # insert students leaving

    "I stopped midway when I saw them synchronously packed their belongings and leave."
    
    """
    Are they that eager to leave from here?
    
    From my understanding. The last bell, was the signal for the end of the class and the start of club activities, or go home.
    """
    
    mc "*sigh* I guess I’ll go back now…"
    
    """
    I repack my things and head out.
    
    But as I go outside the room, I noticed a piece of paper laying on the ground.
    """
    
    mc "Hey, hey… don’t leave any garbage in the room… Geez…"
    
    mc "Hm?"
    
    # insert paper pickup sfx

    """
    As I picked up the piece of paper. I noticed there is a lot of things inscribe here.
    
    Is this the paper that they keep passing through?
    
    Curious I took a seat and read the contents of it.
    """
    
    # Conversation 

    """
    \"Hey, looks like my hunch was spot on, we got another adviser.\"
    
    \"Seriously? What happened to the former one?\"
    
    \"I guess he couldn’t take it and just quits.\"
    
    \"I mean we really did a number on him.\"
    
    \"Ahahaha, but it was fun though.\"
    
    \"Yeah…\"
    
    \"So, what do you think of our new adviser?\"
    
    \"[He] looks younger than our previous teachers, maybe a new graduate?\"
    
    \"Interesting… since [he]’s younger, maybe something good will happen.\"
    
    … 
    
    … 
    
    …
    
    \"Yo, what do you think of his rules.\"
    
    \"They’re as awful as the other teacher’s we’ve dealt with.\"
    
    \"Forcing us to obey, or risk immediate Detention or Suspension? Isn’t that just too harsh as punishment? What happened to fairness?\"
    
    \"Just because [he]’s our adviser doesn’t mean that [he] boss us around.\"
    
    \"I’m starting to lose hope from all of this. Are all teachers like this? Forcing their ideals on us students so that we can have a ‘good life’?\"
    
    \"This is nuts.\"
    
    \"Anyway… [He]’s just the same as the rest of them, focused on molding us into their ideals and didn’t bother thinking about what really is ‘us’.\"
    … 
    
    … 
    
    …
    """

    "So, they are comparing me to their other professors."
    
    "Well... not that I care. I’m here to help and if I’ll be hated, then so be it."

    # paper torn sfx

    "I tore the piece of paper then put it in the trash bin, and went back to the faculty."
    
    scene black with Dissolve(1.5)
    
    """
    … 
    
    … 
    
    …
    """
    show faculty with dissolve

    "Back the faculty I was greeted by Alfred."
    
    show alfred happy at correct_pos_alfred with dis

    alfred "Hey, how’s your first day? Did they do something to you?"
    
    mc "Aside from their sharp stares? Nothing much."
    
    alfred "Ahahaha, looks like they gave you the same treatment as the rest of us."
    
    mc "Really!? All of you?"
    
    "I looked at every teacher in the faculty and all of them nodded."
    
    alfred "Oh… look at the time. I guess, I’ll leave you there now, got some leftover work to finish."
    
    hide alfred with dis
    
    """
    Alfred went back on his desk, and resumes his work.
    
    I guess I’ll finish the other materials that needed to be done here.
    
    I went on my desk and continued to finish my work.
    """

    mc "I hope that it doesn’t get any worse in the future."
    
    scene black with Dissolve(1.5)

    """
    …
    
    I really shouldn’t have said that.
    
    …
    """
    
    # Insert Bell SFX

    scene faculty with fade

    "...*Bell Alarms*..."

    mc "...*SIGH*..."
    
    $ renpy.notify("2 MONTHS LATER")

    "Lunch break, I went back face planted to my desk, and everyone seems to notice."
    
    teacher1 "A-are you alright?"
    
    mc "I-I’m fine…"
    
    
    "It’s been 2 months since I started to work here, and I’m already accustomed to the work environment."
    
    "But if we’re talking about Class 12-F, things got from fine to worse."
    
    
    mc "I’m just tired and annoyed about them, that’s all."
    
    teacher1 "Care to elaborate?"
    
    mc "Aside from the continuous glares at me, it seems they can’t do what I asked them to do."
    
    mc "Like for example, whenever the lunch bell rings. I always asked someone to help me carry their assignments back to the faculty."
    
    show alfred happy at correct_pos_alfred with dis

    mc "But when I looked back, the student was gone and the rest went to the cafeteria, so I’ll just have to carry things in rounds wasting my time."
    
    show alfred serious at correct_pos_alfred with dis

    mc "Or like whenever I asked them to help me setup something, they always leave halfway due to some circumstances, and leave me struggling to finish the setup."

    show alfred gloom at correct_pos_alfred with dis

    mc "Or when the time –" 
    
    extend "EH?!" with vpunch
    
    "As I said my problems with the whole faculty, all of them felt like they’re having a Post-Traumatic Stress Disorder even Alfred."
    
    teacher1 "Uhh… we… can… relate…"
    
    mc "A-are you guys, okay?"
    
    alfred "Y-yeah… it’s just… bad memories are coming back… whenever you complain about them."
    
    alfred "Because… they also… did that to us… and we’re quite… impressed that you only suffered little… from what they’ve done to you in two months."
    
    alfred "Most of us… didn’t last that long and some lost their minds."
    
    mc "W-wait… Really?"
    
    teacher2 "Y-Yeah… I was the one who lost it last school year. Remembering it right now… make me want to barf."
    
    teacher2 "It took me 2 weeks to recover from it, so I was transferred to a different class."
    
    "I couldn’t help but feel sorry for these guys."
    
    "I stood up and bowed to them and everyone was startled."
    
    
    mc "Uh… I’m really sorry… I shouldn’t have talk about them. I didn’t know you guys have bad memories with my class."
    
    show alfred happy at correct_pos_alfred with dis

    alfred "N-no! no… It’s okay… really. Man, I never knew you can be this sincere to us."
    
    mc "Want a piece of my fist, Alfred?"
    
    alfred "Aaaand you’re back to your usual self. Ahahaha…"
    
    "As I was about to punch him in the gut. We heard a knock from the door."
    
    hide alfred with dis

    "The door opened and it was a female student from a different class, carrying a pile of paper."
    
    student "Umm… who is [Mr] [player]?"
    
    
    "Time froze for a moment when I realized that I tasked someone to collect and bring their assignments here."
    
    "I smacked my face with my hand out of pure regret, which surprised Alfred and the student."
    

    show alfred serious at correct_pos_alfred with dis

    alfred "Are you okay?"
    
    mc "Yeah… there was just a fly in my face."
    
    hide alfred with dis

    "I went to the student and hand me the papers."

    mc "Uh… that would be me, but may I ask, did someone gave it to you?"
    
    student "Uh. No… I just found it on the table of Class 12-F." 
    
    student "Since no one was in the room, I thought maybe the teacher forgot to bring it."
    
    student "So I went inside and looked on the contents and found your name, then I picked it up and here we are."
    
    student "I was scared at first of getting caught by one of the 12-F’s students but I got lucky and didn’t met a single one."
    
    
    "So, it really is true that other students are scared of Class 12-F."
    
    "And this girl needs to muster up her courage in order to complete what my students didn’t accomplished."
    
    "That made me angry a little bit, but I must remain my composure."
    
    mc "Thank you, and I apologize that you need to bring it back here and for wasting your time."
    
    student "It’s okay, I shall take my leave then."
    
    mc "Ah… but before you leave."
    
    student "Hm?"
    
    mc "Coffee… which do you prefer… hot or cold?"
    
    student "I like it cold, but I’m sorry, I don’t drink black coffee."
    
    mc "Oh, that’s perfect… wait a second."
    
    student "?"
    
    
    "I went back to my desk and picked up a special container."
    
    "I opened the container and picked up a cold can."
    

    "Alfred immediately noticed what I picked up and started to panic."
    
    show alfred happy at correct_pos_alfred with dis

    alfred "Hey, you’re giving her that coffee?"
    
    mc "What? It’s compensation for bringing her the papers."
    
    hide alfred with dis

    "I hand over a cold vanilla cappuccino coffee in a can at her."
    
    "The female student realized that it was no ordinary coffee."

    student "Eh!? You’re giving me this? But –"
    
    mc "You don’t need to pay for it. Take it as a token of my gratitude."
    
    mc "Oh… but be sure to drink it, otherwise it will lose its heavenly taste."
    
    "The student was astonished that she received a very special coffee for what she did."
    
    student "I-I will… I shall take my leave, a-and t-thank you very much for this coffee."
    
    "The student went back to her class ecstatic."

    show alfred happy at correct_pos_alfred with dis

    alfred "I can’t believe you really gave that girl that coffee."
    
    teacher1 "Alfred… what did [he] gave to the girl?"
    
    alfred "That coffee was imported and it’s currently not available here."
    
    alfred "And because of its perfect taste, it’s 5 times as expensive as our usual brewed coffee here."
    
    "The whole faculty was shocked at the price of the coffee that I gave to the girl."

    teacher1 "A-are you… by any chance... came from a rich family?"
    
    mc "Nope... Two years ago, when I was still in University. I emailed a complaint in that company about their coffee being bland despite being 3 times expensive."
    
    teacher2 "Y-you really did that?"
    
    mc "Yeah, I gave them the details why it was bland, and they politely asked if I could be their taste tester, then I said, ‘why not as long as I get free coffee’"
    
    mc "Since then, they’re sending me a box coffee, and often coffee beans every month or two."
    
    teacher1 "Why did you complain to them? You could have just search for another coffee shop."
    
    mc "Well, they fit my ideal taste of coffee that I always brew at home but still lacking, so I just helped them out to find the missing piece to make it even taste better."
    
    alfred "Ahahaha… That’s a cafephile for you."
    
    teacher1 "Huh, what does that mean?"
    
    mc "Brewing coffee is kind of my hobby, and Alfred sometimes comes to my place just to drink coffee so he calls me that from time to time."
    
    mc "And I though you promised not to call me that again."
    
    alfred "Sorry… sorry… I just suddenly remembered that nickname."
    
    alfred "Anyway… now that your coffee is gone –"
    
    mc "What are you talking about?"
    
    show alfred serious at correct_pos_alfred with dis

    alfred "Pardon?"
    
    "I opened my special container and show it to them."
    
    mc "I always bring three cans whenever I go somewhere outside my house."
    
    show alfred sigh at correct_pos_alfred with dis

    every "…"
    
    "The shocked on their face agreed that I:"
    
    every "As expected of a cafephile."
    
    show alfred serious at correct_pos_alfred with dis

    alfred "Alright back to your places everyone we’ve only got a 10 mins left on our break."
    
    "Alfred put us back in place with that one sentence." 
    
    hide alfred with dis

    "I guess he isn’t just all talk and can actually lead people."
    
    teacher1 "Oh yeah, I would like to warn you about two specific students in your class."
    
    "Huh… that’s new, it’s been two months since I’ve met my students and nothing’s really bad is happening except from their passive aggressiveness towards me."
    
    mc "And who might those two students be?"
    
    teacher1 "Mamoru and Tadao…"
    
    "I knew Mamoru was one they will mention… but why Tadao?"
    
    mc "What’s with those two?"
    
    show alfred serious at correct_pos_alfred with dis 

    alfred "It’s because they were feared by everyone in this school because of the rumors circulating around them, especially Mamoru."
    
    "Alfred came to butt in again on our conversation."
    
    teacher1 "Yeah… One of his rumors said, that someone saw him beat up a teacher outside the school because he got bumped or something."
    
    teacher2 "And some students said that he picked a fight with 7 adult guys alone and won with a few scratches."
    
    alfred "And I’ve heard murmurs from the students that he regularly got prisoned, since the police are always escorting him."
    
    mc "I-Isn’t that just rumors? Why do you guys believe in those things?"
    
    mc "Didn’t you even question him?"
    
    teacher1 "Well, we tried… but we got scared halfway, have you seen his face whenever he sees us?"
    
    "I expected this reaction since I also have that same feeling when I first met him."
    
    "Whenever I tried to talk or even walk near him. Not just only his face, but his whole body becomes somewhat hostile like a rattle snake shaking his tail."
    
    "His intimidating aura is cannot be underestimated, so I kind of get why they believe these rumors."
    

    mc "But why Tadao was included?"
    
    alfred "He was rumored to be Mamoru’s right-hand man." 
    
    alfred "Some rumors circulating around him saying that, Mamoru picked a fight with his club in which he won." 
    
    alfred "And he took Tadao like some kind of a spoils of war, and then later corrupted to become his right-hand."
    
    "Isn’t this rumor just, over the charts for a Highschool student. Can he really do that?"
    
    teacher1 "So be careful when dealing with those two" 
    
    mc "*sigh* I’ll take your word for it"
    
    hide alfred with dis

    scene black with Dissolve(2.0)
    
    "…"
    
    "…"
    
    "…"
    
    scene faculty with Dissolve(1.5)

    "I look at the time and I realized that it’s almost time for my next period."
    
    "While I prepare my materials, Alfred announced something."
    
    show alfred serious at correct_pos_alfred with dis

    alfred "Before you guys forgot. I just want to let you know that the Periodical Exams has been decided to be on next week. So, please tell it to your students."
    
    "Oh, I definitely forgot about that."
    
    "The Periodical Exams are created 2 weeks before the exam day, so the exam will be ready to be distributed when it the day comes."
    
    "Thank you for reminding us, Alfred."
    
    alfred "As of now, the tests are now being reprinted and I think It should be done by now."
    
    # Insert Door open sfx

    "...*Door opens*..."
    
    teacher2 "Alfred, here are all the copies."
    
    show alfred happy at correct_pos_alfred with dis

    alfred "Oh, what a coincidence."
    
    # insert bell rang

    "...*Bell rang*..."
    
    hide alfred with dis

    "I guess, I better go now."
    
    scene hallway with fade

    "The bell rang for the second time, and I take my leave to teach for the next period on Class 12-F."
    
    scene classroom with fade

    "As I enter the room, I heard subtle voices."

    student2 "Quickly… Before the teacher came."
    
    student3 "I know, I know, I’m copying it as fast as I could."
    
    
    "I saw a group of students bunched up together, and they’re all hastily taking notes."
    
    "It seems like they’re too focused on it and didn’t noticed me entering."
    
    "I went closer to them and asked:"
    
    
    mc "What are you students so focused on?"
    
    students "??!!!"
    
    
    "They were all taken aback and, in a panic, looked at me in cold sweat."
    
    "I noticed one student was hiding something on his back."
    
    "He noticed me and starts to avoid my gaze."
    
    "I started to feel suspicious so I asked him."
    
    mc "Hey, what are you hiding behind your back?"
    
    student3 "…"
    
    mc "Not talking? Fine, let me rephrase it."
    
    mc "Show me what are you hiding behind your back."
    
    student3 "…"
    
    "Annoyed… you’ve left with the only option left."
    
    mc "I guess you leave me no choice."
    
    # Insert paper grab fast sfx

    "I grabbed him and took what he was hiding."

    "It was a piece of paper with printed text on it."
    
    "But as I skim it further, it was no ordinary printed paper."
    
    "It was a copy of the answers for the upcoming test."
    
    "At this moment, I was shaken, disappointed, and frustrated."
    
    "Why would they do this? Why?"
    
    "And then, I blew a fuse."
    
    mc "Where… did you find this?"
    
    students "…"
    
    mc "…"
    mc "I knew, most of you… are still using your phones while we’re having classes, yet I haven’t confiscated one."
    mc "I knew, most of you have been talking behind my back, yet I haven’t called you out in the guidance office."
    mc "I knew, your gazes says that you despise me, that’s why you don’t want to help me when I asked you to."
    mc "I knew, you don’t want me in this classroom, that’s why you leave immediately when the bell rings."
    mc "I’ve endured every single thing you’ve been throwing at me."
    mc "And now this? Now I understand why those teachers gave up."
    mc "But as you see… I’m not one of those people, who would simply give up if they got fed up with your tricks."
    mc "You know… in my opinion, there’s only one type of people I despise the most."
    mc "Cheaters"
    mc "They’re humanity’s worst kind… a scum in society."
    mc "They boast their achievements, but when asked about something related to their course, they can’t even give a simple answer."
    mc "So back to my question."
    mc "WHERE DID YOU GET THIS???!!!" with vpunch
    
    student3 "…*sniffle*… *hic*…"
    
    "I shouted out of sheer anger, and the student that had the answer sheet was on the verge of tears."
    
    mc "hm…"
    mc "Since you can’t answer properly, I’ll asked the whole class."
    mc "Who among of you stole this answer sheet?"
    
    students "…"
    mc "Still no answer huh? Then so be it…"
    mc "If no one opens up who stole it, this whole class will be guilty of this offence and will be suspended."
    students "?!"
    "As I said that, they glared at me with hatred."
    mc "What? No one’s confessing, it just means that everyone here is involved."
    
    # Insert chair moved
    
    "Then I heard someone stood up…"
    
    show tadao serious at correct_pos_tadao with dis

    tadao "It was me… I’m the one who stole it."
    
    "The whole class was distressed when Tadao stood up and confessed."
    
    mc "So you stole it?"
    
    "Tadao bravely looked me in the eye and reassured his conviction."
    
    tadao "Yeah…"
    
    hide tadao with dis
    show mamoru serious at correct_pos_mamoru with dis

    "I grabbed Tadao’s arm and everyone reacted especially Mamoru who was about to stand up."
    
    "Tadao looked at them, especially at Mamoru, and shook his head."
    
    show mamoru serious_away at correct_pos_mamoru with dis

    mamoru "Tsk… suit yourself."
    
    hide mamoru with dis
    mc "Tadao, you’re coming to the principal’s office with me."
    
    "I pulled Tadao out and went to the principal’s office along with the answer sheet as evidence."
    
    scene black with Dissolve(2.0)

    
    "…" 
    
    "…" 
    
    "…"
    
    scene office with Dissolve(1.0)

    "When I brought Tadao to the principal’s office, the principal also called Alfred since he’s the Head Teacher."
    
    "Even though we’re just the 4 of us inside, the nature immediately felt like it was a court trial."
    
    "And with everyone in silence, I said my statement."
    
    mc "Sir Mr. Tadao convicted a serious offense and here is the evidence."
    
    "You handed out the evidence to the principal."
    
    mc "Tadao obtained and leaked to the class the answers of the incoming test that will happen next week."
    
    mc "This is a serious offense that cannot be overlooked."
    
    principal "I see… is there anything you want to add?"
    
    menu:
        "Ask Tadao":
            jump question
        "End you statement":
            jump end_state

    # Option:
    #-	Ask Tadao about his offense
    #-	End your statement
    #-------------------------------------------------------------------------------------------------------------------------------
    
label chap1_1:

    "Tadao continued to provoke us, especially me."
    
    show tadao angry at correct_pos_tadao with dis

    tadao "You teachers have so much pride, that you think that you’re always right."
    tadao "In your minds, you have your ideals of what your students should be, and we must abide to those ideals for you to feel accomplished."
    tadao "And if we can’t, you blame it on us."
    show tadao sarc at correct_pos_tadao with dis
    tadao "And out of all the teachers that we’ve been through in this school."
    "He points his finger at me"
    show tadao angry at correct_pos_tadao with dis
    tadao "By far, you’re the worst of them."
    "Offended, I didn’t control myself and yell at him."
    show tadao serious at correct_pos_tadao with dis
    mc "YOU STILL HAVE THE NERVES TO TALK WHEN –"
    
    hide tadao with dis

    show alfred serious at correct_pos_alfred with dis

    alfred "[player]!"
    "Alfred grabbed my hand tightly and called me."
    "He shook his head telling me to stop."
    mc "Sorry"
    "I cooled myself and returned to my seat."
    hide alfred with dis

    principal "I’ve heard enough, and I will now pass judgement on Mr.Tadao."
    principal "Mr. Tadao, due to your misconduct for obtaining the test’s answer sheet and leaking it to your class. You are hereby suspended for a week."
    principal "And since the exams will be on next week, we will allow you to come to the school and conduct to take the exam on the detention room."
    principal "You may now take your belongings and return to your home."
    "Tadao bowed and left without saying a word."
    principal "[Mr] [player] you should also return to your classroom; the class is not yet over."
    mc "Thank you, I shall take my leave now."
    
    scene classroom with fade
    
    "I returned to your class, and greeted with their glares of hatred from the students."
    "You ignored it and proceed to report what happened to Tadao. Then I added:"
    mc "Since all of you can’t follow to my instructions. I’ll be stricter than before."
    mc "And if another incident like this happens again, I kid you not, this whole class will be suspended."
    
    show kazumi angry at correct_pos_kazumi with dis

    kazumi "TEACHER! Isn’t this too harsh, it’s like you are now treating us like criminals."
    
    show kazumi surprise at correct_pos_kazumi with dis

    mc "And whose fault is that? I’m not here just to teach you these subjects, but also to teach you manners and respect."
    
    hide kazumi with dis
    show hideaki surprise at correct_pos_hideaki with dis
    
    hideaki "But what happened earlier was just –"
    mc "Say what you wanna say to me. I don’t want to hear any more reasons from anyone of you."
    
    show hideaki serious at correct_pos_hideaki with dis
    hideaki "…"
    
    hide hideaki with dis
    kazumi "You’re…"
    
    show kazumi crying at correct_pos_kazumi with dis

    "I looked at Kazumi whose eyes are flooded with her tears."
    
    show kazumi angry at correct_pos_kazumi with dis
    kazumi "Y-you’re the worst!"

    hide kazumi with dis
    "Kazumi left the classroom in tears, disappointed from what I said."
    
    show hideaki surprise at correct_pos_hideaki with dis
    hideaki "Kazumi!"
    
    show hideaki serious at correct_pos_hideaki with dis
    "Hideaki looked at me, shaking with rage. His furious face screams that, he’s going to beat me for making Kazumi cry, but he’s hesitant because of the consequences of what might happen."
    show hideaki serious_away at correct_pos_hideaki with dis
    hideaki "Tch…"
    
    hide hideaki with dis
    "Hideaki left to chase out Kazumi."
    
    
    "As for the class, their glares are much worse than before."
    
    "It’s not just only hatred, they’re now furious that they want to hit me."
    
    "But either way I do not care anymore, there’s so much to do to fix this class."
    
    show mamoru serious_away at correct_pos_mamoru with dis
    mamoru "I had enough of this…"
    "Mamoru stood up with his bag."
    show mamoru serious at correct_pos_mamoru with dis
    mamoru "Teacher… I can leave early as long as I have a reason, right?"
    mc "Then, what is your reason?"
    mamoru "I’m uncomfortable… that’s all."
    hide mamoru with dis
    "Mamoru left the classroom without my approval."
    "I guess he knows if he stays for too long, he might actually do something worse than Tadao."

    # Insert School bell sfx

    "...*Final Bell Rang*..."
    "Coincidentally, the final bell rang and all of them left."
    show alfred serious at correct_pos_alfred with dis
    "Alfred saw what happened as he was outside observing, and came inside."
    alfred "Are you sure that’s the right choice?"
    "I finished packing my materials and stood up." 
    mc "It’s the only way, the reality of this world we live in, is harsher than this. They must realize it now or they’ll fall."
    "I left the classroom and call it a day."

    hide alfred with dis

    scene black with Dissolve(1.5)
    
    "..."
    
    '...'
    
    "..."
    

    $quick_menu = False
    window hide
    with Dissolve(1.5)
    pause (2.0)

jump chapter_2 # Jumps to Chapter 2

label question:
    #(Option 1: Ask Tadao about his offense)
    mc "I would like to ask his reason for this offense."
    principal "Go ahead… I also want to hear it."
    "I looked at Tadao. His eyes were full of disgust and hatred toward me."
    mc "Mr. Tadao… why did you do it? Why steal the answer sheet?"
    
    show tadao serious at correct_pos_tadao with dis

    tadao "…"

    "Tadao didn’t talked, he just stared like he was making fun of me."
    
    "Offended, I went closer to his face and asked him one more time."
    

    mc "I said… why? Why did you do it?"
    
    show tadao sarc at correct_pos_tadao with dis
    "Tadao smirked making me infuriated like a kettle full of heated water that is about to whistle."
    
    tadao "Ahahaha… Why does it matter to you? I’ve confessed my crime, you caught me red handed."
    tadao "I’ll get suspended either way if I said my reason or not. So, it doesn’t matter… T e a c h e r."

    jump chap1_1

label end_state:
    # (Option 2: End your Statement)
    mc "That is all I have to say."
    
    show tadao sarc at correct_pos_tadao with dis
    
    tadao "Ahahaha…"
    
    "Tadao sarcastically laughed at us."
    
    "Infuriated, you looked at him. His eyes were loathing towards me."
    
    "But I didn’t care."
    
    mc "What’s so funny?"
    tadao "Nothing… I just find it funny, that this is how you treat us when we commit a serious offence."
    tadao "You didn’t even try to ask for a reason. You immediately went to the conclusion that we’re offenders now."
    tadao "It feels like, you’re treating us students like criminals… Am I right? T e a c h e r"
    mc "…"

    jump chap1_1