import binascii
import os
import riak.benchmark as benchmark
import riak.riak_pb2

data = binascii.b2a_hex(os.urandom(1024))
iterations = pow(2, 19)

print("Benchmarking PBC:")
print("  Iterations: {0}".format(iterations))

impl = os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] or 'python'

with benchmark.measure() as b:
    for i in xrange(1, 4):
        with b.report('s-{}-{}'.format(impl, i)):
            for x in xrange(0, iterations + 1):
                err = riak.riak_pb2.RpbErrorResp()
                err.errcode = 1024
                err.errmsg = data
                err.SerializeToString()

err = riak.riak_pb2.RpbErrorResp()
err.errcode = 1024
err.errmsg = data
serr = err.SerializeToString()

with benchmark.measure() as b:
    for i in xrange(1, 4):
        with b.report('ds-{}-{}'.format(impl, i)):
            for x in xrange(0, iterations + 1):
                err = riak.riak_pb2.RpbErrorResp()
                err.ParseFromString(serr)
