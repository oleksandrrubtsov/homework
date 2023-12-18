class Person:
    def __init__(self, fname, lname):
        self.fname = fname.title()
        self.lname = lname.title()
        

    @property
    def full_name(self):
        return self.fname.title() + " " + self.lname.title()
    
    @property
    def initials(self):
        return self.fname[0].upper() + self.lname[0].upper()
    
    @full_name.setter
    def full_name(self, name):
        f, l = name.split(" ")
        self.fname = f.title()
        self.lname = l.title()

    @full_name.deleter
    def full_name(self):
        self.fname = None
        self.lname = None
        print("Deleted")



obj = Person('oleksandr', 'rubtsov')
print(obj.full_name)
print(obj.initials)
del obj.full_name
print(obj.fname, obj.lname)

obj.fname = 'eduard'
print (obj.full_name)
print(obj.initials)

obj.lname = 'telitchenko'
print(obj.full_name)
print(obj.initials)

obj.fname = 'natalia'
obj.lname = 'madiar'
print(obj.full_name)
print(obj.initials)


class MyClass:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            raise ValueError("Invalid email address provided.")
    
    @classmethod
    def validate(cls, email):
        if "@" in email:
            prefix, domain = email.split("@", 1)


