from datetime import datetime

# calculate time difference
def time_difference(start_time):
    current_time = datetime.now()
    start_time = start_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)
    elapsed_time = current_time - start_time
    print(elapsed_time.total_seconds())
    return elapsed_time.total_seconds()

# function for monitoring after initial main was run
def monitor_file(file_path):
    ongoing_processes = {}


    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 4:
                timestamp = parts[0].strip()
                task = parts[1].strip()
                status = parts[2].strip()
                pid = parts[3].strip()

                # If procces start
                if status == "START":
                    start_time = datetime.strptime(timestamp, "%H:%M:%S")
                    ongoing_processes[pid] = start_time
                elif status == "END" and pid in ongoing_processes:
                    # If the procces ends, we delete from ongoing_processes because we already log this
                    del ongoing_processes[pid]

    #Check ongoing_processes
    for pid, start_time in list(ongoing_processes.items()):
        elapsed_minutes = time_difference(start_time)
        if elapsed_minutes > 600:
            with open('alerte.txt', 'a') as f:
                f.write(f"ERROR: The JOB with the associated {pid} failed because he ran for more than 10 minutes !!!!!.\n")
        elif elapsed_minutes > 300:
            with open('alerte.txt', 'a') as f:
                f.write(f"ALERT: The JOB with the associated {pid} should be checked because he ran for more than 5 minutes !!!!.\n")
