#include "PythonWrapper.h"

#if defined(_DEBUG) 
#undef _DEBUG 
#include <Python.h> 
#define _DEBUG 
#else 
#include <Python.h> 
#endif

Python* pyth::python = NULL;


static PyObject* SetCameraPosition(PyObject* self, PyObject* args)
{
	float x = 0.0f;
	float y = 0.0f;
	float z = 0.0f;
	if(!PyArg_ParseTuple(args, "fff", &x, &y, &z))
	{
		PyErr_SetString(PyExc_RuntimeError, "GameEngine.Print wants a single string argument");
		MaloW::Debug("SetCameraPosition arguments failed");
		return NULL;
	}

	GetGraphicsEngine()->GetCamera()->setPosition(D3DXVECTOR3(x, y, z));

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* CreateEntity(PyObject* self, PyObject* args)
{
	const char* objFile;
	int id = 0;
	float x = 0.0f;
	float y = 0.0f;
	float z = 0.0f;

	if(!PyArg_ParseTuple(args, "sifff", &objFile, &id, &x, &y, &z))
	{
		PyErr_SetString(PyExc_RuntimeError, "GameEngine.Print wants a single string argument");
		MaloW::Debug("CreateEntity arguments failed");
		return NULL;
	}

	string file = string(objFile);

	Entity* e = new Entity();
	e->id = id;
	e->mesh = GetGraphicsEngine()->CreateStaticMesh(file, D3DXVECTOR3(x, y, z));
	GetPythonWrapper()->entities->add(e);

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* DeleteEntity(PyObject* self, PyObject* args)
{
	int id = 0;

	if(!PyArg_ParseTuple(args, "i", &id))
	{
		PyErr_SetString(PyExc_RuntimeError, "GameEngine.Print wants a single string argument");
		MaloW::Debug("DeleteEntity arguments failed");
		return NULL;
	}

	Entity* e = NULL;
	MaloW::Array<Entity*>* ents = GetPythonWrapper()->entities;
	for(int i = 0; i < ents->size(); i++)
	{
		if(ents->get(i)->id == id)
		{
			delete ents->getAndRemove(i);
			i = ents->size();
			MaloW::Debug(id);
		}
	}


	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef PythonMethods[] = 
{
	{ "SetCameraPosition", SetCameraPosition, METH_VARARGS, "SetCam"},
	{ "CreateEntity", CreateEntity, METH_VARARGS, "fuck u" },
	{ "DeleteEntity", DeleteEntity, METH_VARARGS, "Souqgbte" },
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

	this->entities = new MaloW::Array<Entity*>();
}

Python::~Python()
{
	if(this->entities)
	{
		while(this->entities->size() > 0)
			delete this->entities->getAndRemove(0);
		delete this->entities;
	}
}

PyObject* Python::LoadScript(string filename)
{
	PyObject* lpSrc =  PyString_FromString(filename.c_str());
	if(!lpSrc) // Standard koll f�r null, s� att v�rt program inte kraschar
	{
		cout << "Failed to create pyhon string" << endl;
		return NULL;
	}
	
	PyObject* lpPy = PyImport_Import(lpSrc);
	Py_DECREF(lpSrc); // Plocka bort referensen av v�r python string

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
		Py_XDECREF(lpFunction);  // Plocka bort referensen av v�r python string, XDECREF �r null terminerad
		lpFunction = NULL;
		return NULL;
	}

	PyObject* lpReturnValues = PyObject_CallObject(lpFunction, lpFunctionArgs);
	Py_DECREF(lpFunctionArgs);

	if(!lpReturnValues)
	{
		MaloW::Debug("Failed to get return values from " + string(lpSrc));
		PyErr_Print();
		Py_DECREF(lpFunction);
		return NULL;
	}


	/*
	int numArgs = PyObject_Length(lpReturnValues); // Hur m�nga v�rden returnerade python
	for(int i=0; i<numArgs; i++)
	{
		PyObject *item = PyTuple_GetItem(lpReturnValues, i);
		if(!PyString_Check(item)) // Kolla s� att item �r en str�ng
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