# Practical No. 3
# XML-RPC Client: Calls remote arithmetic operations

import xmlrpc.client

SERVER_URL = "http://127.0.0.1:8000/"


def main():
    # Values sent to the server for remote calculation.
    a = 10
    b = 5

    try:
        with xmlrpc.client.ServerProxy(SERVER_URL, allow_none=True) as server:
            print("Connected to XML-RPC server")
            print("Numbers:", a, "and", b)
            print("Addition:", server.add(a, b))
            print("Subtraction:", server.subtract(a, b))
            print("Multiplication:", server.multiply(a, b))
            print("Division:", server.divide(a, b))

            # Check the division-by-zero condition.
            print("Division by zero:", server.divide(a, 0))

    except (OSError, xmlrpc.client.Error) as error:
        print("Could not communicate with the server:", error)
        print("Make sure server.py is running before starting client.py.")


if __name__ == "__main__":
    main()


# Practical No. 3
# XML-RPC Server: Remote Arithmetic Operations

from xmlrpc.server import SimpleXMLRPCServer


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Divide the first number by the second number."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def main():
    # Create the XML-RPC server on the local computer.
    with SimpleXMLRPCServer(
        ("127.0.0.1", 8000),
        allow_none=True,
        logRequests=False
    ) as server:
        # Make the arithmetic functions available to clients.
        server.register_function(add, "add")
        server.register_function(subtract, "subtract")
        server.register_function(multiply, "multiply")
        server.register_function(divide, "divide")

        print("XML-RPC server is running at http://127.0.0.1:8000/")
        print("Waiting for client requests... Press Ctrl+C to stop.")

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
