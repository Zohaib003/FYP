from bcc import BPF as b
from time import sleep
print("hhh")

cProgram ="""
  int hello_world(void *ctx){
  u64 uid = bpf_get_current_uid_gid();

  if (uid == 0){
    bpf_trace_printk("hellosudo%d",&uid);
    }
    else{
        bpf_trace_printk("helloworld%d",&uid);
    }
  
  return 0;

  }
"""
a = b(text=cProgram)
clone=a.get_syscall_fnname("clone")
a.attach_kprobe(event=clone,fn_name="hello_world")
a.trace_print()
