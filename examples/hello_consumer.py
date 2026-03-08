'''
Importing compatibility features from future Python versions.
absolute_import ensures imports behave like Python 3.
unicode_literals makes all string literals unicode by default.
print_function allows the use of print() as a function.
'''
from __future__ import absolute_import, unicode_literals, print_function

'''
Importing Connection class from kombu library.
Kombu is a messaging library used to interact with message brokers
like RabbitMQ using AMQP protocol.
'''
from kombu import Connection  # noqa


'''
Establishing a connection to the message broker.

Connection URL breakdown:
amqp://      -> protocol used (AMQP)
guest:guest  -> username and password
localhost    -> server where RabbitMQ is running
5672         -> default RabbitMQ port
//           -> default virtual host
'''
with Connection('amqp://guest:guest@localhost:5672//') as conn:

    '''
    Creating or accessing a queue named "simple_queue".
    SimpleQueue provides an easy interface for sending
    and receiving messages from the queue.
    '''
    simple_queue = conn.SimpleQueue('simple_queue')

    '''
    Retrieving a message from the queue.

    block=True  -> wait until a message arrives
    timeout=1   -> wait for only 1 second before raising an error
    '''
    message = simple_queue.get(block=True, timeout=1)

    '''
    Printing the message payload (actual data sent in the message).
    '''
    print('Received: {0}'.format(message.payload))

    '''
    Acknowledging the message.
    This tells the message broker that the message has been
    successfully processed and can be removed from the queue.
    '''
    message.ack()

    '''
    Closing the queue connection after processing the message.
    '''
    simple_queue.close()
