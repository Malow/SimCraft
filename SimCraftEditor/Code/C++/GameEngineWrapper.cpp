//File: GameEngineWrapper.cpp

#include "GameEngineWrapper.h"
#include "GameEngine.h"

GameEngineWrapper::GameEngineWrapper()
{
	m_GameEngine = new GameEngine();
}
GameEngineWrapper::~GameEngineWrapper()
{
	SAFE_DELETE(m_GameEngine);
}

HRESULT GameEngineWrapper::Init(HWND hWnd, int width, int height)	
{
	return m_GameEngine->Init(hWnd, width, height);
}
HRESULT GameEngineWrapper::Shutdown()
{
	SAFE_DELETE(m_GameEngine);

	return S_OK;
}

HRESULT GameEngineWrapper::ProcessFrame()
{
	return m_GameEngine->ProcessFrame();
}
HRESULT GameEngineWrapper::OnResize(int width, int height)
{
	return m_GameEngine->OnResize(width, height);
}

char* GameEngineWrapper::ProcessText(char* msg)
{
	return m_GameEngine->ProcessText(msg);
}