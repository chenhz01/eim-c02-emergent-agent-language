# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P06 emergent-protocol-discoverer — 智能体间涌现语言

L0: AI 们反复说同样的话，其实可以提炼出'暗号'。这个工具从聊天记录里自动找出这些暗号。
L1: 从日志抽取高频 n-gram 作为候选协议 token，按频次与长度打分。
L2: discover(logs, k) 返回候选协议 token 列表。
"""

def discover(logs, k=5, n=2):
    from collections import Counter
    c = Counter()
    for line in logs:
        w = line.split()
        for i in range(len(w)-n+1):
            c[" ".join(w[i:i+n])] += 1
    return [t for t, _ in c.most_common(k)]

def demo():
    logs = ["check db then deploy", "check db first", "deploy after check db"]
    print("[P06]", discover(logs, 3))


if __name__ == "__main__":
    demo()
