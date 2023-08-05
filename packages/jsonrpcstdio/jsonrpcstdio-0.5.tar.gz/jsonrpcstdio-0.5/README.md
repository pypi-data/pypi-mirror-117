# JSON RPC over Standard IO

This package contains a simple implementation of
the [JSON RPC 2.0 specification](https://www.jsonrpc.org/specification) 
for arbitrary `StreamReader/StreamWriter` objects from `asyncio` with
a particular implementation for communication over standard IO.

### Basic usage

General usage follows a Flask-like interface where you define a 
server object and register methods to be accessed via RPC. For example:

```python
import asyncio
from jsonrpcstdio import StdioJSONRPCServer

server = StdioJSONRPCServer()

@server.register('subtract')
def subtract(a, b):
    return a - b

asyncio.run(
    server.run()
)
```

Passing calls to the above server can be done via JSON RPC format, for
example:

```
--> {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}
<-- {"jsonrpc": "2.0", "result": 19, "id": 1}
```

Where `-->` goes to the server over `stdin` and `<--` comes back over `stdout`.

If the above code sits in a script called `server.py`, you can replicate the
above with:

```bash
echo '{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}' | python server.py
```

The package also provides a more general `JSONRPCServer` class that functions much like
the above but accepts arbitrary `StreamReader/StreamWriter` instances as arguments to `run()`, e.g. 
`JSONRPCServer.run(reader, writer)`. See the implementation of `StdioJSONRPCServer` for more details.