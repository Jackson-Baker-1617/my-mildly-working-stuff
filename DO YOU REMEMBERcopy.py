from turtle import *
import random
import time
#list of asian nations and some other stuff
asia = ["JohnWetton","Tibet","Siberia","India","China","Afganistan","Armenia", "Azerbaijan", "Bahrain", "Bangladesh","Bhutan","Brunei","Cambodia","Cyprus", "Georgia", "Indonesia","Iran","Iraq","Isreal","Japan","Jordan","Kazakhstan","North Korea","South Korea","Kuwait","Kyrgyzstan","Laos","Lebanon","Malaysia","Maldives","Mongolia","Myanmar","Nepal"]
#intergers
rice1=random.choice(asia)
rice2=random.choice(asia)
rice3=random.choice(asia)
rice4=random.choice(asia)
rice5=random.choice(asia)
rice11=random.choice(asia)
rice12=random.choice(asia)
rice13=random.choice(asia)
rice14=random.choice(asia)
rice15=random.choice(asia)

#first def class
def wormwaiting():
#COLOURING
    bgcolor('#6f1b72')
    pencolor('#85b25b')
#Atual Start
    reset()
    penup()
    goto(-250, 0)
    write("ASIA TIME LETS DO THIS FRIEND", font=("Times New Roman",45))
    goto(-250,-45)
    write("check out the thingy", font=("Times New Roman",45))
    time.sleep(.5) #dramatic pauses are for the weak
    reset()
    suicide()

def suicide():
    quitter=input("yes (Y/N)")
    if quitter.lower()=="y":
        gameo()
    elif quitter.lower()=="n":
        print ("You moist golfball")
    else:
        print("The human earlobe (lobulus auriculae) is composed of tough areolar and adipose connective tissues, lacking the firmness and elasticity of the rest of the auricle (the external structure of the ear). In some cases the lower lobe is connected to the side of the face. Since the earlobe does not contain cartilage[1] it has a large blood supply and may help to warm the ears and maintain balance. The zoologist Desmond Morris in his book The Naked Ape (1967) conjectured that the lobes developed as an additional erogenous zone to facilitate the extended sexuality necessary in the evolution of human monogamous pair bonding.[2] However, earlobes are not generally considered to have any major biological function.[3] The earlobe contains many nerve endings, and for some people is an erogenous zone.")
        suicide()
def gameo():
    print(rice1,rice2,rice3,rice4,rice5)
    goto(-250,0)
    write(rice1, font=("Times New Roman",45))
    time.sleep(1)
    clear()
    goto(-250,0)
    write(rice2, font=("Times New Roman",45))
    time.sleep(1)
    clear()
    goto(-250,0)
    write(rice3, font=("Times New Roman",45))
    time.sleep(1)
    clear()
    goto(-250,0)
    write(rice4, font=("Times New Roman",45))
    time.sleep(1)
    clear()
    goto(-250,0)
    write(rice5, font=("Times New Roman",45))
    time.sleep(1)
    clear()
    victor()
def victor():
    mooseilini = input("do nukmber one. use grammeer")
    if mooseilini != rice1:
            print("Wrongo")
            whylive()
    else:
            genie=input("numberk 2. STILL USE GRAM")
            if genie != rice2:
                print("Wrongo")
                whylive()
            else:
                commuynism=input("NUM THREE FRIEN")
                if commuynism != rice3:
                    print("Wrongo")
                    whylive()
                else:
                    elfdolf=input("NUMB 4444")
                    if elfdolf != rice4:
                        print("Wrongo")
                        whylive()
                    else:
                        canerdia=input("LAST ONE")
                        if canerdia != rice5:
                            print("Wrongo")
                            whylive()
                        else:
                            print("YOU DID IT")
                            sofast()
    
def whylive():
    ech=input("try it two? (Y/N)")
    if ech.lower()=="y":
        victor()
    elif ech.lower()=="n":
        print ("no")
        victor()
    else:
        print("The Libertarian Party (LP) is a Libertarian political party in the United States that promotes civil liberties, non-interventionism, laissez-faire capitalism and the abolition of the welfare state.[7] It is the third largest political party in the United States.")
        whylive()
def sofast():
    FASTER=input("FASTER(y/n)")
    if FASTER.lower()=="y":
        Mach2()
    elif FASTER.lower()=="n":
        print ("try again")
        sofast()
    else:
        print("The Tetraodontidae are a family of primarily marine and estuarine fish of the order Tetraodontiformes. The family includes many familiar species, which are variously called pufferfish, puffers, balloonfish, blowfish, bubblefish, globefish, swellfish, toadfish, toadies, honey toads, sugar toads, and sea squab.[3] They are morphologically similar to the closely related porcupinefish, which have large external spines (unlike the thinner, hidden spines of the Tetraodontidae, which are only visible when the fish has puffed up). The scientific name refers to the four large teeth, fused into an upper and lower plate, which are used for crushing the shells of crustaceans and mollusks, their natural prey.")
        sofast()
def gameofast():
    print(rice11,rice12,rice13,rice14,rice15)
    goto(-250,0)
    write(rice11, font=("Times New Roman",45))
    time.sleep(.1)
    clear()
    goto(-250,0)
    write(rice12, font=("Times New Roman",45))
    time.sleep(.1)
    clear()
    goto(-250,0)
    write(rice13, font=("Times New Roman",45))
    time.sleep(.1)
    clear()
    goto(-250,0)
    write(rice14, font=("Times New Roman",45))
    time.sleep(.1)
    clear()
    goto(-250,0)
    write(rice15, font=("Times New Roman",45))
    time.sleep(.1)
    clear()
    victorfast()
def victorfast():
    mooseilini1 = input("do nukmber one. use grammeer")
    if mooseilini1 != rice11:
            print("Wrongo")
            whylivefaster()
    else:
            genie1=input("numberk 2. STILL USE GRAM")
            if genie1 != rice12:
                print("Wrongo")
                whylivefaster()
            else:
                commuynism1=input("NUM THREE FRIEN")
                if commuynism1 != rice13:
                    print("Wrongo")
                    whylivefaster()
                else:
                    elfdolf1=input("NUMB 4444")
                    if elfdolf1 != rice14:
                        print("Wrongo")
                        whylivefaster()
                    else:
                        canerdia1=input("LAST ONE")
                        if canerdia1 != rice15:
                            print("Wrongo")
                            whylivefaster()
                        else:
                            print("Well that was all i got. good on you")

def whylivefaster():
    em=input("try it two? (Y/N)")
    if em.lower()=="y":
        victorfast()
    elif em.lower()=="n":
        print ("NOPE")
        victorfast()
    else:
       print("iPhone (/ˈaɪfoʊn/ eye-fohn) is a line of smartphones designed and marketed by Apple Inc. They run Apple's iOS mobile operating system.[15] The first generation iPhone was released on June 29, 2007; the most recent iPhone model is the iPhone 7, which was unveiled at a special event on September 7, 2016.[16][17]")
       whylivefaster()        
def Mach2():
    gameofast()
def whydoeslaosexist():
    wormwaiting()
whydoeslaosexist()
