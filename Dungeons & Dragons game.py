#import libraries
import random
import time
import math

#Proficiency Bonus Calculator
def ProficiencyBonusCalculator():
    if Level <= 4:
        ProficiencyBonus = 2
    elif Level >= 5 and Level <= 8:
        ProficiencyBonus = 3
    elif Level >= 9 and Level <= 12:
        ProficiencyBonus = 4
    elif Level >= 13 and Level <= 16:
        ProficiencyBonus = 5
    else:
        ProficiencyBonus = 6
    return ProficiencyBonus

#Level Calculator
def LevelCalculator():
    if Experience <= 299:
        Level = 1
    elif Experience >= 300 and Experience <= 899:
        Level = 2
    elif Experience >= 900 and Experience <= 2699:
        Level = 3
    elif Experience >= 2700 and Experience <= 6499:
        Level = 4
    elif Experience >= 6500 and Experience <= 13999:
        Level = 5
    elif Experience >= 14000 and Experience <= 22999:
        Level = 6
    elif Experience >= 23000 and Experience <= 33999:
        Level = 7
    elif Experience >= 34000 and Experience <= 47999:
        Level = 8
    elif Experience >= 48000 and Experience <= 63999:
        Level = 9
    elif Experience >= 64000 and Experience <= 84999:
        Level = 10
    elif Experience >= 85000 and Experience <= 99999:
        Level = 11
    elif Experience >= 100000 and Experience <= 119999:
        Level = 12
    elif Experience >= 120000 and Experience <= 139999:
        Level = 13
    elif Experience >= 140000 and Experience <= 164999:
        Level = 14
    elif Experience >= 165000 and Experience <= 194999:
        Level = 15
    elif Experience >= 195000 and Experience <= 224999:
        Level = 16
    elif Experience >= 225000 and Experience <= 264999:
        Level = 17
    elif Experience >= 265000 and Experience <= 304999:
        Level = 18
    elif Experience >= 305000 and Experience <= 354999:
        Level = 19
    else:
        Level = 20
    return Level

#Armour Class Calculator
def ArmorClassCalculator():

    #Not wearing Armour
    if WearingArmour == False:
        ArmourClass = 10

        #Barbarian
        if Class == "Barbarian":
            ArmourClass += DexterityAbilityModifier
            ArmourClass += ConstitutionAbilityModifier

        #Monk
        elif Class == "Monk":
            ArmourClass += DexterityAbilityModifier
            ArmourClass += WisdomAbilityModifier

        #Neither
        else:
            ArmourClass += DexterityAbilityModifier

    #Wearing Armour
    else:

        #Padded or Leather Armour
        if Armour == "Padded" or Armour == "Leather":
            ArmourClass = 11
            ArmourClass += DexterityAbilityModifier

        #Studded Leather Armour
        elif Armour == "Studded Leather":
            ArmourClass = 12
            ArmourClass += DexterityAbilityModifier

        #Hide Armour
        elif Armour == "Hide":
            ArmourClass = 12
            if DexterityAbilityModifier >= 3:
                ArmourClass += 2
            else:
                ArmourClass += DexterityAbilityModifier

        #Chain shirt
        elif Armour == "Chain shirt":
            ArmourClass = 13
            if DexterityAbilityModifier >= 3:
                ArmourClass += 2
            else:
                ArmourClass += DexterityAbilityModifier

        #Scale mail or Breastplate Armour
        elif Armour == "Scale mail" or Armour == "Breastplate":
            ArmourClass = 14
            if DexterityAbilityModifier >= 3:
                ArmourClass += 2
            else:
                ArmourClass += DexterityAbilityModifier

        #Half plate Armour
        elif Armour == "Half plate":
            ArmourClass = 15
            if DexterityAbilityModifier >= 3:
                ArmourClass += 2
            else:
                ArmourClass += DexterityAbilityModifier

        #Ring mail
        elif Armour == "Ring mail":
            ArmourClass = 14

        #Chain mail
        elif Armour == "Chain mail":
            ArmourClass = 16

        #Splint Armour
        elif Armour == "Splint":
            ArmourClass = 17

        #Plate Armour
        elif Armour == "Plate":
            ArmourClass = 18

    #Check for shield
    if HasShield == True:
        ArmourClass += 2

    return ArmourClass

#Strength Saving Throw Calculator
def StrengthSavingThrowCalculator():
    if Class == "Barbarian" or Class == "Fighter" or Class == "Monk" or Class == "Ranger":
        StrengthSavingThrow = StrengthAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        StrengthSavingThrow += ProficiencyBonus
    else:
        StrengthSavingThrow = StrengthAbilityModifier
    return StrengthSavingThrow

#Dexterity Saving Throw Calculator
def DexteritySavingThrowCalculator():
    if Class == "Bard" or Class == "Monk" or Class == "Ranger" or Class == "Rogue":
        DexteritySavingThrow = DexterityAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        DexteritySavingThrow += ProficiencyBonus
    else:
        DexteritySavingThrow = DexterityAbilityModifier
    return DexteritySavingThrow

#Constitution Saving Throw Calculator
def ConstitutionSavingThrowCalculator():
    if Class == "Barbarian" or Class == "Fighter" or Class == "Sorceror":
        ConstitutionSavingThrow = ConstitutionAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        ConstitutionSavingThrow += ProficiencyBonus
    else:
        ConstitutionSavingThrow = ConstitutionAbilityModifier
    return ConstitutionSavingThrow

#Intelligence Saving Throw Calculator
def IntelligenceSavingThrowCalculator():
    if Class == "Druid" or Class == "Rogue" or Class == "Wizard":
        IntelligenceSavingThrow = IntelligenceAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        IntelligenceSavingThrow += ProficiencyBonus
    else:
        IntelligenceSavingThrow = IntelligenceAbilityModifier
    return IntelligenceSavingThrow

#Wisdom Saving Throw Calculator
def WisdomSavingThrowCalculator():
    if Class == "Cleric" or Class == "Druid" or Class == "Paladin" or Class == "Warlock" or Class == "Wizard":
        WisdomSavingThrow = WisdomAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        WisdomSavingThrow += ProficiencyBonus
    else:
        WisdomSavingThrow = WisdomAbilityModifier
    return WisdomSavingThrow

#Charisma Saving Throw Calculator
def CharismaSavingThrowCalculator():
    if Class == "Bard" or Class == "Cleric" or Class == "Paladin" or Class == "Sorceror" or Class == "Warlock":
        CharismaSavingThrow = CharismaAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        CharismaSavingThrow += ProficiencyBonus
    else:
        CharismaSavingThrow = CharismaAbilityModifier
    return CharismaSavingThrow

#Athletics Bonus Calculator
def AthleticsBonusCalculator():
    if BackgroundSkillProficiency1 == "Athletics" or SkillProficiency1 == "Athletics" or SkillProficiency2 == "Athletics" or SkillProficiency3 == "Athletics" or SkillProficiency4 == "Athletics":
        Athletics = StrengthAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Athletics += ProficiencyBonus
        return Athletics
    else:
        Athletics = StrengthAbilityModifier
        return Athletics

#Acrobatics Bonus Calculator
def AcrobaticsBonusCalculator():
    if SkillProficiency1 == "Acrobatics" or SkillProficiency2 == "Acrobatics" or SkillProficiency3 == "Acrobatics" or SkillProficiency4 == "Acrobatics":
        Acrobatics = DexterityAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Acrobatics += ProficiencyBonus
        return Acrobatics
    else:
        Acrobatics = DexterityAbilityModifier
        return Acrobatics

#Sleight of Hand Bonus Calculator
def SleightOfHandBonusCalculator():
    if SkillProficiency1 == "Sleight of Hand" or SkillProficiency2 == "Sleight of Hand" or SkillProficiency3 == "Sleight of Hand" or SkillProficiency4 == "Sleight of Hand":
        SleightOfHand = DexterityAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        SleightOfHand += ProficiencyBonus
        return SleightOfHand
    else:
        SleightOfHand = DexterityAbilityModifier
        return SleightOfHand

#Stealth Bonus Calculator
def StealthBonusCalculator():
    if BackgroundSkillProficiency2 == "Stealth" or SkillProficiency1 == "Stealth" or SkillProficiency2 == "Stealth" or SkillProficiency3 == "Stealth" or SkillProficiency4 == "Stealth":
        Stealth = DexterityAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Stealth += ProficiencyBonus
        return Stealth
    else:
        Stealth = DexterityAbilityModifier
        return Stealth

#Arcana Bonus Calculator
def ArcanaBonusCalculator():
    if BackgroundSkillProficiency1 == "Arcana" or SkillProficiency1 == "Arcana" or SkillProficiency2 == "Arcana" or SkillProficiency3 == "Arcana":
        Arcana = IntelligenceAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Arcana += ProficiencyBonus
        return Arcana
    else:
        Arcana = IntelligenceAbilityModifier
        return Arcana

#History Bonus Calculator
def HistoryBonusCalculator():
    if BackgroundSkillProficiency2 == "History" or SkillProficiency1 == "History" or SkillProficiency2 == "History" or SkillProficiency3 == "History":
        History = IntelligenceAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        History += ProficiencyBonus
        return History
    else:
        History = IntelligenceAbilityModifier
        return History

#Investigation Bonus Calculator
def InvestigationBonusCalculator():
    if SkillProficiency1 == "Investigation" or SkillProficiency4 == "Investigation" or SkillProficiency3 == "Investigation" or SkillProficiency4 == "Investigation":
        Investigation = IntelligenceAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Investigation += ProficiencyBonus
        return Investigation
    else:
        Investigation = IntelligenceAbilityModifier
        return Investigation

#Nature Bonus Calculator
def NatureBonusCalculator():
    if SkillProficiency1 == "Nature" or SkillProficiency2 == "Nature" or SkillProficiency3 == "Nature":
        Nature = IntelligenceAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Nature += ProficiencyBonus
        return Nature
    else:
        Nature = IntelligenceAbilityModifier
        return Nature

#Religion Bonus Calculator
def ReligionBonusCalculator():
    if BackgroundSkillProficiency2 == "Religion" or SkillProficiency1 == "Religion" or SkillProficiency2 == "Religion" or SkillProficiency3 == "Religion":
        Religion = IntelligenceAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Religion = ProficiencyBonus
        return Religion
    else:
        Religion = IntelligenceAbilityModifier
        return Religion

#Animal Handling Bonus Calculator
def AnimalHandlingBonusCalculator():
    if SkillProficiency1 == "Animal Handling" or SkillProficiency2 == "Animal Handling" or SkillProficiency3 == "Animal Handling":
        AnimalHandling = WisdomAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        AnimalHandling += ProficiencyBonus
        return AnimalHandling
    else:
        AnimalHandling = WisdomAbilityModifier
        return AnimalHandling

#Insight Bonus Calculator
def InsightBonusCalculator():
    if BackgroundSkillProficiency1 == "Insight" or SkillProficiency1 == "Insight" or SkillProficiency2 == "Insight" or SkillProficiency3 == "Insight" or SkillProficiency4 == "Insight":
        Insight = WisdomAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Insight += ProficiencyBonus
        return Insight
    else:
        Insight = WisdomAbilityModifier
        return Insight

#Medicine Bonus Calculator
def MedicineBonusCalculator():
    if SkillProficiency1 == "Medicine" or SkillProficiency2 == "Medicine" or SkillProficiency3 == "Medicine":
        Medicine = WisdomAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Medicine += ProficiencyBonus
        return Medicine
    else:
        Medicine = WisdomAbilityModifier
        return Medicine

#Perception Bonus Calculator
def PerceptionBonusCalculator():
    if SkillProficiency1 == "Perception" or SkillProficiency2 == "Perception" or SkillProficiency3 == "Perception" or SkillProficiency4 == "Perception":
        Perception = WisdomAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Perception += ProficiencyBonus
        return Perception
    else:
        Perception = WisdomAbilityModifier
        return Perception

#Survival Bonus Calculator
def SurvivalBonusCalculator():
    if SkillProficiency1 == "Survival" or SkillProficiency2 == "Survival" or SkillProficiency3 == "Survival":
        Survival = WisdomAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Survival = ProficiencyBonus
        return Survival
    else:
        Survival = WisdomAbilityModifier
        return Survival

#Deception Bonus Calculator
def DeceptionBonusCalculator():
    if BackgroundSkillProficiency1 == "Deception" or SkillProficiency1 == "Deception" or SkillProficiency2 == "Deception" or SkillProficiency3 == "Deception" or SkillProficiency4 == "Deception":
        Deception = CharismaAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Deception += ProficiencyBonus
        return Deception
    else:
        Deception = CharismaAbilityModifier
        return Deception

