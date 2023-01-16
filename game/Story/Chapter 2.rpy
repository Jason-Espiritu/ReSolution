# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label chapter_2:
    
    scene classroom with dissolve

    window show
    $ quick_menu = True
    with Dissolve(2.0)     
    
    $renpy.notify("Chapter 2: Re:concile")

    """
    Two weeks had passed since the last incident, and everything went back to “normal\".
    
    Tadao was back in class after a week-long suspension.
    
    And Kazumi is somewhat back to her usual self. 

    The only difference is their gazes, it didn’t change ever since that day. They’re still glaring with hostility but, I ignored them until I grew accustomed to it.

    I became a lot stricter than before: all of their gadgets we’re all on my table until break and until the last bell, and any violators were automatically sent to detention for counselling.

    I’m currently teaching English to them and.

    """
    
    mc "Instead, you can build this sentence like –"

    """
    ...*Bell rang*...
    
    I ran out of time explaining.
    
    As per usual, the students leave as fast as they could to go to the cafeteria.
    
    I packed my things and went back to the faculty room.
    """
    
    scene hallway with fade
    
    "Walking in the hallway, I feel that something is different."
    
    """
    Some students from other classes are looking at me.
    
    And they are whispering something that I can’t pick up.
    
    Is there something on my face?

    """
    
    scene faculty with fade
    
    """
    
    Back in the faculty, I decided to review my students’ grades, and to my surprise, every one of them scored fairly high.
    
    """

    mc "Huh… so they’re actually smart at all."

    """
    Since the incident, I spent two days creating a new exam for them, so that the leaked answers will be useless to them.
    
    """
    
    teacher1 "Yeah, that was also my reaction when I saw the results."
    
    teacher1 "They are smart and hardworking students. It’s just that, we can’t figure out why they we’re like that to us teachers."
    
    "Then a co-teacher just came back from her lecture."
    
    teacher3 "Hey [player], have you heard?" 
    
    mc "What?" 
   
    teacher3 "Students from other classes are talking about you."
    
    teacher3 "I’ve only just heard a little bit but, I think its related to what happened two weeks ago."
    
    teacher2 "Oh yeah, some of my students were talking about that… I was puzzled at first since they use an alias instead of a name but now it makes sense."
    
    teacher1 "What’s the alias given to [him]?" 
    
    teacher2 "They call [him] “The Teacher from Hell\" or something."
    
    teacher1 "Wow… what a really bad nickname to be called for."
    
    teacher1 "[player], what do you say about this?"

    "Looks like the whole school now knows about the incident."

    mc """
    
    *sigh* I guess they heard me get angry at my students and that’s why I get that nickname.
    
    But, there’s nothing can be done about that, and I was expecting it to happen sometime soon.
    
    Well, I don’t care either way. If they think of me like that, then so be it.
    
    ...*sigh*... I’m gonna stroll around for a bit.

    """
    show alfred gloom at correct_pos_alfred with dis

    alfred "This is my first time I see [him] like that."
    
    teacher1 "Alfred… do you think [he]’s okay?"

    show alfred sigh at correct_pos_alfred with dis
    
    alfred "I don’t know… [He] is not acting like [him]self since the incident happened."
    
    teacher1 "What was [he] like before?"
    
    alfred "[He] was a bit carefree and likes to stay at home and do nothing but relax."
    
    alfred "[He]\'s not going to be a teacher but, I convinced [him] to be one."
    
    show alfred serious at correct_pos_alfred with dis
    
    alfred "6 years ago, before I go apply for a job here. I was an intern at [his] school, luckily enough [his] class was under my advisory."
    
    alfred "During those times in my intern, he’s always enthusiastic about the topics that I’ve been teaching them."
    
    alfred "And then one day, I’ve given them a group activity where they need to discuss a certain topic."
    
    alfred "One by one, they give their best delivering their topics. But [him]? [He] goes beyond what I was expecting."
    
    alfred "[He] delivered the topic like [he] was a teacher to [his] students. And manages to simplify the topic for them to further understand."
    
    alfred "The look on [his] face was enthusiastic whenever [he] saw his classmates understand what [he] was saying."
    
    alfred "After witnessing [his] delivery, I was at awe and felt jealous."
    
    alfred "\"I want to be like [him]\", that’s what I said to myself."
    
    alfred "Then when I asked [him], where will [he] go after [he] graduates. [He] said that [he] was going to find work since, [he] just wants a simple life."
    
    teacher2 "Really?! [He] just want to live a simple life?"

    show alfred laugh at correct_pos_alfred with dis
    
    alfred "Ahahaha, you wouldn’t believe how many attempts I made to convince him to go to University"
    
    show alfred happy at correct_pos_alfred with dis

    alfred "That’s why I have so much respect on [him]."
    
    alfred "And I kind of get it why [he]’s angry at me. Since I’ve pushed him to the other direction."
    
    teacher1 "So it was your fault all along… [his] dream was to live peacefully and you ruined it."
    
    show alfred laugh at correct_pos_alfred with dis

    alfred "Ahahaha, I guess you’re right."
    
    show alfred serious at correct_pos_alfred with dis

    alfred "That’s why I’m worried that I might have pushed [him] way to hard this time."
    
    hide alfred with dis

    scene black with Dissolve(2.0)

    scene hallway with Dissolve(1.5)    
    
    "I stood up and left the room for a change of pace to ease up my mind."
    
    "The faculty is becoming uncomfortable for me to even stay."
    
    "Ever since what happened two week ago, I’m building up a lot of stress in my head."
    
    """
    Recalling what happened, I feel disgusted at myself.
    
    I should have dealt with it professionally, but my emotions came ahead of me.
    
    """
    
    student "Hey, is that [him]?"
    
    student "Yeah that’s [him]."

    mc "Hm?"
    
    "I’ve noticed the students are taking a glance at me, and buzzing something to their fellow fears."
    
    student "They said that [he] got angry and shouted at a female student two weeks ago because she made a mistake. That student left and cried on the back of the school."
    
    student "What a terrible teacher…"

    """
    
    Hey, I can hear you, you know.
    
    The other students also are talking about me.
    
    """

    student "So we also have that kind of teacher…"
    
    student "And [he] is also a new hire."
    
    student "I hope [he] is not our teacher next school year."
    
    "I let out a sigh and moved on."

    """    
    It’s still lunch time and I haven’t eaten yet that my stomach is about to growl.
    
    I was planning on going to the cafeteria but, knowing there is a lot of students there and the fact that I’ve been the talk of all the students in this school. I’ve got less options to pick.
    
    I also want some peace and quiet for me to at least forget some of these events.
    
    I’ve thought of areas where that it possible and I’ve narrowed it down to two places.
    
    The first is the school open grounds, which have tables and chairs for me to relax.
    
    And since everyone is in the cafeteria, there are less students using it.
    
    The second is the roof, which students rarely use because of how empty it feels.
    
    And it’s only populated when they are practicing.
    
    Hmm… both of them are good but which one should I go.
    
    """

    menu:
        "Go to the Roof":
            jump to_roof
            $ route = "hideaki"
        "Go to Open Grounds":
            jump to_open
            $ route = "kazumi"
    
    
    #Option:
    #-	Go to the Roof
    #-	Go to the Open Grounds

    #-------------------------------------------------------------------------------------------------------------------------------
