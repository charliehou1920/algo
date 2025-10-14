'''
用滑窗收集所有的k长度的substring 然后把他们放入 dictionary里 进行统计
'''

from collections import Counter
def frequent_words(text, k):
    if k <= 0 or k > len(text):
        return []
    
    counts = Counter(text[i:i+k] for i in range(len(text) - k + 1))
    max_count = max(counts.values())
    top_kmers = [kmer for kmer, c in counts.items() if c == max_count]
    return top_kmers

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
top_kmers = frequent_words(text, k)
print(top_kmers)