#!/bin/bash

# Запуск скрипта: chmod u+x bash_script.sh; ./bash_script.sh START

main_command=$1

case $main_command in
    "START")
      	if [ -f "monitoring.csv" ]; then
      		rm monitoring.csv
  	    fi
      	touch monitoring.csv
      	
      	nohup bash $0 "DEAMON" > /dev/null 2>&1 &
      	pid=$!
      	if [ ! -f "pid_id.txt" ]; then
      		touch pid_id.txt
      	fi
      	echo $pid > "pid_id.txt"
          
        echo "process started with PID: $pid"
        ;;
    "STOP")
      	pid=$(cat pid_id.txt)
      	rm pid_id.txt
      	echo "process stopped with PID: $pid"
      	kill -9 $pid
        ;;
    "STATUS")
        if pgrep -f "$0 DEAMON" >/dev/null; then
            echo "Deamon is running"
        else
            echo "Deamon is not running"
        fi
        ;;
    "DEAMON")
	      pid=$(cat pid_id.txt)
        cpu_utilization=$(top -b -n 2 -d 0.2 -p $pid | tail -1 | awk '{print $9}')
        timestamp=$(date +"%Y-%m-%d %T")
        echo "$timestamp;$cpu_utilization" >> monitoring.csv
        sleep 600
        bash $0 "DEAMON"
        ;;
    *)
        echo "Invalid command"
        ;;
esac