#Intimidation Bonus Calculator
def IntimidationBonusCalcualtor():
    if BackgroundSkillProficiency2 == "Intimidation" or SkillProficiency1 == "Intimidation" or SkillProficiency2 == "Intimidation" or SkillProficiency3 == "Intimidation" or SkillProficiency4 == "Intimidation":
        Intimidation = CharismaAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Intimidation += ProficiencyBonus
        return Intimidation
    else:
        Intimidation = CharismaAbilityModifier
        return Intimidation

#Performance Bonus Calculator
def PerformanceBonusCalculator():
    if SkillProficiency1 == "Performance" or SkillProficiency2 == "Performance" or SkillProficiency3 == "Performance" or SkillProficiency4 == "Performance":
        Performance = CharismaAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Performance += ProficiencyBonus
        return Performance
    else:
        Performance = CharismaAbilityModifier
        return Performance

#Persuasion Bonus Calculator
def PersuasionBonusCalculator():
    if SkillProficiency1 == "Persuasion" or SkillProficiency2 == "Persuasion" or SkillProficiency3 == "Persuasion" or SkillProficiency4 == "Persuasion":
        Persuasion = CharismaAbilityModifier
        ProficiencyBonus = ProficiencyBonusCalculator()
        Persuasion += ProficiencyBonus
        return Persuasion
    else:
        Persuasion = CharismaAbilityModifier
        return Persuasion

#Character Variables
Name = ""
Class = ""
Background = ""
Species = ""
Language1 = ""
Language2 = ""
LanguageChoice = ""
Alignment1 = ""
Alignment2 = ""
AlignmentPersonality1 = ""
AlignmentPersonality2 = ""

#Strength Variables
Strength = 0
StrengthOriginal = 0
StrengthAppearance = ""
StrengthSavingThrow = 0
StrengthAbilityModifier = 0
BackgroundStrengthModifier = 0

#Dexterity Variables
Dexterity = 0
DexterityOriginal = 0
DexterityAppearance = ""
DexteritySavingThrow = 0
DexterityAbilityModifier = 0
BackgroundDexterityModifier = 0

#Constitution Variables
Constitution = 0
ConstitutionOriginal = 0
ConstitutionAppearance = ""
ConstitutionSavingThrow = 0
ConstitutionAbilityModifier = 0
BackgroundConstitutionModifier = 0

#Intelligence Variables
Intelligence = 0
IntelligenceOriginal = 0
IntelligenceAppearance = ""
IntelligenceSavingThrow = 0
IntelligenceAbilityModifier = 0
BackgroundIntelligenceModifier = 0

#Wisdom Variables
Wisdom = 0
WisdomOriginal = 0
WisdomAppearance = ""
WisdomSavingThrow = 0
WisdomAbilityModifier = 0
BackgroundWisdomModifier = 0

#Charisma Variables
Charisma = 0
CharismaOriginal = 0
CharismaAppearance = ""
CharismaSavingThrow = 0
CharismaAbilityModifier = 0

BackgroundModifierChoice = ""
BackgroundModifierBoolean = False

BackgroundSkillProficiency1 = ""
BackgroundSkillProficiency2 = ""
SkillProficiency1 = ""
SkillProficiency2 = ""
SkillProficiency3 = ""
SkillProficiency4 = ""

Athletics = 0
Acrobatics = 0
SleightOfHand = 0
Stealth = 0
Arcana = 0
History = 0
Investigation = 0
Nature = 0
Religion = 0
AnimalHandling = 0
Insight = 0
Medicine = 0
Perception = 0
Survival = 0
Deception = 0
Intimidation = 0
Performance = 0
Persuasion = 0

DiceRoll = 0
Experience = 0
Level = 0
MaxHealth = 0
CurrentHealth = 0
Initiative = 0
Armour = ""
ArmourClass = 0
HasShield = False
WearingArmour = False
ProficiencyBonus = 0

#Username
print("Welcome, please input your username")
Name = input()
while len(Name) <3 or len(Name) > 10:
    Name = input("That username is too short, please use a username that is 3 - 10 characters long")

#Class
print("Now we need to pick a class for you! Choose one of the following:")
time.sleep(1)
print("1 = Barbarian")
time.sleep(1)
print("2 = Bard")
time.sleep(1)
print("3 = Cleric")
time.sleep(1)
print("4 = Druid")
time.sleep(1)
print("5 = Fighter")
time.sleep(1)
print("6 = Monk")
time.sleep(1)
print("7 = Paladin")
time.sleep(1)
print("8 = Ranger")
time.sleep(1)
print("9 = Rogue")
time.sleep(1)
print("10 = Sorceror")
time.sleep(1)
print("11 = Warlock")
time.sleep(1)
print("12 = Wizard")
time.sleep(1)
Class = int(input())

#Checking if number is valid
while Class <= 0 or Class >= 13:
    Class = int(input("Please enter a valid number"))

#Number conversion
if Class == 1:
    Class = "Barbarian"
elif Class == 2:
    Class = "Bard"
elif Class == 3:
    Class = "Cleric"
elif Class == 4:
    Class = "Druid"
elif Class == 5:
    Class = "Fighter"
elif Class == 6:
    Class = "Monk"
elif Class == 7:
    Class = "Paladin"
elif Class == 8:
    Class = "Ranger"
elif Class == 9:
    Class = "Rogue"
elif Class == 10:
    Class = "Sorceror"
elif Class == 11:
    Class = "Warlock"
else:
    Class = "Wizard"

#Ability Scores
if Class == "Barbarian":
    Strength = 15
    Dexterity = 13
    Constitution = 14
    Intelligence = 10
    Wisdom = 12
    Charisma = 8

    StrengthOriginal = 15
    DexterityOriginal = 13
    ConstitutionOriginal = 14
    IntelligenceOriginal = 10
    WisdomOriginal = 12
    CharismaOriginal = 8
elif Class == "Bard":
    Strength = 8
    Dexterity = 14
    Constitution = 12
    Intelligence = 13
    Wisdom = 10
    Charisma = 15

    StrengthOriginal = 8
    DexterityOriginal = 14
    ConstitutionOriginal = 12
    IntelligenceOriginal = 13
    WisdomOriginal = 10
    CharismaOriginal = 15
elif Class == "Cleric":
    Strength = 14
    Dexterity = 8
    Constitution = 13
    Intelligence = 10
    Wisdom = 15
    Charisma = 12

    StrengthOriginal = 14
    DexterityOriginal = 8
    ConstitutionOriginal = 13
    IntelligenceOriginal = 10
    WisdomOriginal = 15
    CharismaOriginal = 12
elif Class == "Druid":
    Strength = 8
    Dexterity = 12
    Constitution = 14
    Intelligence = 13
    Wisdom  = 15
    Charisma = 10

    StrengthOriginal = 8
    DexterityOriginal = 12
    ConstitutionOriginal = 14
    IntelligenceOriginal = 13
    WisdomOriginal  = 15
    CharismaOriginal = 10
elif Class == "Fighter":
    Strength = 15
    Dexterity = 14
    Constitution = 13
    Intelligence = 8
    Wisdom = 10
    Charisma = 12

    StrengthOriginal = 15
    DexterityOriginal = 14
    ConstitutionOriginal = 13
    IntelligenceOriginal = 8
    WisdomOriginal = 10
    CharismaOriginal = 12
elif Class == "Monk":
    Strength = 12
    Dexterity = 15
    Constitution = 13
    Intelligence = 10
    Wisdom = 14
    Charisma = 8

    StrengthOriginal = 12
    DexterityOriginal = 15
    ConstitutionOriginal = 13
    IntelligenceOriginal = 10
    WisdomOriginal = 14
    CharismaOriginal = 8
elif Class == "Paladin":
    Strength = 15
    Dexterity = 10
    Constitution = 13
    Intelligence = 8
    Wisdom = 12
    Charisma = 14

    StrengthOriginal = 15
    DexterityOriginal = 10
    ConstitutionOriginal = 13
    IntelligenceOriginal = 8
    WisdomOriginal = 12
    CharismaOriginal = 14
elif Class == "Ranger":
    Strength = 12
    Dexterity = 15
    Constitution = 13
    Intelligence = 8
    Wisdom = 14
    Charisma = 10

    StrengthOriginal = 12
    DexterityOriginal = 15
    ConstitutionOriginal = 13
    IntelligenceOriginal = 8
    WisdomOriginal = 14
    CharismaOriginal = 10
elif Class == "Rogue":
    Strength = 12
    Dexterity = 15
    Constitution = 13
    Intelligence = 14
    Wisdom = 10
    Charisma = 8

    StrengthOriginal = 12
    DexterityOriginal = 15
    ConstitutionOriginal = 13
    IntelligenceOriginal = 14
    WisdomOriginal = 10
    CharismaOriginal = 8
elif Class == "Sorceror":
    Strength = 10
    Dexterity = 13
    Constitution = 14
    Intelligence = 8
    Wisdom = 12
    Charisma = 15

    StrengthOriginal = 10
    DexterityOriginal = 13
    ConstitutionOriginal = 14
    IntelligenceOriginal = 8
    WisdomOriginal = 12
    CharismaOriginal = 15
elif Class == "Warlock":
    Strength = 8
    Dexterity = 14
    Constitution = 13
    Intelligence = 12
    Wisdom = 10
    Charisma = 15

    StrengthOriginal = 8
    DexterityOriginal = 14
    ConstitutionOriginal = 13
    IntelligenceOriginal = 12
    WisdomOriginal = 10
    CharismaOriginal = 15
else:
    Strength = 8
    Dexterity = 12
    Constitution = 13
    Intelligence = 15
    Wisdom = 14
    Charisma = 10

    StrengthOriginal = 8
    DexterityOriginal = 12
    ConstitutionOriginal = 13
    IntelligenceOriginal = 15
    WisdomOriginal = 14
    CharismaOriginal = 10

#Background
print("Now we'll choose your background! Pick one of the following:")
time.sleep(1)
print("1 = Acolyte")
time.sleep(1)
print("2 = Criminal")
time.sleep(1)
print("3 = Sage")
time.sleep(1)
print("4 = Soldier")
time.sleep(1)
Background = int(input())

#Checking if number is valid
while Background <= 0 or Background >= 5:
    Background = int(input("Please enter a valid number"))

#Number conversion
if Background == 1:
    Background = "Acolyte"
elif Background == 2:
    Background = "Criminal"
elif Background == 3:
    Background = "Sage"
else:
    Background = "Soldier"

