#!/bin/bash

echo -e "\n$(date) Chicken Service Shell----------------------------" >> /home/andrew/logs/chicken.service.log

sleep 1

/home/andrew/.virtualenvs/chicken_door/bin/python /home/andrew/chicken_service/chicken_service.py >> /home/andrew/logs/chicken.service.log 2>&1


