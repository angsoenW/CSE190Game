#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "The Utopia"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Jasper Wang']
PROBLEM_CREATION_DATE = "11-SEP-2020"
PROBLEM_DESC=\
'''This version differs from earlier ones by (a) using a new
State class to represent problem states, rather than just
a dictionary, and (b) avoidance of list comprehensions
and the use of default parameter values in lambda expressions.

The following are new methods here for the State version of
the formulation:
__eq__, __hash__, __str__, and the implcit constructor State().

The previous version was written to accommodate the
Brython version of the solving client
and the Brython version of Python.
However, everything else is generic Python 3, and this file is intended
to work a future Python+Tkinter client that runs on the desktop.
Anything specific to the Brython context should be in the separate 
file MissionariesVisForBRYTHON.py, which is imported by this file when
being used in the Brython SOLUZION client.

The operators are defined here in the same order as on the
worksheet "Depth-First Search for the M&C Problem."

This version is compatible with the 2020 version of ItrDFS.py, which
gives a more detailed printout of its execution than older versions did.
'''

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>
'''pop up message explaining whats going on'''
'''intro to our title'''
#<COMMON_CODE>
class State:

  
  def __init__(self, old=None):
    # Default new state is a state objects initialized as the
    # initial state.
    # If called with old equal to a non-empty state, then
    # the new instance is made to be a copy of that state.
    self.role = -1
    self.has1op = False
    
    self.physHP = 100
    self.mentHP = 100
    self.money = -1
    self.socRLSP = -1
    self.famRLSP = -1
    
    self.others = True
    self.tC = 1
    
    self.Jes15Enable = False
    self.JesIsGoal = False
    
    self.Drs45Enable = False
    self.DrsIsGoal = False
    self.displayStage = 0

    if not old is None:
      self.role = old.role
      self.has1op = old.has1op
      self.physHP = old.physHP
      self.mentHP = old.mentHP
      self.money =old.money
      self.socRLSP = old.socRLSP
      self.famRLSP = old.famRLSP
      self.Jes15Enable = old.Jes15Enable
      self.others = old.others
      self.tC = old.tC
      self.JesIsGoal = old.JesIsGoal
      self.DrsIsGoal = old.DrsIsGoal
      self.Drs45Enable = old.Drs45Enable
      self.displayStage = old.displayStage

  def can_move(self, p, t):

#Initial role set:

    if self.role == -1 and p[0:4] == "set_":
      return True
    if self.role == 1 and p == "Jes" and t == 0:
      return True
    if self.role == 2 and p == "Drs" and t == 0:
      return True
    #if self.role == 3 and p == "Vct" and t == 0:
      #return True

#@Jessica consequential events:

    if self.role == 1 and p == "Jes" and self.has1op == False:
      if self.role == 1 and self.Jes15Enable and t == 1.5:
        self.Jes15Enable = False
        self.others = False
        self.has1op = True
        return True

#	@Jessica main story:

      if self.role == 1 and p == "Jes" and self.others == True and self.has1op == False:
        if t == self.tC:
          self.tC += 1
          self.has1op = True
          return True

# @Darius consequential story:
    if self.role == 2 and p == "Drs" and self.has1op == False:
      if self.role == 2 and self.Drs45Enable and t == 4.5:
        self.Drs45Enable = False
        self.other = False
        self.has1op = True
        return True

