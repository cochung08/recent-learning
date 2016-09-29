Clearly describes how you implemented your functionality
------------------------------------------------
**ECHO:**

Server echo back what the client sent.

**TRANSFER:**
Server keeps sending chunks to Client until there is no more data read from the file.
Client keeps receving chunks until the read() returns non-positive value.

**GFLIB:**
Client sends a request to the Server.
Then server parses the request by trying to find "GETFILE ", then "GET " and then "\r\n\r\n" to determine the path.
If correct scheme is not found, it will not try to find method.
If correct method is not found, it will not try to find end_sequence hence no path will be found.
If Server can find a path, it will call the writeback handler or sendheader() if content state is not reached or the ctx->status != GF_OK.

The memory-leak is minimized given the fact that there will be at least two alloc() from gfcontext_create() and gfserver_create() cannot be freed if the server is not supposed to stop. strdup() is either avoided or freed later.

**MTGF:**

Client will first enqueue all the req_path. After that it will initiate a thread_pool from thread_info_init(). Within the pool each thread created will be assigned a thread_main() function to dequeue the request_path from the steque and then perform the same job in gflib(send request and save the data returned from server). The pop() is within the lock.

The server will first initiate a pool of workers ready. All the workers will wait to dequeue a request from a request queue until a signal is received telling that the request queue is not empty.
The server also keeps listening from the client. Once a connection is accepted, it will enqueue the request into the request queue and signal a worker thread.


Clearly describes how you tested your components
------------------------------------------------

**for gfserver_mt:**

    make clean
    make
    valgrind --leak-check=full --show-leak-kinds=all ./gfserver_main -t 1
    valgrind --leak-check=full --show-leak-kinds=all ./gfserver_main -t 2
    valgrind --leak-check=full --show-leak-kinds=all ./gfserver_main -t 4
    valgrind --leak-check=full --show-leak-kinds=all ./gfserver_main -t 8

**for gfclient_mt:**
(here in my ./server_root, I have 10 different files, so I used multiple of 10 for easy comparison with "wc")

    make
    rm courses/ud923/filecorpus/*
    valgrind --leak-check=full --show-leak-kinds=all ./gfclient_download -n 10
    valgrind --leak-check=full --show-leak-kinds=all ./gfclient_download -t 10 -n 10
    wc courses/ud923/filecorpus/*
    wc server_root/courses/ud923/filecorpus/*

Clearly describes challenges you overcame during your implementation
--------------------------------------------------------------------
Some observations:
1.Avoid using strdup() which creates a pointer needed to be freed later.
2.Pointer propagated to several functions deeper via function calls are harder to be found and freed.
3.The less lock()/unlock(), the faster MT server-client. Lock contention takes time.
4.<regexp.h> could be helpful to parse the HTTP request, especially to match keywords like GETFILE,\r\n\r\n . Could be simpler than manually parsing the request char by char.
5. Lesson learnt:the order to free() matters in handler.c, should be a pointer problem,     I should free(req) then free(node), see my code in handler.c for concrete example.



References any external materials that you consulted during your development process
Major references:
http://man7.org/tlpi/code/online/interfaces.html
Beej's guide of Network Programming
K&R's The C Programming Language
stackoverflow
The idea of "state diagram" used for parsing URL 	was inspired by "hailcaesar"


Suggestions on how you would improve the documentation, sample code, testing, or other aspects of the project

Improvement suggestions to the project:
It will be very interesting if we can be introduced to the profiling part of the valgrind to test our implementation.

The current project indeed complemented the course material very well especially in concurrency model

If there can be some addtion to the current project, I would like to learn how to implement a prototype OS like xv6 currently being used in cs3210.
