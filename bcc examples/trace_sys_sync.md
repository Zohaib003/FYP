run file in one terminal and do write sync in other terminal, see the results.....

There are few things to learn here 

1. kprobe__ : It is short cut for dynamic kernal tracing by kprobe. If C function start with kprobe__, rest of it is kernal function name. In this case sys_sync.
 
2. bpf_trace_printk: A simple kernel facility for printf() to the common trace_pipe.

3. trace_print: print every thing in common trace point.
