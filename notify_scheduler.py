from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import os
# win10 系统使用
#from win10toast import ToastNotifier
#toaster = ToastNotifier()

# 定义通知函数，可以根据需要扩展为调用系统通知API
def notify(message):
    os.system(f'''osascript -e 'display notification "{message}" with title "課程提醒"' ''')
    print(message)
    # 例如在Linux系统可以使用 os.system("notify-send '{}'".format(message))
    # 或者调用其他第三方通知库

# 定义上课时间列表（日期格式为日/月，12小时制带am/pm）
class_times = [
    "7/2 8:30pm",
    "8/2 8:30pm",
    "9/2 10:00am",
    "14/2 8:30pm",
    "15/2 9:00pm",
    "16/2 8:30pm"
]

# 设置提前通知时间，比如提前10分钟
lead_minutes = 10
lead_time = timedelta(minutes=lead_minutes)

# 获取当前年份（假设所有日期都在当前年份内）
current_year = datetime.now().year

scheduler = BlockingScheduler()

for time_str in class_times:
    # 解析输入时间，需要确保格式匹配 "%d/%m %I:%M%p"（日/月 小时:分钟am/pm）
    # 注意：在 Windows 下可能需要保证 am/pm 为小写或者大写与系统匹配
    try:
        class_time = datetime.strptime(f"{time_str} {current_year}", "%d/%m %I:%M%p %Y")
    except Exception as e:
        print(f"解析时间 {time_str} 失败: {e}")
        continue

    notify_time = class_time - lead_time
    # 判断如果通知时间已经过去，可以选择跳过或者立即通知
    if notify_time < datetime.now():
        print(f"{class_time} 的通知时间 {notify_time} 已经过期，跳过调度。/n")
        continue

    # 添加调度任务：到 notify_time 时执行 notify 函数，传入消息
    scheduler.add_job(notify, 'date', run_date=notify_time,
                      args=[f"提醒：您的课程将在 {class_time.strftime('%Y-%m-%d %I:%M %p')} 开始"])
    print(f"已调度 {class_time.strftime('%Y-%m-%d %I:%M %p')} 前 {lead_minutes} 分钟通知，即 {notify_time}。")

# 开启调度器
try:
    print("\n================ Notification Scheduler Started (Please do not close the program) =================\n")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("\n================ Notification Scheduler Stopped =================\n")
