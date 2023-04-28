# Chat-Application-between-two-clients using Socket Programming

The provided codes implement a simple
chat application using socket programming in Python.
The application consists of a server and multiple
clients that can connect to the server and send
messages to each other.
 The server listens for incoming
client connections on a specified host and port. When
a client connects to the server, the server prompts the
client to enter a nickname. The nickname is then
associated with the client's socket in a dictionary. The
server also broadcasts a message to all connected
clients that a new client has joined the chat.
 Once a client is connected and
has entered a nickname, it can send messages to the
server, which then broadcasts the message to all
connected clients except for the sender. The server
adds the sender's nickname to the message so that
each client knows who sent the message.
 The client code prompts the user to
enter a nickname and then connects to the server.
Once connected, the client continuously listens for
incoming messages from the server. When a message
is received, the client prints the message to the
console. The client also continuously prompts the user
to enter messages, which are then sent to the server
and broadcasted to all other clients by the server.
