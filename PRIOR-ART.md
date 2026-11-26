# 定题前查新与成稿复核（2026-11-26）

**候选创新**：对每个有限简单图，用两份图的欧氏两距离配置实现一个逆优化量。固定两个指定配置，在第一个配置满足半径 p、容差 η 的局部约束时，对站点奖励取最大值，所得目标差恰为带每块费用的分数边界最小值。达到此差值的同一组奖励还能让第二个配置成为全局最优。参数变化时几何固定，奖励可以变化。

| 结果 | 已有工作与本稿判断 |
|---|---|
| 定理 1 的分数划分一侧 | Lovász 已给出分数小块划分和边界代价。零容差时，本稿只改变了归一化；拆分不连通块保持总边界。正容差时拆块会改变每块费用。该图参数的零容差版本属于已有工作。[原文](https://arxiv.org/pdf/1709.03179) |
| 受限联盟和支付向量 | Deng–Papadimitriou 定义诱导边权联盟价值。Meir、Rosenschein 与 Malizia 已讨论有规模上限的联盟、平衡族和稳定支付。分数划分与支付约束之间的线性规划对偶是标准工具。[诱导子图博弈](https://doi.org/10.1287/moor.19.2.257) · [受限合作](https://ijcai.org/proceedings/2011/60) |
| 欧氏构造与局部搜索 | 两距离图的谱表示已有系统研究。Cevallos 的博士论文定理 4.13 使用两组点证明多交换局部搜索的乘性下界；前一篇公开稿也使用双组例子。这里的候选贡献限于任意图、上述精确值以及指定全局最优的同时实现。[Roy](https://arxiv.org/abs/0812.3707) · [Cevallos，第 59 页](https://infoscience.epfl.ch/record/222873/files/EPFL_TH7291.pdf) · [前一稿](https://github.com/lujiayilu/dispersion-four-point) |
| 推论 2–4 | 零值条件和参数凹性来自有限线性规划；对称图的轨道平均、半径二时的分数匹配及三角形差距都是标准推论。其在该欧氏目标中的数值意义由定理 1 给出。 |

检索覆盖公开论文、作者稿、学位论文、出版社和会议原文。定题前检索组合包括 max-sum dispersion + multi-exchange locality gap、fractional graph partition + boundary / separation、restricted coalition size + balanced collections、Euclidean two-distance graph representation。成稿后以 fractional partition + dispersion + local search、inverse locality gap + two-distance、graph separation + prescribed global optimum 等交叉复核。所查文献中未找到定理 1 的完整等价陈述。尚未完成 MathSciNet、zbMATH、Web of Science 全库及双向引文链的系统检索。受限合作博弈中的等价支付定理是进一步独立查新的重点。
