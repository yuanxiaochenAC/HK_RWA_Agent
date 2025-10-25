# RWA智能咨询系统 - 快速使用指南

## 🚀 5分钟快速开始

### 第一步：确认环境已就绪 ✅

所有准备工作已完成，无需额外配置！

```bash
✅ Python 虚拟环境
✅ OpenAI API密钥
✅ RAG文档索引
✅ 所有依赖包
✅ UTF-8编码配置
```

### 第二步：选择使用方式

#### 方式1：Windows批处理（推荐，自动处理编码）

```bash
# 基础查询
.\run_rwa.bat --query "您的问题"

# 快速模式
.\run_rwa.bat --query "Hong Kong RWA regulations" --quick

# 辩论模式（最详细）
.\run_rwa.bat --query "Solar farm tokenization" --debate

# 交互模式
.\run_rwa.bat
```

#### 方式2：直接运行Python

```bash
python run_rwa_consultant.py --query "您的问题"
```

---

## 📝 典型使用案例

### 案例1：初次了解香港RWA监管

**问题：** "香港RWA的基本监管要求是什么？"

```bash
.\run_rwa.bat --query "Hong Kong RWA basic requirements" --quick
```

**预期输出：**
- 监管定义和适用范围
- 许可证申请流程和时间节点
- 核心合规要求
- 所需文档清单

**响应时间：** 约10-15秒

---

### 案例2：光伏项目RWA发行准备

**问题：** "我有一个50MW的光伏项目，想在香港发行RWA，需要准备什么？"

```bash
.\run_rwa.bat --query "I have a 50MW solar project, what do I need for RWA issuance in Hong Kong?"
```

**预期输出：**
- 项目资质评估
- 法律合规文档清单
- 金融结构设计建议
- 技术文档要求
- 时间规划和里程碑
- 风险点和注意事项

**涉及的Expert Agents：**
- Solar RWA Specialist
- Legal & Compliance Specialist
- Financial Structuring Specialist
- RAG Document Expert

**响应时间：** 约20-30秒

---

### 案例3：复杂项目全面分析（使用Debate模式）

**问题：** "如何设计一个太阳能资产支持的代币化产品，包括法律框架和投资者结构？"

```bash
.\run_rwa.bat --query "Design a solar-backed tokenized product with legal framework and investor structure" --debate
```

**Debate机制输出：**
1. **Initial Proposals** - 每个专家提供独立方案
2. **Cross-Examination** - 专家相互质疑和挑战
3. **Refinement** - 基于反馈优化方案
4. **Consensus Building** - 识别共识和解决分歧
5. **Final Synthesis** - 综合专业报告

**响应时间：** 约60-90秒（因为有5个辩论阶段）

---

### 案例4：快速查询实时数据

**问题：** "当前BTC价格和以太坊Gas费是多少？"

```bash
.\run_rwa.bat --query "Current BTC price and Ethereum gas fee" --quick
```

**系统行为：**
- Web Researcher Agent调用实时API
- 返回最新市场数据
- 快速响应（5-10秒）

---

### 案例5：交互式持续对话

```bash
.\run_rwa.bat
```

然后系统会进入交互模式：

```
请输入您的RWA问题（输入 'quit' 退出）: 香港RWA许可证申请流程

[系统分析并回答...]

请输入您的RWA问题（输入 'quit' 退出）: 如果我是一家太阳能公司呢？

[系统基于上下文继续回答...]
```

---

## 🎯 三种模式的选择建议

| 模式 | 适用场景 | 响应时间 | 专家数量 | 输出详细度 |
|------|---------|----------|---------|-----------|
| **Quick** | 简单事实查询、快速了解 | 10-15秒 | 1-2个 | ⭐⭐⭐ |
| **Enhanced**（默认） | 复杂问题、需要多角度分析 | 20-30秒 | 2-4个 | ⭐⭐⭐⭐ |
| **Debate** | 关键决策、需要深度验证 | 60-90秒 | 3-6个 | ⭐⭐⭐⭐⭐ |

### 选择指南：

**使用 --quick 当：**
- 只需要基本事实
- 时间紧迫
- 问题明确简单

**使用默认模式当：**
- 需要综合分析
- 问题涉及多个维度
- 需要实用建议

**使用 --debate 当：**
- 涉及重大决策
- 需要专家交叉验证
- 问题高度复杂
- 需要最高质量输出

---

## 💡 提问技巧

### ✅ 好的提问示例：

1. **具体的项目咨询**
   ```
   "我有一个50MW的光伏发电站，想在香港发行RWA，需要哪些文件？"
   ```

2. **明确的法律问题**
   ```
   "香港稳定币发行需要什么许可证？申请流程是什么？"
   ```

3. **金融结构设计**
   ```
   "如何设计一个太阳能资产代币的投资者权益结构？"
   ```

4. **复合性问题**
   ```
   "光伏RWA项目的法律、金融和技术要求是什么？"
   ```

### ❌ 避免的提问方式：

1. **过于宽泛**
   ```
   "告诉我关于RWA的一切"  ❌
   ```

2. **多个不相关问题**
   ```
   "RWA是什么？BTC价格多少？香港天气如何？"  ❌
   ```

3. **缺乏上下文**
   ```
   "需要什么文件？"  ❌  （没说明是什么项目）
   ```

---

## 🔍 系统输出说明

系统的回答通常包含以下结构化内容：

### 1. 问题分析
- 问题类型识别
- 复杂度评估
- 所需专家判断

### 2. 专家意见
- 每个专家的专业分析
- 基于RAG文档的引用
- 实时数据（如需要）

### 3. 综合建议
- 操作步骤
- 文档清单
- 时间规划
- 风险提示

### 4. 具体数据
- 监管时间节点
- 文档模板建议
- 成本估算（如适用）
- 联系方式和资源

---

## ⚡ 性能和限制

### 性能指标
- **Quick模式：** 10-15秒
- **Enhanced模式：** 20-30秒
- **Debate模式：** 60-90秒

### API调用量估算
- **Quick模式：** 2-3次LLM调用
- **Enhanced模式：** 4-6次LLM调用
- **Debate模式：** 10-15次LLM调用

### 使用建议
- 优先使用Quick模式节省时间和成本
- 重要决策使用Debate模式确保质量
- 一般咨询使用默认Enhanced模式

---

## 🛠️ 故障排除

### 问题1：出现编码错误
**解决方案：** 使用 `.\run_rwa.bat` 而不是直接运行Python脚本

### 问题2：API调用失败
**检查：** 
1. `openai_api_key.txt` 文件是否存在
2. API密钥是否有效
3. OpenAI账户是否有余额

### 问题3：系统响应慢
**原因：**
- 网络延迟
- LLM调用排队
- RAG检索大量文档

**建议：** 
- 使用 `--quick` 模式
- 确保网络连接稳定

### 问题4：输出不够详细
**解决方案：** 
- 移除 `--quick` 参数，使用默认Enhanced模式
- 或使用 `--debate` 获得最详细的输出

---

## 📞 获取帮助

### 查看帮助信息
```bash
.\run_rwa.bat --help
```

### 查看使用示例
```bash
.\run_rwa.bat --help-examples
```

### 查看完整文档
- `README.md` - 完整系统文档
- `PROJECT_SUMMARY.md` - 项目总结
- 代码内注释 - 详细的技术说明

---

## 🎉 开始使用

**现在就试试第一个查询！**

```bash
.\run_rwa.bat --query "Hong Kong RWA regulations" --quick
```

**祝您使用愉快！** 🚀

---

*提示：系统会持续学习和改进。如有任何问题或建议，欢迎反馈。*

