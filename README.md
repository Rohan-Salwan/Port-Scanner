# INSPIRATION
I chose to develop port scanner because nowadays cyberattacks are growing rapidly so with the help of portscanner we can easily scan our network vulnerabilities and afterthat we can secure it from cyberthreats. I used python language to develop this tool and for making this tool more efficient and faster, I used advance concepts of python language such like Concurrency and parallelism which I studied from python documentation.

# 4 versions of portscannner are available
1. Default portscanner with no modification
2. Threaded portscanner
3. Asyncio portscanner
4. Multiprocessing portscanner
 
# ___Default portscanner___
In first version of portscanner it is using default settings like single thread and single coreto scan ports so there is no other modification in this version.

# ___Threaded portscanner___
In this version portscanner is going to use multiplethreads which will enhance the overall speed of portscanner. Moreover, threads can be increase and decrease by user so users can speed up the tool according to thier convenience.

# ___Asyncio portscanner___
In this version tool is going to use eventloop and its main feature is that it pre empt the task which is waiting for any i/o operations and start another task and what this all process do eventually increase the speed of portscanner.

# ___Multiprocessing portscanner___
In this version portscanner is going to use all cores of user machine so portscanning will be superquick because all operation is going to run parallely but in threaded version and aysncio version operations are not going to run parallely that is why multiprocessing is more efficient.

# Testing results

___My local machine configuration___

Processor            Intel(R) Core(TM) i7-10710U CPU @ 1.10GHz 1.61 GHz
Installed RAM        16.0 GB (15.8 GB usable)
Cores count          6
Logical processors   12
System type          64-bit operating system, x64-based processor

![lit](C:\Users\rohan\Desktop\lit.PNG)


