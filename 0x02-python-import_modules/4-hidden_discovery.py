#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    sum_name = dir(hidden_4)
    for name in sum_name:
        if name[:2] != '__':
        print("{}".format(name))
