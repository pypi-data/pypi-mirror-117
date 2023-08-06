# Priority Based Connected Components
It takes an integer as an input and prints it square.

## Installation
```pip install priorityY```

## How to use it?
```
from priorityY import *
G = [(1,4,1),(1,5,3),(2,3,2),(2,6,2),(6,7,3),(4,8,2),(5,9,1)]
threshold = 3
components = priority_based_linkage(G,threshold)
print(components)
```
## Output
```
[[1, 4, 8], [2, 3, 6], [5, 9], [7]]
```
Let us visualise the above example for better understanding how the library works.
The threshold is set to 3, limiting the size of components. Dotted edges denote the link and priority associated.

![](https://github.com/walmartlabs/priorityY/blob/main/img/1.png?raw=true)


At the first iteration, all nodes having edges with Priority-1 get connected.

![](https://github.com/walmartlabs/priorityY/blob/main/img/2.png?raw=true)
1–4 and 5–9 gets connected.

In the next iteration, the algorithm connects nodes with edges between them of Priority-2.

![](https://github.com/walmartlabs/priorityY/blob/main/img/3.png?raw=true)
1–4–8 gets connected, 2–3–6 gets connected and both reach the threshold

The algorithm stops as the threshold is reached for components and no more edges left. Above are the final connected components with the set threshold and provided edges priority.

## License

© 2021 Abhishek Mungoli, Pravesh Garg, Somedip Karmakar

This repository is licensed under the MIT license. See LICENSE for details.
