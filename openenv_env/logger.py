def log(message):

    with open("env_log.txt", "a") as f:
        f.write(message + "\n")