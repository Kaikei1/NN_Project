import sys
import argparse
import os


def extract_info(file,new_filename):
    if not os.path.exists("output"):
        os.makedirs("output")    
    with open(file) as f:
        with open("output/"+new_filename,"w") as s:
            for line in f:
                if  line.isspace():                    
                    s.write('*\n')
                elif '#' == line[0]:
                    continue
                else:
                        line = line.split()
                        poaw = line[2]
                        word = line[3]
                        POS = line[4]
                        s.write(poaw + '\t' + word + '\t' + POS + '\n' )

def create_info_file(file,new_filename):
    tags = dict()
    sequence_ls = []
    n_words = 0
    sequence = []
    with open("output/"+file) as f:
        for line in f:
            if line[0]=='*':
                if sequence != []:
                    sequence_ls.append(len(sequence))
                    sequence=[]
            else:
                line = line.split()
                sequence.append(line[1])
                n_words += 1
                if line[2] in tags:
                    tags[line[2]] += 1
                else:
                    tags[line[2]] = 1
    max_l = max(sequence_ls)
    min_l = min(sequence_ls)
    mean_l = sum(sequence_ls)/len(sequence_ls)
    num_seq = len(sequence_ls)
    for tag in tags:
        tags[tag] /= n_words
    with open("output/"+new_filename,'w') as s:
         s.write('Max sequence length: '+str(max_l)+'\n')
         s.write('Min sequnece length: '+str(min_l)+'\n')
         s.write('Mean sequnece length: '+str(mean_l)+'\n')
         s.write('Number of sequences: '+str(num_seq)+'\n'+'\n'+'Tags:'+'\n')
         for tag in tags:
             s.write(tag+'\t'+str(tags[tag])+'\n')



def main():
    parser = argparse.ArgumentParser(description='create .tsv and .info file from .conll file')
    parser.add_argument('conll_file')
    parser.add_argument('filename',help='name for .tsv and .info file')
    args=parser.parse_args()
    if not args.conll_file.endswith('.conll'):
        print('Error! First argument has the wrong type! Should be .conll file')
        sys.exit()
    extract_info(args.conll_file,args.filename+'.tsv')
    create_info_file(args.filename+'.tsv',args.filename+'.info')

if __name__ == "__main__":
    main()































             
             
