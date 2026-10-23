# C02 · Emergent Agent Language

> **机制簇**：智能体间涌现语言 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
两个 AI 协作用人类话太啰嗦，改用它们自己约定的「暗号」，又快又省字——但必须能翻回人话。

**L1 · 机制本质**
从多智能体对话轨迹挖高频复用符号，压成共享词表（lexicon）；有损压缩 + 回译校验；协议发现器挖通信模板，协商器对齐词表版本。

**L2 · 怎么用上**
Lingua 压缩器做 token 级改写；协议发现器从轨迹找可复现消息模式；握手协商器定双方词表版本。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c02-emergent-agent-language.git && cd eim-c02-emergent-agent-language
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p05-agent-lingua-compressor/impl.py        # 看 demo 输出
python components/p05-agent-lingua-compressor/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P05` | agent-lingua-compressor | 统计高频短语→映射为符号 token，压缩后测压缩率。 | `components/p05-agent-lingua-compressor/` |
| `P06` | emergent-protocol-discoverer | 从日志抽取高频 n-gram 作为候选协议 token，按频次与长度打分。 | `components/p06-emergent-protocol-discoverer/` |
| `P07` | symbolic-handshake-negotiator | 取双方词表交集作为共享符号表；交集为空则回退到最小公共协议。 | `components/p07-symbolic-handshake-negotiator/` |
| `P08` | cross-llm-message-translator | 按显式映射表翻译内部表示字段，未知字段保守透传。 | `components/p08-cross-llm-message-translator/` |

## 该用 / 不该用 / 常见误用

**该用**
智能体之间高频、结构化、可回译的消息流；token 成本占比高的多体系统。

**不该用**
消息必须人类审计或合规留痕（压缩后不可读）；单智能体任务。

**常见误用（这条最重要）**
追求压缩率最大化。错——回译不一致时必须回退自然语言，否则语义漂移会静默累积。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C02 · Emergent Agent Language © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
