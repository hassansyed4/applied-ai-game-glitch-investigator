import datetime

def log_result(bug, cause, fix, result):
    with open("debug_log.txt", "a") as file:
        file.write(f"\n[{datetime.datetime.now()}]\n")
        file.write(f"Bug: {bug}\n")
        file.write(f"Cause: {cause}\n")
        file.write(f"Fix: {fix}\n")
        file.write(f"Result: {result}\n")
        file.write("-" * 50 + "\n")