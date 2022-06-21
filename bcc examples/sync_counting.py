from bcc import BPF
import time


b = BPF(text="""
        #include <uapi/linux/ptrace.h>

        BPF_HASH(table);
        int do_count(struct pt_regs *ctx){
            u64 *p;
            u64 key=0;
            u64 count=0;

            p = table.lookup(&key);
            if (p!=NULL){
                count = *p;
            }
            count ++;
            table.update(&key,&count);
            return 0;
        }
""")

b.attach_kprobe(event=b.get_syscall_fnname("sync"),fn_name="do_count")
table = b.get_table("table")
value =0
while True:
	time.sleep(2)
	values = table.items()
	
	if len(table)!=0:
	    value = values[0][1].value
	    
	print(f"sync is called <{value}> times")
