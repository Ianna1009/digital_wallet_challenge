# Table of Contents

1. [Challenge Summary] (README.md#challenge-summary)
2. [Details of Implementation] (README.md#details-of-implementation)


##Challenge Summary

Imagine you're a data engineer at a "digital wallet" company called PayMo that allows users to easily request and make payments to other PayMo users. The team at PayMo has decided they want to implement features to prevent fraudulent payment requests from untrusted users. 

###Feature 1
When anyone makes a payment to another user, they'll be notified if they've never made a transaction with that user before.

* "unverified: You've never had a transaction with this user before. Are you sure you would like to proceed with this payment?"

###Feature 2
The PayMo team is concerned that these warnings could be annoying because there are many users who haven't had transactions, but are still in similar social networks. 

For example, User A has never had a transaction with User B, but both User A and User B have made transactions with User C, so User B is considered a "friend of a friend" for User A.

For this reason, User A and User B should be able to pay each other without triggering a warning notification since they're "2nd degree" friends. 

<img src="./images/friend-of-a-friend1.png" width="500">

To account for this, PayMo would like you to also implement this feature. When users make a payment, they'll be notified when the other user is outside of their "2nd-degree network".

* "unverified: This user is not a friend or a "friend of a friend". Are you sure you would like to proceed with this payment?"


###Feature 3
More generally, PayMo would like to extend this feature to larger social networks. Implement a feature to warn users only when they're outside the "4th degree friends network".

<img src="./images/fourth-degree-friends2.png" width="600">

In the above diagram, payments have transpired between User

* A and B 
* B and C 
* C and D 
* D and E 
* E and F

Under this feature, if User A were to pay User E, there would be no warning since they are "4th degree friends". 

However, if User A were to pay User F, a warning would be triggered as their transaction is outside of the "4th-degree friends network."

(Note that if User A were to pay User C instead, there would be no warning as they are "2nd-degree" friends and within the "4th degree network") 


##Details of implementation

[Back to Table of Contents] (README.md#table-of-contents)

1. Implementation Language: Python
2. Packages involved: Set, csv, sys. This packages have imported in the head of file ``antifraud.py``.
3. Data Structure: Graph, implemented through dict in Python.

#### Implementation on Feature 1
For feature 1, I used a graph stored with adjacent lists.

Implemented with ``dict``, once a payment happened,  `id1` will be added as a key to the  `dict`, and `id2` will be add as `id1's` value if `id1` was not in the graph.
At the same time, `id2` as key and `id1` as its value will also be updated in the graph since we consider there is no order difference between these two users.

Once the graph is well constructed, it can be used to check if the user in the new payment information is unverified or not.
In fact, we just need to check if `new_id1` or `new_id2` is in the graph, and also if its key is `new_id2` or `new_id1`, correspondingly.
#### Implementation on Feature 2
Based on the first implementation, this second step is just needed to check if `key1` and `key2` has common 'friend', if they have at least one common friend, they must be within 2nd connection.
#### Implementation on Feature 3

Simply idea for 4th-degree friend network is 'second's second', which means if we constructed a larger graph stored with values of both 1st-degree and 2nd-degree friends list. Then the problem will be simplified.