label chap2_1:
    scene black with Dissolve(2.0)
    """
    ...
    
    ...
    
    ...
    """

    scene classroom with Dissolve(1.0)

    mc "And with that our lesson for today has come to an end."

    """
    Time flies by, and by the time I finished my lecture there’s only 10 minutes left before the final bell rings.
    
    I collected my things, and waited for the bell to ring.
    
    Without nothing to do… the whole class was just stared at me, it’s like they were also waiting something from me.
    
    """

    """
    Thinking what it is, someone spokes…
    
    """

    jump spec_int
    #Interaction Dependent based on the choice of the player during the first option of this chapter 

label chap2_2:
    """
    Now, the rest looked at me, puzzled as to what I have said.
    """
    
    mc "What? I’m already done teaching you the lesson, and we’re just waiting for the last bell to ring."
    
    """
    They’re still confused, that I let out a sigh and gave them one small push.
    
    """

    mc "You students can do whatever you want in the remaining time we have. Just don’t go outside this room unless necessary, and don’t get too noisy."
    
    """
    The students looked at each other and cautiously did what they want in the remaining time inside this class.
    
    The classroom became lively for this very moment. 
    
    Some students pulled out their phones chatting or playing. 
    
    Some female students started to fix and applying cosmetics on themselves. 
    
    And some are just chatting with their peers inside the classroom.
    
    ...*Bell Ring*...
    
    The bell rang, and everyone began to pack their belongings.
    
    Before they leave, I called out someone.
    """
    
    mc "Tadao…"
    
    show tadao surprise at correct_pos_tadao with dis

    students "?!"
    
    """
    The whole class instantly turns sour when I called Tadao.
    
    The students glared back at me menacingly, even him.
   
    """

    mc "Could you stay here for a while… I just need to talk to you for a bit."
    
    show tadao serious at correct_pos_tadao with dis

    """
    I looked straight back at him, conveying that I am serious about this.
    
    He let out a sigh, nodded and stayed until we’re the only people in this room.
    
    I grabbed my things and walked outside.
   
    """
    
    mc "Tadao… let’s go outside for a bit…"

    tadao "…"
    
    scene school_back with fade

    """
    Tadao followed me outside, specifically to the back of the school building where the park is placed.
    
    I bought a cold can of local coffee that is conveniently placed for students who wants to grab a cold drink after long sessions of physical practice.
    
    And sat on the nearest open table we could find.
    
    He seems a bit tensed and hostile towards me since I’m the one who put him into suspension.
    """
    
    mc "I assume you drink coffee so here…"
    
    """
    I brought out my last can of coffee from my special container and gave it to him.
    
    """
    show tadao surprise at correct_pos_tadao with dis
    
    tadao "… Thanks …"
    
    """
    Tadao took and gave it a sip, and his eyes widened.
    """
    tadao "This is really delicious…"
    
    mc "I’m glad that you like it."
    
    tadao "Where did you get this?"
    
    mc "It’s actually imported from here…"
    
    "Tadao stops drinking the coffee knowing what he’s drinking isn’t available from here."

    show tadao happy_away at correct_pos_tadao with dis
    tadao "Umm… how much is this?"
    
    mc "hmm… roughly, five times the price of this coffee that I brought from that vending machine."
    
    show tadao surprise at correct_pos_tadao with dis
    tadao "Uhh…"
    
    """
    Tadao was stunned, and almost dropped the coffee when he heard the price.
    
    He bowed and apologized for realizing it late.
    
    """
    show tadao grin at correct_pos_tadao with dis
    tadao "I’m really sorry I should have realized it sooner that this was an expensive coffee."
    
    mc "Ahahaha, don’t mind it… I gave it to you without any malice."
    
    show tadao surprise at correct_pos_tadao with dis
    tadao "But…"
    
    mc "Just think of it as a gift… it’s yours the moment you took it."
    
    show tadao happy at correct_pos_tadao with dis
    tadao "*sigh* Fine"

    """
    Tadao gave up and finished the drink.
    
    """
    show tadao serious at correct_pos_tadao with dis
    tadao "So, what do you want to talk about?"
    
    """
    Tadao looked serious. His eyes do not show hostility, though I can tell that he is still nervous.
    
    I guess he want to finish this talk as fast as possible.
    
    """

    mc "I’ll be frank, this is about the events that happened two weeks ago." 
    
    show tadao surprise at correct_pos_tadao with dis
    tadao "!?"
    
    """
    Tadao flinched for a moment and made him sweat a bit.
    
    """

    mc """Someone told me recently that you didn’t do it, and it was all a huge misunderstanding.
    
    I’m going to ask this once so answer me honestly.
    
    """
    
    """
    I can see Tadao moved his throat, he’s even more nervous than before.
    
    """
    
    mc "Was it true?"
    
    show tadao serious at correct_pos_tadao with dis
    tadao "…"
    
    "Tadao’s stern face is now full of sweat."
    
    "I looked at him seriously as I want to know the whole truth about what really happened."
    
    show tadao happy at correct_pos_tadao with dis

    "He was silent for a whole minute then he just gave up and let out a sigh."
    
    show tadao happy_away at correct_pos_tadao with dis
    tadao """*sigh* I guess the cats out of the bag…
    
    Yes, I didn’t do it. I didn’t steal that answer sheet.
    
    It was our classmate that you forcefully asked that almost burst to tears that acquired it.
    """
    
    """
    So, it was really that student that stole it… wait… did he just said acquired?
    
    """

    mc "Wait… you said… he acquired it? Not stole it?"
    
    show tadao serious at correct_pos_tadao with dis
    
    tadao """Yes… that paper wasn’t stolen, we we’re going back from break when we found it lying on the ground.
    
    When we found out that it was an answer sheet, we were planning on returning it immediately.
    
    But the others found out about the paper and convinced him to let them copy at least a bit of the answers before returning it and then you came.
    
    """
    
    """
    So, it’s true that it was a really huge misunderstanding.
    
    I put my hand on my face regretting everything.
    
    Why did let my emotion do the talking?
    
    Maybe if, I should have asked sincerely maybe thing didn’t turned out that way.
    
    But one thing is making me curious.
    
    """

    
    mc "Why did you stood up and claim the blame to yourself?"
    
    show tadao happy at correct_pos_tadao with dis
    """
    Tadao just smiled and answered:
    
    """
    
    tadao """Well… he can’t speak because of your anger and he was about to cry.
    
    That classmate can’t speak for himself since he’s always being bullied by the students from other classes, so that’s why I’m always helping if he’s in trouble.
    
    The other reason is because you threaten to the class that if no one show up then the whole class will be suspended.
    
    \"One must be sacrificed to save everyone\", that’s what I thought to myself. So, I stood up and lied that I took it.
    
    And the last reason is… I wanted to be like Master Mamoru…"""
    
    mc "Mamoru?"

    """
    As I remember, Mamoru was feared among the school and Tadao was his right-hand man.
    
    So why does he want to be like him?
    
    I’m starting to get curious between the relationship with him and Mamoru.
    
    """
    
    mc "Why do you want to be like him?"
    
    show tadao serious at correct_pos_tadao with dis
    tadao "It’s because he saved me…"
    
    mc "Hm?"
    
    tadao """Even I have this athletic body; I’m still weak-hearted inside.
    
    Last year when I transferred here, my classmates were bullying me for being a weakling inside a well-built body.
    
    Then one day, when I was practicing late. I was ganged up by three delinquents.
    
    I couldn’t bring myself to fight back, and I was down on the ground, getting kicked.
    
    Then Master Mamoru came and beat them to a pulp.
    
    After that, I met him again and begged if he can teach me to be like him.
    
    And to his response, he said, \"suit you self\".
    
    From then on, I kept on training with him.

    He really inspired me to be what I am right now, but I’m still far away from his level."""


    """
    So, the rumor that Mamoru corrupted him actually happened but on a positive way.
    
    But I’m at a loss for words.
    
    Tadao’s selflessness became his courage. He’s more concerned about others rather than himself.
    
    That he is willing to save everyone even if it ruins him.
    
    It makes me little bit jealous because I wouldn’t be able to do that.
    
    I stood up and bowed at him.
    """
    
    mc "I’m really sorry, I’ve made a grave mistake."
    
    show tadao surprise at correct_pos_tadao with dis
    """
    Tadao took aback, and didn’t know what to do.
    
    """
    
    mc """Because of me jumping to conclusions, I ended up tarnishing your record.
    
    And I don’t have the authority to revoke it
    
    So, I can only give you an apology for my mistake."""

    """
    Tadao felt ashamed and began to panic.
    """

    show tadao happy at correct_pos_tadao with dis
    tadao "Teacher, please raise your head. You don’t need to bow."
    
    """
    I sat back and faced Tadao, whose face is relieved and happy.
    
    Then Tadao gave me a thumbs up.
    
    """
    show tadao grin at correct_pos_tadao with dis
    tadao "Hey, at least you understand that you are wrong, so I’ll forgive you."
    
    mc "Thank you."
    
    unk "Hey!!... Tadao!"
    
    """
    We heard someone shouted his name.

    """
    show tadao surprise at correct_pos_tadao with dis
    tadao "Ah… It’s Master…"
    
    """
    Looking closer, it was Mamoru waving at him.
    
    """
    show tadao grin at correct_pos_tadao with dis
    tadao "Sorry teacher, looks like I need to go now…"
    
    mc "No worries, I’m glad that I got to talk to you."
    
    """
    Tadao stood up and picked hup his bag.
    """
    show tadao happy at correct_pos_tadao with dis
    tadao """Thanks for this wonderful drink you gave me.
    
    You know… you’re not bad at all.
    
    Now you just need to show that side of yours to everyone, so that they will accept you.
    """

    
    "My eyes widened in realization from what he said, like pieces of a puzzle are coming together."
    
    tadao "Well, see you tomorrow, Teacher!"
    
    "I went back to my senses and smiled back."
    
    mc "Yeah, Take care."

    hide tadao with dis
    
    """
    Tadao waved and left together with Mamoru.
    
    Recalling what he said before, left me deep in thought.
    
    """

    mc """Show this side of me to them huh?
    
    I guess it’s worth giving it a try."""
    
    """
    I grinned as I pack my things, and went back to call it a day.
    
    """
    scene black with Dissolve (1.5)
    """
    ...
    
    ...

    ...
    """
    $quick_menu = False
    window hide
    with Dissolve(1.5)
    pause (2.0)
    
    jump thank_you