#@Darius main story:

      if self.role == 2 and p == "Drs" and self.others == True and self.has1op == False:
        if t == self.tC:
          self.tC += 1
          self.has1op = True
          return True

    
    return False
    

  def move(self,p,user_choice):
    news = State(old=self)
    if p == "set_Jes":
      news.role = 1
      news.physHP = 50
      news.mentHP = 55
      news.money = 50
      news.socRLSP = 65
      news.famRLSP = 75
      news.displayStage = 0
    
    if p == "set_Drs":
      news.role = 2
      news.physHP = 65
      news.mentHP = 60
      news.money = 30
      news.socRLSP = 65
      news.famRLSP = 55
      news.displayStage = 8
      
    if p == "Jes1" and str(user_choice) == "1":
      news.Jes15Enable = True
      news.has1op = False
      news.displayStage = 1
      print("  You are assigned to a three-leg race with Racheal and Taylor. During the game, their speed is too fast, you try very hard to follow their steps, but still always take the wrong foot, finally, all groups pass the line in time except yours. ")
    if p == "Jes1" and str(user_choice) == "0":
      news.socRLSP -= 5
      news.mentHP -= 5
      news.has1op = False
      news.displayStage = 1
      print("  You choose not to participate in the game. Few students noticed you and you are left alone with no friends...'")
      
    if p == "Jes1.5" and str(user_choice) == "1":
      news.others = True
      news.socRLSP -= 5
      news.mentHP -= 10
      news.Jes15Enable = False
      news.has1op = False
      news.displayStage = 1.5
      
      print("  Due to your poor English skill, they start making fun of your pronunciation. You can’t bear it anymore and run away angrily.")
    if p == "Jes1.5" and str(user_choice) == "0":
      news.socRLSP -= 10
      news.mentHP -= 10
      news.has1op = False
      news.others = True
      news.displayStage = 1.5
      print("  They become further intensified and shout at you loudly," + "\n" + " “You shouldn't even join this game, you are fat as a pig, and can’t even balance well.”" + "\n" + " Now, everyone in the playground stares at you, you are afraid of their eyesights and run away from the playground....")
    
    if p == "Jes2" and str(user_choice) == "1":
      news.money -= 15
      news.mentHP -= 10
      news.has1op = False
      news.displayStage = 2
      print("  Your roommate also invites her other friends to go shipping. You find a lovely dress but you are not silm enough to fit in that dress after you break the front side, but your friends can't stop laughing. Even your roommate is laughing at you. You feel angry and argue with them, finally you go back to the dormitory by yourself. But soon the whole school know this 'funny' story about you...")
    if p == "Jes2" and str(user_choice) == "0":
      news.socRLSP -= 5
      news.mentHP -= 5
      news.has1op = False
      news.displayStage = 2
      print("  Your roommate knows you are alone so she wants to introduce new friends to you through this experience. Even though she sincerely invited you, you still refused her. It really hurts her. Your relationship with her became worse and worse, eventually she applied to move to another dormitory...")
      
    if p == "Jes3" and str(user_choice) == "1":
      news.physHP -= 10
      news.mentHP -= 10
      news.socRLSP -= 10
      news.has1op = False
      news.displayStage = 3
      print('  Others trust Richeal because your reputation is bad and your English is not fluent. The crowd starts blaming you,' + "\n" +  """  "This fat Korean girl means it. She poured the juice because she is envious and she wants to catch others attention." You two end up with fighting...""")
    if p == "Jes3" and str(user_choice) == "0":
      news.money -= 20
      news.mentHP -= 10
      news.socRLSP -= 10
      news.has1op = False
      news.displayStage = 3
      print("  Even though you paid her more than the dress’s price, the girl doesn’t put this down. Her and her friends keep spreading about behind youOthers thought you intentionally poured the juice because you envy that she is more beautiful than you, which made your reputation very bad....")
    
    if p == "Jes4" and str(user_choice) == "1":
      news.physHP -= 15
      news.mentHP -= 10
      news.socRLSP += 5
      news.has1op = False
      news.displayStage = 4
      print('  However, Norris is very mean, he and his friends make fun of you and said,' + "\n" + '''“  if you can lose 80 pounds, I might start to consider dating with you." You can’t bear the person you like laughing at you, and decide to prove yourself that you can do it. You start lifting and be on diet everyday...''')
    if p == "Jes4" and str(user_choice) == "0":
      news.mentHP -= 10
      news.has1op = False
      news.displayStage = 4
      print("Unfortunately, a gorgeous-looking girl likes him and falls in love with him. You feel pity and realize that you are not attractive enough. You start lifting everyday to make yourself in shape...")
    
    if p == "Jes5" and str(user_choice) == "1":
      news.physHP -= 15
      news.mentHP -= 10
      news.has1op = False
      news.displayStage = 5
      print('  You run away from the dormitory to home during the night, but your parents are not here. You wait until 11 pm. It seems they won’t be back today, but you are about to collapse. You really need someone to talk to, so you call them again and again. Unfortunately, their phones are always busy. You hear the phone ring once and once again". ' + "\n" + ' "  At 3 in the morning, your father finally picks up the phone. "  You finally feel relieved and quickly tell him about the rumor.' + "\n" + '  However, your father said angrily,' + "\n" + ' “  I have no time to deal with your girly school things, go to your teacher to ask for help because that’s what I paid for."' + "\n" + '  Then he hangs up.' + "\n" + '  It’s raining outside, you stare at the window all night until the sunrise. ' + "\n" + '  You quickly get up and run back to the dorm. Because nobody is trying to help you, the bullies become more unscrupulous...')
    if p == "Jes5" and str(user_choice) == "0":
      news.physHP -= 10
      news.socRLSP -= 10
      news.has1op = False
      news.displayStage = 6
      print("  Your teacher found the person who circulated the rumor and gave them detentions." + "\n" + "  However, you now have a special nickname “the gooky songbird” and more students get to know the rumor. Norris laughed when he heard that rumor, thinking you are a coward...")
      
    if p == "Jes6" and user_choice == None:
      if news.mentHP > 10:
        news.JesIsGoal = True
        news.displayStage = 7
        print("  You beg your parents for transfering to another school. Your parents are confused why you are so insisted for transfering and they blame you for not knowing how to behave property... ")
      if news.mentHP <= 10:
        news.JesIsGoal = True
        news.displayStage = 7
        print("  You stayed at The Utopia High School until you graduate. However, every minutes was cruel during the four years. After graduating from that school, you are dignosised with serious mental disorders and those brutal scenes keep flashing back in your head. Life loses colors and you are now looking for an end on your miserable life... ")
    
