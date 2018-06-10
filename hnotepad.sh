#!/bin/bash

function test(){
    ps aux |grep myflask_main|grep -v "grep"|awk '{i++;pids[i]=$2}END{for(j=1;j<=NR;j++){printf pids[j];if(j!=NR) printf " " }}'
}
function printTest(){
    pids=`test`
    if [ ! "$pids" == "" ]
    then
        echo "INFO: Notepad process: $pids."
        echo "INFO: Notepad is running."
    else
        echo "INFO: Notepad is not running."
    fi
}

##############################################
#             main entry point               #
##############################################
ACTION=""
if [ $# -eq 1 ]
then 
    ACTION="$1"
else
    echo "Usage: hnotepad --start/--stop"
    exit 1
fi

#workdir=$(cd $(dirname $0); pwd)
DIR=/Users/jianghai/mydoc/projects/src/myflask
case $ACTION in
    --start)
        pids=`test`
        if [ "$pids" == "" ] 
        then
            echo "INFO: start Notepad ..."
            #DIR=$(dirname $(readlink -f "$0"))
            cd $DIR
	        `python myflask_main.py > database/log.txt 2>&1 &`
            sleep 2
        fi
        printTest
	;;
    --stop)
        pids=`test`
        if [ ! "$pids" == "" ]
        then
            echo "INFO: Stopd Notepad ..."
            kill `test`
            sleep 2
        fi
        printTest
	;;
    --test)
        printTest
        ;;
    *)
	echo "Error: unknown action $ACTION"
	exit 2
   	;;
esac	 
