INSPIRATION
-----------
I chose to develop port scanner because nowadays cyberattacks are growing rapidly so with the help of portscanner we can easily scan our network vulnerabilities and afterthat we can secure it from cyberthreats. I used python language to develop this tool and for making this tool more efficient and faster, I used advance concepts of python language such like Concurrency and parallelism which I studied from python documentation.

Several Versions of Port-Scanner are Available
----------------------------------------------

    Default Port-Scanner
    MultiThreaded Port-Scanner
    Asyncio Port-Scanner
    Multiprocessing Port-Scanner
 
Installing
----------

Use Clone Command To Install Port-Scanner

    $ git clone https://github.com/Rohan-Salwan/Port-Scanner.git

For Installing Dependencies:

    $ pip install -r requirements.txt

Activate Port-Scanner
---------------------

For Starting Default Port-Scanner:

    $ python3 Call.py DefaultPortScanner Activate

For Starting Multi-Threaded Port-Scanner:

    $ python3 Call.py MultiThreadedPortScanner Activate

for starting Multi-Processing Port-Scanner:

    $ python3 Call.py MultiProcessingPortScanner Activate

for starting Asyncio Port-Scanner:

    $ pyhton3 Call.py AsyncioPortScanner Activate
For Help:

    $ python3 Call.py - -- --help


Default Port-Scanner
-------------------

In first version of portscanner, it is using default settings like single thread and single core to scan ports. There is no other modification in this version.

Multi-Threaded Port-Scanner
--------------------------

In this version portscanner is going to use multiplethreads which will enhance the overall speed of portscanner. Moreover, threads can be increase and decrease by user so users can speed up the tool according to thier convenience.

Asyncio Port-Scanner
--------------------

In this version tool is going to use eventloop and its main feature is that it pre empt the task which is waiting for any i/o operations and start another task and what this all process do eventually increase the speed of portscanner.

Multi-Processing Port-Scanner
----------------------------

In this version portscanner is going to use all cores of user machine so portscanning will be superquick because all operation is going to run parallely but in threaded version and aysncio version operations are not going to run parallely that is why multiprocessing is more efficient.


# My Local Machine Configuration

Processor            Intel(R) Core(TM) i7-10710U CPU @ 1.10GHz 1.61 GHz
Installed RAM        16.0 GB (15.8 GB usable)
Cores count          6
Logical processors   12
System type          64-bit operating system, x64-based processor

# For Testing 
___I scanned 2000 ports several times with all four versions of portscanner and recorded average runtime of every version which is represented by bar graph and that is given down below___

# Testing Results


___Figures represented seconds and minutes in the graph___


![lit](https://i.ibb.co/mz6ktbq/brooo.png)
















