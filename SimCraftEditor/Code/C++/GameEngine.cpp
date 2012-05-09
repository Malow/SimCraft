//File: GameEngine.h

#include "GameEngine.h"

GameEngine::GameEngine()
{
	MaloW::ClearDebug();
	this->eng = NULL;

	this->m_ScreenWidth = 0;
	this->m_ScreenHeight = 0;
}
GameEngine::~GameEngine()
{
	SAFE_DELETE(this->eng);
}

HRESULT GameEngine::Init(HWND hWnd, int width, int height)
{
	this->m_ScreenWidth = width;
	this->m_ScreenHeight = height;

	GraphicsEngineParams params;
	params.CamType = RTS;
	params.FXAAQuality = 2;
	params.ShadowMapSettings = 4;
	params.windowHeight = height;
	params.windowWidth = width;


	this->eng = new GraphicsEngine(params, hWnd, 0);
	eng->SetSleepInRenderingThread(10);

	gfxeng::eng = eng; // Set the global eng to our engine so that GetGraphicsEngine(); can work.
	eng->GetCamera()->setPosition(D3DXVECTOR3(100, 40, 100));
	eng->CreateSkyBox("Media/skymap.dds");
	Terrain* terrain = this->eng->CreateTerrain(D3DXVECTOR3(0, -1, 0), D3DXVECTOR3(200, 1, 200), "Media/TerrainTexture.png", "", 256);
	Light* light = eng->CreateLight(D3DXVECTOR3(50, 50, 50));
	Light* light2 = eng->CreateLight(D3DXVECTOR3(150, 50, 50));
	Light* light3 = eng->CreateLight(D3DXVECTOR3(50, 50, 150));
	Light* light4 = eng->CreateLight(D3DXVECTOR3(150, 50, 150));
	float inte = 100.0f;
	light->SetIntensity(inte);
	light2->SetIntensity(inte);
	light3->SetIntensity(inte);
	light4->SetIntensity(inte);

	return S_OK;
}
HRESULT GameEngine::Shutdown()
{
	return S_OK;
}

HRESULT GameEngine::Update()
{
	
	if(this->eng->isRunning())
	{
		float diff = eng->Update();

		// Key inputs
		if(eng->GetKeyListener()->IsPressed('W'))
			eng->GetCamera()->moveForward(diff);
		if(eng->GetKeyListener()->IsPressed('A'))
			eng->GetCamera()->moveLeft(diff);
		if(eng->GetKeyListener()->IsPressed('S'))	// For keys other than the main-chars you use the VK_ Enums, rightclick on VK_RETURN and "Go to definition" to find the list of all keys
			eng->GetCamera()->moveBackward(diff);
		if(eng->GetKeyListener()->IsPressed('D'))	// For keys other than the main-chars you use the VK_ Enums, rightclick on VK_RETURN and "Go to definition" to find the list of all keys
			eng->GetCamera()->moveRight(diff);
		if(eng->GetKeyListener()->IsClicked(1))
			eng->GetCamera()->setPosition(eng->GetCamera()->getPosition() - D3DXVECTOR3(0, 0.01f, 0) * diff);
		if(eng->GetKeyListener()->IsClicked(2))
			eng->GetCamera()->setPosition(eng->GetCamera()->getPosition() + D3DXVECTOR3(0, 0.01f, 0) * diff);

	}
	
	return S_OK;
}

HRESULT GameEngine::OnResize(int width, int height)
{
	MoveWindow(this->eng->GetWindowHandle(),
           0, 0, width, height, true);

	this->m_ScreenWidth = width;
	this->m_ScreenHeight = height;

	return S_OK;
}

char* GameEngine::ProcessText(char* msg)
{
	return msg;
}