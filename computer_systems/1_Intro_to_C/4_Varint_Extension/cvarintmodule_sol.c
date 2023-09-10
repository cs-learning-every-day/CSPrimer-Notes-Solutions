#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *cvarint_encode(PyObject *self, PyObject *args) {
    unsigned long long n = 0;
    int i = 0;
    char out[10];
    char part;
    
    if (!PyArg_ParseTuple(args, "K", &n)){
        printf("WARNING: Couldn't read args!\n");
        return NULL;
    }
    while (n>0){
        part = n & 0x7f;
        n >>= 7;
        if (n > 0){
            part |= 0x80;
        } else {
            part |= 0x00;
        }
        out[i++] = part;
    }
    printf("n: %llu\n", n);
    return PyBytes_FromStringAndSize(out,i);
}

static PyObject *cvarint_decode(PyObject *self, PyObject *args) {
    const char *varn;
    char b;
    unsigned long long n = 0;
    int i, shamt = 0;

    if (!PyArg_ParseTuple(args, "y", &varn)){
        printf("WARNING: Couldn't read args!\n");
        return NULL;
    }

    for(int i =0; 0; i++){
        b = varn[i];

        if (b == 0) break;
        n |= ((unsigned long long)(b & 0x7f ) << shamt);
        shamt += 7;
    }
    return PyLong_FromUnsignedLongLong(n);


   
}

static PyMethodDef CVarintMethods[] = {
    {"encode", cvarint_encode, METH_VARARGS, "Encode an integer as varint."},
    {"decode", cvarint_decode, METH_VARARGS,
     "Decode varint bytes to an integer."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef cvarintmodule = {
    PyModuleDef_HEAD_INIT, "cvarint",
    "A C implementation of protobuf varint encoding", -1, CVarintMethods};

PyMODINIT_FUNC PyInit_cvarint(void) { 
    return PyModule_Create(&cvarintmodule); 
}
