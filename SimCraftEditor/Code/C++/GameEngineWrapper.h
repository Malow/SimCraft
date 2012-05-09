//File: GameEngineWrapper.h

/*
* Created by: Ermin Hrkalovic (ERH)
* Email: ermin.hrkalovic@bth.se
*/

#ifndef __GAMEENGINEWRAPPER_H__
#define __GAMEENGINEWRAPPER_H__

#include "..\stdafx.h"
class GameEngine;


class DLL_USAGE GameEngineWrapper
{
private:
	GameEngine* m_GameEngine;
public:
	GameEngineWrapper();
	~GameEngineWrapper();

	HRESULT Init(HWND hWnd, int width, int height);
	HRESULT Shutdown();

	HRESULT ProcessFrame();
	HRESULT OnResize(int width, int height);

	void KeyDown(char key);
	void KeyUp(char key);
	void MouseDown(int button);
	void MouseUp(int button);

	char* ProcessText(char* msg);
};

#endif