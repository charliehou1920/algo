def gc_count(text_path):
    results = {}
    current_id = None
    current_seq = ""

    with open(text_path, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith(">Rosalind_"):
                # If we already have a previous sequence, process it
                if current_id is not None:
                    results[current_id] = counting(current_seq)
                
                # start a new sequence
                current_id = line[:1]
                current_seq = ""
            else:
                # The following are DNA sequences
                current_seq += line
            
        if current_id is not None:
            results["current_id"] = counting(current_seq)
            

def counting(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100 