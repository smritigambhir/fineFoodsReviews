class Indexer():
    
    terms=dict()
    
    def indexify(self,index,line):
        t=dict()
        k=0
        for token in line:
            if token not in t:
                la=list()
                lb=list()
                lc=list()
                lb.append(k)
                la.append(index)
                la.append(lb)
                lc.append(la)
                t[token]=lc
            else:
                l=t[token]
                l[0][1].append(k)
            k=k+1
        return t
    
    def merge_one(self,tokens):
        for key in tokens:
            if key in self.terms:
                val=tokens[key][0]
                self.terms[key].append(val)
            else:
                self.terms[key]=tokens[key]
                
    def merge_all_indices(self,tokens):
        indices=[self.indexify(i,tokens[i]) for i in range(0,len(tokens))]
        for i in range(0,len(indices)):
            self.merge_one(indices[i])
            
    def process_review_text(self,review_text,preprocess_text):
        print(preprocess_text)
        tokens=preprocess_text(review_text)
        self.merge_all_indices(tokens)
    