class Seq:
    "A class for representing sequences"
    def __init__(self,strbases):
        self.strbases = strbases #used to store the bases you have passed in self.strbases #self.strbases es un atributte del nuevo objeto
        if not self.valid_sequence(): #no arguments if you put the self. before the function
            self.strbases = "ERROR"
            print("ERROR!!!!")
        else:
            print("New sequence created!")

    @staticmethod
    def valid_sequence2(sequence): #no necesita una clase, es un argumento normal
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence(self): #as this function belongs to Seq class, we have to write it below the init method
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    #def print_seqs(self, seq_list):
        #for elements in seq_list:
            #exit = False
            #while not exit:






    def __str__(self): #trasform the class into a string so that we can print it
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

#Main program
# Main program
# Create an object of the class Seq
#s1 = Seq("AGTACACTGGT")
# Create another object of the Class Seq
#s2 = Seq("CGTAAC")
#print("Testing...")
#print(f"Sequence 1: {s1}")
#print(f"  Length: {s1.len()}")
#print(f"Sequence 2: {s2}")
#print(f"  Length: {s2.len()}")

#class Gene(seq): #gene tiene todas las propiedades de seq y más. Por eso tienes que poner seq dentro de la función
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
#s1 = Seq("AGTACACTGGT")
#g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
#print(f"Sequence 1: {s1}")
#print(f"Gene: {g}")