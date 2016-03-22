.PHONY: protoc

export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION = cpp
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION = 2

protoc:
	protoc --proto_path=riak_pb/src --python_out=riak riak_pb/src/riak.proto
	protoc --proto_path=riak_pb/src --cpp_out=src riak_pb/src/riak.proto
	protoc --proto_path=riak_pb/src --python_out=riak riak_pb/src/riak_kv.proto
	protoc --proto_path=riak_pb/src --cpp_out=src riak_pb/src/riak_kv.proto