#Darius' story
    
    if p == "Drs1" and str(user_choice) == "1":
      news.mentHP += 5
      news.has1op = False
      news.displayStage = 9
      print("  The boy looks up and starts telling Darius the stories behind all of his drawings. They had a great conversation by the end of the group discussion, and both of them feel they are being listened to for the first time...")
    if p == "Drs1" and str(user_choice) == "0":
      news.socRLSP -= 10
      news.mentHP -= 20
      news.has1op = False
      news.displayStage = 9
      print("  You didn’t do anything and students get to know you by make the teacher assign you a teammate the first day of class...")
      
    if p == "Drs2" and str(user_choice) == "1":
      news.socRLSP -= 15
      news.mentHP -= 20
      news.has1op = False
      news.displayStage = 10
      print("  You and your teammates start arguing at the sideline to an extent that you guys have to be separated by others. Walking into the locker room, no one talks to you, and everyone is shaking their heads. Although the coach stands up for you, saying that there was a lot of time to process what's going on, we will win the next one. One of your teammates still says you could have passed the ball...")
    if p == "Drs2" and str(user_choice) == "0":
      news.socRLSP -= 5
      news.mentHP -= 20
      news.has1op = False
      news.displayStage = 10
      print("  Although you apologize for your decision making on the last shot, you feel like your teammates are all disappointed at you, saying" + "\n" + """ "  I thought you were better than this.”...""")
      
    if p == "Drs3" and str(user_choice) == "1":
      news.socRLSP -= 10
      news.physHP -= 15
      news.has1op = False
      news.displayStage = 11
      print("  You stand up for yourself and confront them. However, as they keep saying you took bribes for the game loss, you hit one of them and knock him down while the other runs out of the restroom and calls the security. " + "\n" + "  The next thing you know is that you are sitting in the principal's office, waiting for your mom to come...")
    if p == "Drs3" and str(user_choice) == "0":
      news.socRLSP -= 10
      news.mentHP -= 20
      news.has1op = False
      news.displayStage = 11
      print("  You did not say anything to them. All you did is to put your head down and walk out of the restroom." + "\n" + "  Meanwhile, you can not believe what has been said about you. You are angry, sad, disappointed, and unmotivated...")
      
    if p == "Drs4" and str(user_choice) == "1":
      news.mentHP += 5
      news.socRLSP -= 15
      news.has1op = False
      news.Drs45Enable = True
      news.displayStage = 12
      print("  You officially quit the team after having a conversation with the coach. " + "\n" + """ “  Hopefully I am making the right call. God, please look out for me.”...""")
    if p == "Drs4" and str(user_choice) == "0":
      news.socRLSP -= 10
      news.mentHP -= 15
      news.has1op = False
      news.displayStage = 12
      print("  You often miss practice, and feel unmotivated and ashamed of yourself. You want to change but you don't know how...")
      
    if p == "Drs4.5" and str(user_choice) == "1":
      news.socRLSP -= 5
      news.mentHP -= 20
      news.others = True
      news.Drs45Enale = False
      news.has1op = False
      news.displayStage = 13
      print("  The boy being bullied watches you walking away. He doesn’t expect you would do anything but still, he wishes you could have been in his shoes. Being helpless is the worst thing ever...")
    if p == "Drs4.5" and str(user_choice) == "0":
      news.physHP -= 15
      news.socRLSP += 5
      news.others = True
      news.Drs45Enale = False
      news.has1op = False
      news.displayStage = 13
      print("  The bully and his buddies tell you to knock it off. You, on the other hand, walk up to them and order them to leave the boy alone. Of course, they did not listen to you and start pushing you. You did not back down and warn them that what they did has been recording the whole time. If you do not want to get expelled, you better leave right now...")
      
    if p == "Drs5" and str(user_choice) == "1":
      news.money += 10
      news.has1op = False
      news.displayStage = 14
      print("  Now, it’s midnight. Mom should be asleep. Time to go get some cash,” " + "\n" + "Darius thought. Sneaking into his mom’s bedroom, he unlocks the safety in the closet and takes out about $1,000." + "\n" + " He leaves the scene after quietly putting everything back to place. Next day, right after school, he goes to a shopping mall and buys a pair of jordans, a 18k chain, and a red Supreme hoodie. "  + "\n" +  "  They will never laugh at me ever again” he thought...")
    if p == "Drs5" and str(user_choice) == "0":
      news.socRLSP -= 20
      news.mentHP -= 20
      news.physHP -= 15
      news.money += 5
      news.has1op = False
      news.displayStage = 14
      print("  During lunch time, he doesn’t go eat lunch as usual; rather, he follows one of his classmates into the restroom. " + "\n" + "  “Imma beat him up and take his shoes, wallet, clothes, everything!” he thought. However, little he knows, he just could not do it. The robbery was not simple greed and malice as he expected. you walk out of the restroom with nothing more than his own empty pockets...")
      
    if p == "Drs6" :
      if news.mentHP > 10:
        news.DrsIsGoal = True
        news.displayStage = 15
        print("  Then, you passed out. When you open your eyes again, you are handcuffed on a bed. Bewildered, looking around, it appears like you are in a hospital. " + "\n" + "  Police officers are standing outside of your room. You barely remember what happened, but you are sure a judge will let you know...")
      if news.mentHP <= 15:
        news.DrsIsGoal = True
        news.displayStage = 15
        print("  You feel the satisfaction better than ever, even though killing someone is never something you dream or are proud of before that bully says those words about your mom. " + "\n" + "  You walking out of  the room, pulling out you gun, start to kill students that bullied you before. Students mourning, screaming and crying. " + "\n" + "  About 5 minutes after, you hear a shot that was not from you, realizing polices arrived and shot you. " + "\n" + "  You pick up the revolver and motion it towards your mouth; crying out loud with strange smile, you keep saying sorry to your mom: “Mom, you should’ve took me with you on that day”. Darius thought: “hey mom, we gon meet again. Just wait”")
      
    
    
    
    return news

  def describe_state(self):
    txt = "Hello World"

    return txt


  def is_goal(self):
