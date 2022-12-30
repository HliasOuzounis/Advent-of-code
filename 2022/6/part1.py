def main():
    with open("input.txt") as f:
        datastream = f.read().strip()

    message_len = 4
    for i in range(len(datastream) - message_len):
        if len(set(datastream[i:i + message_len])) == message_len:
            print(i + message_len)
            break


if __name__ == "__main__":
    main()