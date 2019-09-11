import schedule
import time

from prophet.alphavantage.commands.daily_metrics import DailyMetrics

daily_metrics_command = DailyMetrics()

daily_metrics_command.get_schedule().do(daily_metrics_command.get_runnable())

while True:
    schedule.run_pending()
    time.sleep(1)