#    if self.mentHP <= 10 or self.physHP <= 10:
#      return True
    if self.JesIsGoal:
      return True
    if self.DrsIsGoal:
    	return True
    return False
      
    

  def __eq__(self, s2):
    if s2==None: return False
    if self.role != s2.role: return False
    if self.has1op != s2.has1op: return  False
    if self.physHP != s2.physHP: return False
    if self.mentHP != s2.mentHP: return False
    if self.tC != s2.tC: return False
    if self.money != s2.money: return False
    if self.socRLSP != s2.socRLSP: return False
    if self.famRLSP != s2.famRLSP: return False
    if self.Jes15Enable != s2.Jes15Enable: return False
    if self.JesIsGoal != s2.JesIsGoal: return False
    if self.others != s2.others: return False
    return True

  def __str__(self):
    Cname = "None"
    if self.role == 1:
      Cname = "Jessica"
    if self.role == 2:
      Cname = "Darius"
    if self.role == 3:
      Cname = "Vincent"
    if self.role == -1:
      st = "No students has been choosen."
    if self.role != -1:
      st = "Student: " + Cname + "." +"\n" + "role:" + str(self.role) + "\n" + "Stauts: " + "\n" + "Mental health: " + str(self.mentHP)+ "\n" + "Physical health: " + str(self.physHP) + "\n" + "Money: " + str(self.money) + "\n" + "Social relationships: " + str(self.socRLSP) + "\n" + "Family relationships: " + str(self.famRLSP) + "\n"
    return st

  def __hash__(self):
    return (str(self)).__hash__()

  def goal_message(self):
    return "Demo is finished and Thanks for playing"

