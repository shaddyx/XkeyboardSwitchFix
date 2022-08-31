import subprocess

_utf = 'utf-8'


def run(args):
    if isinstance(args, list):
        args = " ".join(args)

    proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return ((out or b'').decode(_utf), (err or b'').decode(_utf), proc.returncode)


def run_and_get_stdout(args):
    return run(args)[0]


def test_run():
    # res, err, code = run(["ls", "/"])
    # print ("answer:", code, res, err)
    res, err, code = run('./xkblayout-state print "%C"')
    print("answer:", code, res, err)
