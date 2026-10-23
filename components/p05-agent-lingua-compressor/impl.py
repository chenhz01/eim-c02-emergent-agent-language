# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P05 agent-lingua-compressor — 智能体间涌现语言

L0: 两个 AI 聊天时用一长串话，很费钱。这个工具让它们用缩写符号说话，省好几倍。
L1: 统计高频短语→映射为符号 token，压缩后测压缩率。
L2: compress(text, symbols) 返回(压缩文本, 压缩率)；symbols 由 build_symbols 生成。
"""

def build_symbols(texts, top=8, min_len=4):
    from collections import Counter
    c = Counter()
    for t in texts:
        for w in t.split():
            if len(w) >= min_len: c[w] += 1
    return {w: f"§{i}" for i, (w, _) in enumerate(c.most_common(top))}

def compress(text, symbols):
    out = text
    for w, sym in symbols.items():
        out = out.replace(w, sym)
    ratio = 1 - len(out) / max(1, len(text))
    return out, round(ratio, 3)

def demo():
    t = "please verify the database connection before the deployment window"
    sym = build_symbols([t])
    print("[P05]", compress(t, sym))


if __name__ == "__main__":
    demo()
