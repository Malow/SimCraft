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

}}}