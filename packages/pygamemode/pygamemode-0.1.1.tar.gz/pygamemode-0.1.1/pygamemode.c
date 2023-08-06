#define PY_SSIZE_T_CLEAN
#define Py_LIMITED_API 0x03060000
#include <Python.h>
#include "gamemode_client.h"

PyDoc_STRVAR(request_start__doc__,
             "int request_start() - Request gamemode starts\n"
             "    0 if the request was sent successfully\n"
             "   -1 if the request failed\n");

static PyObject *request_start(PyObject *self, PyObject *noargs)
{
    return PyLong_FromLong(gamemode_request_start());
}

PyDoc_STRVAR(request_end__doc__,
             "int request_end() - Request gamemode ends\n"
             "    0 if the request was sent successfully\n"
             "   -1 if the request failed\n");

static PyObject *request_end(PyObject *self, PyObject *noargs)
{
    return PyLong_FromLong(gamemode_request_end());
}

PyDoc_STRVAR(query_status__doc__,
             "int query_status() - Query the current status of gamemode\n"
             "    0 if gamemode is inactive\n"
             "    1 if gamemode is active\n"
             "    2 if gamemode is active and this client is registered\n"
             "   -1 if the query failed\n");
static PyObject *query_status(PyObject *self, PyObject *noargs)
{
    return PyLong_FromLong(gamemode_query_status());
}

PyDoc_STRVAR(request_start_for__doc__,
             "int request_start_for(int pid) - Request gamemode starts for another process\n"
             "   0 if the request was sent successfully\n"
             "  -1 if the request failed\n"
             "  -2 if the request was rejected\n");
static PyObject *request_start_for(PyObject *self, PyObject *args)
{
    int pid;
    if (!PyArg_ParseTuple(args, "i", &pid))
    {
        return NULL;
    }
    return PyLong_FromLong(gamemode_request_start_for(pid));
}

PyDoc_STRVAR(request_end_for__doc__,
             "int request_end_for(int pid) - Request gamemode ends for another process\n"
             "   0 if the request was sent successfully\n"
             "   -1 if the request failed\n"
             "   -2 if the request was rejected\n");
static PyObject *request_end_for(PyObject *self, PyObject *args)
{
    int pid;
    if (!PyArg_ParseTuple(args, "i", &pid))
    {
        return NULL;
    }
    return PyLong_FromLong(gamemode_request_end_for(pid));
}

PyDoc_STRVAR(query_status_for__doc__,
             "int query_status_for(pid_t pid) - Query status of gamemode for another process\n"
             "   0 if gamemode is inactive\n"
             "   1 if gamemode is active\n"
             "   2 if gamemode is active and this client is registered\n"
             "   -1 if the query failed\n");
static PyObject *query_status_for(PyObject *self, PyObject *args)
{
    int pid;
    if (!PyArg_ParseTuple(args, "i", &pid))
    {
        return NULL;
    }
    return PyLong_FromLong(gamemode_query_status_for(pid));
}

PyDoc_STRVAR(error_string__doc__,
             "string error_string() - Get an error string\n"
             "    returns a string with more detailed error messages.");

static PyObject *error_string(PyObject *self, PyObject *noargs)
{
    return PyUnicode_FromString(gamemode_error_string());
}

static PyMethodDef gamemode_meths[] = {
    {"request_start", request_start, METH_NOARGS, request_start__doc__},
    {"request_end", request_end, METH_NOARGS, request_end__doc__},
    {"query_status", query_status, METH_NOARGS, query_status__doc__},
    {"request_start_for", request_start_for, METH_VARARGS, request_start_for__doc__},
    {"request_end_for", request_end_for, METH_VARARGS, request_end_for__doc__},
    {"query_status_for", query_status_for, METH_VARARGS, query_status_for__doc__},
    {"error_string", error_string, METH_NOARGS, error_string__doc__},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef gamemodemodule = {
    PyModuleDef_HEAD_INIT, "gamemode", NULL, -1, gamemode_meths};

PyMODINIT_FUNC
PyInit_gamemode(void)
{
    return PyModule_Create(&gamemodemodule);
}
