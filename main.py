from PC_Health_Check import *
from pyfiglet import figlet_format as format
from termcolor import colored


def main():
    response = format(" PC HEALTH CHECK !")
    color_it = colored(response, color="blue", attrs=["blink"])
    print(color_it)

    free_hard_disk_percent = check_disk_usage("/")
    print("*" * 60)
    print(f"You have {free_hard_disk_percent:.2f}% Hard disk Space left")
    if free_hard_disk_percent < 20:
        print("This device would soon run out of storage space.")
        print("Upgrade the storage drive very soon or delete files not needed")

    elif 35 >= free_hard_disk_percent >= 20:
        print("This device currently has enough storage space.")
        print("But Consider upgrading the storage drive")

    else:
        print("This device has sufficient disk space!")
    print("*" * 60)
    print("\n")

    print("*" * 60)
    free_CPU_percent = check_cpu_usage()
    print(f"This device is currently utilizing {free_CPU_percent}% of CPU power.")
    print("*" * 60)
    print("\n")

    print("*" * 60)
    try:
        if check_localhost():
            print("The network adapter of this device is working properly!")

    except:
        print("The network adapter of this device has issues")
        print("NB: It could be the wired or wireless network adapter")
    print("*" * 60)
    print("\n")

    print("*" * 60)
    try:
        if check_connectivity():
            print(f"This device has access to the Internet!")
    except:
        print(f"This device has network conectivity issues")
        print("i.e. This device si unable to access the internet")
    print("*" * 60)


if __name__ == "__main__":
    main()
