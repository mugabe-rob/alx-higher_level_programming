#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

	void print_python_bytes(PyObject *p)
{
	long int size;
	int counter;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (counter = 0; counter <= size && counter < 10; counter++)
		printf(" %02hhx", trying_str[counter]);
	printf("\n");
}

	void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int counter;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (counter = 0; counter < size; counter++)
	{
	type = (list->ob_item[counter])->ob_type->tp_name;
	printf("Element %i: %s\n", counter, type);
	if (!strcmp(type, "bytes"))
	print_python_bytes(list->ob_item[counter]);
	}
}
