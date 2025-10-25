#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编码工具类 - 解决Windows控制台Unicode字符显示问题
"""
import sys
import os


def safe_print(*args, **kwargs):
    """安全打印函数，自动处理编码问题"""
    try:
        print(*args, **kwargs)
    except UnicodeEncodeError as e:
        # 如果遇到编码错误，尝试替换问题字符
        safe_args = []
        for arg in args:
            if isinstance(arg, str):
                # 替换常见的Unicode字符为ASCII等价物
                safe_arg = (arg.replace('✓', '[OK]')
                             .replace('✗', '[X]')
                             .replace('❌', '[ERROR]')
                             .replace('🔄', '[PROCESSING]')
                             .replace('📝', '[NOTE]')
                             .replace('🎯', '[TARGET]')
                             .replace('⚠️', '[WARNING]')
                             .replace('👋', '[GOODBYE]')
                             .replace('🚀', '[START]'))
                safe_args.append(safe_arg)
            else:
                safe_args.append(arg)
        
        try:
            print(*safe_args, **kwargs)
        except UnicodeEncodeError:
            # 如果还是有问题，使用errors='ignore'
            for arg in safe_args:
                if isinstance(arg, str):
                    sys.stdout.write(arg.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore'))
                else:
                    sys.stdout.write(str(arg))
            sys.stdout.write('\n')


def setup_console_encoding():
    """设置控制台编码"""
    try:
        # 设置环境变量
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        
        # 在Windows上尝试切换到UTF-8代码页
        if sys.platform == 'win32':
            try:
                import subprocess
                subprocess.run(['chcp', '65001'], check=False, capture_output=True)
            except:
                pass  # 如果失败就忽略
                
    except Exception:
        pass  # 如果设置失败也不影响主要功能


# 导出安全打印函数
__all__ = ['safe_print', 'setup_console_encoding']


