#include "PythonWrapper.h"

#if defined(_DEBUG) 
#undef _DEBUG 
#include <Python.h> 
#define _DEBUG 
#else 
#include <Python.h> 
#endif

Python* pyth::python = NULL;

static PyMethodDef PythonMethods[] = 
{
	//{ "Print", WrapGameEnginePrint, METH_VARARGS, "Use GameEngine to print a message"},
	//{ "GetValue", WrapGameEngineGetValue, METH_VARARGS, "Get a specific value" },
	//{ "SetValue", WrapGameEngineSetValue, METH_VARARGS, "Set a specific value" },
	//{ "SetPerson", SetPerson, METH_VARARGS, "LOL" },
	//{ "SetLastPrintedString", SetLastPrintedString, METH_VARARGS, "LOL2" },
	{ NULL, NULL, 0, NULL },
};

Python::Python()
{
	Py_Initialize();

	m_PyModule = Py_InitModule("Python", PythonMethods);
	PyObject* capsule = PyCapsule_New((void*) this, "Python._C_API", NULL);
	if (NULL == capsule)
		MaloW::Debug("Failed to capsule Python module");

	PyModule_AddObject(m_PyModule, "_C_API", capsule);
}

Python::~Python()
{

}

PyObject* Python::LoadScript(string filename)
{
	PyObject* lpSrc =  PyString_FromString(filename.c_str());
	if(!lpSrc) // Standard koll för null, så att vårt program inte kraschar
	{
		cout << "Failed to create create pyhon string" << endl;
		return NULL;
	}
	
	PyObject* lpPy = PyImport_Import(lpSrc);
	Py_DECREF(lpSrc); // Plocka bort referensen av vår python string

	if(!lpPy)
	{
		if(PyErr_Occurred())
			PyErr_Print();
		MaloW::Debug("Failed to load python script");
	}
	return lpPy;
}

PyObject* Python::CallFunction(PyObject* pModule, string functionName, PyObject* lpFunctionArgs)
{
	const char* lpSrc = functionName.c_str();
	PyObject* lpFunction = PyObject_GetAttrString(pModule, lpSrc);
	if(!lpFunction || (!PyCallable_Check(lpFunction)))
	{
		if(PyErr_Occurred())
			PyErr_Print();

		MaloW::Debug("Can not find " + string(lpSrc) + " or its not a callable function");
		Py_XDECREF(lpFunction);  // Plocka bort referensen av vår python string, XDECREF är null terminerad
		lpFunction = NULL;
		return NULL;
	}

	PyObject* lpReturnValues = PyObject_CallObject(lpFunction, lpFunctionArgs);
	Py_DECREF(lpFunctionArgs);

	if(!lpReturnValues)
	{
		MaloW::Debug("Failed to call and get return values from " + string(lpSrc));
		PyErr_Print();
		Py_DECREF(lpFunction);
		return NULL;
	}


	/*
	int numArgs = PyObject_Length(lpReturnValues); // Hur många värden returnerade python
	for(int i=0; i<numArgs; i++)
	{
		PyObject *item = PyTuple_GetItem(lpReturnValues, i);
		if(!PyString_Check(item)) // Kolla så att item är en sträng
		{
			cout << "argument " << i << " is not a string" << endl;
			continue;
		}
		cout << "Python returned value(" << i << "): " << PyString_AsString(item) << endl;
	}
	Py_DECREF(lpReturnValues);
	*/



	return lpReturnValues;
}