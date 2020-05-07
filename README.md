# notebook
<ul>
<li>inode object can be a regular file or a directory<br />
<ul>
<li>every component of a file path is represented by&nbsp;<em>dentry object</em></li>
<li>dentry object is created on the fly when searching for the file and tree structure is created dynamically&nbsp;</li>
</ul>
</li>
</ul>


<ul>
<li>kernel uses only virtual address
<ul>
<li>kernel <em>logical addresses</em> are a range of addresses that permanently map and contiguous(Low Memory)</li>
<li>kernel&nbsp;<em>virtual</em> addresses(used with&nbsp;<em>vmalloc</em>)<em>&nbsp;are not permanently mapped</em>&nbsp;and not contiguous(<em>High Memory)</em></li>
<li>good video explaining about high/low memory&nbsp;<a href="https://www.youtube.com/watch?v=7aONIVSXiJ8">https://www.youtube.com/watch?v=7aONIVSXiJ8</a></li>
<li>virtual to physical translation code: https://stackoverflow.com/questions/36639607/how-exactly-do-kernel-virtual-addresses-get-translated-to-physical-ram</li>
<li>the above is applicable to 32bit architecture</li>
<li>each process has a user-space stack and a kernel space stack. kernel space stack resides in low memory(direct mapping/logical address</li>
<li>VMA(virtual memory area) corresponds to an interval in the proccess virutal memory(like a contract)</li>
<li>PTE(page table entry) is the&nbsp;<em>actual</em> mapping of a physical page</li>
<li>page fault occurs by the processor
<ul>
<li>kernel looks for the VMA
<ul>
<li>if not present - SEGEMENTATIN_FAULT</li>
<li>if present, check permissions(read/write) and then either call do_anonymous_page(if pte is null) or do_swap_page(in the case the pte holds physical address of the disk)</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
