import psutil

#Take CPU Threshold from user as an input
# check current cpu usage (psutil se pata krenge)
# if CPU usage more than Threshold the email it



def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold: "))

    current_cpu = psutil.cpu_percent(interval=1) #last one sec me aapka cpu % kitna tha

    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent....")

    else:
        print("CPU is in safe state")

check_cpu_threshold()

cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {mem}%")