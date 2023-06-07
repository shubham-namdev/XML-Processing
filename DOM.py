"""
-> XML Parsing with DOM
"""

#~ DOM - Document Object Model
#>> Loads full document
#>> Faster than SAX

import xml.dom.minidom

domtree = xml.dom.minidom.parse("group.xml")
group = domtree.documentElement

persons = group.getElementsByTagName("person")

for person in persons:
    print("------Person------")

    if person.hasAttribute("id"):
        print(f"ID : {person.getAttribute('id')}")

    name = person.getElementsByTagName("name")[0].firstChild.data
    age = person.getElementsByTagName("age")[0].firstChild.data
    weight = person.getElementsByTagName("weight")[0].firstChild.data
    height = person.getElementsByTagName("height")[0].firstChild.data

    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Weight : {weight}")
    print(f"Height : {height}")


#~ Manipulating Values

#>> Changing values

persons = group.getElementsByTagName("person")
persons[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = "Albert Steam"

# Printing
for person in persons:
    print("------Person------")

    if person.hasAttribute("id"):
        print(f"ID : {person.getAttribute('id')}")

    name = person.getElementsByTagName("name")[0].firstChild.data
    age = person.getElementsByTagName("age")[0].firstChild.data
    weight = person.getElementsByTagName("weight")[0].firstChild.data
    height = person.getElementsByTagName("height")[0].firstChild.data

    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Weight : {weight}")
    print(f"Height : {height}")

#>> Setting Attributes
persons[0].setAttribute("id", "10")

#>> Saving Changes
domtree.writexml(open("group.xml", "w"))

#>> Creating new Elements

newPerson = domtree.createElement("person")
newPerson.setAttribute("id", "6")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Antonio Garcia"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("28"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("75"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("168"))

newPerson.appendChild(name)
newPerson.appendChild(age)
newPerson.appendChild(weight)
newPerson.appendChild(height)

group.appendChild(newPerson)

domtree.writexml(open("group.xml", "w"))
