#include <Python.h>

static PyMethodDef RiakPbMethods[] = {
	{NULL, NULL, 0, NULL} /* Sentinel */
};

PyMODINIT_FUNC
initriak_pb2(void)
{
	PyObject *m;
	m = Py_InitModule("riak.pb.riak_pb2", RiakPbMethods);
	if (m == NULL)
		return;
}
