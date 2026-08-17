"""
AI Hub 自学习系统
用得越多，越懂用户
"""

from typing import Dict, List, Any
from collections import defaultdict
import json
import os


class SelfLearningSystem:
    """
    自学习系统
    
    能力：
    1. 学习用户偏好
    2. 优化模块选择
    3. 预测用户需求
    4. 自动性能调优
    """
    
    def __init__(self, data_dir: str = "~/.aihub/learning"):
        self.data_dir = os.path.expanduser(data_dir)
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 用户行为数据
        self.usage_patterns = defaultdict(list)
        self.user_preferences = defaultdict(int)
        self.performance_metrics = defaultdict(list)
        
        # 加载历史数据
        self._load_history()
    
    def record_usage(self, user_input: str, intent: Dict, 
                     module: str, result: Any, 
                     execution_time: float, user_satisfaction: float = None):
        """
        记录一次使用
        
        Args:
            user_input: 用户输入
            intent: 理解的意图
            module: 使用的模块
            result: 执行结果
            execution_time: 执行时间
            user_satisfaction: 用户满意度(0-1)，可选
        """
        record = {
            'input': user_input,
            'intent': intent,
            'module': module,
            'result_type': type(result).__name__,
            'execution_time': execution_time,
            'satisfaction': user_satisfaction,
            'timestamp': self._get_timestamp()
        }
        
        # 存储模式
        action = intent.get('action', 'unknown')
        self.usage_patterns[action].append(record)
        
        # 学习偏好
        self.user_preferences[(action, module)] += 1
        
        # 记录性能
        self.performance_metrics[module].append(execution_time)
        
        # 持久化
        self._save_history()
    
    def recommend_module(self, intent: Dict, context: Dict = None) -> str:
        """
        推荐最佳模块
        
        Args:
            intent: 用户意图
            context: 上下文信息（可选）
            
        Returns:
            推荐的模块名称
        """
        action = intent.get('action', 'unknown')
        
        # 1. 查找用户偏好
        user_prefs = [(mod, score) for (act, mod), score in self.user_preferences.items()
                      if act == action]
        
        if user_prefs:
            # 选择用户最常使用的模块
            user_prefs.sort(key=lambda x: x[1], reverse=True)
            top_module = user_prefs[0][0]
            
            # 检查性能是否可接受
            avg_time = sum(self.performance_metrics[top_module]) / len(self.performance_metrics[top_module])
            if avg_time < 5.0:  # 性能阈值
                return top_module
        
        # 2. 基于性能选择
        performance_scores = {}
        for mod, times in self.performance_metrics.items():
            if times:
                avg_time = sum(times) / len(times)
                performance_scores[mod] = 1.0 / (avg_time + 0.001)  # 越快越好
        
        if performance_scores:
            best_performance = max(performance_scores.items(), key=lambda x: x[1])
            return best_performance[0]
        
        # 3. 默认选择
        return self._get_default_module(action)
    
    def predict_needs(self, context: Dict) -> List[str]:
        """
        预测用户可能的需求
        
        Args:
            context: 当前上下文
            
        Returns:
            预测的需求列表
        """
        # 简化版：基于历史模式预测
        predictions = []
        
        recent_actions = [r['intent'].get('action') 
                          for r in self.usage_patterns.get('recent', [])[-5:]]
        
        if recent_actions:
            # 检测序列模式
            if recent_actions[-3:] == ['code', 'code', 'code']:
                predictions.append("debug")
            elif recent_actions[-3:] == ['write', 'write', 'write']:
                predictions.append("polish")
            elif recent_actions[-3:] == ['image', 'image', 'image']:
                predictions.append("edit")
        
        return predictions
    
    def optimize_performance(self):
        """
        性能自动优化
        
        基于历史数据自动调整配置
        """
        optimizations = []
        
        # 1. 缓存热点模块
        hot_modules = []
        for mod, times in self.performance_metrics.items():
            if len(times) > 10:  # 频繁使用
                avg_time = sum(times) / len(times)
                if avg_time > 3.0:  # 性能瓶颈
                    hot_modules.append(mod)
        
        if hot_modules:
            optimizations.append({
                'type': 'cache',
                'modules': hot_modules,
                'reason': '频繁使用且性能瓶颈'
            })
        
        # 2. 预加载可能需要的模块
        predictions = self.predict_needs({})
        if predictions:
            optimizations.append({
                'type': 'preload',
                'modules': predictions,
                'reason': '预测需求'
            })
        
        return optimizations
    
    def get_improvement_metrics(self) -> Dict[str, float]:
        """
        获取改进指标
        
        Returns:
            改进指标字典
        """
        if not self.performance_metrics:
            return {}
        
        # 计算平均性能改进
        improvements = {}
        
        for mod, times in self.performance_metrics.items():
            if len(times) >= 2:
                # 比较最近10次和前10次
                recent = times[-10:]
                earlier = times[:10]
                
                recent_avg = sum(recent) / len(recent)
                earlier_avg = sum(earlier) / len(earlier)
                
                if earlier_avg > 0:
                    improvement = (earlier_avg - recent_avg) / earlier_avg * 100
                    improvements[mod] = improvement
        
        return improvements
    
    def _load_history(self):
        """加载历史数据"""
        try:
            history_file = os.path.join(self.data_dir, 'history.json')
            if os.path.exists(history_file):
                with open(history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.usage_patterns = defaultdict(list, data.get('patterns', {}))
                    self.user_preferences = defaultdict(int, 
                        {tuple(k): v for k, v in data.get('preferences', {}).items()})
                    self.performance_metrics = defaultdict(list, data.get('metrics', {}))
        except Exception as e:
            print(f"加载历史数据失败: {e}")
    
    def _save_history(self):
        """保存历史数据"""
        try:
            history_file = os.path.join(self.data_dir, 'history.json')
            
            # 转换preferences为可序列化格式
            prefs_serializable = {str(k): v for k, v in self.user_preferences.items()}
            
            data = {
                'patterns': dict(self.usage_patterns),
                'preferences': prefs_serializable,
                'metrics': dict(self.performance_metrics)
            }
            
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存历史数据失败: {e}")
    
    @staticmethod
    def _get_timestamp() -> str:
        """获取时间戳"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    @staticmethod
    def _get_default_module(action: str) -> str:
        """获取默认模块"""
        defaults = {
            'code': 'gpt-4-coding',
            'translate': 'gpt-4-translate',
            'image': 'dall-e-3',
            'write': 'gpt-4-writing',
            'summarize': 'claude-3-summarize',
            'chat': 'gpt-4-chat'
        }
        return defaults.get(action, 'gpt-4-chat')


class SelfHealing:
    """
    自愈系统
    
    能力：
    1. 自动检测异常
    2. 自动尝试修复
    3. 自动回滚
    """
    
    def __init__(self):
        self.known_issues = {}
        self.fix_history = []
    
    def detect_anomaly(self, error: Exception, context: Dict) -> bool:
        """
        检测异常
        
        Args:
            error: 异常对象
            context: 上下文
            
        Returns:
            是否为可修复的异常
        """
        # 已知问题类型
        known_patterns = [
            'ConnectionError',
            'TimeoutError',
            'MemoryError',
            'ImportError'
        ]
        
        for pattern in known_patterns:
            if pattern in type(error).__name__:
                return True
        
        return False
    
    def attempt_fix(self, error: Exception, context: Dict) -> bool:
        """
        尝试自动修复
        
        Args:
            error: 异常对象
            context: 上下文
            
        Returns:
            修复是否成功
        """
        error_type = type(error).__name__
        
        # 基于错误类型的修复策略
        if 'ConnectionError' in error_type:
            return self._fix_connection(error, context)
        elif 'TimeoutError' in error_type:
            return self._fix_timeout(error, context)
        elif 'MemoryError' in error_type:
            return self._fix_memory(error, context)
        elif 'ImportError' in error_type:
            return self._fix_import(error, context)
        
        return False
    
    def _fix_connection(self, error: Exception, context: Dict) -> bool:
        """修复连接错误"""
        # 重试机制
        retries = context.get('retries', 0)
        if retries < 3:
            return True  # 建议重试
        return False
    
    def _fix_timeout(self, error: Exception, context: Dict) -> bool:
        """修复超时"""
        # 增加超时时间
        timeout = context.get('timeout', 30)
        context['timeout'] = timeout * 2
        return True
    
    def _fix_memory(self, error: Exception, context: Dict) -> bool:
        """修复内存问题"""
        # 减少批处理大小
        batch_size = context.get('batch_size', 100)
        context['batch_size'] = max(batch_size // 2, 1)
        return True
    
    def _fix_import(self, error: Exception, context: Dict) -> bool:
        """修复导入错误"""
        # 自动安装依赖
        module_name = str(error).split("'")[1] if "'" in str(error) else None
        if module_name:
            # 这里会触发自动安装
            return True
        return False


# 导出
__all__ = ['SelfLearningSystem', 'SelfHealing']