#Acolyte Ability Modifier
if Background == "Acolyte":
    print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
    print("Intelligence =", Intelligence)
    print("Wisdom =", Wisdom)
    print("Charisma =", Charisma)
    BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

    while BackgroundIntelligenceModifier <= -1 or BackgroundIntelligenceModifier >= 3:
        BackgroundIntelligenceModifier = int(input("Please input a valid number"))

    Intelligence += BackgroundIntelligenceModifier

    #Adding 2 onto Intelligence
    if BackgroundIntelligenceModifier == 2:
        BackgroundWisdomModifier = int(input("By how much would you like to modify your wisdom?"))

        while BackgroundWisdomModifier <= -1 or BackgroundWisdomModifier >= 2:
            BackgroundWisdomModifier = int(input("Please input a valid number"))

        if BackgroundWisdomModifier == 1:
            Wisdom += BackgroundWisdomModifier
        else:
            Charisma += 1

    #Adding 1 onto Intelligence
    elif BackgroundIntelligenceModifier == 1:
        BackgroundWisdomModifier = int(input("By how much would you like to modify your Wisdom?"))

        while BackgroundWisdomModifier <= -1 or BackgroundWisdomModifier >= 3:
            BackgroundWisdomModifier = int(input("Please input a valid number"))

        if BackgroundWisdomModifier == 2:
            Wisdom += BackgroundWisdomModifier
        elif BackgroundWisdomModifier == 1:
            Wisdom += BackgroundWisdomModifier
            Charisma += 1
        else:
            Charisma += 2

    #Adding 0 onto Intelligence
    else:
        BackgroundWisdomModifier = int(input("By how much would you like to modify your Wisdom?"))

        while BackgroundWisdomModifier <= 0 or BackgroundWisdomModifier >= 3:
            BackgroundWisdomModifier = int(input("Please input a valid number"))

        if BackgroundWisdomModifier == 2:
            Wisdom += BackgroundWisdomModifier
            Charisma += 1
        else:
            Wisdom += BackgroundWisdomModifier
            Charisma += 2

    #Displaying modified Ability Scores
    print("These are your modified Ability Scores:")
    print("Intelligence =", Intelligence)
    print("Wisdom =", Wisdom)
    print("Charisma =", Charisma)
    BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
    if BackgroundModifierChoice == "Y":
        BackgroundModifierBoolean = True

        #Loop for when player isn't happy with choices
        while BackgroundModifierBoolean == True:
            Intelligence = IntelligenceOriginal
            Wisdom = WisdomOriginal
            Charisma = CharismaOriginal
            print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
            print("Intelligence =", Intelligence)
            print("Wisdom =", Wisdom)
            print("Charisma =", Charisma)
            BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

            while BackgroundIntelligenceModifier <= -1 or BackgroundIntelligenceModifier >= 3:
                BackgroundIntelligenceModifier = int(input("Please input a valid number"))

            Intelligence += BackgroundIntelligenceModifier

            #Adding 2 onto Intelligence
            if BackgroundIntelligenceModifier == 2:
                BackgroundWisdomModifier = int(input("By how much would you like to modify your wisdom?"))

                while BackgroundWisdomModifier <= -1 or BackgroundWisdomModifier >= 2:
                    BackgroundWisdomModifier = int(input("Please input a valid number"))

                if BackgroundWisdomModifier == 1:
                    Wisdom += BackgroundWisdomModifier
                else:
                    Charisma += 1

            #Adding 1 onto Intelligence
            elif BackgroundIntelligenceModifier == 1:
                BackgroundWisdomModifier = int(input("By how much would you like to modify your Wisdom?"))

                while BackgroundWisdomModifier <= -1 or BackgroundWisdomModifier >= 3:
                    BackgroundWisdomModifier = int(input("Please input a valid number"))

                if BackgroundWisdomModifier == 2:
                    Wisdom += BackgroundWisdomModifier
                elif BackgroundWisdomModifier == 1:
                    Wisdom += BackgroundWisdomModifier
                    Charisma += 1
                else:
                    Charisma += 2

            #Adding 0 onto Intelligence
            else:
                BackgroundWisdomModifier = int(input("By how much would you like to modify your Wisdom?"))

                while BackgroundWisdomModifier <= 0 or BackgroundWisdomModifier >= 3:
                    BackgroundWisdomModifier = int(input("Please input a valid number"))

                if BackgroundWisdomModifier == 2:
                    Wisdom += BackgroundWisdomModifier
                    Charisma += 1
                else:
                    Wisdom += BackgroundWisdomModifier
                    Charisma += 2

            #Displaying modified Ability Scores
            print("These are your modified Ability Scores:")
            print("Intelligence =", Intelligence)
            print("Wisdom =", Wisdom)
            print("Charisma =", Charisma)
            BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
            if BackgroundModifierChoice == "Y":
                BackgroundModifierBoolean = True
            else:
                BackgroundModifierBoolean = False

#Criminal Ability Modifier
elif Background == "Criminal":
    print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
    print("Dexterity =", Dexterity)
    print("Constitution =", Constitution)
    print("Intelligence =", Intelligence)
    BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

    while BackgroundDexterityModifier <= -1 or BackgroundDexterityModifier >= 3:
        BackgroundDexterityModifier = int(input("Please input a valid number"))

    Dexterity += BackgroundDexterityModifier

    #Adding 2 onto Dexterity
    if BackgroundDexterityModifier == 2:
        BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

        while BackgroundConstitutionModifier <= -1 or BackgroundConstitutionModifier >= 2:
            BackgroundConstitutionModifier = int(input("Please input a valid number"))

        if BackgroundConstitutionModifier == 1:
            Constitution += BackgroundConstitutionModifier
        else:
            Intelligence += 1

    #Adding 1 onto Dexterity
    elif BackgroundDexterityModifier == 1:
        BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

        while BackgroundConstitutionModifier <= -1 or BackgroundConstitutionModifier >= 3:
            BackgroundConstitutionModifier = int(input("Please input a valid number"))

        if BackgroundConstitutionModifier == 2:
            Constitution += BackgroundConstitutionModifier
        elif BackgroundConstitutionModifier == 1:
            Constitution += BackgroundConstitutionModifier
            Intelligence += 1
        else:
            Intelligence += 2

    #Adding 0 onto Dexterity
    else:
        BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

        while BackgroundConstitutionModifier <= 0 or BackgroundConstitutionModifier >= 3:
            BackgroundConstitutionModifier = int(input("Please input a valid number"))

        if BackgroundConstitutionModifier == 2:
            Constitution += BackgroundConstitutionModifier
            Intelligence += 1
        else:
            Constitution += BackgroundConstitutionModifier
            Intelligence += 2

    #Displaying modified Ability Scores
    print("These are your modified Ability Scores:")
    print("Dexterity =", Dexterity)
    print("Constitution", Constitution)
    print("Intelligence =", Intelligence)
    BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
    if BackgroundModifierChoice == "Y":
        BackgroundModifierBoolean = True

        #Loop for when player isn't happy with choices
        while BackgroundModifierBoolean == True:
            Dexterity = DexterityOriginal
            Constitution = ConstitutionOriginal
            Intelligence = IntelligenceOriginal
            print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
            print("Dexterity =", Dexterity)
            print("Constitution =", Constitution)
            print("Intelligence =", Intelligence)
            BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

            while BackgroundDexterityModifier <= -1 or BackgroundDexterityModifier >= 3:
                BackgroundDexterityModifier = int(input("Please input a valid number"))

            Dexterity += BackgroundDexterityModifier

            #Adding 2 onto Dexterity
            if BackgroundDexterityModifier == 2:
                BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

                while BackgroundConstitutionModifier <= -1 or BackgroundConstitutionModifier >= 2:
                    BackgroundConstitutionModifier = int(input("Please input a valid number"))

                if BackgroundConstitutionModifier == 1:
                    Constitution += BackgroundConstitutionModifier
                else:
                    Intelligence += 1

            #Adding 1 onto Dexterity
            elif BackgroundDexterityModifier == 1:
                BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

                while BackgroundConstitutionModifier <= -1 or BackgroundConstitutionModifier >= 3:
                    BackgroundConstitutionModifier = int(input("Please input a valid number"))

                if BackgroundConstitutionModifier == 2:
                    Constitution += BackgroundConstitutionModifier
                elif BackgroundConstitutionModifier == 1:
                    Constitution += BackgroundConstitutionModifier
                    Intelligence += 1
                else:
                    Intelligence += 2

            #Adding 0 onto Dexterity
            else:
                BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

                while BackgroundConstitutionModifier <= 0 or BackgroundConstitutionModifier >= 3:
                    BackgroundConstitutionModifier = int(input("Please input a valid number"))

                if BackgroundConstitutionModifier == 2:
                    Constitution += BackgroundConstitutionModifier
                    Intelligence += 1
                else:
                    Constitution += BackgroundConstitutionModifier
                    Intelligence += 2

            #Displaying modified Ability Scores
            print("These are your modified Ability Scores:")
            print("Dexterity =", Dexterity)
            print("Constitution", Constitution)
            print("Intelligence =", Intelligence)
            BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
            if BackgroundModifierChoice == "Y":
                BackgroundModifierBoolean = True
            else:
                BackgroundModifierBoolean = False

#Sage Background Modifier
elif Background == "Sage":
    print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
    print("Constitution =", Constitution)
    print("Intelligence =", Intelligence)
    print("Wisdom =", Wisdom)
    BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

    while BackgroundConstitutionModifier <= -1 or BackgroundConstitutionModifier >= 3:
        BackgroundConstitutionModifier = int(input("Please input a valid number"))

    Constitution += BackgroundConstitutionModifier

    #Adding 2 onto Constitution
    if BackgroundConstitutionModifier == 2:
        BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

        while BackgroundIntelligenceModifier <= -1 or BackgroundIntelligenceModifier >= 2:
            BackgroundIntelligenceModifier = int(input("Please input a valid number"))

        if BackgroundIntelligenceModifier == 1:
            Intelligence += BackgroundIntelligenceModifier
        else:
            Wisdom += 1

    #Adding 1 onto Constitution
    elif BackgroundConstitutionModifier == 1:
        BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

        while BackgroundIntelligenceModifier <= -1 or BackgroundIntelligenceModifier >= 3:
            BackgroundIntelligenceModifier = int(input("Please input a valid number"))

        if BackgroundIntelligenceModifier == 2:
            Intelligence += BackgroundIntelligenceModifier
        elif BackgroundIntelligenceModifier == 1:
            Intelligence += BackgroundIntelligenceModifier
            Wisdom += 1
        else:
            Wisdom += 2

    #Adding 0 onto Constitution
    else:
        BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

        while BackgroundIntelligenceModifier <= 0 or BackgroundIntelligenceModifier >= 3:
            BackgroundIntelligenceModifier = int(input("Please input a valid number"))

        if BackgroundIntelligenceModifier == 2:
            Intelligence += BackgroundIntelligenceModifier
            Wisdom += 1
        else:
            Intelligence += BackgroundIntelligenceModifier
            Wisdom += 2

    #Displaying modified Ability Scores
    print("These are your modified Ability Scores:")
    print("Constitution", Constitution)
    print("Intelligence =", Intelligence)
    print("Wisdom =", Wisdom)
    BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
    if BackgroundModifierChoice == "Y":
        BackgroundModifierBoolean = True

        #Loop for when player isn't happy with choices
        while BackgroundModifierBoolean == True:
            Constitution = ConstitutionOriginal
            Intelligence = IntelligenceOriginal
            Wisdom = WisdomOriginal
            print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
            print("Constitution =", Constitution)
            print("Intelligence =", Intelligence)
            print("Wisdom =", Wisdom)
            BackgroundConstitutionModifier = int(input("By how much would you like to modify your Constitution?"))

            while BackgroundConstitutionModifier <= -1 or BackgroundConstitutionModifier >= 3:
                BackgroundConstitutionModifier = int(input("Please input a valid number"))

            Constitution += BackgroundConstitutionModifier

            #Adding 2 onto Constitution
            if BackgroundConstitutionModifier == 2:
                BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

                while BackgroundIntelligenceModifier <= -1 or BackgroundIntelligenceModifier >= 2:
                    BackgroundIntelligenceModifier = int(input("Please input a valid number"))

                if BackgroundIntelligenceModifier == 1:
                    Intelligence += BackgroundIntelligenceModifier
                else:
                    Wisdom += 1

            #Adding 1 onto Constitution
            elif BackgroundConstitutionModifier == 1:
                BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

                while BackgroundIntelligenceModifier <= -1 or BackgroundIntelligenceModifier >= 3:
                    BackgroundIntelligenceModifier = int(input("Please input a valid number"))

                if BackgroundIntelligenceModifier == 2:
                    Intelligence += BackgroundIntelligenceModifier
                elif BackgroundIntelligenceModifier == 1:
                    Intelligence += BackgroundIntelligenceModifier
                    Wisdom += 1
                else:
                    Wisdom += 2

            #Adding 0 onto Constitution
            else:
                BackgroundIntelligenceModifier = int(input("By how much would you like to modify your Intelligence?"))

                while BackgroundIntelligenceModifier <= 0 or BackgroundIntelligenceModifier >= 3:
                    BackgroundIntelligenceModifier = int(input("Please input a valid number"))

                if BackgroundIntelligenceModifier == 2:
                    Intelligence += BackgroundIntelligenceModifier
                    Wisdom += 1
                else:
                    Intelligence += BackgroundIntelligenceModifier
                    Wisdom += 2

            #Displaying modified Ability Scores
            print("These are your modified Ability Scores:")
            print("Constitution", Constitution)
            print("Intelligence =", Intelligence)
            print("Wisdom =", Wisdom)
            BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
            if BackgroundModifierChoice == "Y":
                BackgroundModifierBoolean = True
            else:
                BackgroundModifierBoolean = False

