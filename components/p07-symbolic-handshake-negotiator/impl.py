# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P07 symbolic-handshake-negotiator — 智能体间涌现语言

L0: 两个 AI 第一次合作，先对一下彼此都懂的词，避免鸡同鸭讲。
L1: 取双方词表交集作为共享符号表；交集为空则回退到最小公共协议。
L2: handshake(a_vocab, b_vocab) 返回共享符号表。
"""

def handshake(a_vocab, b_vocab, fallback=("req", "ack", "err")):
    shared = sorted(set(a_vocab) & set(b_vocab))
    return shared if shared else list(fallback)

def demo():
    print("[P07]", handshake(["db","deploy","check"], ["deploy","check","rollback"]))


if __name__ == "__main__":
    demo()