label to_roof:
    #Option 1: Go to the 
    
    
    "Since no one will be there, the school rooftop is fine for today."
    
    scene roof with fade

    "I walked up the stairs to the roof and then you heard a noise."
    
    unk """This is what you get for denying us. *thump*
    
    Yeah… this is what you get. *thump*"""
    
    hideaki "Argh…"
    
    """
    Was that Hideaki I hear?
    
    I rushed in to the roof and saw 2 students ganging up on Hideaki.
    
    """

    unk "Oh shoot… RUN!!!"
    
    mc "HEY!!"
    
    """
    Both of them quickly ran down and I didn’t have time to catch them.
    
    I let out a sigh and helped Hideaki get up his feet.
    """
    show hideaki serious at correct_pos_hideaki with dis
    hideaki "You shouldn’t have helped."
    
    mc """Are you stupid? You could have been beaten up to a pulp.
    
    Come on, let’s get you to the clinic."""

    show hideaki serious_away at correct_pos_hideaki with dis
    hideaki "It’s fine… I’ll just needed to rest here."
    
    """
    He sat down in silence and grumpy, the awkwardness that I feel came from our bad relationship with each other.
    
    And I still don’t fully know him, so I don’t know what to do.
    
    If this goes on, we’re going to feel like idiots.
    
    """
    mc "*sigh* Here…"
    
    """
    I pulled a can of iced coffee out of my bag and gave it to him…
    
    """ 
    show hideaki serious at correct_pos_hideaki with dis
    hideaki "…"
    
    """
    He suspiciously looked at me, I guess he knows that it’s an expensive coffee.
   
    """

    mc "It’s coffee, Iced Latte to be exact. It might help you feel better."
    
    show hideaki sad at correct_pos_hideaki with dis
    hideaki "… thanks…"
    
    show hideaki surprise at correct_pos_hideaki with dis
    """
    Hideaki took and drank it. The surprised look on his face speaks that he has never tasted something like that before.
    
    """

    hideaki "It’s tasty."
    
    mc "I’m glad that you like it."
    
    """
    He gave it back to me half empty.
    
    """

    mc "Huh?"
    
    show hideaki serious at correct_pos_hideaki with dis
    hideaki "It’s still your coffee, I only just drank half of it."
    
    mc "You know it doesn’t work that way, right?"
    
    """
    His eyes widened as he realized what he has done.
    
    Then he went pale.
   
    """
    show hideaki serious_away at correct_pos_hideaki with dis
    hideaki "I-I guess… I’ll have to break my savings just to pay for this."
    
    """
    I didn’t expect this.
    
    """

    mc "No… You don’t have to pay me for it."

    show hideaki serious at correct_pos_hideaki with dis

    hideaki "I’ll have to pay you back. You probably wasted a quarter of your salary to buy this one can for the first time and I took it from you."
    
    mc "No… It’s okay I got two more in here, see."
    
    """
    I showed him my special container for these coffees and his face was in shock when he saw it.
    
    I briefly explained to him how I got these coffees and his face is the same as ever.
    
    """
    show hideaki surprise at correct_pos_hideaki with dis
    hideaki "Are you a cafephile?"
    
    mc "Ahahaha… people always call me that."
    
    show hideaki smile at correct_pos_hideaki with dis
    hideaki "I give up, thanks for this coffee anyway."
    
    mc "Don’t mention it."
    
    """
    I also opened up mine and grabbed a sandwich to eat.
    
    I ate silently so I don’t bother Hideaki who sits beside me recovering from his bruises.
    
    Aside from Hideaki, the silent of this roof under the clear sky makes me feel relaxed.
    
    It’s a good thing I decided to go and eat here.
    
    Then Hideaki break those silence.

    """
    show hideaki serious_away at correct_pos_hideaki with dis
    hideaki "Uh…"
    
    mc "Hm?"
    
    show hideaki smile at correct_pos_hideaki with dis
    hideaki "You’re not going to ask, why I got beat up?"

    """
    He’s got a point there… but I knew the reason, so I answered him.

    """
    
    mc """Umm… I think it wouldn’t matter either way since my relationship with you is as bad as eating raw fish.
    
    And even if I asked why, you would probably not say a thing because it doesn’t concern me, so I didn’t
    
    """
    show hideaki sad at correct_pos_hideaki with dis
    hideaki "… I guess that’s right… sorry"
    
    """
    He seems a little bit disappointed, like a puppy realizing his treat is not his favorite food.
    
    Does he really want to share it? Fine, I’ll give it a go.
    
    """

    mc """But, if you want to vent it out on someone.
    
    I wouldn’t mind lending an ear while I’m eating."""
    
    show hideaki serious at correct_pos_hideaki with dis
    hideaki "…"
    
    """
    I continued to finish my lunch when he started to talk.
   
    """
    
    hideaki """Those two guys were from the other class; I’ve known them since I entered this school.
    
    They we’re friendly and always beside me, but all of that was a lie.
    
    They we’re just friendly because they know that I’m smart just like my brother.
    
    So they always asked me to help with their projects, I thought I would help them create it, but it was the other way around.
    
    They didn’t even help, and when I was done, they left.
    
    Now that I know why, I tried to refuse once. But they ended beating me up.
    
    I remembered that I tried fighting back, but it didn’t end well and got me hospitalized.
    
    Even if I reported them and got suspended, they were still persistent and still beat me up.
    
    So, out of fear, I did their projects until last year.
    
    And now that the project has been difficult. I’ve had enough of their requests and mustered my courage to fight back again.
    
    """
    show hideaki sad at correct_pos_hideaki with dis
    
    """
    But… that ended up me losing.

    """
    
    """
    I looked at him, and I can clearly tell he’s frustrated that he talks down to himself.
    
    """
    
    hideaki "If only, I have a bit of Tadao or Mamoru’s strength then maybe, things would have been different."
    
    mc "If you have done that then you’re probably not gonna last long in this school."
    
    show hideaki surprise at correct_pos_hideaki with dis
    hideaki "What do you mean?"
    
    mc """Strength comes in different ways, it’s not always the body sometimes it’s the brains.
    
    And your strength is in your head.
    
    """
    show hideaki sad at correct_pos_hideaki with dis

    hideaki "But because of this I always get beaten up."
    
    mc "Then you’re not using your brain enough."
    
    show hideaki surprise at correct_pos_hideaki with dis
    hideaki "?!"
    
    mc "Have you thought about asking for help from your parents? Your friends? Or even your teachers?"
    
    show hideaki sad at correct_pos_hideaki with dis
    hideaki "But that’s how a coward does…"
    
    mc "YOU! –"
    
    mc "*ahem*"

    """
    I almost lost my cool there for a second.
    """

    mc """I mean…. That’s your problem, you are prioritizing your pride.
    
    You think being a man must be able to take anything they threw at you? What are you? A masochist?
    
    Being a MAN is the ability to accept their weakness and be able to adapt, using their strengths. That is what a MAN is.
    
    In order to fight back, you must swallow your pride and accept that you are weak, and then use that strength of yours to your advantage.
    
    You are already brave, but you are not properly using your only strength that you have, that’s why you’re getting beat up.
    
    So think properly, sometimes the answer is right around you. You’ll just have to find it.
    
    """

    """
    I looked at him again and I saw a different him, even if it doesn’t show on his face, I can already call that he took what I said and put it onto his heart.
    
    Then Hideaki muttered something that I can’t pick up.
    
    """
    show hideaki serious at correct_pos_hideaki with dis
    hideaki "{size=10}I guess you’re not the same as them after all.{/size}"
    
    mc "What was that?"
    
    show hideaki happy at correct_pos_hideaki with dis
    """
    Hideaki stood up and smiled at me.
    
    """

    hideaki "It was nothing."
    
    """
    I smiled back in return.
    
    """

    mc "If you say so…"
    
    hideaki "Well I got to go to the cafeteria and buy some lunch for my friend… you don’t mind if I leave you here now?"
    
    mc "Oh don’t mind me, I’m just here because I want some time to myself."
    
    hide hideaki with dis 
    """
    He waved and went down, and I was left alone enjoying my lunch.
    
    """
    show hideaki sad at correct_pos_hideaki with dis
    hideaki "Oh Teacher, I almost forgot."
    
    """
    Hideaki came back with something to say.
    
    """
    mc "Hm? What is it?"
    
    show hideaki serious at correct_pos_hideaki with dis
    hideaki "Two week ago, Tadao did nothing wrong."
    
    mc "…"
    
    hideaki "If you want to know what happened? Talk to him."
    
    hide hideaki with dis
    """
    Hideaki went back, leaving me confused.
    
    Then it had me thinking.
    
    If what he said was true then I’ve falsely accused Tadao for that offense.
    
    But he already said that he did it.
    
    Wait… what if he was just covering up to someone.
    
    Hmm…
    
    """
    mc "I guess I have no other choice but to talk to him."
    
    """...*Bell Rang*...
    
    I guess I better go back now.
    
    """

    jump chap2_1

