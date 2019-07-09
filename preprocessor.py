# Rajath Akshay Vanikul (29498724)

#Class is created to tokenise the given text.
class Preprocessor:
#Initiated the reference token list under the constructor for this class.
    def __init__(self):
        self.tokenised_list=[]

#Overload the print function to display each element of the list in readable format.        
    def __str__(self):
        ref = ""
        for i in self.tokenised_list:
            ref += str('   \t    '+ i + '\n')
        return ref

#Splitting the input sequence over space
    def tokenise(self, input_sequence):
        self.tokenised_list = input_sequence.split()

#Return the tokenised list    
    def get_tokenised_list(self):
        return self.tokenised_list
    