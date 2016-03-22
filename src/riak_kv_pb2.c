#include <Python.h>

static PyMethodDef RiakKvPbMethods[] = {
	{NULL, NULL, 0, NULL} /* Sentinel */
};

PyMODINIT_FUNC
initriak_kv_pb(void)
{
	PyObject *m;
	m = Py_InitModule("riak.riak_kv_pb2", RiakKvPbMethods);
	if (m == NULL)
		return;
}
