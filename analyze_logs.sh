#!/bin/bash

# Файл с логами
logfile="access.log"

# Общее количество запросов
total_requests=$(wc -l < "$logfile")

# Количество уникальных IP-адресов
unique_ips=$(awk '{print $1}' "$logfile" | sort | uniq | wc -l)

# Количество запросов по методам (GET, POST и т.д.)
request_methods=$(awk '{print $6}' "$logfile" | sort | uniq -c | awk '{print $2": "$1}' | sed 's/"//g')

# Найти самый популярный URL
popular_url=$(awk '{print $7}' "$logfile" | sort | uniq -c | sort -nr | head -1 | awk '{print $2}')

# Создать отчет в виде текстового файла
report_file="report.txt"
 {
     echo "Общее количество запросов: $total_requests"
     echo "Количество уникальных IP-адресов: $unique_ips"
     echo -e "Количество запросов по методам:\n$request_methods"
     echo "Самый популярный URL: $popular_url"
 } > "$report_file"

echo "Отчет сохранен в $report_file"
