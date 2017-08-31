from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

class Text_Processor():
    
    stemmer = PorterStemmer()
    stop_words = ['a','an','the','of','at','for','with','what','when',
              'where','how','is','was','between','and','in',',','(',')',
              '.','{','}','?','!','this','that','etc','there',
              'me','my','you','your','i','their','has','have','been','do',
              'give', 'got','had','one']
    
    def remove_stop_words(self,line):
        line = [word for word in line if word not in self.stop_words]
        return line
    
    def stem_query(self,line):
        line = [self.stemmer.stem(x) for x in line]
        return line
    
    def preprocess_text(self,queries):
        queries=[x.lower() for x in queries]
        tokens=[word_tokenize(x) for x in queries]
        tokens=[self.remove_stop_words(x) for x in tokens]   
        tokens=[self.stem_query(x) for x in tokens]
        return tokens
    
    def preprocess_query(self,query):
        query=query.replace('-',' ')
        query=query.lower()
        tokens=word_tokenize(query)
        tokens=self.remove_stop_words(tokens)
        tokens=self.stem_query(tokens)
        return tokens
