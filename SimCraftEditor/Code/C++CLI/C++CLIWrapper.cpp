//File: C++CLIWrapper.cpp

#include "C++CLIWrapper.h"
#include <sstream>

namespace System { namespace Windows { namespace Interop
{
	CppCLI::CppCLI()
	{
		//myInitMemoryCheck();
		m_GameEngine = new GameEngineWrapper();
	}

	CppCLI::~CppCLI()
	{
		SAFE_DELETE(m_GameEngine);
		//DumpMemoryLeaks();
	}

	HRESULT CppCLI::Init(IntPtr hWnd, int width, int height)
	{
		HWND hwnd = (HWND)(void*)hWnd;
		return m_GameEngine->Init(hwnd, width, height);

		return S_OK;
	}

	HRESULT CppCLI::Shutdown()
	{
		SAFE_DELETE(m_GameEngine);

		return S_OK;
	}

	HRESULT CppCLI::ProcessFrame()
	{
		return m_GameEngine->ProcessFrame();
	}

	HRESULT CppCLI::OnResize(int width, int height)
	{
		return m_GameEngine->OnResize(width, height);
	}

	String^ CppCLI::ProcessText(String^ msg)
	{
		char* lpText = nullptr;
		String^ returnText;

		//Konvertera String^ -> char*
		try
		{
			lpText = (char*)Marshal::StringToHGlobalAnsi(msg).ToPointer();

			returnText = gcnew String(m_GameEngine->ProcessText(lpText));
		}
		finally
		{
			Marshal::FreeHGlobal((IntPtr) const_cast<char*>(lpText)); // Free memory
		}

		return returnText;
	}

	void CppCLI::KeyDown(int key) 
	{ 
		if(m_GameEngine)
			m_GameEngine->KeyDown(key); 
	}
	void CppCLI::KeyUp(int key) 
	{ 
		if(m_GameEngine)
			m_GameEngine->KeyUp(key); 
	}
	void CppCLI::MouseDown(int button) 
	{ 
		if(m_GameEngine)
			m_GameEngine->MouseDown(button); 
	}
	void CppCLI::MouseUp(int button) 
	{ 
		if(m_GameEngine)
			m_GameEngine->MouseUp(button); 
	}

	void CppCLI::DeleteUnitClosestToArrow()
	{
		if(m_GameEngine)
			m_GameEngine->DeleteUnitClosestToArrow(); 
	}

	void CppCLI::CreateHuman(bool male, int age)
	{
		if(m_GameEngine)
			m_GameEngine->CreateHuman(male, age);
	}
	void CppCLI::CreateWolf(bool male, int age)
	{
		if(m_GameEngine)
			m_GameEngine->CreateWolf(male, age);
	}
	void CppCLI::CreateTree(int age, int wood)
	{
		if(m_GameEngine)
			m_GameEngine->CreateTree(age, wood);
	}
	void CppCLI::CreateFoodBush(int food)
	{
		if(m_GameEngine)
			m_GameEngine->CreateFoodBush(food);
	}

	void CppCLI::SaveToPath(String^ path)
	{
		if(m_GameEngine)
		{
			char* lpText = nullptr;

			//Konvertera String^ -> char*
			try
			{
				lpText = (char*)Marshal::StringToHGlobalAnsi(path).ToPointer();
				m_GameEngine->SaveToPath(lpText);
			}
			finally
			{
				Marshal::FreeHGlobal((IntPtr) const_cast<char*>(lpText)); // Free memory
			}

		}
	}

	void CppCLI::LoadFromPath(String^ path)
	{
		if(m_GameEngine)
		{
			char* lpText = nullptr;

			//Konvertera String^ -> char*
			try
			{
				lpText = (char*)Marshal::StringToHGlobalAnsi(path).ToPointer();
				m_GameEngine->LoadFromPath(lpText);
			}
			finally
			{
				Marshal::FreeHGlobal((IntPtr) const_cast<char*>(lpText)); // Free memory
			}

		}
	}

	void CppCLI::ResetScene()
	{
		if(m_GameEngine)
			m_GameEngine->ResetScene();
	}

}}}