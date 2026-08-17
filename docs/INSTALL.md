# AI Hub 安装指南

## 系统要求

- Python 3.10 或更高版本
- pip（Python包管理器）
- 8GB+ 内存
- 10GB+ 可用磁盘空间

---

## 安装方式

### 方式1：使用pip安装（推荐）

```bash
pip install aihub-platform
```

### 方式2：从源码安装

```bash
# 克隆仓库
git clone https://github.com/yaowanxiang/ai-hub-platform.git
cd ai-hub-platform

# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖（可选）
pip install -r requirements-dev.txt

# 安装项目
pip install -e .
```

### 方式3：使用Docker

```bash
# 拉取镜像
docker pull yaowanxiang/ai-hub:latest

# 运行容器
docker run -it --rm yaowanxiang/ai-hub:latest
```

---

## 验证安装

```bash
# 运行示例
python -c "from aihub import AIHub; print('安装成功！')"

# 或者运行演示
python main.py
```

---

## 依赖安装

### 核心依赖

已包含在`requirements.txt`中：
- anthropic>=0.18.0（Anthropic API）
- openai>=1.3.0（OpenAI API）
- requests>=2.31.0（HTTP请求）
- pandas>=2.0.0（数据处理）
- whisper>=20231117（语音识别）
- opencv-python>=4.8.0（计算机视觉）
- mediapipe>=0.10.0（手语识别）
- bandit>=1.7.5（安全审计）
- psutil>=5.9.0（性能监控）

### 开发依赖（可选）

已包含在`requirements-dev.txt`中：
- pytest>=7.4.0（测试框架）
- pytest-cov>=4.0.0（测试覆盖率）
- black>=23.7.0（代码格式化）
- isort>=5.12.0（导入排序）
- mypy>=1.4.0（类型检查）

---

## 配置API密钥

### OpenAI API

```bash
# 设置环境变量
export OPENAI_API_KEY="your-openai-api-key"

# 或在代码中设置
import openai
openai.api_key = "your-openai-api-key"
```

### Anthropic API

```bash
# 设置环境变量
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# 或在代码中设置
import anthropic
client = anthropic.Anthropic(api_key="your-anthropic-api-key")
```

---

## 故障排除

### 问题1：安装失败

```bash
# 更新pip
python -m pip install --upgrade pip

# 清理缓存
pip cache purge

# 重新安装
pip install aihub-platform
```

### 问题2：依赖冲突

```bash
# 使用虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

pip install aihub-platform
```

### 问题3：权限错误

```bash
# 使用--user安装
pip install --user aihub-platform

# 或使用sudo（Linux/Mac）
sudo pip install aihub-platform
```

---

## 卸载

```bash
# 使用pip卸载
pip uninstall aihub-platform

# 从源码卸载
pip uninstall aihub-platform
cd ai-hub-platform
rm -rf venv  # 删除虚拟环境（如果使用）
```

---

## 下一步

- 阅读[用户指南](docs/user-guide.md)
- 查看[示例代码](examples/)
- 加入[社区讨论](https://github.com/yaowanxiang/ai-hub-platform/discussions)

---

**遇到问题？**

- 查看[常见问题](docs/faq.md)
- 提交[GitHub Issue](https://github.com/yaowanxiang/ai-hub-platform/issues)
- 联系：yaowanxiang@qut.edu.cn