label to_open:
    #Option 2: Go to the Open Grounds
    "Hm… I guess eating under a tree is nice, and the scenery is good too, then open grounds it is."

    scene school_back with fade

    """
    I went on the back of school building, and I was met with a wonderful breeze of the floral arrangements of the school’s open grounds.
    
    I took the closest open seat and layout my lunch; 
    
    I have three slices of different sandwich types namely: a ham sandwich, vegetable sandwich, and grilled cheese sandwich; 
    
    And a can of Iced coffee latte which kept its cool inside my special container.
    
    """
    mc "Thank you for the food."
    
    """
    I was savoring my lunch while enjoying the scenery that these open grounds can give.
    
    It really feels comfortable here. It felt like a park dedicated solely on the people working and studying inside this school.
    
    It was a really quiet lunch break until a female student went outside followed by group of female students talking about something that I can’t understand due to the distance but I can clearly tell that the girl the group are following felt unsettled.
    
    The center of the flock of female students continues to point at the girl and making a weird face.
    
    I think she was mocking her.
    """
    show kazumi sad_away at correct_pos_kazumi with dis

    """
    
    Looking closely at the girl who is being mocked. I immediately recognize her face.
    
    It was Kazumi, and it seems she’s uncomfortable.
    
    Without having second thoughts, I went close to them.
    
    """

    student "And if you don’t mind, you’re being a nuisance to –"

    """
    I went in between of them blocking her eye contact from Kazumi and smiled.
    
    """

    mc "Excuse me miss, is there anything that bothering you with my student right here?"
    
    """
    Their face was in total shock as they never expect that a teacher will come.
    
    """

    student "[He] said it was her student? Friend, that’s the ‘Teacher from Hell’"
    

    """
    I looked at the center girl of this group and her face went pale…
    """

    student "U-umm… we – we’re sorry for troubling you… We-We’ll leave right away. Come on girls."
    
    """
    The group of girls went back in a hurry.
    """

    mc "I was just asking if there is any trouble, and they just left? Is that the new trend these days?"
    
    """
    I looked at Kazumi who is still frightened about what happened.
    
    I guess she’s fragile when it comes to these.
    """

    mc "Kazumi…"
    
    """
    I lend her my hand.

    """
    show kazumi surprise at correct_pos_kazumi with dis

    kazumi "Huh?"
    
    mc "I know you’re still frightened and can’t walk but; would you mind having a seat with me just to calm your nerves?"
    
    show kazumi sad at correct_pos_kazumi with dis

    """
    Kazumi nodded and slowly escorted her to a seat facing mine.
    
    """

    show kazumi happy at correct_pos_kazumi with dis
    kazumi "Thank you for what you did earlier."
    
    mc "Don’t mention it, any teacher would have done that, even if you are being hated."
    
    show kazumi sad at correct_pos_kazumi with dis
    kazumi "…"
    
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "Yeah I guess so…"
    
    """
    Looks like I stepped on that landmine again.
    
    I guess she’s trying really hard to forget it.
    
    """

    mc "Sorry..."
    
    show kazumi happy_away at correct_pos_kazumi with dis
    kazumi "It’s okay…"
    
    """
    She’s still a bit shaken, I guess she’s more uncomfortable in front of the [guy] that made her cry.
    
    I guess I need to break that first…
    
    """

    mc "Do you like coffee?"
    
    show kazumi sad at correct_pos_kazumi with dis
    
    kazumi "I’m not very fond of coffee, it’s too strong for me."
    
    """
    I pulled out another can from my special container and hand it over to her.
    
    """
    mc "Here…"
    
    show kazumi surprise at correct_pos_kazumi with dis
    kazumi "Hueh?"

    mc """It’s a can of Iced Mocha Latte; I’m sorry, I’ve already drank the latte, this the lightest coffee that I currently have right now.
    
    It’s a little bit stronger than cappuccino, but it’s still worth a try.
    """
    
    kazumi "…"
    
    show kazumi happy at correct_pos_kazumi with dis

    """
    Kazumi sighed and smiled.
    """

    kazumi "I guess I’ll try."
    
    """
    Kazumi opened and took a sip, and her expression speaks for itself.
    
    """
    show kazumi surprise at correct_pos_kazumi with dis

    kazumi "It’s tasty..."

    show kazumi laugh at correct_pos_kazumi with dis
    
    kazumi "It’s strong but, the chocolate makes it sweet and not bitter."
    
    mc "I’m glad you liked it, I think you haven’t eaten lunch yet, and coffee is acidic, why not grab one of the two sandwiches that I have here."
    
    show kazumi happy_away at correct_pos_kazumi with dis
    kazumi "Ah… it’s okay, my friend is getting my lunch for me from the cafeteria."
    
    mc "I see…"
    
    show kazumi laugh at correct_pos_kazumi with dis
    """
    We had some light talk here and there, and I taught her about coffee and its types which she enjoyed hearing about it.
    
    """
    show kazumi surprise at correct_pos_kazumi with dis
    kazumi "I can’t believe there are so many types of coffee."
    
    mc "Well, you don’t need to learn every single one, just find one coffee type that suits your taste then stick with it until you get bored and then the cycle repeats."
    
    show kazumi happy at correct_pos_kazumi with dis
    kazumi "I’ll keep that in mind"
    
    
    """
    I guess this is the perfect time to question her about her interaction with that group of women.
    
    """
    
    mc "Would you mind if we, change our topic?"
    
    kazumi "Not at all, what do you want to talk about teacher?"
    
    mc "About what happened earlier with the group of women. Why did they gang you up?"
    
    show kazumi sad at correct_pos_kazumi with dis
    """
    Kazumi immediately changed her expression. I guess she’s really fragile when it comes to her.
    
    But she’s not rattled this time.
    
    """
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "Ah... that…"
    
    kazumi "…"
    
    """
    She was silent for a moment but she continued.
    
    """

    kazumi "I actually don’t know… maybe jealousy?"
    
    mc "Hmmm… interesting… jealous of what though?"
    
    kazumi "Hmmm… maybe it’s because of how I look? From the way they insult me, it feels like it is directed on how I look… and how they’re irritated about it."
    
    """
    From her looks?
    
    Looking closely at her, she really is stylish but that’s not why those girls are irritated at her.
    
    """

    mc "Hmm…  *Looking closely*"
    
    show kazumi fluster at correct_pos_kazumi with dis
    kazumi "Uhh… Teacher? You’re making me embarrassed."
    
    """
    She was embarrassed and with that, I found what’s making those girls jealous.
    
    """
    mc "Ahh… so that’s why…"
    
    show kazumi surprise at correct_pos_kazumi with dis
    kazumi "Eh???"
    
    """
    I pulled out a mirror, and show it to her, reflecting her face.
    
    """
    mc "It’s because of that."
    
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "My face?"
    
    mc "No…"
    
    """
    Kazumi is puzzled? She’s moving her face in front of the mirror to find out what I was talking about.
    
    """

    mc "It’s you… it’s because you are naturally cute like that, that group of girls are jealous about you."
    
    show kazumi fluster at correct_pos_kazumi with dis
    kazumi "Hueh?!"
    
    """
    Realizing what I said, she buried her face in embarrassment.
    
    """
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "So it was me that they were jealous of."
    
    """
    Kazumi went silent again and felt down.
    
    I’ve seen this pattern before with my peers back in high school and I think I know what she’s going to say next. 
   
    """
    kazumi "Should I change back my appearance? I knew this getup will make things more complicated."
    
    show kazumi crying at correct_pos_kazumi with dis

    kazumi "I thought no one would bully me if I change but it turns out, the same thing happened."
    
    """
    Just as I thought, she starts to look down on herself, and I’m already getting pissed at it.
    """

    mc "Blasphemous!"
    
    """
    Shoot, why did I say it like I’m a royalty of something.
    """

    show kazumi surprise at correct_pos_kazumi with dis
    kazumi "Huh?"
    
    """
    I guess I’ll just roll with it.
    
    """
    
    mc """
    Those foolish women should learn a thing or two about your beauty.
    
    If they are just loathing at someone who is more beautiful than them, instead of bringing more effort in refining their own beauty, they will remain ugly for the rest of their life.
    """
    
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "But teacher, those girls are already beautiful, and really making an effort." 
    
    kazumi "Why would you say that they’re still ugly?"
    
    mc "You call those wretched women beautiful? Then I must call you a fool instead."
    
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "!?"
    
    """
    Looks like I went too far. I got to fix this immediately. 
    
    """
    
    mc """You think that beauty only shows on the inside? That is where you are wrong, young lady.
    
    Beauty is also what is inside your heart. You hone it by being kind to your people.
    
    And that beauty is what those girls’ problem or a lack thereof.
    
    So do not look down on your beauty, young lady. In fact, be proud of it, because that beauty cannot be obtained in a short amount of time.
    """
    show kazumi surprise at correct_pos_kazumi with dis

    mc """
    You also worked hard precuring it, you just did not know it, so don’t you dare lose it or you will end up like them.
    
    Forget those women, they are not worthy of your time.
    
    And if you stumble those women again and provoke you, I assure you, with that beauty of yours, a knight with shining armor will come to your aid.
   
    """
    kazumi "..."
    
    "Kazumi was captivated by speech for a while then laughed."
    
    show kazumi laugh at correct_pos_kazumi with dis
    kazumi "ppfffttt… ahahaha…"
    
    """
    I guess she realized it.
    
    """
    show kazumi happy at correct_pos_kazumi with dis
    kazumi "Teacher, stop with the act. I get it."
    
    mc "Sorry… I got too worked up that I just did it unconsciously."
    
    kazumi "But, thank you… that was really inspiring."
    
    mc "I’m glad that you get the message."
    
    kazumi "I guess now it’s my time to tell you something."
    
    """
    Hmm? What is it this time?
    
    She looked a me in a straight face that, I knew it was something serious.
    
    """
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "Remember what happened two weeks ago? When you sent Tadao to the principal’s office and got suspended for a week?"
    
    show kazumi sad at correct_pos_kazumi with dis
    kazumi "The truth behind is, Tadao didn’t do it."
    
    """
    Tadao didn’t do it?
    
    """

    kazumi "In fact, Tadao just lied that he took it, to save everyone from being suspended."
    
    """
    So, it was my threat that triggered Tadao to stand up.
    
    """

    kazumi "From what I can tell, no one stole the paper, and it just happen that the paper was obtained but, I don’t know where."
    
    show kazumi sad_away at correct_pos_kazumi with dis
    kazumi "I know you won’t believe me but, at least try to talk to Tadao. He knows everything what happened during that day."
    
    """
    And Tadao knew everything.
    """

    show kazumi happy at correct_pos_kazumi with dis

    """
    She stood up, while I was deep in thought.
    
    I looked at her, and I can see girl reborn, and inspired, like all the weight that she’s been holding for a long time have all been dropped.
    
    Now she’s ready to take on another challenge without breaking apart.
    
    """
    show kazumi surprise at correct_pos_kazumi with dis
    kazumi "Ah… I’ve stayed here for so long that I think my friend is now looking for me."
    
    show kazumi happy at correct_pos_kazumi with dis

    kazumi "Thank you, for everything you’ve to me until now, I really appreciate it."
    
    mc "No worries… I’m just doing what I do the most as a teacher."
    
    """
    Kazumi muttered something that I could pick up.

    """
    show kazumi happy_away at correct_pos_kazumi with dis
    kazumi "{size= 10} I think what you did just now was beyond the job of a teacher.{/size}"
    
    mc "Hm? You said something?"
    
    show kazumi happy at correct_pos_kazumi with dis
    kazumi "Ah… it was nothing."
    
    kazumi "Anyway, I’m going back first my friend is probably worried now."
    
    mc "Yup… Take care."

    hide kazumi with dis
    
    """
    Kazumi waved and came back inside, while I’m still lost in thought on what she said.
    
    Hm… so I might have made a mistake accusing Tadao.
    
    """
    
    "There’s only one thing to find out."
    
    mc "I guess I’ll have to talk to him after all."
    
    """...*Bell Rang*...
    
    I guess I better go back now.
    
    """
    jump chap2_1

