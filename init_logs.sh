#!/bin/bash
mkdir -p iot-core/docs iot-core/backups env-setup
echo "时间,错误描述,相关文件,修复措施,状态" > iot-core/docs/error_tracker.csv
echo "[2025-02-17] 初始环境创建" > env-setup/env_changelog.txt
echo "# ISTJ学习日志\n## 完成项\n- [x] 初始化记录文件" > iot-core/docs/learning_progress.md
