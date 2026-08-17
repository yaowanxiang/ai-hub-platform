# 贡献指南

感谢你考虑为AI Hub做出贡献！

## 📋 贡献类型

我们欢迎以下类型的贡献：

- 🐛 **Bug修复**
- ✨ **新功能**
- 📚 **文档改进**
- 🎨 **UI/UX改进**
- ⚡ **性能优化**
- 🧪 **测试用例**
- 🌐 **国际化**

---

## 🚀 快速开始

### 1. Fork项目

```bash
# 在GitHub上Fork项目
# 然后克隆你的Fork
git clone https://github.com/your-username/ai-hub-platform.git
cd ai-hub-platform
```

### 2. 创建分支

```bash
git checkout -b feature/your-feature-name
```

### 3. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_core.py

# 查看覆盖率
pytest --cov=core --cov-report=html
```

### 5. 提交代码

```bash
# 添加更改
git add .

# 提交
git commit -m "feat: 添加你的功能描述"

# 推送到你的Fork
git push origin feature/your-feature-name
```

### 6. 创建Pull Request

在GitHub上创建Pull Request，并填写PR模板。

---

## 📝 代码规范

### Python代码

- 遵循 [PEP 8](https://pep8.org/) 风格指南
- 使用类型提示（Type Hints）
- 编写文档字符串（Docstrings）
- 添加类型检查

```python
from typing import Dict, List, Any

def process_input(
    user_input: str,
    modality: str = "text"
) -> Dict[str, Any]:
    """
    处理用户输入
    
    Args:
        user_input: 用户输入
        modality: 输入模态
        
    Returns:
        处理结果
    """
    # 代码实现
    pass
```

### 文档

- 使用Markdown格式
- 中文文档使用简体中文
- 添加代码示例
- 包含使用场景

---

## 🧪 测试要求

### 测试覆盖

- 新功能必须有测试用例
- 测试覆盖率不低于85%
- 使用pytest框架

### 测试示例

```python
import pytest
from core.interface import SimpleInterface

class TestSimpleInterface:
    """测试傻瓜化接口"""
    
    def setup_method(self):
        self.interface = SimpleInterface()
    
    def test_understand_intent(self):
        """测试意图理解"""
        result = self.interface.understand("写一段Python代码")
        assert result['action'] == 'code'
```

---

## 📚 文档贡献

### 文档类型

- 用户指南
- API参考
- 开发者文档
- 教程和示例

### 文档位置

- 用户文档：`docs/user-guide.md`
- API文档：`docs/api-reference.md`
- 开发文档：`docs/developer-guide.md`
- 示例代码：`examples/`

---

## 🤝 社区行为准则

- 尊重所有贡献者
- 保持友好和建设性的讨论
- 欢迎新手提问
- 拒绝任何形式的骚扰

---

## 🐛 报告Bug

使用[GitHub Issues](https://github.com/yaowanxiang/ai-hub-platform/issues)报告Bug，请包含：

- Bug描述
- 复现步骤
- 预期行为
- 实际行为
- 环境信息（操作系统、Python版本）

---

## 💡 功能请求

使用[GitHub Issues](https://github.com/yaowanxiang/ai-hub-platform/issues)提出功能请求，请包含：

- 功能描述
- 使用场景
- 预期收益
- 实现建议（可选）

---

## 📧 联系我们

- **GitHub Issues**: https://github.com/yaowanxiang/ai-hub-platform/issues
- **Email**: yaowanxiang@qut.edu.cn

---

## 📄 许可证

所有贡献均遵循MIT许可证。

---

再次感谢你的贡献！🎉