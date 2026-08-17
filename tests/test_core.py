"""
测试核心模块
"""

import pytest
from core.interface import SimpleInterface, ZeroConfigInstall
from core.learning import SelfLearningSystem, SelfHealing
from core.agents import AgentOrchestrator, AgentLevel


class TestSimpleInterface:
    """测试傻瓜化接口"""
    
    def setup_method(self):
        """初始化"""
        self.interface = SimpleInterface()
    
    def test_understand_intent(self):
        """测试意图理解"""
        # 测试代码意图
        result = self.interface.understand("写一段Python代码")
        assert result['action'] == 'code'
        assert result.get('language') == 'python'
        
        # 测试翻译意图
        result = self.interface.understand("翻译成英文")
        assert result['action'] == 'translate'
        assert result.get('target') == 'en'
    
    def test_auto_select_module(self):
        """测试自动选择模块"""
        # 代码任务
        result = self.interface.auto_select_module({'action': 'code'})
        assert 'gpt-4' in result
        
        # 翻译任务
        result = self.interface.auto_select_module({'action': 'translate'})
        assert 'translate' in result
    
    def test_process_simple(self):
        """测试简单处理"""
        result = self.interface.process("2+2等于几？")
        assert result is not None
        assert 'module' in result


class TestSelfLearningSystem:
    """测试自学习系统"""
    
    def setup_method(self):
        """初始化"""
        self.learning = SelfLearningSystem()
    
    def test_record_usage(self):
        """测试记录使用"""
        self.learning.record_usage(
            user_input="测试输入",
            intent={'action': 'test'},
            module='test-module',
            result={'output': 'test'},
            execution_time=1.5
        )
        
        # 验证记录
        assert len(self.learning.usage_patterns['test']) == 1
        assert self.learning.user_preferences[('test', 'test-module')] == 1
    
    def test_recommend_module(self):
        """测试模块推荐"""
        # 先记录一些使用历史
        for i in range(5):
            self.learning.record_usage(
                user_input=f"测试{i}",
                intent={'action': 'code'},
                module='gpt-4-coding',
                result={'output': 'code'},
                execution_time=1.0
            )
        
        # 应该推荐gpt-4-coding
        recommendation = self.learning.recommend_module({'action': 'code'})
        assert recommendation == 'gpt-4-coding'
    
    def test_performance_metrics(self):
        """测试性能指标"""
        self.learning.record_usage(
            user_input="测试",
            intent={'action': 'test'},
            module='test-module',
            result={'output': 'test'},
            execution_time=1.0
        )
        
        # 修改执行时间
        self.learning.performance_metrics['test-module'].append(0.5)
        
        metrics = self.learning.get_improvement_metrics()
        assert 'test-module' in metrics


class TestSelfHealing:
    """测试自愈系统"""
    
    def setup_method(self):
        """初始化"""
        self.healing = SelfHealing()
    
    def test_detect_anomaly(self):
        """测试异常检测"""
        # 已知异常类型
        error = ConnectionError("Test")
        result = self.healing.detect_anomaly(error, {})
        assert result is True
    
    def test_attempt_fix_connection(self):
        """测试连接修复"""
        error = ConnectionError("Test")
        result = self.healing.attempt_fix(error, {'retries': 0})
        assert result is True
    
    def test_attempt_fix_timeout(self):
        """测试超时修复"""
        error = TimeoutError("Test")
        result = self.healing.attempt_fix(error, {'timeout': 30})
        assert result is True


class TestAgentOrchestrator:
    """测试Agent编排器"""
    
    def setup_method(self):
        """初始化"""
        self.orchestrator = AgentOrchestrator()
    
    def test_l1_simple_task(self):
        """测试L1简单任务"""
        request = {'query': '2+2等于几？'}
        result = self.orchestrator.route_request(request)
        
        assert result['level'] == 1
        assert 'result' in result
    
    def test_l3_complex_task(self):
        """测试L3复杂任务"""
        request = {'task': '写一个Web应用'}
        result = self.orchestrator.route_request(request)
        
        assert result['level'] == 3
        assert 'subtasks' in result
        assert 'final_result' in result
    
    def test_task_escalation(self):
        """测试任务升级"""
        # L2专家（如果失败会升级到L3）
        request = {'task': '复杂任务'}
        result = self.orchestrator.route_request(request)
        
        assert result is not None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])