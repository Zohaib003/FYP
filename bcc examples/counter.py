from bcc import BPF as b
from time import sleep
print("hhh")

cProgram ="""
  BPF_HASH(table);
  
  int hello_world(void *ctx){

  u64  uid;
  u64 counter = 0;
  u64 *p;

  uid = bpf_get_current_uid_gid();

  p = table.lookup(&uid);
  if (p != 0){
    counter = *p;
  }

  counter ++;
  table.update(&uid,&counter);
  return 0;
  }
"""
a = b(text=cProgram)
clone=a.get_syscall_fnname("clone")
a.attach_kprobe(event=clone,fn_name="hello_world")
# a.trace_print()

while True:
  sleep(2)
  if len(a["table"].items()):
    for k,v in a["table"].items():
      print(f"Id:{k.value} , count: {v.value}")
  else:
    print("no enytries yet")