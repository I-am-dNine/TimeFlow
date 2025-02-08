from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import os
# Windows 系统使用
#from win10toast import ToastNotifier
#toaster = ToastNotifier()

# for test
def test_notification():
    """测试通知功能"""
    print("测试通知开始...")
    # 测试立即通知
    notify("这是一条测试通知消息！")

    # 测试定时通知
    test_scheduler = BlockingScheduler()
    test_time = datetime.now() + timedelta(seconds=10)  # 设置10秒后触发
    test_scheduler.add_job(notify, 'date', run_date=test_time,
                          args=[f"这是一条定时测试通知（设定在 {test_time.strftime('%H:%M:%S')}）"])
    print(f"已设置在 {test_time.strftime('%H:%M:%S')} 触发定时通知...")
    print("请等待约10秒钟查看定时通知效果。")
    
    try:
        test_scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("测试被中断")
    
# 定义通知函数，可以根据需要扩展为调用系统通知API
def notify(message):
    try:
        os.system(f'''osascript -e 'display notification "{message}" with title "課程提醒"' ''')
        print(f"[通知发送成功] {message}")
        # 例如在Linux系统可以使用 os.system("notify-send '{}'".format(message))
        # 例如在Windowstoaster.show_toast("课程提醒", message, duration=10)
        # 或者调用其他第三方通知库
    except Exception as e:
        print(f"[错误] 发送通知失败: {e}")


# for test
# 定义上课时间列表（日期格式为日/月，12小时制带am/pm）
class_times = [
    # 添加一个即将到来的时间用于测试
    (datetime.now() + timedelta(seconds=10)).strftime("%d/%m %I:%M%p"),  # 10秒后
    # ... 其他原有时间 ...
]

# 定义上课时间列表（日期格式为日/月，12小时制带am/pm）
#class_times = [
#    "7/2 8:30pm",
#    "8/2 8:30pm",
#    "9/2 10:00am",
#    "14/2 8:30pm",
#    "15/2 9:00pm",
#    "16/2 8:30pm"
#]

# for test
# 设置提前通知时间，比如测试时可以改为较短的时间
lead_minutes = 0.6  # 设置为6秒，方便测试

# 设置提前通知时间，比如提前10分钟
#lead_minutes = 10
lead_time = timedelta(minutes=lead_minutes)

# 获取当前年份（假设所有日期都在当前年份内）
current_year = datetime.now().year

scheduler = BlockingScheduler()

for time_str in class_times:
    try:
        class_time = datetime.strptime(f"{time_str} {current_year}", "%d/%m %I:%M%p %Y")
        notify_time = class_time - lead_time
        
        if notify_time < datetime.now():
            print(f"[警告] {class_time.strftime('%Y-%m-%d %H:%M')} 的通知时间已过期，跳过。")
            continue

        # 添加调度任务：到 notify_time 时执行 notify 函数，传入消息
        scheduler.add_job(notify, 'date', run_date=notify_time,
                        args=[f"课程提醒：将在 {lead_minutes} 分钟后开始（{class_time.strftime('%H:%M')}）"])
        print(f"[成功] 已设置 {class_time.strftime('%Y-%m-%d %H:%M')} 的课程提醒")
    
    except Exception as e:
        print(f"[错误] 处理时间 {time_str} 时发生错误: {e}")
        continue


if __name__ == "__main__":
    # 添加测试选项
    test_mode = input("是否要进行通知测试？(y/n): ").lower().strip() == 'y'

    if test_mode:
        test_notification()
    else:
        # 开启调度器
        try:
            print("\n================ Notification Scheduler Started (Please do not close the program) =================\n")
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            print("\n================ Notification Scheduler Stopped =================\n")
