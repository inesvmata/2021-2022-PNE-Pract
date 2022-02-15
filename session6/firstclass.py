class Seq:
    "A class for representing sequences"
    def __init__(self,strbases):
        self.strbases = strbases #used to store the bases you have passed in self.strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

#Main program
# Main program
# Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
# Create another object of the Class Seq
s2 = Seq("CGTAAC")
print("Testing...")
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")

#class Gene(seq): #gene etiene todas las propiedades de seq y más. Por eso tienes que poner seq dentro de la función
class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases) #it will execute the init function of the classsequence above (because sequence is inside gene)
        self.name = name
        print("New gene created")

# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")