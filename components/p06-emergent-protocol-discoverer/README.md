# P06 · emergent-protocol-discoverer

> 机制簇：**智能体间涌现语言** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
AI 们反复说同样的话，其实可以提炼出'暗号'。这个工具从聊天记录里自动找出这些暗号。

**L1 · 机制本质**
从日志抽取高频 n-gram 作为候选协议 token，按频次与长度打分。

**L2 · 怎么用上**
discover(logs, k) 返回候选协议 token 列表。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P06] ['check db', 'db then', 'then deploy']
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 多 agent 长会话、跨轮通信 token 占比高、双方可共享同一字典的场景。 |
| **不该用** | 跨组织通信、需要人类逐条审计的合规链路（压缩后不可读即审计断链）。 |
| **常见误用** | 只压不存字典：一旦无法回译，日志就变成不可追溯的密文。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P05` agent-lingua-compressor · `P07` symbolic-handshake-negotiator · `P08` cross-llm-message-translator
- 本仓是 **P06 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P06-emergent-protocol-discoverer/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P06 · emergent-protocol-discoverer © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
