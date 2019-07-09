# Rajath Akshay Vanikul (29498724)

#import pandas package as 'pd' for further usage.
import pandas as pd

#Create a class 'AnalysisVisualiser' which contains methods to plot the analysis performed.
class AnalysisVisualiser:

#Initiated the reference character list under the constructor to store word analysis.
    def __init__(self, all_text_stats):
        self.list = all_text_stats
#Define a method to take the instance variable and plot the graph (Character vs Normalised Count)
    def visualise_character_frequency(self):
        df = pd.concat(self.list,axis=1)
        df.plot(x='Characters', y ='Normalised_count',legend=False)
#Define a method to take the instance variable and plot the graph (Punctuations vs Normalised Count)
    def visualise_punctuation_frequency(self):
        df = pd.concat(self.list,axis=1)
        df.plot(x='Punctuations', y ='Normalised_count',legend=False)
#Define a method to take the instance variable and plot the graph (Stopword vs Normalised Count)
    def visualise_stopword_frequency(self):
        df = pd.concat(self.list,axis=1)
        df.plot(x='Stop Words', y ='Normalised_count',legend=False)
#Define a method to take the instance variable and plot the graph (Word_length vs Normalised Count)
    def visualise_word_length_frequency(self):
        df = pd.concat(self.list,axis=1)
        df.plot(x='Words', y ='Normalised_length',legend=False)