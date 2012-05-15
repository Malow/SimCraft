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
	return m_GameEngine->Update();
}
HRESULT GameEngineWrapper::OnResize(int width, int height)
{
	return m_GameEngine->OnResize(width, height);
}

char* GameEngineWrapper::ProcessText(char* msg)
{
	return m_GameEngine->ProcessText(msg);
}

void GameEngineWrapper::KeyDown(char key) 
{ 
	if(GraphicsEngine* eng = this->m_GameEngine->GetEngine())
	{
		if((int)key == 38)
			eng->GetKeyListener()->KeyDown(VK_UP); 
		else if((int)key == 40)
			eng->GetKeyListener()->KeyDown(VK_DOWN); 
		else if((int)key == 37)
			eng->GetKeyListener()->KeyDown(VK_LEFT); 
		else if((int)key == 39)
			eng->GetKeyListener()->KeyDown(VK_RIGHT); 
		else
			eng->GetKeyListener()->KeyDown(key); 
	}
}
void GameEngineWrapper::KeyUp(char key) 
{ 
	if(GraphicsEngine* eng = this->m_GameEngine->GetEngine())
	{
		if((int)key == 38)
			eng->GetKeyListener()->KeyUp(VK_UP); 
		else if((int)key == 40)
			eng->GetKeyListener()->KeyUp(VK_DOWN); 
		else if((int)key == 37)
			eng->GetKeyListener()->KeyUp(VK_LEFT); 
		else if((int)key == 39)
			eng->GetKeyListener()->KeyUp(VK_RIGHT); 
		else
			eng->GetKeyListener()->KeyUp(key); 
	}
}
void GameEngineWrapper::MouseDown(int button) 
{ 
	if(GraphicsEngine* eng = this->m_GameEngine->GetEngine())
		eng->GetKeyListener()->MouseDown(button); 
}
void GameEngineWrapper::MouseUp(int button) 
{ 
	if(GraphicsEngine* eng = this->m_GameEngine->GetEngine())
		eng->GetKeyListener()->MouseUp(button); 
}

void GameEngineWrapper::DeleteUnitClosestToArrow()
{
	if(this->m_GameEngine)
		this->m_GameEngine->DeleteUnitClosestToArrow();
}

void GameEngineWrapper::CreateHuman(bool male, int age)
{
	if(m_GameEngine)
		m_GameEngine->CreateHuman(male, age);
}

void GameEngineWrapper::CreateTree(int age, int wood)
{
	if(m_GameEngine)
		m_GameEngine->CreateTree(age, wood);
}

void GameEngineWrapper::CreateFoodBush(int food)
{
	if(m_GameEngine)
		m_GameEngine->CreateFoodBush(food);
}

void GameEngineWrapper::SaveToPath(char* path)
{
	if(m_GameEngine)
		m_GameEngine->SaveToPath(path);
}

void GameEngineWrapper::LoadFromPath(char* path)
{
	if(m_GameEngine)
		m_GameEngine->LoadFromPath(path);
}

void GameEngineWrapper::ResetScene()
{
	if(m_GameEngine)
		m_GameEngine->ResetScene();
}