def copy_state(s):
  return State(old=s)


class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_STATE = State()
#</INITIAL_STATE>

#<OPERATORS>

#Role Selection Part:

phi0 = Operator('''Player selection 1: Jesscia. You immigrated from Korea to the United States a few years ago. You are introverted and care about what others think about you. Your parents are flight attendants and barely have time to company with you, but they very care about your education and values. After hearing about the Utopia concept, they decide to send you to Sainvint High School.'''+"\n",
  lambda s: s.can_move("set_Jes", 0),
  lambda s: s.move("set_Jes",0))

phi1 = Operator('''Player selection 2: Darius. You grew up in a small neighborhood with your parents. However, when you were young, other kids in your community often say you have no father because your mom was cheated but she chose to keep you alive. You remember your dad rushed out of the house without even saying goodbye; it was the last time you saw him. Your mom took full responsibility, worked double shifts, and made sure that you were fed up even when she was not. There was always something going on in your old community: police brutality, crime, poverty. Now, you are 15 years old, and your mom decides to take you and start a new life somewhere else. Y'all come all the way from Brooklyn to Camden, a small city near Philadelphia, and you go to Sainvint High School as a transfer sophomore.''',
  lambda s: s.can_move("set_Drs", 0),
  lambda s: s.move("set_Drs",0))

phi2 = Operator('''This is a blooper operator, have a good day:) ''',
  lambda s: s.can_move("sethgj_V", 89),
  lambda s: s.move("setfgh_hVct",89)) 

#Jessica's Story

phi3 = Operator('''Ice breaker activity: on the first day of school, all freshmen gather together and do some ice breaker game, would you join the game?  (type 3 to continue)''',
  lambda s: s.can_move("Jes", 1),
  lambda s: s.move("Jes1",input("Type 1 for yes and 0 for no. --->> "))) 

phi4 = Operator('''Two girls start blaming you “if you could run faster, we’ll win the game”, you decide to: (type 4 to continue)''',
  lambda s: s.can_move("Jes", 1.5),
  lambda s: s.move("Jes1.5",input("1 to make excuses and 0 to apologize. --->> ")))

phi5 = Operator('''During weekend, your roommate invite you to go shopping with her, what would you do?(type 5 to contine)''',
  lambda s: s.can_move("Jes", 2),
  lambda s: s.move("Jes2",input("1 for Yes and 0 for No. --->> ")))
  
phi6 = Operator('''Your school holds a homecoming party, you were interested and went to the party. In the homecoming party, Racheal intentionally tripped you, made your juice poured and stained another girl’s dress. And Richeal blaming at you first, you decide to: (type 6 to contine)''',
  lambda s: s.can_move("Jes", 3),
  lambda s: s.move("Jes3",input("1 to argue with her and 0 to keep slience and pay for the dress. --->> ")))
  
phi7 = Operator('''Few weeks past, you start to like a handsome boy (Norris), but Norris seems indifferent to you. You decide to: (type 7 to contine)''',
  lambda s: s.can_move("Jes", 4),
  lambda s: s.move("Jes4",input("1 to propose to him and 0 for doing nothing. --->> ")))
  
phi8 = Operator('''After the Christmas break, you found a note from the classroom that said “Jessica is an illegitimate child and was thought of the shame of her yellow family. Jessica was abandoned when she was born, such a solitary orphan XD. ” You are very angry, but you don’t know how to deal with it, You decide to: (type 8 to contine)''',
  lambda s: s.can_move("Jes", 5),
  lambda s: s.move("Jes5",input("1 to ask your parents for 0 to ask your teacher for help. --->> ")))
  
