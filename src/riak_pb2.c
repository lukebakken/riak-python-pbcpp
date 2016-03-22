#include <Python.h>

static PyMethodDef RiakPbMethods[] = {
	{NULL, NULL, 0, NULL} /* Sentinel */
};

PyMODINIT_FUNC
initriak_pb(void)
{
	PyObject *m;
	m = Py_InitModule("riak.riak_pb2", RiakPbMethods);
	if (m == NULL)
		return;
}
