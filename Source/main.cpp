#include "stdafx.h"
#include "GraphicsEngine.h"
#include "PythonWrapper.h"

#if defined(_DEBUG) 
#undef _DEBUG 
#include <Python.h> 
#define _DEBUG 
#else 
#include <Python.h> 
#endif

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, LPWSTR, int nCmdShow)
{
#if defined(DEBUG) || defined(_DEBUG)
	myInitMemoryCheck();
#endif
	
	MaloW::ClearDebug();
	// Create parameters for the graphics engine, LOAD THEM FROM .cfg-FILE later on!
	GraphicsEngineParams params;
	params.windowHeight = 900;
	params.windowWidth = 1600;
	params.FXAAQuality = 3;			// 0 - 6
	params.ShadowMapSettings = 6;	// 0 - 10 (works with higher but VERY consuming)
	params.CamType = RTS;
	
	// Create the graphics engine
	GraphicsEngine* ge = new GraphicsEngine(params, hInstance, nCmdShow);
	gfxeng::eng = ge; // Set the global eng to our engine so that GetGraphicsEngine(); can work.
	ge->CreateSkyBox("Media/skymap.dds");

	// Create the Python engine
	Python* python = new Python();
	pyth::python = python;
	python = GetPythonWrapper();	// To get python anywhere

	PyObject* script = python->LoadScript("Scripts.SimCraftMain");

	float diff = ge->Update();	// To not get a high first diff
	while(ge->isRunning())	// Returns true as long as ESC hasnt been pressed, if it's pressed the game engine will shut down itself (to be changed)
	{
		float diff = ge->Update();	// Updates camera etc, does NOT render the frame, another process is doing that, so diff should be very low.


		PyObject* funcArgs = Py_BuildValue("(f)", diff);
		PyObject* ret = python->CallFunction(script, "Update", funcArgs);
		if(ret) Py_DECREF(ret);


		if(ge->GetKeyListener()->IsPressed('W'))
			ge->GetCamera()->moveForward(diff);
		if(ge->GetKeyListener()->IsPressed('A'))
			ge->GetCamera()->moveLeft(diff);
		if(ge->GetKeyListener()->IsPressed('S'))	// For keys other than the main-chars you use the VK_ Enums, rightclick on VK_RETURN and "Go to definition" to find the list of all keys
			ge->GetCamera()->moveBackward(diff);
		if(ge->GetKeyListener()->IsPressed('D'))	// For keys other than the main-chars you use the VK_ Enums, rightclick on VK_RETURN and "Go to definition" to find the list of all keys
			ge->GetCamera()->moveRight(diff);
		if(ge->GetKeyListener()->IsClicked(1))
			ge->GetCamera()->moveBackward(diff);
	}


	// Delete graphics engine
	delete ge;
	// delete python
	delete python;
	return 0;
}