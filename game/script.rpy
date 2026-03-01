# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Calypso")

define b = Character("Bomfey")

define d = Character("Dwight")

define N = Character("You")

define n = Character("")

define k = Character("Officer Knees")

define t = Character("Officer Toes")

image LivingRoom = "images/bgs/Living.png"
image Kitchen = "images/bgs/Kitchen.png"
image Deaddavey = "images/bgs/Deaddavey.png"
image Necklace = "images/bgs/Hand.png"


transform far_right_down:
    xpos 1.0
    xanchor 1.0
    ypos 1.0
    yanchor 1.0

transform left:
    xpos 0.0
    xanchor 0.0
    ypos 1.0
    yanchor 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene deaddavey
    with Dissolve(0.5)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show test sprite

    style window background "#00000000"
    n ""

    # These display lines of dialogue.

    

    style window background "#000000A2"
    
    N "Is that..."

    N "Is that Davie??"

    show k_oops at far_right_down 
    

    k "Hey kiddo. You wouldn't happen to be Davie's sibling, would ya?"

    N "uhh... yeah that's me."
    hide k_oops
    show k_uhmm at far_right_down

    k "I'm so sorry, I hate to break it to you but-"
    hide k_uhmm
    show k_reaction at far_right_down
    show t_speaking at left

    t "{size=+10} DAVIE IS DEAD"

    N "..."
    hide t_speaking
    hide k_reaction
    show t_idle at left
    show k_normal at far_right_down

    k "...we need to tell you something."
    hide t_idle
    hide k_normal
    show t_speaking at left
    show k_reaction at far_right_down

    t "{size=+10}THEY WERE MURDERED"
    hide k_reaction
    hide t_speaking
    show t_idle at left
    show k_mann at far_right_down

    k "...Davie was found dead in a ditch. We suspect blunt head trauma, but it seems too severe to be accidental."

    N "Oh wow..."

    N "How is this possible?? I only dropped them off here a couple hours ago!"

    N "I can’t believe it..."
    hide k_mann
    show k_normal at far_right_down

    k "I understand you’re probably in shock. We’d appreciate if you could help us out. Is there any information you have that could help us with investigating this case? "

    N "I-I don’t know... I just got here."
    hide k_normal
    show k_oops at far_right_down

    k "Hmm... maybe you could help us by asking the others some questions? We’ve tried asking around a bit, but they’re understandably frightened. Maybe you’d have more success."
    hide t_idle
    show t_speaking at left
    hide k_oops
    show k_srsly at far_right_down

    t "Yeah, we needa find {size=+10} WHODUNNIT"
    
    N "um, o-ok? I guess I can try asking around..."
    hide t_speaking
    show t_idle at left
    hide k_srsly
    show k_normal at far_right_down

    k "Good luck, and remember to let us know if you find out anything."
    hide k_normal
    hide t_idle

    
    menu:
        n "{i} You go into the house, and head to the living room.{p=1} Who will you talk to first?{/i}"
        "Bomfey":
            jump choice2_Bomfeyfirst
        "Dwight":
            jump choice2_Dwightfirst

label choice2_Bomfeyfirst:
    jump BomfeyTalk
    jump DwightTalk
    jump after_LR

label choice2_Dwightfirst:
    jump DwightTalk
    jump BomfeyTalk
    jump after_LR

label BomfeyTalk:

    scene LivingRoom
    with Dissolve(0.5)
    show b_frustrated
    b "You! You’re here."
    b "Did you hear what happened?? I don’t know what’s happening?!"
    hide b_frustrated
    show b_idle
    b "The officers are being very discreet, they didn’t even let us see Davie!"
    N "Yeah… I just heard from them now."
    N "Uh… Where were you during all this?"
    hide b_idle
    show b_joyful
    b "Ohhh yes! Me and my fam were out for some fishing for ‘BBMF’. Today was nice and sunny… mmm, and there were also plenty of fish!"
    hide b_joyful
    show b_idle
    b "That is… Until I got the call from Dwight…"
    N "Dwight? Did he tell you about the death first?"
    b "No, not that…"
    b "Do you not know about the proposal…?"
    N "Proposal? What proposal?"
    hide b_idle
    show b_frustrated
    b "I don’t think I’m the one who should be telling you this."
    N "Uh-"
    b "Actually, did you know about what was happening? I’m sure you would’ve…"
    hide b_frustrated
    show b_crash out
    b "You’re their sibling for goodness sake! You knew, didn’t you?? You knew and you didn’t tell me… Why didn’t you tell-"
    N "Woah, look I don’t even know what you’re talking about!! Plus, Davie and I… weren’t that close. They wouldn’t have told me anyway."
    hide b_crash out
    show b_idle
    b "I just… this has all been too much. I don’t really know…"
    N "Look, I can see you’re pretty upset so uh… I’m gonna go. Um, thanks for answering some questions? "
    hide b_idle
    n "{i}Bomfey looks confused, but you leave before they have the chance to respond.{/i}"