label spec_int:
    if route == "hideaki":    
        show hideaki serious_away at correct_pos_hideaki with dis

        hideaki "Teacher, since we’re just waiting… can I use my handheld console to kill time?"
        
        """
        The whole class shockingly looked at him, like they saw his death wish or something.
        Then I immediately answered:
        """
        
        mc "Yeah… go ahead, just don’t play on loud speakers."
        
        show hideaki happy at correct_pos_hideaki with dis
        
        hideaki "Got it. Cool."

        """
        Hideaki pulled out his handheld console, plugged his earphone and starts to play with it.
        """
        hide hideaki with dis
    else: #Automatically picked Kazumi route
        #If picked Kazumi
        show kazumi fluster at correct_pos_kazumi with dis

        kazumi "Ummm… Teacher… since we’re waiting, c-can I use my phone just to kill time?"
        
        """
        The whole class shockingly looked at her, like they saw his death wish or something.
        
        Kazumi noticed them and flinched in cower.
        Then I immediately answered:
        """
        mc "Yeah… go ahead. As long as you’re not making too much noise."
        
        show kazumi laugh at correct_pos_kazumi with dis

        kazumi "Great."
        
        """
        Kazumi enthusiastically brought out her phone and fiddled with it. 

        """
        hide kazumi with dis
    jump chap2_2
    #-------------------------------------------------------------------------------------------------------------------------------
    
label thank_you:
    window show 
    with dissolve

    """
    Thank you, for playing the Demo of RE : SOLUTION

    It has been a fun development creating this game.

    Even with the sudden problems here and there I'm still happy that this demo will be out for you to enjoy.

    I'm actually quite dissapointed that this ended up with a \"cliff hangger\" end.

    And because of that I'm planning to expand it's story sometime in the future. (If I still have the motivation to write this story)

    But all in all Thank You and have a nice day. - Seishin
    """
    window hide 
    with dissolve
    pause (2.0)
    
    return # END OF GAME