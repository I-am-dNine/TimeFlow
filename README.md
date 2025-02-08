# TimeFlow

自动化流畅处理多个时间设定通知的小工具

## 功能特点
- 自动化时间管理
- 系统级通知提醒
- 跨平台支持 (Windows/macOS/Linux)
- 可自定义提醒时间

## 快速开始

### 1. 克隆项目
bash
git clone https://github.com/[your-username]/TimeFlow.git
cd TimeFlow

### 2. 环境配置
bash

创建虚拟环境
python -m venv venv
激活虚拟环境
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
安装依赖
pip install -r requirements.txt

### 3. 运行程序
bash
python notify_scheduler.py



## 系统要求

### Windows
- Python 3.6+
- win10toast（可选）：`pip install win10toast`

### macOS
- Python 3.6+
- osascript（系统自带）

### Linux
- Python 3.6+
- notify-send

## 配置说明

### 时间设置
- 在 `class_times` 列表中修改时间
- 时间格式：`"日/月 时:分am/pm"`
- 示例：`"1/5 9:30am"`

### 提醒设置
- 默认提前10分钟提醒
- 通过修改 `lead_minutes` 变量调整提醒时间

## 注意事项
1. 保持终端窗口开启以确保程序持续运行
2. 确保系统通知权限已开启
3. 检查系统时间格式是否正确

## 常见问题
如果遇到问题，请检查：
- [ ] Python 环境是否正确安装
- [ ] 依赖包是否完整安装
- [ ] 系统时间格式是否正确
- [ ] 是否有通知权限


