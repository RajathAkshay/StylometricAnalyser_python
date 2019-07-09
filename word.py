# Rajath Akshay Vanikul (29498724)

#import pandas package as 'pd' for further usage.
import pandas as pd

#Create a class 'WordAnalyser' which contains methods to count occurrence each word in tokenised list.
class WordAnalyser:

#Initiated the reference character dataframe under the constructor to store word analysis.
    def __init__(self):
        self.word_df = pd.DataFrame()

#Overload the print function to display dataframe in readable format.    
    def __str__(self):
        ref = ""
        for i,j in self.word_series.iteritems():
            ref += str(i+' occured   '+ str(j) +' times '+ '\n')

#Define a method to analyse the count of each word in the list of words and return the
#normalised occurrence of each character as a dataframe.    
    def analyse_words(self, tokenised_list):
        import string
        list = [x.lower() for x in tokenised_list]
        word_list = []
        for item in list:
            if item not in string.punctuation:
                word_list.append(item)
        series = pd.value_counts(word_list).sort_index()
        self.word_df = pd.DataFrame({'Words':series.index, 'Occurences':series.values})
        sum = self.word_df['Occurences'].sum()
        self.word_df['Normalised_count'] = self.word_df['Occurences']/sum
 
#We also import and filter the set of stopwords from a desired web-page to copare and
#count the occurrence of each stop word in the file and return the normalised occurrences.
    def get_stopword_frequency(self):
        import urllib.request 
        url = "http://www.lextek.com/manuals/onix/stopwords1.html"
        filename = "stopwords.txt" 
        urllib.request.urlretrieve(url,filename)
        with open(filename, 'r') as myfile:
            data=myfile.read()
        st_list = data.split()
        last = st_list.index('z')
        first = st_list.index('about')
        list = st_list[first:last+1]
        for item in list:
            if len(item) == 1:
                list.remove(item)
        stopword_list = list
        dict = {}
        for index,row in self.word_df.iterrows():
            if row['Words'] in stopword_list:
                dict[row['Words']] = row['Occurences']
        series = pd.Series(dict)
        self.word_df = pd.DataFrame({'Stop Words':series.index,'Occurences':series.values})
        sum = self.word_df['Occurences'].sum()
        self.word_df['Normalised_count'] = self.word_df['Occurences']/sum
        return self.word_df
    
#Introduce another method to count the word length used in each file and 
#return the normalised word length in a dataframe.
    def get_word_length_frequency(self):
        self.word_df['Length_Word'] = self.word_df['Words'].apply(len)
        sum = self.word_df['Occurences'].sum()
        self.word_df['Normalised_length'] = self.word_df['Occurences']/sum
        return self.word_df