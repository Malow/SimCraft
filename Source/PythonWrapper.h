#pragma once

#include "stdafx.h"

#include <string>
#include <map>
#include <Windows.h>

using namespace std;

typedef struct _object PyObject;
typedef map<string, string> EngineValues;


class Python
{
private:
	PyObject* m_PyModule;

public:
	Python();
	virtual ~Python();	

	PyObject* LoadScript(string fileName);
	PyObject* CallFunction(PyObject* pModule, string functionName, PyObject* lpFunctionArgs);

};


// Used as an easy singleton
struct pyth
{
	static Python* python;
};

inline Python* GetPythonWrapper()
{
	return pyth::python;
}