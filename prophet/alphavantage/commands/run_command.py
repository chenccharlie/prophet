import schedule
import time

from prophet.alphavantage.commands.daily_metrics import DailyMetrics

scheduler = schedule.Scheduler()

daily_metrics_command = DailyMetrics()

daily_metrics_command.get_schedule(scheduler).do(daily_metrics_command.get_runnable())

while True:
    scheduler.run_pending()
    time.sleep(1)