phi9 = Operator('''With your consistent effort, you finally lose 80 pounds but you now have serious anorexia. Norris was also shocked by you when he saw you and surprisingly complimented you, which made you very happy. After school, when you are planning to find Norris, a girl forces you to go to the bathroom with her. When you enter the bathroom, Racheal and five other girls are also here, they seem waiting for you for a long time. They locked the door and blocked your mouth. You try to resist but you are exhausted due to the diet. Racheal laughing at you evilly “I’ve heard you like Norris.” She takes out a clipper from the pocket and strokes your hair slowly “look at your lovely hair, do you think Norris will like you if you are a monk?” Then you see strands of hair fall on the ground, which break your pitiful hope...(type 9 to contine)''',
  lambda s: s.can_move("Jes", 6),
  lambda s: s.move("Jes6", None))


#Darius's Story

phi10 = Operator('''Today is your first day of class. After being dropped off, you notice that most people drive their own vehicles to school; they seem friendly, chatting and joking with their buddies. As the first bell rings, you walk into your first class, History. The teacher greets everyone and asks students to share how their summer went. “We will do groups of four, let’s go!” The next thing you know, you are left out as well as another boy at the other corner of the classroom. Would you go up and talk to him or just sit on your chair...?(type 10 to contine)''',
  lambda s: s.can_move("Drs", 1),
  lambda s: s.move("Drs1", input("1 to go up and talk to him and 0 to sit on the chair and do nothing. --->> ")))
  
phi11 = Operator('''You have been playing basketball since you were 6 years old. Growing up, you always wanna be an NBA player because you hope basketball is your way out. After trying out for basketball, you got in the Sainvint varsity team. Today, it is your first game as a starter. You can’t wait to show off your skills and impress everyone. Despite you playing very hard, 20 pts and 8 rebounds, your team is down 2 pts with 3 seconds left on the clock. The ball is in your hands, and you push it to the front court. Although you see a teammate is wide open, you want to be the hero so you shot a three with tough defense. Unfortunately, you did not make it. You have two options: Blame teammates for their terrible performance or acknowledge your fault...(type 11 to contine)''',
  lambda s: s.can_move("Drs", 2),
  lambda s: s.move("Drs2", input("1 to blame teammates and 0 to acknowledge fault. --->> ")))
  
phi12 = Operator('''Next day, when you come to school, you notice that everyone is giving you a weird look. You could not figure out why until you hear two people discussing you in the restroom. “Yo, have you heard, Darius intentionally lost the game last night,” one of them said. “Nah, why do you say that?” the other asks. “Coz he definitely saw his teammate is wide open, but he decided to shoot the ball. He is bought off because he is broke.” Now you have two options, either go argue with them or go out of the restroom without saying anything...(type 12 to contine)''',
  lambda s: s.can_move("Drs", 3),
  lambda s: s.move("Drs3", input("1 to fight for yourself and 0 to remain silence. --->> ")))
  
phi13 = Operator('''Because of rumors and what happened, your teammates no longer trust you and your coach thinks you are not capable of his team. You start feeling miserable during practices. You don’t want to be on the basketball team anymore. Plus, instead of going to practice, getting a part-time job after school might help your family a lot. What would you do...?(type 13 to contine)''',
  lambda s: s.can_move("Drs", 4),
  lambda s: s.move("Drs4", input("1 to quit the team and 0 to stay. --->> ")))
  
phi14 = Operator('''One day, on the way to your work place, you saw a student giving a hard time to another student who is keeping his mouth shut. Their conversation is about why he did not let him cheat on the exam. You notice that the bully is about to hit him, you decide to...?(type 14 to contine)''',
  lambda s: s.can_move("Drs", 4.5),
  lambda s: s.move("Drs4.5", input("1 to step away and 0 to help him out. --->> ")))
  
