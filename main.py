from datetime import datetime

start_time = []
start_pid = []
description = []
end_time = []
end_pid = []


with open('logs.log', 'r') as file:
    # Read every line from log file
    for line in file:
        parts = line.strip().split(',')  # Comma split


    #vom face impartirea proceselor dupa start si final in timpul parsarii fisierlui
        if(parts[2].strip() == 'START'):
            pid = parts[3].strip()
            start_time.append(parts[0].strip())
            start_pid.append(parts[3].strip())
            description.append(parts[1].strip()) #creating the lists that will contain start info
        if (parts[2].strip() == 'END'):
            end_time.append(parts[0].strip())
            end_pid.append(parts[3].strip()) #creating the lists that will contain ending info
        #check the time difference and log the old data
    for pid in start_pid:
        for i in end_pid:
            if pid == i:
                index_start = start_pid.index(pid)
                index_end = end_pid.index(pid)
                datetime.strptime(end_time[index_end], "%H:%M:%S")
                time_diff =(datetime.strptime(end_time[index_end], "%H:%M:%S") - datetime.strptime(start_time[index_start], "%H:%M:%S")).total_seconds()

                if time_diff >= 600:
                    with open('alerte.txt', 'a') as f:
                        f.write(f"ERROR: The JOB with the associated {pid} failed because he ran for more than 10 minutes !!!!!.\n")
                elif time_diff >= 300:
                    with open('alerte.txt', 'a') as f:
                        f.write(f"ALERT: The JOB with the associated {pid} should be checked because he ran for more than 5 minutes !!!!.\n")


