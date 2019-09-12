import schedule
import sys
import time

from prophet.alphavantage.commands.daily_metrics import DailyMetrics

COMMANDS = {
  "daily_metrics": DailyMetrics(),
}

scheduler = schedule.Scheduler()
command = COMMANDS[sys.argv[1]]

def run_job():
  runnable = command.get_runnable()
  runnable()

command.get_schedule(scheduler).do(run_job)

while True:
    scheduler.run_pending()
    time.sleep(1)
