#!/usr/bin/env python3

import os

from apscheduler.schedulers.blocking import BlockingScheduler

import mylogging as log

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=60)
def once_per_hour():
    """
    If you lauch this script at time T, then this function will be called
    at T+60 minutes for the first time.
    Ex.: if you lauch the script at 13h07, then this function will be called at 14h07
    for the first time.
    """
    log.info('calling once_per_hour')


@sched.scheduled_job('interval', minutes=2)
def once_per_hour():
    """
    Call it every 2 minutes.
    """
    log.info('2 minutes passed')


@sched.scheduled_job('cron', hour='*/4', minute=2)
def four_hours():
    """
    Run this function every four hour + 2 minutes.
    Ex.: it's called at 00h02, 04h02, 08h02, etc.
    """
    log.info('calling four_hours')


@sched.scheduled_job('cron', day='*', hour=0, minute=5)
def daily_backup():
    """
    Run it once a day at 5 minutes after midnight.

    !!! If it takes time, then don't do the work here because the work
    here will block the calling of the other functions! If it takes time, then
    simply launch the work in the background. Here the slow work is collected in
    a batch file and the batch file is launched in the background.
    """
    log.info('calling daily_backup')
    os.system("./daily_backup.sh &")


@sched.scheduled_job('cron', day='*', hour=0)
def midnight():
    """
    Call it at midnight.
    """
    log.info('calling midnight')


@sched.scheduled_job('cron', day='*', hour=18)
@sched.scheduled_job('cron', day='*', hour=19)
@sched.scheduled_job('cron', day='*', hour=20)
def triple_check():
    """
    Call this function every day at 18h00, 19h00 and 20h00.
    """
    log.info('calling triple_check')


@sched.scheduled_job('cron', day_of_week='wed', hour=19, minute=0)
@sched.scheduled_job('cron', day_of_week='sun', hour=19, minute=0)
def mini_backup():
    """
    Call this function on Wednesday at 19h00 and
    on Sunday at 19h00.
    """
    log.info('calling mini_backup')


def main():
    log.info('the scheduler is running...')
    sched.start()

##############################################################################

if __name__ == "__main__":
    main()
