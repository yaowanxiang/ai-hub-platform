"""
AI Hub - 完整示例演示
展示核心功能：傻瓜化使用、自学习、多模态、多层次Agent
"""

import time
import sys
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from core.interface import SimpleInterface, ZeroConfigInstall
from core.learning import SelfLearningSystem, SelfHealing
from core.agents import AgentOrchestrator, AgentLevel
from core.multimodal import (
    MultimodalInputProcessor, VoiceInputManager, 
    SignLanguageInterpreter, MultimodalFusion,
    InputModality, Language
)
from core.security import SecurityAuditor, RuntimeMonitor, SandboxManager


class AIHub:
    """
    AI Hub 主类
    
    整合所有核心功能，提供统一接口
    """
    
    def __init__(self):
        # 初始化核心组件
        print("🚀 初始化 AI Hub...")
        
        # 1. 简单化接口
        self.interface = SimpleInterface()
        print("✅ 傻瓜化接口已就绪")
        
        # 2. 自学习系统
        self.learning_system = SelfLearningSystem()
        print("✅ 自学习系统已就绪")
        
        # 3. 多层次Agent
        self.agent_orchestrator = AgentOrchestrator()
        print("✅ 多层次Agent已就绪")
        
        # 4. 多模态输入
        self.multimodal_processor = MultimodalInputProcessor()
        self.voice_manager = VoiceInputManager(self.multimodal_processor)
        self.sign_interpreter = SignLanguageInterpreter(self.multimodal_processor)
        self.multimodal_fusion = MultimodalFusion(self.multimodal_processor)
        print("✅ 多模态输入已就绪")
        
        # 5. 安全系统
        self.security_auditor = SecurityAuditor()
        self.runtime_monitor = RuntimeMonitor()
        self.sandbox_manager = SandboxManager()
        print("✅ 安全系统已就绪")
        
        print("\n🎉 AI Hub 启动完成！")
        print("=" * 50)
    
    def process_user_input(self, user_input: str, 
                          modality: InputModality = InputModality.TEXT,
                          language: Language = Language.CHINESE) -> str:
        """
        处理用户输入（核心方法）
        
        Args:
            user_input: 用户输入
            modality: 输入模态
            language: 语言
            
        Returns:
            处理结果
        """
        start_time = time.time()
        
        # 1. 多模态处理
        if modality != InputModality.TEXT:
            multimodal_result = self.multimodal_processor.process(
                user_input, modality, language
            )
            user_input = multimodal_result['text']
            print(f"📡 多模态识别: {multimodal_result['modality']} -> {user_input}")
        
        # 2. 通过傻瓜化接口处理
        result = self.interface.process(user_input)
        
        # 3. 记录到自学习系统
        execution_time = time.time() - start_time
        self.learning_system.record_usage(
            user_input=user_input,
            intent=self.interface.understand(user_input),
            module=result.get('module', 'unknown'),
            result=result,
            execution_time=execution_time
        )
        
        # 4. 返回结果
        return result
    
    def demonstrate_capabilities(self):
        """演示核心功能"""
        
        print("\n" + "=" * 50)
        print("📚 功能演示")
        print("=" * 50)
        
        # 演示1：傻瓜化文本输入
        print("\n【演示1：傻瓜化文本输入】")
        user_input = "写一段Python代码来读取文件"
        print(f"用户输入: {user_input}")
        result = self.process_user_input(user_input)
        print(f"系统响应: {result}")
        
        # 演示2：多层次Agent
        print("\n【演示2：多层次Agent】")
        print("L1 快速助手:")
        simple_request = {
            'query': '2+2等于几？'
        }
        l1_result = self.agent_orchestrator.route_request(simple_request)
        print(f"  结果: {l1_result['result']}")
        
        print("\nL3 复杂编排:")
        complex_request = {
            'task': '写一个Web应用'
        }
        l3_result = self.agent_orchestrator.route_request(complex_request)
        print(f"  分解任务: {l3_result['subtasks']}")
        print(f"  整合结果: {l3_result['final_result']}")
        
        # 演示3：自学习系统
        print("\n【演示3：自学习系统】")
        
        # 使用几次后查看学习效果
        test_inputs = [
            "写一段Python代码",
            "写一段Python代码来计算斐波那契数列",
            "写一段Python代码来处理JSON数据"
        ]
        
        for inp in test_inputs:
            self.process_user_input(inp)
        
        # 查看学习效果
        improvements = self.learning_system.get_improvement_metrics()
        print(f"性能提升: {improvements}")
        
        # 获取智能推荐
        recommendations = self.learning_system.recommend_module(
            {'action': 'code'}
        )
        print(f"推荐模块: {recommendations}")
        
        # 演示4：多模态输入
        print("\n【演示4：多模态输入】")
        
        # 语音输入（模拟）
        print("语音输入:")
        # 模拟音频数据
        mock_audio = b"mock_audio_data"
        voice_result = self.multimodal_processor.process(
            mock_audio, InputModality.VOICE, Language.CHINESE
        )
        print(f"  识别结果: {voice_result['text']}")
        print(f"  置信度: {voice_result['confidence']}")
        
        # 手语输入（模拟）
        print("\n手语输入:")
        mock_sign_video = b"mock_sign_video_data"
        sign_result = self.sign_interpreter.interpret(
            mock_sign_video, 'CSL', Language.CHINESE
        )
        print(f"  翻译结果: {sign_result}")
        
        # 演示5：多模态融合
        print("\n【演示5：多模态融合】")
        inputs = [
            {'text': '我想买这个', 'modality': 'text'},
            {'text': '红色', 'modality': 'image'},
            {'text': '大号', 'modality': 'gesture'}
        ]
        fused = self.multimodal_fusion.fuse(inputs)
        print(f"融合结果: {fused['fused_text']}")
        print(f"识别意图: {fused['intent']}")
        
        # 演示6：安全审计
        print("\n【演示6：安全审计】")
        
        # 模拟审计一个模块
        print("审计模块: /tmp/test_module")
        # 这里会审计一个真实模块
        audit_result = self.security_auditor.audit_module(
            '/tmp/test_module',
            source='github'
        )
        print(f"审计结果: {audit_result['overall']['status']}")
        print(f"原因: {audit_result['overall']['reason']}")
        
        # 演示7：沙箱隔离
        print("\n【演示7：沙箱隔离】")
        sandbox_id = self.sandbox_manager.create_sandbox('test_module')
        print(f"沙箱创建: {sandbox_id}")
        print(f"资源限制: {self.sandbox_manager.active_sandboxes[sandbox_id]['resources']}")
        
        # 演示8：自动修复
        print("\n【演示8：自动修复】")
        self_healing = SelfHealing()
        error = ConnectionError("Connection failed")
        fix = self_healing.attempt_fix(error, {})
        print(f"检测异常: {error}")
        print(f"自动修复: {fix}")
        
        print("\n" + "=" * 50)
        print("✨ 演示完成！")
        print("=" * 50)


def main():
    """主函数"""
    print("\n" + "=" * 50)
    print("🌟 AI Hub - 通用人工智能平台")
    print("🎯 让AI能力像水电一样触手可及")
    print("=" * 50)
    
    # 创建AI Hub实例
    aihub = AIHub()
    
    # 演示功能
    aihub.demonstrate_capabilities()
    
    # 交互模式
    print("\n" + "=" * 50)
    print("💬 交互模式")
    print("=" * 50)
    print("输入你的问题（输入 'exit' 退出）：")
    
    while True:
        user_input = input("\n用户: ")
        
        if user_input.lower() in ['exit', '退出', 'quit']:
            print("👋 再见！")
            break
        
        # 处理输入
        try:
            result = aihub.process_user_input(user_input)
            print(f"AI: {result}")
        except Exception as e:
            print(f"❌ 处理失败: {str(e)}")


if __name__ == '__main__':
    main()