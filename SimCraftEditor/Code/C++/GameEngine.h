//File: GameEngine.h

/*
* Created by: Ermin Hrkalovic (ERH)
* Email: ermin.hrkalovic@bth.se
*/

#ifndef __GAMEENGINE_H__
#define __GAMEENGINE_H__

#include "stdafx.h"

#include "GraphicsEngine.h"

class GameEngine
{
private:
	GraphicsEngine* eng;

	int m_ScreenWidth;
	int m_ScreenHeight;

public:
	GameEngine();
	~GameEngine();

	HRESULT Init(HWND hWnd, int width, int height);
	HRESULT Shutdown();

	HRESULT Update();
	HRESULT OnResize(int width, int height);

	GraphicsEngine* GetEngine() { return this->eng; }

	char* ProcessText(char* msg);
};
#endif