#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    PyListObject *obj = (PyListObject *)p;
    long int size = PyList_Size(p);
    int i;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", obj->allocated);
    for (i = 0; i < size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}

int main(void)
{
    Py_Initialize();
    PyObject *my_list = Py_BuildValue("[isOf]", 1, "hello", 3.14, Py_BuildValue("(ii)", 4, 5));

    if (my_list == NULL)
    {
        PyErr_Print();
        return 1;
    }

    print_python_list_info(my_list);
    Py_DECREF(my_list);

    Py_Finalize();
    return 0;
}
