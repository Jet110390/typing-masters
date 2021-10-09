import random,time
# from threading import Timer

def typingTest():
    tests=[
        'The peacock is the national bird of India. They have colourful feathers, two legs and a small beak. They are famous for their dance. When a peacock dances it spreads its feathers like a fan. It has a long shiny dark blue neck. Peacocks are mostly found in the fields they are very beautiful birds. The females are known as ‘Peahen1. Their feathers are used for making jackets, purses etc. We can see them in a zoo.',
        'Ants are found everywhere in the world. They make their home in buildings, gardens etc. They live in anthills. Ants are very hardworking insects. Throughout the summers they collect food for the winter season. Whenever they find a sweet lying on the floor they stick to the sweet and carry it to their home. Thus, in this way, they clean the floor.Ants are generally red and black in colour. They have two eyes and six legs. They are social insects. They live in groups or colonies. Most ants are scavengers they collect whatever food they can find. They are usually wingless but they develop wings when they reproduce. Their bites are quite painful.',
        'The camels are called the “ships of the desert”. They are used to carry people and loads from one place to another. They have a huge hump on their body where they! Store their fat. They can live without water for many days. Their thick fur helps them to stop the sunshine from warming their bodies. Camels have long necks and long legs. They have two toes on each foot.} They move very quickly on sand. They eat plants, grasses and bushes. They do not’ harm anyone. Some of the camels have two humps. These camels are called! Bactrian camels.',
        'An elephant is the biggest living animal on land. It is quite huge in size. It is usually black or grey in colour. Elephants have four legs, a long trunk and two white tusks near their trunk. Apart from this, they have two big ears and a short tail. Elephants are vegetarian. They eat all kinds of plants especially bananas. They are quite social, intelligent and useful animals. They are used to carry logs of wood from one place to another. They are good swimmers.',
        'Horses are farm animals. They are usually black, grey, white and brown in colour. They are known as beasts of burden. They carry people and goods from one place to another. They have long legs, which are very strong. They can easily run long distances. Horses have hard hoofs which protect their feet. They like eating grass and grams they are used in sports like polo and hors riding. An adult male horse is called a stallion and an adult female is called a mare whereas the female baby horse is called a foal and a male baby horse is called a colt. Horses usually move in herds. They live in a stable. They are very useful animals.',
        'The Dog is a pet animal. It is one of the most obedient animals. There are many kinds of dogs in the world. Some of the are very friendly while some of them a dangerous. Dogs are of different color like black, red, white and brown. Some old them have slippery shiny skin and some have rough skin. Dogs are carnivorous animals. They like eating meat. They have four legs, two ears and a tail. Dogs are trained to perform different tasks. They protect us from thieves b) guarding our house. They are loving animals. A dog is called man’s best friend. They are used by the police to find hidden things. They are one of the most useful animals in the world.',
        'The stars are tiny points of light in the space. On a clear night we can see around 2,000 to 3,000 stars without using a telescope. Stars look tiny in the sky because they are far away from the Earth. In ancient times the sky watchers found patterns of stars in the sky.These astronauts Neil Armstrong and patterns of people and the creatures from the myths and the legends. As the Earth spins from east to west the stars also appear to cross from east to west. The stars are made up of gases.'
    ]
    start=time.time()
    errorCount=0
    count=0
    test=random.choice(tests)
    print('\n \r')
    print(test +'\n \r')
    print('Type the phrase presented in the test. \n \r')
    print('Press enter ONLY when the test is complete.\n \r')

    userInput=input()
    wordsTyped=round(len(userInput)/5)

    for i in range(len(test)):
        if len(userInput)<len(test):
            addChars=(len(test)-len(userInput))*' '
            userInput+=addChars          
            # print(len(userInput),len(test))  

        elif userInput[i] is test[i] and userInput[i] != ' ':
            count+=1
            print(userInput[i]+'c')
        
        else:
            errorCount+=1
            # print('error char',i,userInput[i])
    while len(userInput)>len(test):
            l=list(userInput)
            l.pop(-1)
            userInput="".join(l)
            errorCount+=1
    if userInput == ' '*len(test):
        print('Nothing was typed')
        
    else:
        acc=(count/len(test))*100
        mins=(1/60)*round(time.time()-start)
        correct=round(count/5)
        incorrect=round(errorCount/mins)
        gwpm=wordsTyped/mins
        nwpm=gwpm - incorrect
        if nwpm<1:
            nwpm=0
        print('\n\r')
        print('%d words typed'%wordsTyped)
        print('%d correct words'%correct)
        print('incorrect words %d'%incorrect)
        print('grosswpm',round(gwpm,1))
        print ('netwpm',round(nwpm,1))
        print('acc %d percent'%acc)
        if mins>1:
            print('mins typed: ',round(mins,2))
        else:
            print('secs typed ',mins*60)

typingTest()