#Soldier Background Modifier
else:
    print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
    print("Strength =", Strength)
    print("Dexterity =", Dexterity)
    print("Constitution =", Constitution)
    BackgroundStrengthModifier = int(input("By how much would you like to modify your Strength?"))

    while BackgroundStrengthModifier <= -1 or BackgroundStrengthModifier >= 3:
        BackgroundStrengthModifier = int(input("Please input a valid number"))

    Strength += BackgroundStrengthModifier

    #Adding 2 onto Strength
    if BackgroundStrengthModifier == 2:
        BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

        while BackgroundDexterityModifier <= -1 or BackgroundDexterityModifier >= 2:
            BackgroundDexterityModifier = int(input("Please input a valid number"))

        if BackgroundDexterityModifier == 1:
            Dexterity += BackgroundDexterityModifier
        else:
            Constitution += 1

    #Adding 1 onto Strength
    elif BackgroundStrengthModifier == 1:
        BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

        while BackgroundDexterityModifier <= -1 or BackgroundDexterityModifier >= 3:
            BackgroundDexterityModifier = int(input("Please input a valid number"))

        if BackgroundDexterityModifier == 2:
            Dexterity += BackgroundDexterityModifier
        elif BackgroundDexterityModifier == 1:
            Dexterity += BackgroundDexterityModifier
            Constitution += 1
        else:
            Constitution += 2

    #Adding 0 onto Strength
    else:
        BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

        while BackgroundDexterityModifier <= 0 or BackgroundDexterityModifier >= 3:
            BackgroundDexterityModifier = int(input("Please input a valid number"))

        if BackgroundDexterityModifier == 2:
            Dexterity += BackgroundDexterityModifier
            Constitution += 1
        else:
            Dexterity += BackgroundDexterityModifier
            Constitution += 2

    #Displaying modified Ability Scores
    print("These are your modified Ability Scores:")
    print("Strength", Strength)
    print("Dexterity =", Dexterity)
    print("Constitution =", Constitution)
    BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
    if BackgroundModifierChoice == "Y":
        BackgroundModifierBoolean = True

        #Loop for when player isn't happy with choices
        while BackgroundModifierBoolean == True:
            Strength = StrengthOriginal
            Dexterity = DexterityOriginal
            Constitution = ConstitutionOriginal
            print("These are your ability scores you can modify. You can choose to either increase one by 2 and a different one by 1 or increase all three by 1")
            print("Strength =", Strength)
            print("Dexterity =", Dexterity)
            print("Constitution =", Constitution)
            BackgroundStrengthModifier = int(input("By how much would you like to modify your Strength?"))

            while BackgroundStrengthModifier <= -1 or BackgroundStrengthModifier >= 3:
                BackgroundStrengthModifier = int(input("Please input a valid number"))

            Strength += BackgroundStrengthModifier

            #Adding 2 onto Strength
            if BackgroundStrengthModifier == 2:
                BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

                while BackgroundDexterityModifier <= -1 or BackgroundDexterityModifier >= 2:
                    BackgroundDexterityModifier = int(input("Please input a valid number"))

                if BackgroundDexterityModifier == 1:
                    Dexterity += BackgroundDexterityModifier
                else:
                    Constitution += 1

            #Adding 1 onto Strength
            elif BackgroundStrengthModifier == 1:
                BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

                while BackgroundDexterityModifier <= -1 or BackgroundDexterityModifier >= 3:
                    BackgroundDexterityModifier = int(input("Please input a valid number"))

                if BackgroundDexterityModifier == 2:
                    Dexterity += BackgroundDexterityModifier
                elif BackgroundDexterityModifier == 1:
                    Dexterity += BackgroundDexterityModifier
                    Constitution += 1
                else:
                    Constitution += 2

            #Adding 0 onto Strength
            else:
                BackgroundDexterityModifier = int(input("By how much would you like to modify your Dexterity?"))

                while BackgroundDexterityModifier <= 0 or BackgroundDexterityModifier >= 3:
                    BackgroundDexterityModifier = int(input("Please input a valid number"))

                if BackgroundDexterityModifier == 2:
                    Dexterity += BackgroundDexterityModifier
                    Constitution += 1
                else:
                    Dexterity += BackgroundDexterityModifier
                    Constitution += 2

            #Displaying modified Ability Scores
            print("These are your modified Ability Scores:")
            print("Strength", Strength)
            print("Dexterity =", Dexterity)
            print("Constitution =", Constitution)
            BackgroundModifierChoice = input("Would you like to change your options? Y or N.").upper()
            if BackgroundModifierChoice == "Y":
                BackgroundModifierBoolean = True
            else:
                BackgroundModifierBoolean = False

#Acolyte Background Skill Proficiencies
if Background == "Acolyte":
    BackgroundSkillProficiency1 = "Insight"
    BackgroundSkillProficiency2 = "Religion"

#Criminal Background Skill Proficiencies
elif Background == "Criminal":
    BackgroundSkillProficiency1 = "Deception"
    BackgroundSkillProficiency2 = "Stealth"

#Sage Background Skill Proficiencies
elif Background == "Sage":
    BackgroundSkillProficiency1 = "Arcana"
    BackgroundSkillProficiency2 = "History"

#Soldier Background Skill Proficiencies
elif Background == "Soldier":
    BackgroundSkillProficiency1 = "Athletics"
    BackgroundSkillProficiency2 = "Intimidation"

#Choosing Skills
print("Now you have to pick your skills you will be proficient in")
time.sleep(1)

#Barbarian Skill Proficiencies
if Class == "Barbarian":
    print("Since you picked Barbarian as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if background is Soldier so skills don't overlap
    if Background == "Soldier":
        print("1 = Animal Handling")
        time.sleep(1)
        print("2 = Nature")
        time.sleep(1)
        print("3 = Perception")
        time.sleep(1)
        print("4 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

    #Not soldier
    else:
        print("1 = Animal Handling")
        time.sleep(1)
        print("2 = Nature")
        time.sleep(1)
        print("3 = Perception")
        time.sleep(1)
        print("4 = Survival")
        time.sleep(1)
        print("5 = Athletics")
        time.sleep(1)
        print("6 = Intimidation")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill:")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number")) 

    #Number Converter
    if SkillProficiency1 == 1:
        SkillProficiency1 = "Animal Handling"
    elif SkillProficiency1 == 2:
        SkillProficiency1 = "Nature"
    elif SkillProficiency1 == 3:
        SkillProficiency1 = "Perception"
    elif SkillProficiency1 == 4:
        SkillProficiency1 = "Survival"
    elif SkillProficiency1 == 5:
        SkillProficiency1 = "Athletics"
    else:
        SkillProficiency1 = "Intimidation"

    if SkillProficiency2 == 1:
        SkillProficiency2 = "Animal Handling"
    elif SkillProficiency2 == 2:
        SkillProficiency2 = "Nature"
    elif SkillProficiency2 == 3:
        SkillProficiency2 = "Perception"
    elif SkillProficiency2 == 4:
        SkillProficiency2 = "Survival"
    elif SkillProficiency2 == 5:
        SkillProficiency2 = "Athletics"
    else:
        SkillProficiency2 = "Intimidation"