phi15 = Operator('''Your family barely has any money. When you need clothes, your mom takes you to resale shops or charity organizations. When you wear used stuff to school everybody notices. Your classmates start making fun of you for being poor and throwing trash every day during lunch. You decide to do something. As you walk on the way home, you have an idea. “Why can’t I be a bully, too? Stealing sh*t, selling drugs, easy money! Look at all of them bullies, they are stacked. Plus, they are not getting into any troubles for bullying me. Imma do something like that, too.”, Darius thinks that way. What would he do?..?(type 15 to contine)''',
  lambda s: s.can_move("Drs", 5),
  lambda s: s.move("Drs5", input("1 to steal cash from his mom and 0 to beat a freshman up and take his lunch money. --->> ")))
  
phi16 = Operator("\n" + "One day, you are waiting for your mom to pick you up as she promised. After 10 mins, she is still not here. You sigh impatiently and decide to call her." + "\n" + "Darius: Mom, your coming? It’s cold outside. When are you gonna be here?" + "\n" + "Mom: D, i’m on my way. I had some extra work to do. You wanna eat Chick-fil-A? Imma pick some on the way." + "\n" + "Darius: Nooo, mom! I don’t wanna no chicken sandwiches. Can you buy me some sushi tonight maybe?" + "\n" +"Mom: Aight, if you say so. Imma just turn around real quick and go get some sushi instead." + "\n" + "Darius: Thank you mom. You are the best!" + "\n" + "Mom: “Whatever, I’ll see you in…"+ "\n" + "BANG! The phone was dropped" + "\n" + "Darius: Mom Mom you okay? Can you hear me? What happened???" + "\n" + "She does not respond. "+ "\n" + "Darius: “talk to me Mom, talk to me!” You start losing control and have no clue what to do..." + "\n" + "The next thing you know, whether you believe it or not, your mom, the one cares the most about you is gone. Everything has changed ever since, except one thing---the bullies are still picking up on you. Now, they start making fun of your dead mother. " + "\n" + "Bully: You that little mohterfucker without no momma huh? I would think about adopting you if you called me daddy. Huhhuhhuhhuh~" + "\n" + "Darius says nothing. " + "\n" + 
"Bully continues: You are scared like a bitch. Look at you, your mom should’ve took you with her. Laugh out Loud~"+ "\n" + 
"Bullies walk away. You stare up, emotionlessly, and tighten your fists. You thought: you are not getting away with this."+ "\n" + "Next day, in a black hoodie, you casually get to the school in the morning, go to classes, and eat lunch. After school, you stop the bully. "+ "\n" + "Darius: hey, yo, can i talk to you for a second. I have something for you"+ "\n" + 
"Bully look shocked as if it were the first time he heard Darius talking." + "\n" + "Bully: what’sssup, my son. What you gonna say to your daddy.” he feels smug." + "\n" + "They went into an empty classroom, just them two. Darius closes the door and locks it up." + "\n" + "After a few moments, darius says: I would like you to apologize for making fun of my mom." + "\n" + 
"Bully: hahahh. I dare you to say it one mo time. You funny. What are you on today? Let me get some dope you had. For real, what you want?"+ "\n" +  "Darius: I’m serious. Say you are sorry!"+ "\n" + "Bully: Hellll nah, Fuck you and fuck your mom, too. What you gonna do? Beat me up? Kiss my ass you lil pussy."+ "\n" + "After a few moments of silence, you look up and stare the bully right into his eyes. Your cold look reflected on the face gave him shudders. Your hands were tightly closed around the cold surface of the metallic revolver. No sense of humanity or sympathy shown. You then point the gun to his head as he suddenly takes a few steps back and raises his hands up. You see his lips moving but you dont hear anything. You move towards him, smiling, enjoying the last moments of his life." + "\n" + "Darius: You will pay the prize" + "\n" + "Your heart seemed to be made of stone, the way you pulled the trigger. At that exact moment, your body shudders as if you wake up from a nightmare. You look around, a stream of blood dripping out of the skull. Motionlessly, you collapse down to the ground. You had smelt of blood, but that doesn’t make you feel pleasant; rather, you are emotionless...(type 16 to contine)",
  lambda s: s.can_move("Drs", 6),
  lambda s: s.move("Drs6", None))
  
OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7, phi8, phi9, phi10, phi11, phi12, phi13, phi14, phi15, phi16]
#</OPERATORS>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>

#</STATE_VIS>
