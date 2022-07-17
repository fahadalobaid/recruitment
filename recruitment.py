def get_skills():
    skills = ['Python','C','Javascript', 'Eating']
    # Add at least 3 random skills for the user to select from
    return skills


def show_skills(skills):
    
    for i, skills in enumerate(skills,1):
         print( i , "." + skills,end="\n")
    
    
    # Pretty print skills to the user
    # Write your code here
    ...


def get_user_skills(skills):
    chooseskill1 = False
    chooseskill2 = False
    indexlist = [1 , 2 , 3, 4]
    skillslist = []
    while chooseskill1 == False:
        skill1 = input("choose the first skill by entering its number:")
        if int(skill1) in indexlist:
            skill1 = str(skills[int(skill1)-1])
            skillslist.append(skill1)
            chooseskill1 = True
        else:
            print("choose one skill again please!")
    while chooseskill2 == False:
        skill2 = input("choose the second skill by entering its number:")
        if int(skill2) in indexlist:
            skill2 = str(skills[int(skill2)-1])
            skillslist.append(skill2)
            chooseskill2 = True
        else:
            print("choose one skill again please!")
    return skillslist
    

    # Show the available skills and have user pick from them
    # Write your code here
    ...


def get_user_cv(skills):

    cv = {'name' : input("What is your name?"), 'age': int(input("How old are you?")), 'experience' : int(input("How many years of experience do you have?")),'skills':skills}
    return cv



    # Get the users CV from their inputs
    # Write your code here
    ...


def check_acceptance(cv, desired_skill):

    myskills = get_skills()
    checkacceptance = False
    if cv.get('age') < 40 and cv.get('age') > 25 and cv.get('experience') > 3 and myskills[2] in desired_skill:
        checkacceptance = True
    else:
        pass
    return checkacceptance



    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    ...


def main():

    print("Welcome to the special recuitment program , please answer the following questions :")
    getSkills = get_skills()
    showSkills = show_skills(getSkills)
    desired_skill = get_user_skills(getSkills)
    cv = get_user_cv(desired_skill)
    checkAcceptance = check_acceptance(cv=cv , desired_skill = desired_skill)
    if checkAcceptance == True:
        print(f"You have been accepted, {cv.get('name').title()}")
    else:
         print(f"Sorry! You have NOT been accepted, {cv.get('name').title()}")

    
    # Write your main logic here by combining the functions above into the
    # desired outcome
    


if __name__ == "__main__":
    main()
