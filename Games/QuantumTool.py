import uuid
import time
import random
import sys
import subprocess

def printProgressBar(iteration, total, prefix="", suffix="", decimals=1, length=100, fill="█", printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    sys.stdout.write("\r%s |%s| %s%% %s" % (prefix, bar, percent, suffix))
    if iteration == total:
        sys.stdout.write("\n")
    sys.stdout.flush()


def Print(number: int):
    messages = [
        "Successfully cloned into ",
        "Error: Failed to clone into ",
        "Information: The following files have been cloned into ",
        "Clone completed successfully into ",
        "Clone failed. Please check the URL: ",
        "Cloning in progress: ",
        "Clone successful. Files copied into ",
        "Warning: Clone may have failed. Check the URL: ",
        "Clone completed with errors. See output below: "
    ]
    
    urls = [
        "https://aptpackages.ubuntu.org/",
        "https://www.google.com/",
        "https://github.com/",
        "https://stackoverflow.com/",
        "https://docs.python.org/",
        "https://www.amazon.com/",
        "https://www.reddit.com/",
        "https://www.microsoft.com/",
        "https://www.apple.com/",
        "https://www.spotify.com/"
    ]
    
    for i in range(1, number+1):
        message = random.choices(messages, weights=[10, 2, 8, 10, 3, 7, 10, 1, 3], k=1)[0]
        url = random.choice(urls)
        White_Color_Code = "\033[37m"
        reset_color_code = "\033[0m"
        uuid_str = str(uuid.uuid4())
        
        if "Error" in message:
            message_color_code = "\033[31m"
        else:
            message_color_code = White_Color_Code
            
        print(f"{message_color_code}{message}{White_Color_Code}{url}{White_Color_Code}{uuid_str}")
        
        # progress bar with varying speeds
        if random.random() < 0.3:
            for j in range(101):
                speed = random.uniform(0.001, 0.001)  # speed
                time.sleep(speed)
                printProgressBar(j, 100, prefix=f"Progress [{i}/{number}] ", suffix="Complete", length=50)
        
        # delay for the next message
        time.sleep(random.uniform(0.002, 0.0008))
        
        # terminal animation
        if random.random() < 0.3:
            print(f"{White_Color_Code}Working...{reset_color_code}", end="", flush=True)
            time.sleep(0.3)
            print("\b")

Print(number=500)

time.sleep(2)
if input("Would you like to restart. [Y,N]: ") == "Y":
    subprocess.call(["python3", "../main.py"])