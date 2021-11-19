#### Offline Elevator Algorithm
In this algorithm of Yosef Gilad we're trying to improve as much as possible the elevator **off-line** working system, by writing our code in ***python launguage.***

Therefore, first we will explain:
1. The problems of several elevators systems.
2. The difference between online and offline algorithm.
3. explanation of our program, classes and operating way.
4. Links for resources.
***
Let's start with explanation between one elevator system and 2 elevator system in a building to open our mind with problems who might happen, cost of the system, and the efficiency of them to understand how we should deal with the problem when we write the code.

1.**Two elevator system:**

Here it gets a little more complicated, and we can understand deeply what we should take in consideration in our code by dealing with extreme cases, and the way we are planning and programming our elevator.
In some systems we can find one elevator take the calls up and the second take the calls down.
The advantages: simple design, not expensive, not many components.
The problems:
We can't connect the elevators to both buttons since it will make a lot of extreme cases like sending both elevator to same call, which is not efficient.

Another two elevator system is EMR (based on relays) which divide the elevators to group of floors.
For example if we have building with 18 floors.
Then the system will divide 3 elevators to 3 groups .
Low floors, middle floors and high floors.
In this system you make the elevator system faster and more efficient by dividing the building to "3 small buildings".
The problem is this system really expensive since she full of relays.

* In all elevator systems who based on 2 elevator and more you have a TT status who deal with situation like error in elevator.
Then this status send the other elevator to deal with the other calls until the errors is fixed.


2. **Off-line algorithm:**
In off-line algorithm, since we get the elevator calls in advance, we can plan our program to make each elevator a schedule who take calls in the same direction of the elevator trip.
This way we can take calls "on the way".
This way we can save the waiting time of people and even the cost of operating the elevator.

   **On-line algorithm:**
In on-line algorithm, we need to take in consideration the option of getting call anytime.
While the elevator in movement, while the elevator not in movement.
While the elevator in the range of trip and when she's not.
Many extreme cases like if it was worth to take a passenger even if he's "on the way" based on the amount of people who already inside the elevator.
Dealing the question does it worth to save a few second to 1 person and make the amount of people inside the elevator wait to pick up this person.
Obviously it demands calculate.

3. In our off-line algorithm we used the idea of **Greedy Algorithm**, which place an order for an elevator.

At the beginning, the algorithm will place a call to the closer free elevator, and once the elevator take the call we will open kind of timeline for the elevator.
This timeline will update each time we enter another call to the timeline.
Each time we read the next call, the program will look on all elevator's timeline's by using **time_to_arrive** function and will choose the elevator with the shortest timeline to take the call.
Which means - the most unbusy elevator exist at each moment.

The algorithm hold:
**class named Elevator** - of the type Elevator who hold all the features of elevator.
Inside this class we call the **time_to_arrive** function.

**class named Calls** - who hold all the features of callas.
Inside also we have Init.

At the **main () function** all the process happens together.
In the process of our algorithm we use the first function **allocate calls** to run on all calls.
This function assign a call to an elevator.
Inside allocate calls we have another function named **minimum_time** and the purpose of this function is to run on all elevators and calculate which elevator have the shortest timeline as explained above.
The function **Create_output_file** will create the new CSV file, inside this file will be written what we create in the **allocate calls** function.
The function **handle_files** will convert the files to objects.

4. `**Links for resources:**`

https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30

https://github.com/mshang/python-elevator-challenge

https://github.com/lettergram/ElevatorAllocation

https://www.youtube.com/watch?v=BCN9mQOT3RQ

https://www.youtube.com/watch?v=oY1QlCqWOss

How to activate this program:
path to Ex1 directory \python main.py Ex1_Buildings\"Buidling Json file" Ex1_Calls\"Calls csv file" "Out csv file"
for example:

![](../../AppData/Local/Temp/b2156390-d5ff-4197-b189-b811b8364c6c.jpg)