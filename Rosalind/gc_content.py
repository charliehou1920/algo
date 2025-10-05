import os
import re

def counting(seq: str) -> float:
    # 防御：避免除以 0；并统一大写并清洗非 ACGT 字符
    seq = re.sub(r"[^ACGT]", "", seq.upper())
    return 0.0 if not seq else (seq.count("G") + seq.count("C")) / len(seq) * 100

def gc_count(text_path: str):
    # 让相对路径相对于脚本所在目录
    base_dir = os.path.dirname(__file__)
    text_path = os.path.join(base_dir, text_path)

    results = {}
    current_id = None
    current_seq = []

    with open(text_path, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith(">Rosalind_"):
                # 把上一个序列先结算
                if current_id is not None:
                    results[current_id] = counting("".join(current_seq))
                # 开始新的记录：去掉 '>'
                current_id = line[1:]
                current_seq = []
            else:
                # 追加序列行（FASTA 可能多行）
                current_seq.append(line)

    # 别忘了结算最后一个
    if current_id is not None:
        results[current_id] = counting("".join(current_seq))

    # 打印全部
    for seq_id, gc in results.items():
        print(seq_id, "=>", gc)

    # 如果你想要最高 GC 的记录：
    best_id, best_gc = max(results.items(), key=lambda kv: kv[1])
    print("\nMax GC:", best_id, "=>", best_gc)

if __name__ == "__main__":
    gc_count("data/rosalind_gc.txt")