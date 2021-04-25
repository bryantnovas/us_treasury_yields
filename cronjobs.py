from crontab import CronTab
cron = CronTab(tab="""0 16 * * 1-5 python script.py""")
cron.run_scheduler()
