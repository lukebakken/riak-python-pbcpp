#include <Python.h>

static PyMethodDef RiakKvPbMethods[] = {
	{NULL, NULL, 0, NULL} /* Sentinel */
};

PyMODINIT_FUNC
init_riak_kv_pbcpp(void)
{
	PyObject *m;
	m = Py_InitModule("riak._riak_kv_pbcpp", RiakKvPbMethods);
	if (m == NULL)
		return;
}
