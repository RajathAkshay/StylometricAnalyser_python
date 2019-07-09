# Rajath Akshay Vanikul (29498724)

#import pandas package as 'pd' for further usage.
import pandas as pd

#Class is created to analyse characters in the given text.
class CharacterAnalyser:
#Initiated the reference character dataframe under the constructor for this class.
    def __init__(self):
        self.char_df = pd.DataFrame()
#Overload the print function to display each element of the list in readable format.    
    def __str__(self):
        ref = ""
        for i,j in self.char_df.iteritems():
            ref += str(i+'   \t    '+ str(j) + '\n')
        return ref

#Define a method to analyse the count of each character in the text and
#return the occurrence of each character as a dataframe.
#I have used pandas series structure to assist me with count of each character.
    def analyse_characters(self, tokenised_list):
        input_str = "".join(tokenised_list)
        char = input_str.lower()
        char_list = list(char)
        series = pd.value_counts(char_list).sort_index()
        self.char_df = pd.DataFrame({'Characters':series.index,'Occurences':series.values})
        sum = self.char_df['Occurences'].sum()
        self.char_df['Normalised_count'] = self.char_df['Occurences']/sum
        return self.char_df
    
#Define a method to analyse the count of each punctuation in the text and
#return the occurrence of each punctuation as a dataframe.
#I have used a dictionary to assist me with the filter process.
    def get_punctuation_frequency(self):
        import string
        dict = {}
        for index,row in self.char_df.iterrows():
            if row['Characters'] in string.punctuation:
                dict[row['Characters']] = row['Occurences']
        series = pd.Series(dict)
        self.char_df = pd.DataFrame({'Punctuations':series.index,'Occurences':series.values})
        sum = self.char_df['Occurences'].sum()
        self.char_df['Normalised_count'] = self.char_df['Occurences']/sum
        return self.char_df        