#include <Python.h>

void print_info(int info_type);

static PyObject *PyUnameError;

static PyObject *
get(PyObject *self, PyObject *args) {
    int info_type;

    if (!PyArg_ParseTuple(args, "i", &info_type)) {
        PyErr_SetString(PyUnameError, "expected 1 arguments, got 0");
        return NULL;
    }

    print_info(info_type);

    return Py_BuildValue("");
}

static PyMethodDef PyUnameMethods[] = {
    {"get",  get, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef getmodule = {
    PyModuleDef_HEAD_INIT,
    "uname",
    NULL,
    -1,
    PyUnameMethods
};

PyMODINIT_FUNC
PyInit_uname(void){
    PyObject *m;
    m = PyModule_Create(&getmodule);
    if (m == NULL)
        return NULL;

    PyModule_AddIntConstant(m, "SYSNAME", 0);
    PyModule_AddIntConstant(m, "NODENAME", 1);
    PyModule_AddIntConstant(m, "RELEASE", 2);
    PyModule_AddIntConstant(m, "VERSION", 3);
    PyModule_AddIntConstant(m, "MACHINE", 4);

    PyUnameError = PyErr_NewException("uname.Error", NULL, NULL);
    Py_XINCREF(PyUnameError);

    if (PyModule_AddObject(m, "Error", PyUnameError) < 0) {
        Py_XDECREF(PyUnameError);
        Py_CLEAR(PyUnameError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}