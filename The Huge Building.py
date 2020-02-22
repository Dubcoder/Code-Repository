def building():
    print "You've entered a huge building and you are very poor."\
    " You have to make some decisions so you can build a house. What will you do?"
    answer1 = raw_input("There a 3 staircases wich one do you choose? 1,2,or 3 ")
    if answer1 == "1":
        answer2 = raw_input("Now you have 3 tools, a knife, an electric chair, or a saw. "\
                            "The options are knife, chair, or saw. ")
        if answer2 == "knife":
            print "Your a good hunter! You won't be needing groceries anymore."
        elif answer2 == "chair":
             print "Nice chair for a house."
        elif answer2 == "saw":
            print "You cut some wood and made a log house!"
        else:
            building()
    elif answer1 == "2":
        answer3 = raw_input("You have 3 items, a drill, a hammer, or a nail. "\
                            "The options are drill, hammer, or nail. ")
        if answer3 == "drill":
            print "Your were drilling a hole to make a house but accidently drilled your hand."
        elif answer3 == "hammer":
            print "You are making a house using a hammer as a tool."
        elif answer3 == "nail":
            print "You don't have a hammer."
        else:
            building()
    elif answer1 == "3":
        answer4 = raw_input("You have 3 items, a needle, diamonds, or a stick. "\
                            "The options are needle, diamonds, stick. ")
        if answer4 == "needle":
            print  "You knitted a sweater to keep warm in your tough life of making a house!"
            exit(0)
        if answer4 == "diamonds":
            print "You have $50,000,000! Now you can buy a house and everything to go with it."
            exit(0)
        if answer4 == "stick":
            print "You poked yourself and fainted!"
            exit(0)
        else:
            building()
    else:
        building()
building()