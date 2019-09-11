import schedule
import time

from prophet.alphavantage.commands.daily_metrics import DailyMetrics

scheduler = schedule.Scheduler()

daily_metrics_command = DailyMetrics()

def run_job():
  print "start run"
  runnable = daily_metrics_command.get_runnable()
  runnable()

daily_metrics_command.get_schedule(scheduler).do(run_job)

while True:
    scheduler.run_pending()
    time.sleep(1)
