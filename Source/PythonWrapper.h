#pragma once

#include "stdafx.h"

#include <string>
#include <map>
#include <Windows.h>
#include "GraphicsEngine.h"

class Entity
{
public:
	StaticMesh* mesh;
	int id;

	Entity() { this->mesh = NULL; }
	virtual ~Entity() { if(this->mesh) GetGraphicsEngine()->DeleteStaticMesh(this->mesh); }
};

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

	MaloW::Array<Entity*>* entities;

	void PrintErr();
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