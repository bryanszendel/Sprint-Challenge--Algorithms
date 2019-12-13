#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n) as the input increases, the runtime will increase as the same rate as the input because the function is only returning n^2 whereas the base case is set at n^3. With each input increase, the function will have to run the same number of the input. 


b) This problem has nested loops so it will be Polynomial O(n^c). As the input increases, the runtime will increase pretty quickly. It works well for small inputs but it will have poorer performance the larger the input gets. 


c) This problem is recursive and it will be Linear O(n) wherein as the input increases, the runtime increase at the same rate. The algorithm has to perform the function as many times as n increases. It is about the same as a for loop. 

## Exercise II

Questions: 
Are we dropping an egg off each floor, each time?
Are we continuing to throw eggs until we run out?

Inputs: 
n (for how many stories are in the building)
eggs (for number of eggs we start with)

Outputs: f (for which floor is optimal to reduce number of broken eggs)

Assuming we will continue to go through each floor until we have thrown all of our eggs, we will need to start at floor one and throw and egg. If f, the egg will break and we will count the numbers of eggs that are broken as we go on each floor. 

If we reach the top of the building, we will take the elevator down and start over from floor 2. We will repeat the process all the way up and increment the starting floor each time. 

at the end of the series, we will return the f with the lowest number of broken eggs

This type of algorithm contains a nested loop which would give us a Polynomial O(n^c) and the number of stories that we have would significantly affect the time complexity runtime of the looping.  