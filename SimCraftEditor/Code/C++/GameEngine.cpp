//File: GameEngine.h

#include "GameEngine.h"

GameEngine::GameEngine()
{
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

	return S_OK;
}
HRESULT GameEngine::Shutdown()
{
	return S_OK;
}

HRESULT GameEngine::ProcessFrame()
{
	FrameFunc();
	RenderFunc();
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

bool GameEngine::FrameFunc()
{
	if(eng->GetKeyListener()->IsPressed(VK_ESCAPE))
		return true;

	return false;
}

void GameEngine::RenderFunc()
{

}

char* GameEngine::ProcessText(char* msg)
{
	return msg;
}