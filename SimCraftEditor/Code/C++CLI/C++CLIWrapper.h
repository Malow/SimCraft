//File C++CLIWrapper.h

/*
* Created by: Ermin Hrkalovic (ERH)
* Email: ermin.hrkalovic@bth.se
*/

#pragma once
#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include "..\stdafx.h"

//forwarddeklarationen måste ligga innan alla "using" !!! annars tolkas
//det av visual studio som att GameEngineWrapper-klassen ligger i ett namespace
#include "..\C++\GameEngineWrapper.h"

using namespace System;
using namespace System::Windows::Interop;
using namespace System::Windows;
using namespace System::Runtime::InteropServices;

namespace System { namespace Windows { namespace Interop
{
	public ref class CppCLI
	{
	protected:
		GameEngineWrapper* m_GameEngine;
	public:
		CppCLI();
		~CppCLI();

		HRESULT Init(IntPtr hWnd, int width, int height);
		HRESULT Shutdown();

		HRESULT ProcessFrame();
		HRESULT OnResize(int width, int height);

		void KeyDown(int key);
		void KeyUp(int key);
		void MouseDown(int button);
		void MouseUp(int button);

		void DeleteUnitClosestToArrow();

		void CreateHuman(bool male, int age);
		void CreateTree(int age, int wood);
		void CreateFoodBush(int food);


		String^ ProcessText(String^ text);
	};
}}}