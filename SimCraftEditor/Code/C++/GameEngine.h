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
private:
	void RenderFunc();
	bool FrameFunc();
public:
	GameEngine();
	~GameEngine();

	HRESULT Init(HWND hWnd, int width, int height);
	HRESULT Shutdown();

	HRESULT ProcessFrame();
	HRESULT OnResize(int width, int height);

	char* ProcessText(char* msg);
};
#endif