#Bard Skill Proficiencies
elif Class == "Bard":
    print("Since you picked Bard as your Class you get to pick 3 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if background is Acolyte so skills don't overlap
    if Background == "Acolyte":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = Arcana")
        time.sleep(1)
        print("4 = Athletics")
        time.sleep(1)
        print("5 = Deception")
        time.sleep(1)
        print("6 = History")
        time.sleep(1)
        print("7 = Intimidation")
        time.sleep(1)
        print("8 = Investigation")
        time.sleep(1)
        print("9 = Medicine")
        time.sleep(1)
        print("10 = Nature")
        time.sleep(1)
        print("11 = Perception")
        time.sleep(1)
        print("12 = Performance")
        time.sleep(1)
        print("13 = Persuasion")
        time.sleep(1)
        print("14 = Sleight of Hand")
        time.sleep(1)
        print("15 = Stealth")
        time.sleep(1)
        print("16 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 17:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 17:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 17:
            SkillProficiency3 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 9:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 10:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 11:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 12:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 13:
            SkillProficiency1 = "Persuasion"
        elif SkillProficiency1 == 14:
            SkillProficiency1 = "Sleight of Hand"
        elif SkillProficiency1 == 15:
            SkillProficiency1 = "Stealth"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 9:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 10:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 11:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 12:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 13:
            SkillProficiency2 = "Persuasion"
        elif SkillProficiency2 == 14:
            SkillProficiency2 = "Sleight of Hand"
        elif SkillProficiency2 == 15:
            SkillProficiency2 = "Stealth"
        else:
            SkillProficiency2 = "Survival"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Animal Handling"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Arcana"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Deception"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "History"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Intimidation"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 9:
            SkillProficiency3 = "Medicine"
        elif SkillProficiency3 == 10:
            SkillProficiency3 = "Nature"
        elif SkillProficiency3 == 11:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 12:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 13:
            SkillProficiency3 = "Persuasion"
        elif SkillProficiency3 == 14:
            SkillProficiency3 = "Sleight of Hand"
        elif SkillProficiency3 == 15:
            SkillProficiency3 = "Stealth"
        else:
            SkillProficiency3 = "Survival"

    #Check if Background is Criminal so skills don't overlap 
    elif Background == "Criminal":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = Arcana")
        time.sleep(1)
        print("4 = Athletics")
        time.sleep(1)
        print("5 = History")
        time.sleep(1)
        print("6 = Insight")
        time.sleep(1)
        print("7 = Intimidation")
        time.sleep(1)
        print("8 = Investigation")
        time.sleep(1)
        print("9 = Medicine")
        time.sleep(1)
        print("10 = Nature")
        time.sleep(1)
        print("11 = Perception")
        time.sleep(1)
        print("12 = Performance")
        time.sleep(1)
        print("13 = Persuasion")
        time.sleep(1)
        print("14 = Religion")
        time.sleep(1)
        print("15 = Sleight of Hand")
        time.sleep(1)
        print("16 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 17:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 17:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 17:
            SkillProficiency3 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 9:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 10:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 11:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 12:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 13:
            SkillProficiency1 = "Persuasion"
        elif SkillProficiency1 == 14:
            SkillProficiency1 = "Religion"
        elif SkillProficiency1 == 15:
            SkillProficiency1 = "Sleight of Hand"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 9:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 10:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 11:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 12:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 13:
            SkillProficiency2 = "Persuasion"
        elif SkillProficiency2 == 14:
            SkillProficiency2 = "Religion"
        elif SkillProficiency2 == 15:
            SkillProficiency2 = "Sleight of Hand"
        else:
            SkillProficiency2 = "Survival"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Animal Handling"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Arcana"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "History"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Insight"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Intimidation"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 9:
            SkillProficiency3 = "Medicine"
        elif SkillProficiency3 == 10:
            SkillProficiency3 = "Nature"
        elif SkillProficiency3 == 11:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 12:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 13:
            SkillProficiency3 = "Persuasion"
        elif SkillProficiency3 == 14:
            SkillProficiency3 = "Religion"
        elif SkillProficiency3 == 15:
            SkillProficiency3 = "Sleight of Hand"
        else:
            SkillProficiency3 = "Survival"

    #Check if Background is Sage so skills don't overlap
    elif Background == "Sage":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = Athletics")
        time.sleep(1)
        print("4 = Deception")
        time.sleep(1)
        print("5 = Insight")
        time.sleep(1)
        print("6 = Intimidation")
        time.sleep(1)
        print("7 = Investigation")
        time.sleep(1)
        print("8 = Medicine")
        time.sleep(1)
        print("9 = Nature")
        time.sleep(1)
        print("10 = Perception")
        time.sleep(1)
        print("11 = Performance")
        time.sleep(1)
        print("12 = Persuasion")
        time.sleep(1)
        print("13 = Religion")
        time.sleep(1)
        print("14 = Sleight of Hand")
        time.sleep(1)
        print("15 = Stealth")
        time.sleep(1)
        print("16 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 17:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 17:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 17:
            SkillProficiency3 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 9:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 10:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 11:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 12:
            SkillProficiency1 = "Persuasion"
        elif SkillProficiency1 == 13:
            SkillProficiency1 = "Religion"
        elif SkillProficiency1 == 14:
            SkillProficiency1 = "Sleight of Hand"
        elif SkillProficiency1 == 15:
            SkillProficiency1 = "Stealth"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 9:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 10:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 11:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 12:
            SkillProficiency2 = "Persuasion"
        elif SkillProficiency2 == 13:
            SkillProficiency2 = "Religion"
        elif SkillProficiency2 == 14:
            SkillProficiency2 = "Sleight of Hand"
        elif SkillProficiency2 == 15:
            SkillProficiency2 = "Stealth"
        else:
            SkillProficiency2 = "Survival"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Animal Handling"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Deception"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Insight"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Intimidation"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Medicine"
        elif SkillProficiency3 == 9:
            SkillProficiency3 = "Nature"
        elif SkillProficiency3 == 10:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 11:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 12:
            SkillProficiency3 = "Persuasion"
        elif SkillProficiency3 == 13:
            SkillProficiency3 = "Religion"
        elif SkillProficiency3 == 14:
            SkillProficiency3 = "Sleight of Hand"
        elif SkillProficiency3 == 15:
            SkillProficiency3 = "Stealth"
        else:
            SkillProficiency3 = "Survival"

    #Check if Background is Soldier so skills don't overlap
    else:
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = Arcana")
        time.sleep(1)
        print("4 = Deception")
        time.sleep(1)
        print("5 = History")
        time.sleep(1)
        print("6 = Insight")
        time.sleep(1)
        print("7 = Investigation")
        time.sleep(1)
        print("8 = Medicine")
        time.sleep(1)
        print("9 = Nature")
        time.sleep(1)
        print("10 = Perception")
        time.sleep(1)
        print("11 = Performance")
        time.sleep(1)
        print("12 = Persuasion")
        time.sleep(1)
        print("13 = Religion")
        time.sleep(1)
        print("14 = Sleight of Hand")
        time.sleep(1)
        print("15 = Stealth")
        time.sleep(1)
        print("16 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 17:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 17:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 17:
            SkillProficiency3 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 9:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 10:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 11:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 12:
            SkillProficiency1 = "Persuasion"
        elif SkillProficiency1 == 13:
            SkillProficiency1 = "Religion"
        elif SkillProficiency1 == 14:
            SkillProficiency1 = "Sleight of Hand"
        elif SkillProficiency1 == 15:
            SkillProficiency1 = "Stealth"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 9:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 10:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 11:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 12:
            SkillProficiency2 = "Persuasion"
        elif SkillProficiency2 == 13:
            SkillProficiency2 = "Religion"
        elif SkillProficiency2 == 14:
            SkillProficiency2 = "Sleight of Hand"
        elif SkillProficiency2 == 15:
            SkillProficiency2 = "Stealth"
        else:
            SkillProficiency2 = "Survival"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Animal Handling"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Arcana"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Deception"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "History"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Insight"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Medicine"
        elif SkillProficiency3 == 9:
            SkillProficiency3 = "Nature"
        elif SkillProficiency3 == 10:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 11:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 12:
            SkillProficiency3 = "Persuasion"
        elif SkillProficiency3 == 13:
            SkillProficiency3 = "Religion"
        elif SkillProficiency3 == 14:
            SkillProficiency3 = "Sleight of Hand"
        elif SkillProficiency3 == 15:
            SkillProficiency3 = "Stealth"
        else:
            SkillProficiency3 = "Survival"

#Cleric Skill Proficiencies
elif Class == "Cleric":
    print("Since you picked Cleric as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte so skills don't overlap
    if Background == "Acolyte":
        print("1 = History")
        time.sleep(1)
        print("2 = Medicine")
        time.sleep(1)
        print("3 = Persuasion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 4:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 4:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Medicine"
        else:
            SkillProficiency1 = "Persuasion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Medicine"
        else:
            SkillProficiency2 = "Persuasion"

    #Check if Background is Sage so skills don't overlap
    elif Background == "Sage":
        print("1 = Insight")
        time.sleep(1)
        print("2 = Medicine")
        time.sleep(1)
        print("3 = Persuasion")
        time.sleep(1)
        print("4 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Persuasion"
        else:
            SkillProficiency2 = "Religion"

    #Neither Acolyte nor Sage
    else:
        print("1 = History")
        time.sleep(1)
        print("2 = Insight")
        time.sleep(1)
        print("3 = Medicine")
        time.sleep(1)
        print("4 = Persuasion")
        time.sleep(1)
        print("5 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Persuasion"
        else:
            SkillProficiency2 = "Religion"

#Druid Skill Proficiencies
elif Class == "Druid":
    print("Since you picked Druid as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte so skills don't overlap
    if Background == "Acolyte":
        print("1 = Animal Handling")
        time.sleep(1)
        print("2 = Arcana")
        time.sleep(1)
        print("3 = Medicine")
        time.sleep(1)
        print("4 = Nature")
        time.sleep(1)
        print("5 = Perception")
        time.sleep(1)
        print("6 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Perception"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Perception"
        else:
            SkillProficiency2 = "Survival"

    #Check if Background is Sage so skills don't overlap
    elif Background == "Sage":
        print("1 = Animal Handling")
        time.sleep(1)
        print("2 = Insight")
        time.sleep(1)
        print("3 = Medicine")
        time.sleep(1)
        print("4 = Nature")
        time.sleep(1)
        print("5 = Perception")
        time.sleep(1)
        print("6 = Religion")
        time.sleep(1)
        print("7 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 8:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 8:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Religion"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Religion"
        else:
            SkillProficiency2 = "Survival"

    #Neither Acolyte nor Sage
    else:
        print("1 = Animal Handling")
        time.sleep(1)
        print("2 = Arcana")
        time.sleep(1)
        print("3 = Insight")
        time.sleep(1)
        print("4 = Medicine")
        time.sleep(1)
        print("5 = Nature")
        time.sleep(1)
        print("6 = Perception")
        time.sleep(1)
        print("7 = Religion")
        time.sleep(1)
        print("8 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 9:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 9:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Religion"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Religion"
        else:
            SkillProficiency2 = "Survival"

#Fighter Skill Proficiencies
elif Class == "Fighter":
    print("Since you picked Fighter as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte so there is no overlap
    if Background == "Acolyte":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = Athletics")
        time.sleep(1)
        print("4 = History")
        time.sleep(1)
        print("5 = Intimidation")
        time.sleep(1)
        print("6 = Perception")
        time.sleep(1)
        print("7 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 8:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 8:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Perception"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Perception"
        else:
            SkillProficiency2 = "Survival"

    #Check if Background is Sage so there is no overlap
    elif Background == "Sage":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = Athletics")
        time.sleep(1)
        print("4 = Insight")
        time.sleep(1)
        print("5 = Intimidation")
        time.sleep(1)
        print("6 = Perception")
        time.sleep(1)
        print("7 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 8:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 8:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Perception"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Perception"
        else:
            SkillProficiency2 = "Survival"

    #Check if Background is Soldier so there is no overlap
    elif Background == "Soldier":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = History")
        time.sleep(1)
        print("4 = Insight")
        time.sleep(1)
        print("5 = Perception")
        time.sleep(1)
        print("6 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Perception"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Perception"
        else:
            SkillProficiency2 = "Survival"

    #Basically Criminal
    else:
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Animal Handling")
        time.sleep(1)
        print("3 = Athletics")
        time.sleep(1)
        print("4 = History")
        time.sleep(1)
        print("5 = Insight")
        time.sleep(1)
        print("6 = Intimidation")
        time.sleep(1)
        print("7 = Perception")
        time.sleep(1)
        print("8 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 9:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 9:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Perception"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 5:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 6:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Perception"
        else:
            SkillProficiency2 = "Survival"

#Monk Skill Proficiencies
elif Class == "Monk":
    print("Since you picked Monk as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte so there is no overlap
    if Background == "Acolyte":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = History")
        time.sleep(1)
        print("4 = Stealth")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "History"
        else:
            SkillProficiency1 = "Stealth"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "History"
        else:
            SkillProficiency2 = "Stealth"

    #Check if Background is Criminal so there is no overlap
    elif Background == "Criminal":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = History")
        time.sleep(1)
        print("4 = Insight")
        time.sleep(1)
        print("5 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Insight"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Insight"
        else:
            SkillProficiency2 = "Religion"

    #Check if Background is Sage so there is no overlap
    elif Background == "Sage":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = Insight")
        time.sleep(1)
        print("4 = Religion")
        time.sleep(1)
        print("5 = Stealth")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Religion"
        else:
            SkillProficiency1 = "Stealth"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Religion"
        else:
            SkillProficiency2 = "Stealth"

    #Check if Background is Soldier so there is no overlap
    else:
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = History")
        time.sleep(1)
        print("3 = Insight")
        time.sleep(1)
        print("4 = Religion")
        time.sleep(1)
        print("5 = Stealth")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Religion"
        else:
            SkillProficiency1 = "Stealth"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Religion"
        else:
            SkillProficiency2 = "Stealth"

#Paladin Skill Proficiencies
elif Class == "Paladin":
    print("Since you picked Paladin as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte so there is no overlap
    if Background == "Acolyte":
        print("1 = Athletics")
        time.sleep(1)
        print("2 = Intimidation")
        time.sleep(1)
        print("3 = Medicine")
        time.sleep(1)
        print("4 = Persuasion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Medicine"
        else:
            SkillProficiency1 = "Persuasion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Medicine"
        else:
            SkillProficiency2 = "Persuasion"

    #Check if Background is Soldier so there is no overlap
    elif Background == "Soldier":
        print("1 = Insight")
        time.sleep(1)
        print("2 = Medicine")
        time.sleep(1)
        print("3 = Persuasion")
        time.sleep(1)
        print("4 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Persuasion"
        else:
            SkillProficiency2 = "Religion"

    #Neither Acolyte nor Soldier
    else:
        print("1 = Athletics")
        time.sleep(1)
        print("2 = Insight")
        time.sleep(1)
        print("3 = Intimidation")
        time.sleep(1)
        print("4 = Medicine")
        time.sleep(1)
        print("5 = Persuasion")
        time.sleep(1)
        print("6 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Medicine"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Medicine"
        elif SkillProficiency2 == 5:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency2 = "Religion"

#Ranger Skill Proficiencies
elif Class == "Ranger":
    print("Since you picked Ranger as your Class you get to pick 3 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Criminal so there is no overlap
    if Background == "Criminal":
        print("1 = Animal handling")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = Investigation")
        time.sleep(1)
        print("4 = Nature")
        time.sleep(1)
        print("5 = Perception")
        time.sleep(1)
        print("6 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 >= 7:
            SkillProficiency3 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Perception"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Perception"
        else:
            SkillProficiency2 = "Survival"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Animal Handling"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Nature"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Perception"
        else:
            SkillProficiency3 = "Survival"

    #Check if Background is Soldier so there is no overlap
    elif Background == "Soldier":
        print("1 = Animal handling")
        time.sleep(1)
        print("2 = Investigation")
        time.sleep(1)
        print("3 = Nature")
        time.sleep(1)
        print("4 = Perception")
        time.sleep(1)
        print("5 = Stealth")
        time.sleep(1)
        print("6 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 >= 7:
            SkillProficiency3 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Stealth"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Stealth"
        else:
            SkillProficiency2 = "Survival"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Animal Handling"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Nature"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Stealth"
        else:
            SkillProficiency3 = "Survival"

    #Neither Criminal nor Soldier
    else:
        print("1 = Animal handling")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = Investigation")
        time.sleep(1)
        print("4 = Nature")
        time.sleep(1)
        print("5 = Perception")
        time.sleep(1)
        print("6 = Stealth")
        time.sleep(1)
        print("7 = Survival")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 8:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 8:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 >= 8:
            SkillProficiency3 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Animal Handling"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Nature"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Stealth"
        else:
            SkillProficiency1 = "Survival"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Animal Handling"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Nature"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Stealth"
        else:
            SkillProficiency2 = "Survival"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Animal Handling"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Nature"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Stealth"
        else:
            SkillProficiency3 = "Survival"

#Rogue Skill Proficiencies
elif Class == "Rogue":
    print("Since you picked Rogue as your Class you get to pick 4 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte so there is no overlap
    if Background == "Acolyte":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = Deception")
        time.sleep(1)
        print("4 = Intimidation")
        time.sleep(1)
        print("5 = Investigation")
        time.sleep(1)
        print("6 = Perception")
        time.sleep(1)
        print("7 = Performance")
        time.sleep(1)
        print("8 = Persuasion")
        time.sleep(1)
        print("9 = Sleight of Hand")
        time.sleep(1)
        print("10 = Stealth")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 11:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 11:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 11:
            SkillProficiency3 = int(input("Please enter a valid number"))

        #Skill 4
        SkillProficiency4 = int(input())

        while SkillProficiency4 <= 0 or SkillProficiency4 == SkillProficiency3 or SkillProficiency4 == SkillProficiency2 or SkillProficiency4 == SkillProficiency1 or SkillProficiency4 >= 11:
            SkillProficiency4 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Persuasion"
        elif SkillProficiency1 == 9:
            SkillProficiency1 = "Sleight of Hand"
        else:
            SkillProficiency1 = "Stealth"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Persuasion"
        elif SkillProficiency2 == 9:
            SkillProficiency2 = "Sleight of Hand"
        else:
            SkillProficiency2 = "Stealth"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Deception"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Intimidation"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Persuasion"
        elif SkillProficiency3 == 9:
            SkillProficiency3 = "Sleight of Hand"
        else:
            SkillProficiency3 = "Stealth"

        if SkillProficiency4 == 1:
            SkillProficiency4 = "Acrobatics"
        elif SkillProficiency4 == 2:
            SkillProficiency4 = "Athletics"
        elif SkillProficiency4 == 3:
            SkillProficiency4 = "Deception"
        elif SkillProficiency4 == 4:
            SkillProficiency4 = "Intimidation"
        elif SkillProficiency4 == 5:
            SkillProficiency4 = "Investigation"
        elif SkillProficiency4 == 6:
            SkillProficiency4 = "Perception"
        elif SkillProficiency4 == 7:
            SkillProficiency4 = "Performance"
        elif SkillProficiency4 == 8:
            SkillProficiency4 = "Persuasion"
        elif SkillProficiency4 == 9:
            SkillProficiency4 = "Sleight of Hand"
        else:
            SkillProficiency4 = "Stealth"

    #Check if Background is Criminal so there is no overlap
    elif Background == "Criminal":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = Insight")
        time.sleep(1)
        print("4 = Intimidation")
        time.sleep(1)
        print("5 = Investigation")
        time.sleep(1)
        print("6 = Perception")
        time.sleep(1)
        print("7 = Performance")
        time.sleep(1)
        print("8 = Persuasion")
        time.sleep(1)
        print("9 = Sleight of Hand")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 10:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 10:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 10:
            SkillProficiency3 = int(input("Please enter a valid number"))

        #Skill 4
        SkillProficiency4 = int(input())

        while SkillProficiency4 <= 0 or SkillProficiency4 == SkillProficiency3 or SkillProficiency4 == SkillProficiency2 or SkillProficiency4 == SkillProficiency1 or SkillProficiency4 >= 10:
            SkillProficiency4 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Sleight of Hand"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Persuasion"
        else:
            SkillProficiency2 = "Sleight of Hand"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Insight"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Intimidation"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Persuasion"
        else:
            SkillProficiency3 = "Sleight of Hand"

        if SkillProficiency4 == 1:
            SkillProficiency4 = "Acrobatics"
        elif SkillProficiency4 == 2:
            SkillProficiency4 = "Athletics"
        elif SkillProficiency4 == 3:
            SkillProficiency4 = "Insight"
        elif SkillProficiency4 == 4:
            SkillProficiency4 = "Intimidation"
        elif SkillProficiency4 == 5:
            SkillProficiency4 = "Investigation"
        elif SkillProficiency4 == 6:
            SkillProficiency4 = "Perception"
        elif SkillProficiency4 == 7:
            SkillProficiency4 = "Performance"
        elif SkillProficiency4 == 8:
            SkillProficiency4 = "Persuasion"
        else:
            SkillProficiency4 = "Sleight of Hand"

    #Check if Background is Soldier so there is no overlap
    elif Background == "Soldier":
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Deception")
        time.sleep(1)
        print("3 = Insight")
        time.sleep(1)
        print("4 = Investigation")
        time.sleep(1)
        print("5 = Perception")
        time.sleep(1)
        print("6 = Performance")
        time.sleep(1)
        print("7 = Persuasion")
        time.sleep(1)
        print("8 = Sleight of Hand")
        time.sleep(1)
        print("9 = Stealth")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 10:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 10:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 10:
            SkillProficiency3 = int(input("Please enter a valid number"))

        #Skill 4
        SkillProficiency4 = int(input())

        while SkillProficiency4 <= 0 or SkillProficiency4 == SkillProficiency3 or SkillProficiency4 == SkillProficiency2 or SkillProficiency4 == SkillProficiency1 or SkillProficiency4 >= 10:
            SkillProficiency4 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Persuasion"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Sleight of Hand"
        else:
            SkillProficiency1 = "Stealth"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Persuasion"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Sleight of Hand"
        else:
            SkillProficiency2 = "Stealth"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Deception"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Insight"
        elif SkillProficiency3 == 4:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 5:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Persuasion"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Sleight of Hand"
        else:
            SkillProficiency3 = "Stealth"

        if SkillProficiency4 == 1:
            SkillProficiency4 = "Acrobatics"
        elif SkillProficiency4 == 2:
            SkillProficiency4 = "Deception"
        elif SkillProficiency4 == 3:
            SkillProficiency4 = "Insight"
        elif SkillProficiency4 == 4:
            SkillProficiency4 = "Investigation"
        elif SkillProficiency4 == 5:
            SkillProficiency4 = "Perception"
        elif SkillProficiency4 == 6:
            SkillProficiency4 = "Performance"
        elif SkillProficiency4 == 7:
            SkillProficiency4 = "Persuasion"
        elif SkillProficiency4 == 8:
            SkillProficiency4 = "Sleight of Hand"
        else:
            SkillProficiency4 = "Stealth"

    #Basically Sage
    else:
        print("1 = Acrobatics")
        time.sleep(1)
        print("2 = Athletics")
        time.sleep(1)
        print("3 = Deception")
        time.sleep(1)
        print("4 = Insight")
        time.sleep(1)
        print("5 = Intimidation")
        time.sleep(1)
        print("6 = Investigation")
        time.sleep(1)
        print("7 = Perception")
        time.sleep(1)
        print("8 = Performance")
        time.sleep(1)
        print("9 = Persuasion")
        time.sleep(1)
        print("10 = Sleight of Hand")
        time.sleep(1)
        print("11 = Stealth")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 12:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 12:
            SkillProficiency2 = int(input("Please enter a valid number"))

        print("Now choose your third skill")

        #Skill 3
        SkillProficiency3 = int(input())

        while SkillProficiency3 <= 0 or SkillProficiency3 == SkillProficiency2 or SkillProficiency3 == SkillProficiency1 or SkillProficiency3 >= 12:
            SkillProficiency3 = int(input("Please enter a valid number"))

        #Skill 4
        SkillProficiency4 = int(input())

        while SkillProficiency4 <= 0 or SkillProficiency4 == SkillProficiency3 or SkillProficiency4 == SkillProficiency2 or SkillProficiency4 == SkillProficiency1 or SkillProficiency4 >= 12:
            SkillProficiency4 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Acrobatics"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Athletics"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 6:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 7:
            SkillProficiency1 = "Perception"
        elif SkillProficiency1 == 8:
            SkillProficiency1 = "Performance"
        elif SkillProficiency1 == 9:
            SkillProficiency1 = "Persuasion"
        elif SkillProficiency1 == 10:
            SkillProficiency1 = "Sleight of Hand"
        else:
            SkillProficiency1 = "Stealth"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Acrobatics"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Athletics"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 4:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 5:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 6:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 7:
            SkillProficiency2 = "Perception"
        elif SkillProficiency2 == 8:
            SkillProficiency2 = "Performance"
        elif SkillProficiency2 == 9:
            SkillProficiency2 = "Persuasion"
        elif SkillProficiency2 == 10:
            SkillProficiency2 = "Sleight of Hand"
        else:
            SkillProficiency2 = "Stealth"

        if SkillProficiency3 == 1:
            SkillProficiency3 = "Acrobatics"
        elif SkillProficiency3 == 2:
            SkillProficiency3 = "Athletics"
        elif SkillProficiency3 == 3:
            SkillProficiency3 = "Deception"
        elif SkillProficiency3 == 4:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 5:
            SkillProficiency3 = "Intimidation"
        elif SkillProficiency3 == 6:
            SkillProficiency3 = "Investigation"
        elif SkillProficiency3 == 7:
            SkillProficiency3 = "Perception"
        elif SkillProficiency3 == 8:
            SkillProficiency3 = "Performance"
        elif SkillProficiency3 == 9:
            SkillProficiency3 = "Persuasion"
        elif SkillProficiency3 == 10:
            SkillProficiency3 = "Sleight of Hand"
        else:
            SkillProficiency3 = "Stealth"

        if SkillProficiency4 == 1:
            SkillProficiency4 = "Acrobatics"
        elif SkillProficiency4 == 2:
            SkillProficiency4 = "Athletics"
        elif SkillProficiency4 == 3:
            SkillProficiency4 = "Deception"
        elif SkillProficiency4 == 4:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 5:
            SkillProficiency4 = "Intimidation"
        elif SkillProficiency4 == 6:
            SkillProficiency4 = "Investigation"
        elif SkillProficiency4 == 7:
            SkillProficiency4 = "Perception"
        elif SkillProficiency4 == 8:
            SkillProficiency4 = "Performance"
        elif SkillProficiency4 == 9:
            SkillProficiency4 = "Persuasion"
        elif SkillProficiency4 == 10:
            SkillProficiency4 = "Sleight of Hand"
        else:
            SkillProficiency4 = "Stealth"

#Sorceror Skill Proficiencies
elif Class == "Sorceror":
    print("Since you picked Sorceror as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte
    if Background == "Acolyte":
        print("1 = Arcana")
        time.sleep(1)
        print("2 = Deception")
        time.sleep(1)
        print("3 = Intimidation")
        time.sleep(1)
        print("4 = Persuasion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Intimidation"
        else:
            SkillProficiency1 = "Persuasion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Intimidation"
        else:
            SkillProficiency2 = "Persuasion"

    #Check if Background is Criminal so there is no overlap
    elif Background == "Criminal":
        print("1 = Arcana")
        time.sleep(1)
        print("2 = Insight")
        time.sleep(1)
        print("3 = Intimidation")
        time.sleep(1)
        print("4 = Persuasion")
        time.sleep(1)
        print("5 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Persuasion"
        else:
            SkillProficiency2 = "Religion"

    #Check if Background is Sage so there is no overlap
    elif Background == "Sage":
        print("1 = Deception")
        time.sleep(1)
        print("2 = Insight")
        time.sleep(1)
        print("3 = Intimidation")
        time.sleep(1)
        print("4 = Persuasion")
        time.sleep(1)
        print("5 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Persuasion"
        else:
            SkillProficiency2 = "Religion"

    #Check if Background is Soldier so there is no overlap
    else:
        print("1 = Arcana")
        time.sleep(1)
        print("2 = Deception")
        time.sleep(1)
        print("3 = Insight")
        time.sleep(1)
        print("4 = Persuasion")
        time.sleep(1)
        print("5 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Persuasion"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Persuasion"
        else:
            SkillProficiency2 = "Religion"

#Warlock Skill Proficiencies
elif Class == "Warlock":
    print("Since you picked Warlock as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte
    if Background == "Acolyte":
        print("1 = Arcana")
        time.sleep(1)
        print("2 = Deception")
        time.sleep(1)
        print("3 = History")
        time.sleep(1)
        print("4 = Intimidation")
        time.sleep(1)
        print("5 = Investigation")
        time.sleep(1)
        print("6 = Nature")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Investigation"
        else:
            SkillProficiency1 = "Nature"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Investigation"
        else:
            SkillProficiency2 = "Nature"

    #Check if Background is Criminal so there is no overlap
    elif Background == "Criminal":
        print("1 = Arcana")
        time.sleep(1)
        print("2 = History")
        time.sleep(1)
        print("3 = Intimidation")
        time.sleep(1)
        print("4 = Investigation")
        time.sleep(1)
        print("5 = Nature")
        time.sleep(1)
        print("6 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Nature"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Nature"
        else:
            SkillProficiency2 = "Religion"

    #Check if Background is Sage so there is no overlap
    elif Background == "Sage":
        print("1 = Deception")
        time.sleep(1)
        print("2 = Intimidation")
        time.sleep(1)
        print("3 = Investigation")
        time.sleep(1)
        print("4 = Nature")
        time.sleep(1)
        print("5 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 6:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 6:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Intimidation"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Nature"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Intimidation"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Nature"
        else:
            SkillProficiency2 = "Religion"

    #Check if Background is Soldier so there is no overlap
    else:
        print("1 = Arcana")
        time.sleep(1)
        print("2 = Deception")
        time.sleep(1)
        print("3 = History")
        time.sleep(1)
        print("4 = Investigation")
        time.sleep(1)
        print("5 = Nature")
        time.sleep(1)
        print("6 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        print("Now choose your second skill")

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Deception"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Nature"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Deception"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Nature"
        else:
            SkillProficiency2 = "Religion"

#Wizard Skill Proficiencies
else:
    print("Since you picked Wizard as your Class you get to pick 2 of the following Skills. First, pick your first skill to be proficient in:")
    time.sleep(1)

    #Check if Background is Acolyte so there is no overlap
    if Background == "Acolyte":
        print("1 = Arcana")
        time.sleep(1)
        print("2 = History")
        time.sleep(1)
        print("3 = Investigation")
        time.sleep(1)
        print("4 = Medicine")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Investigation"
        else:
            SkillProficiency1 = "Medicine"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Investigation"
        else:
            SkillProficiency2 = "Medicine"

    #Check if Background is Sage so there is no overlap
    elif Background == "Sage":
        print("1 = Insight")
        time.sleep(1)
        print("2 = Investigation")
        time.sleep(1)
        print("3 = Medicine")
        time.sleep(1)
        print("4 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 5:
            SkillProficiency1 = int(input("Please enter a valid number"))

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 5:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Medicine"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Medicine"
        else:
            SkillProficiency2 = "Religion"

    #Neither Acolyte nor Sage
    else:
        print("1 = Arcana")
        time.sleep(1)
        print("2 = History")
        time.sleep(1)
        print("3 = Insight")
        time.sleep(1)
        print("4 = Investigation")
        time.sleep(1)
        print("5 = Medicine")
        time.sleep(1)
        print("6 = Religion")

        #Skill 1
        SkillProficiency1 = int(input())

        while SkillProficiency1 <= 0 or SkillProficiency1 >= 7:
            SkillProficiency1 = int(input("Please enter a valid number"))

        #Skill 2
        SkillProficiency2 = int(input())

        while SkillProficiency2 <= 0 or SkillProficiency2 == SkillProficiency1 or SkillProficiency2 >= 7:
            SkillProficiency2 = int(input("Please enter a valid number"))

        if SkillProficiency1 == 1:
            SkillProficiency1 = "Arcana"
        elif SkillProficiency1 == 2:
            SkillProficiency1 = "History"
        elif SkillProficiency1 == 3:
            SkillProficiency1 = "Insight"
        elif SkillProficiency1 == 4:
            SkillProficiency1 = "Investigation"
        elif SkillProficiency1 == 5:
            SkillProficiency1 = "Medicine"
        else:
            SkillProficiency1 = "Religion"

        if SkillProficiency2 == 1:
            SkillProficiency2 = "Arcana"
        elif SkillProficiency2 == 2:
            SkillProficiency2 = "History"
        elif SkillProficiency2 == 3:
            SkillProficiency2 = "Insight"
        elif SkillProficiency2 == 4:
            SkillProficiency2 = "Investigation"
        elif SkillProficiency2 == 5:
            SkillProficiency2 = "Medicine"
        else:
            SkillProficiency2 = "Religion"

#Strength Score Modifiers
if Strength == 3:
    StrengthAbilityModifier = -4
elif Strength == 4 or Strength == 5:
    StrengthAbilityModifier = -3
elif Strength == 6 or Strength == 7:
    StrengthAbilityModifier = -2
elif Strength == 8 or Strength == 9:
    StrengthAbilityModifier = -1
elif Strength == 12 or Strength == 13:
    StrengthAbilityModifier = 1
elif Strength == 14 or Strength == 15:
    StrengthAbilityModifier = 2
elif Strength == 16 or Strength == 17:
    StrengthAbilityModifier = 3
elif Strength == 18 or Strength == 19:
    StrengthAbilityModifier = 4
elif Strength == 20:
    StrengthAbilityModifier = 5

#Strength Appearance
if StrengthAbilityModifier >= 0:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        StrengthAppearance = "Muscular"
    elif DiceRoll == 2:
        StrengthAppearance = "Sinewy"
    elif DiceRoll == 3:
        StrengthAppearance = "Protective"
    else:
        StrengthAppearance = "Direct"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        StrengthAppearance = "Weak"
    elif DiceRoll == 2:
        StrengthAppearance = "Slight"
    elif DiceRoll == 3:
        StrengthAppearance = "Self-conscious"
    else:
        StrengthAppearance = "Indirect"

#Dexterity Score Modifiers
if Dexterity == 3:
    DexterityAbilityModifier = -4
elif Dexterity == 4 or Dexterity == 5:
    DexterityAbilityModifier = -3
elif Dexterity == 6 or Dexterity == 7:
    DexterityAbilityModifier = -2
elif Dexterity == 8 or Dexterity == 9:
    DexterityAbilityModifier = -1
elif Dexterity == 12 or Dexterity == 13:
    DexterityAbilityModifier = 1
elif Dexterity == 14 or Dexterity == 15:
    DexterityAbilityModifier = 2
elif Dexterity == 16 or Dexterity == 17:
    DexterityAbilityModifier = 3
elif Dexterity == 18 or Dexterity == 19:
    DexterityAbilityModifier = 4
elif Dexterity == 20:
    DexterityAbilityModifier = 5

#Dexterity Appearance
if DexterityAbilityModifier >= 0:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        DexterityAppearance = "Lithe"
    elif DiceRoll == 2:
        DexterityAppearance  = "Dynamic"
    elif DiceRoll == 3:
        DexterityAppearance = "Fidgety"
    else:
        DexterityAppearance = "Poised"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        DexterityAppearance = "Jittery"
    elif DiceRoll == 2:
        DexterityAppearance = "Clumsy"
    elif DiceRoll == 3:
        DexterityAppearance = "Hesitant"
    else:
        DexterityAppearance = "Unsteady"

#Constitution Score Modifiers
if Constitution == 3:
    ConstitutionAbilityModifier = -4
elif Constitution == 4 or Constitution == 5:
    ConstitutionAbilityModifier = -3
elif Constitution == 6 or Constitution == 7:
    ConstitutionAbilityModifier = -2
elif Constitution == 8 or Constitution == 9:
    ConstitutionAbilityModifier = -1
elif Constitution == 12 or Constitution == 13:
    ConstitutionAbilityModifier = 1
elif Constitution == 14 or Constitution == 15:
    ConstitutionAbilityModifier = 2
elif Constitution == 16 or Constitution == 17:
    ConstitutionAbilityModifier = 3
elif Constitution == 18 or Constitution == 19:
    ConstitutionAbilityModifier = 4
elif Constitution == 20:
    ConstitutionAbilityModifier = 5

#Constitution Appearance
if ConstitutionAbilityModifier >= 0:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        ConstitutionAppearance = "Energetic"
    elif DiceRoll == 2:
        ConstitutionAppearance = "Hale"
    elif DiceRoll == 3:
        ConstitutionAppearance = "Hearty"
    else:
        ConstitutionAppearance = "Stable"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        ConstitutionAppearance = "Frail"
    elif DiceRoll == 2:
        ConstitutionAppearance = "Squeamish"
    elif DiceRoll == 3:
        ConstitutionAppearance = "Lethargic"
    else:
        ConstitutionAppearance = "Fragile"

#Intelligence Score Modifiers
if Intelligence == 3:
    IntelligenceAbilityModifier = -4
elif Intelligence == 4 or Intelligence == 5:
    IntelligenceAbilityModifier = -3
elif Intelligence == 6 or Intelligence == 7:
    IntelligenceAbilityModifier = -2
elif Intelligence == 8 or Intelligence == 9:
    IntelligenceAbilityModifier = -1
elif Intelligence == 12 or Intelligence == 13:
    IntelligenceAbilityModifier = 1
elif Intelligence == 14 or Intelligence == 15:
    IntelligenceAbilityModifier = 2
elif Intelligence == 16 or Intelligence == 17:
    IntelligenceAbilityModifier = 3
elif Intelligence == 18 or Intelligence == 19:
    IntelligenceAbilityModifier = 4
elif Intelligence == 20:
    IntelligenceAbilityModifier = 5

#Intelligence Appearance
if IntelligenceAbilityModifier >= 0:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        IntelligenceAppearance = "Decisive"
    elif DiceRoll == 2:
        IntelligenceAppearance = "Logical"
    elif DiceRoll == 3:
        IntelligenceAppearance = "Informative"
    else:
        IntelligenceAppearance = "Curious"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        IntelligenceAppearance = "Artless"
    elif DiceRoll == 2:
        IntelligenceAppearance = "Illogical"
    elif DiceRoll == 3:
        IntelligenceAppearance = "Uninformed"
    else:
        IntelligenceAppearance = "Frivolous"

#Wisdom Score Modifiers
if Wisdom == 3:
    WisdomAbilityModifier = -4
elif Wisdom == 4 or Wisdom == 5:
    WisdomAbilityModifier = -3
elif Wisdom == 6 or Wisdom == 7:
    WisdomAbilityModifier = -2
elif Wisdom == 8 or Wisdom == 9:
    WisdomAbilityModifier = -1
elif Wisdom == 12 or Wisdom == 13:
    WisdomAbilityModifier = 1
elif Wisdom == 14 or Wisdom == 15:
    WisdomAbilityModifier = 2
elif Wisdom == 16 or Wisdom == 17:
    WisdomAbilityModifier = 3
elif Wisdom == 18 or Wisdom == 19:
    WisdomAbilityModifier = 4
elif Wisdom == 20:
    WisdomAbilityModifier = 5

#Wisdom Appearance
if WisdomAbilityModifier >= 0:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        WisdomAppearance = "Serene"
    elif DiceRoll == 2:
        WisdomAppearance = "Considerate"
    elif DiceRoll == 3:
        WisdomAppearance = "Attentive"
    else:
        WisdomAppearance = "Wary"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        WisdomAppearance = "Rash"
    elif DiceRoll == 2:
        WisdomAppearance = "Distracted"
    elif DiceRoll == 3:
        WisdomAppearance = "Oblivious"
    else:
        WisdomAppearance = "Naive"

#Charisma Score Modifiers
if Charisma == 3:
    CharismaAbilityModifier = -4
elif Charisma == 4 or Charisma == 5:
    CharismaAbilityModifier = -3
elif Charisma == 6 or Charisma == 7:
    CharismaAbilityModifier = -2
elif Charisma == 8 or Charisma == 9:
    CharismaAbilityModifier = -1
elif Charisma == 12 or Charisma == 13:
    CharismaAbilityModifier = 1
elif Charisma == 14 or Charisma == 15:
    CharismaAbilityModifier = 2
elif Charisma == 16 or Charisma == 17:
    CharismaAbilityModifier = 3
elif Charisma == 18 or Charisma == 19:
    CharismaAbilityModifier = 4
elif Charisma == 20:
    CharismaAbilityModifier = 5

#Charisma Appearance
if CharismaAbilityModifier >= 0:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        CharismaAppearance = "Charming"
    elif DiceRoll == 2:
        CharismaAppearance = "Commanding"
    elif DiceRoll == 3:
        CharismaAppearance = "Hilarious"
    else:
        CharismaAppearance = "Inspiring"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        CharismaAppearance = "Pedantic"
    elif DiceRoll == 2:
        CharismaAppearance = "Humorless"
    elif DiceRoll == 3:
        CharismaAppearance = "Reserved"
    else:
        CharismaAppearance = "Tactless"

#Species
print("Time to choose your Specie. Pick one of the following Species:")
time.sleep(1)
print("1 = Dragonborn")
time.sleep(1)
print("2 = Dwarf")
time.sleep(1)
print("3 = Elf")
time.sleep(1)
print("4 = Gnome")
time.sleep(1)
print("5 = Goliath")
time.sleep(1)
print("6 = Halfling")
time.sleep(1)
print("7 = Human")
time.sleep(1)
print("8 = Orc")
time.sleep(1)
print("9 = Tiefling")
time.sleep(1)
Species = int(input())

#Checking if number is valid
while Species <= 0 or Species >= 10:
    Species = int(input("Please enter a valid number"))

#Number conversion
if Species == 1:
    Species = "Dragonborn"
elif Species == 2:
    Species = "Dwarf"
elif Species == 3:
    Species = "Elf"
elif Species == 4:
    Species = "Gnome"
elif Species == 5:
    Species = "Goliath"
elif Species == 6:
    Species = "Halfling"
elif Species == 7:
    Species = "Human"
elif Species == 8:
    Species = "Orc"
else:
    Species = "Tiefling"

#Alignment picking
print("Now it's time to pick your alignment, first pick your morality:")
time.sleep(1)
print("1 = Good")
time.sleep(1)
print("2 = Neutral")
time.sleep(1)
print("3 = Evil")
Alignment1 = int(input())

while Alignment1 <= 0 or Alignment1 >= 4:
    Alignment1 = int(input("Please enter a valid number"))

print("Now pick your attitude toward order")
time.sleep(1)
print("1 = Lawful")
time.sleep(1)
print("2 = Neutral")
time.sleep(1)
print("3 = Chaotic")
Alignment2 = int(input())

while Alignment2 <= 0 or Alignment2 >= 4:
    Alignment2 = int(input("Please enter a valid number"))

#Alignment Converter
if Alignment1 == 1:
    Alignment1 = "Good"
elif Alignment1 == 2:
    Alignment1 = "Neutral"
else:
    Alignment1 = "Evil"

if Alignment2 == 1:
    Alignment2 = "Lawful"
elif Alignment2 == 2:
    Alignment2 = "Neutral"
else:
    Alignment2 = "Chaotic"

#Personality 1 based on Alignment
if Alignment1 == "Good":
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        AlignmentPersonality1 = "Compassionate"
    elif DiceRoll == 2:
        AlignmentPersonality1 = "Helpful"
    elif DiceRoll == 3:
        AlignmentPersonality1 = "Honest"
    else:
        AlignmentPersonality1 = "Kind"
elif Alignment1 == "Neutral":
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        AlignmentPersonality1 = "Selfish"
    elif DiceRoll == 2:
        AlignmentPersonality1 = "Disinterested"
    elif DiceRoll == 3:
        AlignmentPersonality1 = "Laconic"
    else:
        AlignmentPersonality1 = "Pragmatic"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        AlignmentPersonality1 = "Dishonest"
    elif DiceRoll == 2:
        AlignmentPersonality1 = "Vengeful"
    elif DiceRoll == 3:
        AlignmentPersonality1 = "Cruel"
    else:
        AlignmentPersonality1 = "Greedy"

#Personality 2 based on Alignment
if Alignment2 == "Lawful":
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        AlignmentPersonality2 = "Cooperative"
    elif DiceRoll == 2:
        AlignmentPersonality2 = "Loyal"
    elif DiceRoll == 3:
        AlignmentPersonality2 = "Judgmental"
    else:
        AlignmentPersonality2 = "Methodical"
elif Alignment2 == "Neutral":
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        AlignmentPersonality2 = "Selfish"
    elif DiceRoll == 2:
        AlignmentPersonality2 = "Disinterested"
    elif DiceRoll == 3:
        AlignmentPersonality2 = "Laconic"
    else:
        AlignmentPersonality2 = "Pragmatic"
else:
    DiceRoll = random.randint(1,4)
    if DiceRoll == 1:
        AlignmentPersonality2 = "Boastful"
    elif DiceRoll == 2:
        AlignmentPersonality2 = "Impulsive"
    elif DiceRoll == 3:
        AlignmentPersonality2 = "Rebellious"
    else:
        AlignmentPersonality2 = "Self-Absorbed"

#Language
LanguageChoice = input("Would you like to choose your languages? Type Y or N").upper()

#User picks
if LanguageChoice == "Y":

    print("Pick one of the following languages as your first language:")
    time.sleep(1)
    print("1 = Common Sign Language")
    time.sleep(1)
    print("2 = Draconic")
    time.sleep(1)
    print("3 = Dwarvish")
    time.sleep(1)
    print("4 = Elvish")
    time.sleep(1)
    print("5 = Giant")
    time.sleep(1)
    print("6 = Goblin")
    time.sleep(1)
    print("7 = Halfling")
    time.sleep(1)
    print("8 = Orc")

    #Language 1
    Language1 = int(input())

    #Checking if number is valid
    while Language1 <= 0 or Language1 >= 9:
        Language1 = int(input("Please enter a valid number"))

    print("Now pick your second language")

    #Language 2
    Language2 = int(input())

    while Language2 <= 0 or Language2 == Language1 or Language2 >= 9:
        Language2 = int(input("Please enter a valid number"))

    #Number Conversion
    if Language1 == 1:
        Language1 = "Common Sign Language"
    elif Language1 == 2:
        Language1 = "Draconic"
    elif Language1 == 3:
        Language1 = "Dwarvish"
    elif Language1 == 4:
        Language1 = "Elvish"
    elif Language1 == 5:
        Language1 = "Giant"
    elif Language1 == 6:
        Language1 = "Gnomish"
    elif Language1 == 7:
        Language1 = "Goblin"
    elif Language1 == 8:
        Language1 = "Halfling"
    else:
        Language1 = "Orc"

    #Number Conversion
    if Language2 == 1:
        Language2 = "Common Sign Language"
    elif Language2 == 2:
        Language2 = "Draconic"
    elif Language2 == 3:
        Language2 = "Dwarvish"
    elif Language2 == 4:
        Language2 = "Elvish"
    elif Language2 == 5:
        Language2 = "Giant"
    elif Language2 == 6:
        Language2 = "Gnomish"
    elif Language2 == 7:
        Language2 = "Goblin"
    elif Language2 == 8:
        Language2 = "Halfling"
    else:
        Language2 = "Orc"

#Computer picks
else:

    DiceRoll = random.randint(1,12)

    #DiceRoll = 1
    if DiceRoll == 1:
        Language1 = "Common Sign Language"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 1:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        elif DiceRoll == 10 or DiceRoll == 11:
            Language2 = "Halfling"
        else:
            Language2 = "Orc"

    #DiceRoll = 2
    elif DiceRoll == 2:
        Language1 = "Draconic"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 2:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        elif DiceRoll == 10 or DiceRoll == 11:
            Language2 = "Halfling"
        else:
            Language2 = "Orc"

    #DiceRoll = 3 or 4
    elif DiceRoll == 3 or DiceRoll == 4:
        Language1 = "Dwarvish"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 3 or DiceRoll == 4:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        elif DiceRoll == 10 or DiceRoll == 11:
            Language2 = "Halfling"
        else:
            Language2 = "Orc"

    #DiceRoll = 5 or 6
    elif DiceRoll == 5 or DiceRoll == 6:
        Language1 = "Elvish"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 5 or DiceRoll == 6:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        elif DiceRoll == 10 or DiceRoll == 11:
            Language2 = "Halfling"
        else:
            Language2 = "Orc"

    #DiceRoll = 7
    elif DiceRoll == 7:
        Language1 = "Giant"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 7:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        elif DiceRoll == 10 or DiceRoll == 11:
            Language2 = "Halfling"
        else:
            Language2 = "Orc"

    #DiceRoll = 8
    elif DiceRoll == 8:
        Language1 = "Gnomish"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 8:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        elif DiceRoll == 10 or DiceRoll == 11:
            Language2 = "Halfling"
        else:
            Language2 = "Orc"

    #DiceRoll = 9
    elif DiceRoll == 9:
        Language1 = "Goblin"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 9:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 10 or DiceRoll == 11:
            Language2 = "Halfling"
        else:
            Language2 = "Orc"

    #DiceRoll = 10 or 11
    elif DiceRoll == 10 or DiceRoll == 11:
        Language1 = "Halfling"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 10 or DiceRoll == 11:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        else:
            Language2 = "Orc"

    #DiceRoll = 12
    else:
        Language1 = "Orc"
        DiceRoll = random.randint(1,12)
        while DiceRoll == 9:
            DiceRoll = random.randint(1,12)
        if DiceRoll == 1:
            Language2 = "Common Sign Language"
        elif DiceRoll == 2:
            Language2 = "Draconic"
        elif DiceRoll == 3 or DiceRoll == 4:
            Language2 = "Dwarvish"
        elif DiceRoll == 5 or DiceRoll == 6:
            Language2 = "Elvish"
        elif DiceRoll == 7:
            Language2 = "Giant"
        elif DiceRoll == 8:
            Language2 = "Gnomish"
        elif DiceRoll == 9:
            Language2 = "Goblin"
        else:
            Language2 = "Halfling"

#Health
if Class == "Barbarian":
    MaxHealth = 12
    MaxHealth += ConstitutionAbilityModifier
elif Class == "Fighter" or Class == "Paladin" or Class == "Ranger":
    MaxHealth = 10
    MaxHealth += ConstitutionAbilityModifier
elif Class == "Bard" or Class == "Cleric" or Class == "Druid" or Class == "Monk" or Class == "Rogue" or Class == "Warlock":
    MaxHealth = 8
    MaxHealth += ConstitutionAbilityModifier
else:
    MaxHealth = 6
    MaxHealth += ConstitutionAbilityModifier

CurrentHealth = MaxHealth

print("Name =", Name)
print("Class =", Class)
print("Background =", Background)
print("Specie =", Species)
print("First Language =", Language1)
print("Second Language =",Language2)
print("")
print("Strength =", Strength)
print("Strength Modifier =", StrengthAbilityModifier)
StrengthSavingThrow = StrengthSavingThrowCalculator()
print("Strength Saving Throw =", StrengthSavingThrow)
print("Personality =", StrengthAppearance)
print("")
print("Dexterity =", Dexterity)
print("Dexterity Modifier =", DexterityAbilityModifier)
DexteritySavingThrow = DexteritySavingThrowCalculator()
print("Dexterity Saving Throw =", DexteritySavingThrow)
print("Personality =", DexterityAppearance)
print("")
print("Constitution =", Constitution)
print("Constitution Modifier =", ConstitutionAbilityModifier)
ConstitutionSavingThrow = ConstitutionSavingThrowCalculator()
print("Constitution Saving Throw =", ConstitutionSavingThrow)
print("Personality =", ConstitutionAppearance)
print("")
print("Intelligence =", Intelligence)
print("Intelligence Modifier =", IntelligenceAbilityModifier)
IntelligenceSavingThrow = IntelligenceSavingThrowCalculator()
print("Intelligence Saving Throw =", IntelligenceSavingThrow)
print("Personality =", IntelligenceAppearance)
print("")
print("Wisdom =", Wisdom)
print("Wisdom Modifier =", WisdomAbilityModifier)
WisdomSavingThrow = WisdomSavingThrowCalculator()
print("Wisdom Saving Throw =", WisdomSavingThrow)
print("Personality =", WisdomAppearance)
print("")
print("Charisma =", Charisma)
print("Charisma Modifier =", CharismaAbilityModifier)
CharismaSavingThrow = CharismaSavingThrowCalculator()
print("Charisma Saving Throw =", CharismaSavingThrow)
print("Personality =", CharismaAppearance)
print("")
if Alignment1 == Alignment2:
    print(Alignment1)
    print(AlignmentPersonality1)
else:
    print(Alignment1)
    print(Alignment2)
    print("")
    print(AlignmentPersonality1)
    print(AlignmentPersonality2)
print("")
print("Maximum Health =", MaxHealth)
print("Current Health =", CurrentHealth)
Initiative = DexterityAbilityModifier
print("Initiative =", Initiative)
Level = LevelCalculator()
print("Level =", Level)
ProficiencyBonus = ProficiencyBonusCalculator()
print("Proficiency Bonus =", ProficiencyBonus)
ArmourClass =  ArmorClassCalculator()
print("Armour Class =", ArmourClass)
print("")
print(BackgroundSkillProficiency1)
print(BackgroundSkillProficiency2)
print(SkillProficiency1)
print(SkillProficiency2)
print(SkillProficiency3)
print(SkillProficiency4)
Athletics = AthleticsBonusCalculator()
print("Athletics =", Athletics)
Acrobatics = AcrobaticsBonusCalculator()
print("Acrobatics =", Acrobatics)
SleightOfHand = SleightOfHandBonusCalculator()
print("Sleight of Hand =", SleightOfHand)
Stealth = StealthBonusCalculator()
print("Stealth =", Stealth)
Arcana = ArcanaBonusCalculator()
print("Arcana =", Arcana)
History = HistoryBonusCalculator()
print("History =", History)
Investigation = InvestigationBonusCalculator()
print("Investigation =", Investigation)
Nature = NatureBonusCalculator()
print("Nature =", Nature)
Religion = ReligionBonusCalculator()
print("Religion =", Religion)
AnimalHandling = AnimalHandlingBonusCalculator()
print("Animal Handling =", AnimalHandling)
Insight = InvestigationBonusCalculator()
print("Insight =", Insight)
Medicine = MedicineBonusCalculator()
print("Medicine =", Medicine)
Perception = PerceptionBonusCalculator()
print("Perception =", Perception)
Survival = SurvivalBonusCalculator()
print("Survival =", Survival)
Deception = DeceptionBonusCalculator()
print("Deception =", Deception)
Intimidation = IntimidationBonusCalcualtor()
print("Intimidation =", Intimidation)
Performance = PerformanceBonusCalculator()
print("Performance =", Performance)
Persuasion = PersuasionBonusCalculator()
print("Persuasion =", Persuasion)