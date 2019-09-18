import schedule
import sys
import time

from prophet.alphavantage.commands.daily_metrics import DailyMetrics

COMMANDS = {
  "daily_metrics": DailyMetrics(),
}

command = COMMANDS[sys.argv[1]]

print "Start running:", sys.argv[1]
runnable = command.get_runnable()
runnable()
print "Finished running:", sys.argv[1]
