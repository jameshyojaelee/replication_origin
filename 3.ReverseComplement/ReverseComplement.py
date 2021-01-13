def ReverseComplement(Pattern):
    pattern = list(Pattern[::-1])
    complements = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    reverse = [complements[i] for i in pattern]
    return ''.join(reverse)

ReverseComplement('AAAACCCGGT')

#import text file and immediately covert it to string
input = open('C:/Users/james/Desktop/UCSD/BENG181/replication_origin/3.ReverseComplement/dataset_442776_2.txt', 'r').read().splitlines()
DNA = ''.join(input)
len(DNA)
reverse = ReverseComplement(DNA)

#write the file to text file
output = open("C:/Users/james/Desktop/UCSD/BENG181/replication_origin/3.ReverseComplement/output.txt", "w")
output.write(reverse)
output.close()