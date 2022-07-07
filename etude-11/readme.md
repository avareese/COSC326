Ava Reese - 2678742
Katherine Butt - 4347525

Test cases:

We did a few tests cases to check there is only one instance being made. We tested this by adding in and deleting different amounts of clips to vm and vm2 to see it is working correctly.

Resources used:

To learn about the structure of the singleton design pattern I found an example from stack overflow which helped me understand how to implement this design pattern.

Instructions on how to run program:

Unzip the folder and run the main by java videoMain.

Challanges with software design:

Problems with the singleton design can occur when using multiple classloaders. The implementation ensures there is one instance per classloader not per JVM so when using more than one JVM there will be more instances.


Singleton class:
We used a singleton design pattern because as per the spec "The key requirements for the video manager class is that there is only one instance of this class and that this instance is easy to access from other components of the software framework that you design."
The singleton pattern is a software design pattern which restricts the instantiation of a class to one signle instance.
As you can see from our main method we are create two 'instances' however from checking the size you can see they are actually referring to the same 'instance' of vm as I add clip 1 and clip 4 to vm and clip 2 and clip 3 to vm2. If it was not a singleton pattern it would hold 2 clips in each instance however as they are referring to the same 'instance' there are 4 clips being held. this saves memory as the single instance can be reused again and again.