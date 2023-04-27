#sr6bf Sarah Raza
#This assignment looks through an url of computer science classes to see the departments certain instructors teach in as well as the compatability of two classes

import urllib.request

def instructor_lectures(department, instructor):
    '''
    :param department: An argument for the given departments that instructors teach in
    :param instructor: An argument to see if the lecture is being taught my a given professor
    :return: Returns a list of all the course names for the lectures taught by a given instructor
    '''
    link = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + department)

    class_list = []

    for professors in link:
       if not professors.decode("UTF-8").strip().split("|")[3] in class_list:
         if instructor == professors.decode("UTF-8").strip().split("|")[4] or instructor + "+1" == professors.decode("UTF-8").strip().split("|")[4]:
            if professors.decode("UTF-8").strip().split("|")[5] == "Lecture":
                class_list.append(professors.decode("UTF-8").split("|")[3])
    return class_list

def compatible_classes(first_class, second_class, needs_open_space = False):
    '''
    :param first_class: An argument for the first class and the time and day it takes place
    :param second_class: An argument for the second class and the time and day it takes place
    :param needs_open_space: When this argument is true, the function should return false if class reached enrollment capacity
    :return: Return booleans depending on if two classes are compatible with no overlap
    '''
    theurl = "http://cs1110.cs.virginia.edu/files/louslist/"
    theurl2 = "http://cs1110.cs.virginia.edu/files/louslist/"
    listtemp1 = first_class.split(" ")
    listtemp2 = second_class.split(" ")
    theurl += listtemp1[0]
    theurl2 += listtemp2[0]
    link = urllib.request.urlopen(theurl)
    link2 = urllib.request.urlopen(theurl2)
    first_class_list = []
    second_class_list = []
    department1 = first_class.replace("-"," ").split(" ")
    department2 = second_class.replace("-", " ").split(" ")
    for classes in link:
        if (department1[0] == classes.decode("UTF-8").strip().split("|")[0]):
            if (department1[1] == classes.decode("UTF-8").strip().split("|")[1]):
                if (department1[2] == classes.decode("UTF-8").strip().split("|")[2]):
                    first_class_list.append(classes.decode("UTF-8").split("|")[0])
                    first_class_list.append(classes.decode("UTF-8").split("|")[1])
                    first_class_list.append(classes.decode("UTF-8").split("|")[2])
                    first_class_list.append(classes.decode("UTF-8").split("|")[3])
                    first_class_list.append(classes.decode("UTF-8").split("|")[4])
                    first_class_list.append(classes.decode("UTF-8").split("|")[5])
                    first_class_list.append(classes.decode("UTF-8").split("|")[6])
                    first_class_list.append(classes.decode("UTF-8").split("|")[7])
                    first_class_list.append(classes.decode("UTF-8").split("|")[8])
                    first_class_list.append(classes.decode("UTF-8").split("|")[9])
                    first_class_list.append(classes.decode("UTF-8").split("|")[10])
                    first_class_list.append(classes.decode("UTF-8").split("|")[11])
                    first_class_list.append(classes.decode("UTF-8").split("|")[12])
                    first_class_list.append(classes.decode("UTF-8").split("|")[13])
                    first_class_list.append(classes.decode("UTF-8").split("|")[14])
                    first_class_list.append(classes.decode("UTF-8").split("|")[15])
                    first_class_list.append(classes.decode("UTF-8").strip().split("|")[16])
    for classes in link2:
        if (department2[0] == classes.decode("UTF-8").strip().split("|")[0]):
            if (department2[1] == classes.decode("UTF-8").strip().split("|")[1]):
                if (department2[2] == classes.decode("UTF-8").strip().split("|")[2]):
                    second_class_list.append(classes.decode("UTF-8").split("|")[0])
                    second_class_list.append(classes.decode("UTF-8").split("|")[1])
                    second_class_list.append(classes.decode("UTF-8").split("|")[2])
                    second_class_list.append(classes.decode("UTF-8").split("|")[3])
                    second_class_list.append(classes.decode("UTF-8").split("|")[4])
                    second_class_list.append(classes.decode("UTF-8").split("|")[5])
                    second_class_list.append(classes.decode("UTF-8").split("|")[6])
                    second_class_list.append(classes.decode("UTF-8").split("|")[7])
                    second_class_list.append(classes.decode("UTF-8").split("|")[8])
                    second_class_list.append(classes.decode("UTF-8").split("|")[9])
                    second_class_list.append(classes.decode("UTF-8").split("|")[10])
                    second_class_list.append(classes.decode("UTF-8").split("|")[11])
                    second_class_list.append(classes.decode("UTF-8").split("|")[12])
                    second_class_list.append(classes.decode("UTF-8").split("|")[13])
                    second_class_list.append(classes.decode("UTF-8").split("|")[14])
                    second_class_list.append(classes.decode("UTF-8").split("|")[15])
                    second_class_list.append(classes.decode("UTF-8").strip().split("|")[16])

    range1 = (range(int(first_class_list[12])),int(first_class_list[13]))
    range2 = (range(int(second_class_list[12])),int(second_class_list[13]))


    if ((first_class_list[7] == True) and (second_class_list[7] == False)) or ((first_class_list[7] == False) and (second_class_list[7] == True)):
        if ((first_class_list[8] == True) and (second_class_list[8] == False)) or ((first_class_list[8] == False) and (second_class_list[8] == True)):
            if ((first_class_list[9] == True) and (second_class_list[8] == False)) or ((first_class_list[9] == False) and (second_class_list[9] == True)):
                if ((first_class_list[10] == True) and (second_class_list[10] == False)) or ((first_class_list[10] == False) and (second_class_list[10] == True)):
                    if ((first_class_list[11] == True) and (second_class_list[11] == False)) or ((first_class_list[11] == False) and (second_class_list[11] == True)):
                        if needs_open_space is True:
                            if (first_class_list[15] >= first_class_list[16]) or (second_class_list[15] >= second_class_list[16]):
                                return False
                        else:
                            return True
    else:
        for number in range1:
            if number in range2:
                return False
            elif needs_open_space is True:
                if (first_class_list[15] >= first_class_list[16]) or (second_class_list[15] >= second_class_list[16]):
                    return False
                else:
                    return True
            else:
                return True


