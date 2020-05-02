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
<li>the above is applicable to 32bit architecture</li>
</ul>
</li>
</ul>
