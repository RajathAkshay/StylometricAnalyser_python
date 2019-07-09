# Rajath Akshay Vanikul (29498724)

#import pandas package as 'pd' for further usage.
import pandas as pd

#importing all the pre-written modules to assist with stylometric analysis.
import preprocessor_29498724 as p
import character_29498724 as c
import word_29498724 as w
import visualiser_29498724 as v

# Create a main function
def main():
 
#read all the text files to a variable for further analysis.
    with open('Edward_II_Marlowe.tok', 'r') as myfile:
        ed_marlowe=myfile.read()
    
    with open('Jew_of_Malta_Marlowe.tok', 'r') as myfile:
        jew_marlowe=myfile.read()
            
    with open('Richard_II_Shakespeare.tok', 'r') as myfile:
        rich_shakespeare=myfile.read()
    
    with open('Hamlet_Shakespeare.tok', 'r') as myfile:
        ham_shakespeare=myfile.read()
        
    with open('Henry_VI_Part1_Shakespeare.tok', 'r') as myfile:
        henry1_shakespeare=myfile.read()
        
    with open('Henry_VI_Part2_Shakespeare.tok', 'r') as myfile:
        henry2_shakespeare=myfile.read()

#create a list of all the input variables to assist with iterations.
    input_list = [ed_marlowe,jew_marlowe,rich_shakespeare,ham_shakespeare,henry1_shakespeare,henry2_shakespeare]

#Create a list for holding six dataframes in each analysis for graph plotting
    char_analysis = []
    punc_analysis = []
    length_analysis = []
    stopword_analysis = []
    
#iterating through the input list to call methods and perform the core analysis to obtain analysis.    
    for item in input_list:
        
#Creating an instence of preprocessor class to tokenise the input
        processor= p.Preprocessor()
        processor.tokenise(item)
        token_list = processor.get_tokenised_list()
#Creating an instance of Character Analysis to obtain the analysed output dataframe.         
        char = c.CharacterAnalyser()
        char_df = char.analyse_characters(token_list)
        import string
        dict = {}
        for index,row in char_df.iterrows():
            if row['Characters'] not in string.punctuation:
                dict[row['Characters']] = row['Occurences']
        series = pd.Series(dict)
        char_df = pd.DataFrame({'Characters':series.index,'Occurences':series.values})
        sum = char_df['Occurences'].sum()
        char_df['Normalised_count'] = char_df['Occurences']/sum
        char_analysis.append(char_df)
        
#Creating an instance of punctuation frequency method to obtain the frequency of punctuation.        
        punc = char.get_punctuation_frequency()
        punc_analysis.append(punc)
        
#reating an instance of Word Analysis method to obtain the count of each word.
        word = w.WordAnalyser()
        word.analyse_words(token_list)
        
#Creating an instance of Word length frequency method to obtain the frequency of wordlength.
        word_length = word.get_word_length_frequency()
        length_analysis.append(word_length)

#Creating an instance of Stopword frequency method to obtain the frequency of wordlength.
        stopword = word.get_stopword_frequency()
        stopword_analysis.append(stopword)


#Creating an instances of all the analysis to plot a graph.      
    visual = v.AnalysisVisualiser(char_analysis)
    visual.visualise_character_frequency()

    visual = v.AnalysisVisualiser(punc_analysis)    
    visual.visualise_punctuation_frequency()

    visual = v.AnalysisVisualiser(stopword_analysis)
    visual.visualise_stopword_frequency()
    
    visual = v.AnalysisVisualiser(length_analysis)
    visual.visualise_word_length_frequency()

# This statement confirms that main function should only be executed if the program is executed as a standalone program.
# It will not be executed if the program is imported as a module. 
if __name__ == "__main__":
    main()
