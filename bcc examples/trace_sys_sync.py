from bcc import BPF

bp = BPF(
	text="""
		void kprobe__sys_sync(void *ctx){
		bpf_trace_printk("sys_sync is called");
		}"""
	)
bp.trace_print()
