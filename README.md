# TimeFlow
小工具：自动化流畅处理多个时间设定通知

### 如何启动这个通知提醒的Python项目。以下是步骤说明：

1. 首先需要安装必要的依赖包。创建一个 requirements.txt 文件，然后安装依赖：
    apscheduler==3.10.1


2. 安装步骤：
    # 1. 创建并激活虚拟环境（推荐）
    python -m venv venv

    # Windows激活虚拟环境
    venv\Scripts\activate
    # macOS/Linux激活虚拟环境
    source venv/bin/activate

    # 2. 安装依赖
    pip install -r requirements.txt

3. 运行程序：
    python notify_scheduler.py


### 需要注意的几点：
1. 这个程序使用了系统通知：
    - 在 macOS 上使用 osascript 发送通知（当前代码默认配置）
    - 如果是 Windows 系统，需要取消注释 win10toast 相关代码并安装该包：     
        pip install win10toast
    - 对于 Linux 系统，可以使用 notify-send 命令

2. 程序启动后会持续运行，请不要关闭终端窗口，否则提醒功能会停止。

3. 可以根据需要修改 class_times 列表中的时间，格式为 "日/月 时:分am/pm"。

4. 默认设置为课程开始前10分钟提醒，可以通过修改 lead_minutes 变量来调整提醒时间。

如果遇到任何问题，请确保：
- Python 环境已正确安装
- 所有依赖包都已成功安装
- 系统时间格式正确
- 有适当的系统权限来发送通知