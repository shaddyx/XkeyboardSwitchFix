import sys_util

def run_args(*args):
    #'./xkblayout-state print "%C"'
    arr = ['./xkblayout-state']
    arr += args
    print (arr)
    return sys_util.run_and_get_stdout(arr)

def get_count():
    return run_args("print", "%C")

def get_variants():
    return run_args("print","%S").strip().split("\n")

def get_variants_filtered():
    res = run_args("print", "%S").strip().split("\n")
    res = filter(lambda x: x != 'terminate', res)
    return list(res)


def left(param = 1):
    return run_args("set", "-{}".format(param))


def right(param = 1):
    return run_args("set", "+{}".format(param))