import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm

class DatasetPreprocessor():

  def __init__(self, path):
    self.dataset = pd.read_csv(path, sep="\t", header=None, quotechar="§", quoting=csv.QUOTE_ALL, engine='python')
  
  def process(self):
    seqs = []
    labels = []
    seq = []
    lab = []
 #   pos = []
    for index, row in tqdm(self.dataset.iterrows()):
        if row[0] == "*":
            assert len(seq)==len(lab)
            seqs.append(" ".join(seq))
            labels.append(" ".join(lab))
            #qs.append(seq)
            #labels.append(lab)
            assert len(seq)==len(lab)
            seq = []
            lab = []
        else:
                #print(seq)
                #print(lab)
                #print(row)
                #print(self.dataset.iloc[index+1])
                #input()
            seq.append(str(row[1]))
            lab.append(str(row[2]))
    pos_df = pd.DataFrame({ # 'position':pos,
                             'tokens': seqs,
                             'pos_tags': labels
                        })
    pos_df = pos_df.dropna()
   # dataset.columns = ["position", "tokens", "pos_tags"]
   # dataset = dataset.drop(['position'], axis=1)
    train_set, dev_set = train_test_split(pos_df, test_size=0.1)
    return train_set, dev_set

  def get_labels(self):
    return set(self.dataset[3].to_list())
	
pr = DatasetPreprocessor("complete_data.tsv")

train, test = pr.process()

train.to_csv("sample.csv", index=False)
test.to_csv("tsample.csv", index=False)