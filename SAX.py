"""
-> XML Parsing with SAX

XML = Extensible Markup Language
>> Hierarchically structure our data in file
>> Application-independent, Platform-independent
"""

#~ SAX - Simple API for XML
#>> Better suited for Large XML files; where RAM is limited
#>> Loads only parts of the file to RAM

import xml.sax

handler = xml.sax.ContentHandler()

parser = xml.sax.make_parser()
parser.setContentHandler(handler=handler)
parser.parse("./group.xml")


"""
-> Defining custom ContentHandler Class
"""

import xml.sax

class MyHandler(xml.sax.ContentHandler) :
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("-----PERSON-----")
            id = attrs["id"]
            print(f"ID : {id}")
    
    def endElement(self, name):
        if self.current == "name":
            print(f"Name : {self.name}")
        elif self.current == "age":
            print(f"Age : {self.age}")
        elif self.current == "weight":
            print(f"Weight : {self.weight}")
        elif self.current == "height":
            print(f"Height : {self.height}")
        self.current = ""

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content       


handler = MyHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler=handler)
parser.parse('group.xml')

