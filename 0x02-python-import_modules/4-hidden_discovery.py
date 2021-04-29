#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden = dir(hidden_4)
    for i in range(0, len(hidden)):
        if hidden[i:i+2] != '__':
            print("{}".format(hidden[i]))
