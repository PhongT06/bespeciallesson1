# Task 1.

# Hash Table for Fast Retrieval:
# Use a hash table (or dictionary) to store conversations, where the key is a unique identifier
# Hash tables provide constant-time average-case access for retrieval, which is crucial for fast message lookup.

# Doubly Linked List for Message Ordering and Insertion/Deletion:
# Doubly linked lists maintain the chronological order of messages and allow efficient insertion and deletion operations at the beginning or end.
# New messages can be appended to the end of the linked list in constant time, preserving the order of messages.


# Task 2.

# Polling:
# Approach: Clients periodically send requests to the server to check for new messages.
# Data Structure: A simple queue or list can be used to store new messages on the server-side.

# WebSockets:
# Approach: Clients establish a persistent, bidirectional communication channel with the server, allowing real-time data transfer in both directions.
# Data Structure: A queue or list can be used to store new messages, but more advanced data structures like priority queues or trees may be beneficial for efficient message ordering and delivery.
# Pros: Low latency, efficient use of resources, full-duplex communication.
# Cons: Increased complexity in implementation and infrastructure, potential for scaling issues with a large number of concurrent connections.

# Real-time Database:
# Approach: Use a real-time database (e.g., Firebase Realtime Database, Realm) that provides built-in support for real-time updates and synchronization across clients.
# Data Structure: The underlying data structure used by the real-time database may vary, but it typically involves efficient data structures for fast retrieval and updates.
# Pros: Simplified implementation, automatic synchronization across clients, built-in real-time capabilities.
# Cons: Potential vendor lock-in, limited control over the underlying data structures and algorithms, potential for higher costs compared to self-hosted solutions.


# Task 3.

# Data Structure for Conversation Metadata:
# A combination of a hash table (or dictionary) and a self-balancing binary search tree 

# Sorting and Filtering Conversations:
# The self-balancing binary search tree allows efficient sorting of conversations based on the chosen attribute
# Filtering conversations based on specific criteria (e.g., unread messages, participant names) can be done efficiently by traversing the binary search tree and applying the filter conditions.

# Real-time Updates:
# Implement real-time updates for the conversation list to reflect changes in the conversation metadata, such as new messages, unread counts, or participant changes.

