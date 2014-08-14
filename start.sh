#!/bin/bash
./smsService.py >> log/smsService.log 2>&1 &
./telListService.py >> log/telListService.log 2>&1 &
./webService.py >> log/webService.log 2>&1 &
./readSmsService.py >> log/readSmsService.log 2>&1 &
./sendEmailSMS.py >> log/sendEmailSMS.log 2>&1 &
