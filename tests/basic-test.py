#!/usr/bin/python2

import pstack

threads = pstack.JSON(["tests/basic"])
assert len(threads) == 1
thread = threads[0]
stack = thread["ti_stack"]

if stack[0]["symbol"]["st_name"] == "__kernel_vsyscall":
    stack = stack[1:]
assert stack[0]["symbol"]["st_name"] == "raise" or stack[0]["symbol"]["st_name"] == "__GI_raise" or stack[0]["symbol"]["st_name"] == "gsignal"
assert stack[1]["symbol"]["st_name"] == "abort" or stack[1]["symbol"]["st_name"] == "__GI_abort"
assert stack[2]["die"] == "g" and stack[2]["symbol"]["st_name"] == "g"
assert stack[3]["die"] == "f" and stack[3]["symbol"]["st_name"] == "f"
