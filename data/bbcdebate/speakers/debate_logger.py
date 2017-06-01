import datetime


if __name__ == "__main__":
    while True:
        speaker = input("> ")
        ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        out = "{},{}\n".format(ts, speaker)
        with open('bbcdebate_log_raw.csv', 'a') as f:
            f.write(out)
