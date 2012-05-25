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

	// Create the Terrain and lights etc
	ge->GetCamera()->setPosition(D3DXVECTOR3(100, 40, 100));
	Terrain* terrain = ge->CreateTerrain(D3DXVECTOR3(0, -1, 0), D3DXVECTOR3(200, 1, 200), "Media/TerrainTexture.png", "", 256);
	Light* light = ge->CreateLight(D3DXVECTOR3(50, 50, 50));
	Light* light2 = ge->CreateLight(D3DXVECTOR3(150, 50, 50));
	Light* light3 = ge->CreateLight(D3DXVECTOR3(50, 50, 150));
	Light* light4 = ge->CreateLight(D3DXVECTOR3(150, 50, 150));
	float inte = 100.0f;
	light->SetIntensity(inte);
	light2->SetIntensity(inte);
	light3->SetIntensity(inte);
	light4->SetIntensity(inte);

	// Create the Python engine
	Python* python = new Python();
	pyth::python = python;
	python = GetPythonWrapper();	// To get python anywhere

	PyObject* script = python->LoadScript("Scripts.SimCraftMain");

	// Load Map:
	PyObject* funcArgs = Py_BuildValue("(s)", "TestMap1.txt");
	PyObject* ret = python->CallFunction(script, "LoadMap", funcArgs);
	if(ret) Py_DECREF(ret);
	
	
	float SPEED_MUTLIPLIER = 1;
	bool SpeedPlus = true;
	bool SpeedMinus = true;
	float scale = 1.0f;

	float diff = ge->Update();	// To not get a high first diff
	while(ge->isRunning())	// Returns true as long as ESC hasnt been pressed, if it's pressed the game engine will shut down itself (to be changed)
	{
		float diff = ge->Update();	// Updates camera etc, does NOT render the frame, another process is doing that, so diff should be very low.
		
		PyObject* funcArgs = Py_BuildValue("(f)", diff * SPEED_MUTLIPLIER);
		PyObject* ret = python->CallFunction(script, "Update", funcArgs);
		if(ret) Py_DECREF(ret);


		// Make lights face your way
		/*
		D3DXVECTOR3 spot = ge->GetCamera()->getPosition();
		spot.z += spot.y / 2.0f;
		spot.y = 0.0f;
		light->SetLookAt(spot);
		light2->SetLookAt(spot);
		light3->SetLookAt(spot);
		light4->SetLookAt(spot);
		*/

		if(ge->GetKeyListener()->IsPressed(VK_ADD))
		{
			if(SpeedPlus)
			{
				SPEED_MUTLIPLIER *= 2;
				SpeedPlus = false;
				// Update textbox
			}
		}
		else
			SpeedPlus = true;

		if(ge->GetKeyListener()->IsPressed(VK_SUBTRACT))
		{
			if(SpeedMinus)
			{
				SPEED_MUTLIPLIER /= 2;
				SpeedMinus = false;
				// Update textbox
			}
		}
		else
			SpeedMinus = true;

		// Key inputs
		if(ge->GetKeyListener()->IsPressed('W'))
			ge->GetCamera()->moveForward(diff);
		if(ge->GetKeyListener()->IsPressed('A'))
			ge->GetCamera()->moveLeft(diff);
		if(ge->GetKeyListener()->IsPressed('S'))	// For keys other than the main-chars you use the VK_ Enums, rightclick on VK_RETURN and "Go to definition" to find the list of all keys
			ge->GetCamera()->moveBackward(diff);
		if(ge->GetKeyListener()->IsPressed('D'))	// For keys other than the main-chars you use the VK_ Enums, rightclick on VK_RETURN and "Go to definition" to find the list of all keys
			ge->GetCamera()->moveRight(diff);
		if(ge->GetKeyListener()->IsClicked(1))
			ge->GetCamera()->setPosition(ge->GetCamera()->getPosition() - D3DXVECTOR3(0, 0.01f, 0) * diff);
		if(ge->GetKeyListener()->IsClicked(2))
			ge->GetCamera()->setPosition(ge->GetCamera()->getPosition() + D3DXVECTOR3(0, 0.01f, 0) * diff);
	}


	// Delete graphics engine
	delete ge;
	// delete python
	delete python;
	return 0;
}