label DwightTalk:    
    scene LivingRoom

    show deyebrow
    d "What do you want?"
    N "Uhh… can you tell me about what happened tonight?"
    hide deyebrow
    show dconfused
    d "… I wish I didn’t know. Ugh, I’m only at this party since I live here. My roommate G. Angle… she’s always throwing these stupid parties! {p} I knew it’d be trouble. "
    N "... {p=1} So, uhh… What happened tonight?"
    hide dconfused
    show dangry
    d "Seriously? Haven’t you heard enough yet? Everyone’s been talking about it."
    N "About what exactly?"
    hide dangry
    show dchill
    d "…the proposal"
    N "Proposal?"
    hide dchill
    show ddisgust
    d "Ugh, that jerk! They’ve been dating my best friend for ages, and yet…"
    N "…huh?"
    d "I was really mad with Davie after that, and we got into a bit of a fight…"
    hide ddisgust
    show dangry
    d "A verbal fight, I mean. I called Bomfey immediately after, then I went to my room to try calm down by doing some studying."
    N "Right…"
    hide dangry
    show dshock
    d "Ugh, Davie’s such a jerk. We had to work together one time for a group project, and they did nothing and took credit for all my work! They’ve always been so rude to me…"
    N "Oh, that’s not—"
    hide dshock
    show dsmirk
    d "Well maybe if they weren’t such a jerk, they wouldn’t have ended up dead in a ditch."
    N "…"
    d "..."
    N "I’m gonna… go now."
    N "Thanks for, uh…"
    hide dsmirk
    n "{i}You leave.{/i}"

label after_LR:
    n "{i} You head to the kitchen to grab a drink of water.{/i}"

    scene Kitchen
    n "{i}You see Nine and Calypso in the kitchen. You nod to Nine, who nod's back."
    show cside
    c "Oh, you’re here!"
    N "Mhm. So uh… can you tell me what happened tonight?"
    hide cside
    show ccry
    c "Oh, it was so awful!! It’s been such a blur…"
    N "Can you try tell me what you remember?"
    hide ccry
    show cside
    c "Well, I remember feeling like Davie was ignoring me for the first part of the party. I was with my friend, Nine, while Davie was laughing with their friends."
    c "Eventually they approached me and… um."
    N "And?"
    hide cside
    show cshade
    c "Well, they yelled to get the attention of the room, and um… proposed to me."
    N "Davie proposed to you?? But I thought they were dating Bomfey!"
    c "They were, apparently… "
    c "I didn’t know that!!"
    c "The proposal itself felt really strange… we hadn’t been together for that long, so I was confused. And the whole thing felt really off."
    hide cshade
    show ccry
    c "Then Dwight came up and started yelling at Davie, which is how I found out that they were dating Bomfey. I couldn’t believe it! I felt so betrayed."
    c "Then Davie claimed that the proposal had been a dare from one of their friends, and that it was all “a joke."
    N "Oh wow."
    c "I was mortified. Nine dragged me to the nearby GYG to get away from the party."
    hide ccry
    show cgyg
    c "I’ve gotta admit, it did make feel a bit better."
    N "How come you came back here?"
    hide cgyg
    show cside
    c "Nine convinced me to break things off with Davie, tonight. But when we came back-"
    hide cside
    show ccry
    c "We heard sirens and there were police and they were questioning people a-and, and then I saw Davie’s body so I started crying again and I think they were missing their necklace and—and…"
    n "{i}Huh… their necklace?{/i}"
    c "…sorry"
    N "No, it’s fine. I’ll uh, I’ll leave you be. Thanks for telling me about what happened."
    hide ccry
    n "{i}Calypso nods, and you walk away. You decide to head back to the police.{/i}"

    
label police2:
    scene Deaddavey
    show k_normal at far_right_down

    k "Ah, Kiddo. You’re back. Did you manage to talk to everyone?"
    N "Yeah… I talked to everyone. They’re all pretty shaken."
    show t_speaking at left
    t "GOOD. SHAKEN PEOPLE SPILL SECRETS"
    hide k_normal
    show k_mann at far_right_down
    k "Well… anything stand out?"
    t "SPILL THE BEANS"
    hide t_speaking
    show t_idle at left
    N "Well… Bomfey said Davie proposed to Calypso in front of everyone. Dwight said they got into a fight after that. And Calypso mentioned that Davie’s necklace was missing when she saw the body."
    hide k_mann
    show k_normal at far_right_down
    k "Missing necklace… interesting."
    N "I just… wanted to give you everything I heard. Bomfey was confused, Dwight was angry, Calypso was crying. Everyone’s really shaken."
    N "They all disliked Davie; Bomfey and Calypso felt betrayed and Dwight… he seemed to really dislike Davie. Oh, they all had alibis though. "
    k "You did good. We’ll let our chief, Officer Head, know what’s happened."
    t "SHOULDERS STAYED HOME SICK TODAY"
    k "… We’ll let them know too. Anyway, go take a breather, alright? We’ll probably be heading off soon, give us a call if you need anything. Stay safe, kid."
    N "Thanks, officers."
label end:
    scene black
    n "{i}You head to the bathroom to catch your breath.{/i}"
    scene Necklace
    n ""


    return
