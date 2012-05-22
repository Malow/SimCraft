//File: GameEngine.h

/*
* Created by: Ermin Hrkalovic (ERH)
* Email: ermin.hrkalovic@bth.se
*/

#ifndef __GAMEENGINE_H__
#define __GAMEENGINE_H__

#include "stdafx.h"

#include "GraphicsEngine.h"

#define MaxWood 5000.0f
#define MaxFood 1000.0f

enum UNIT_TYPE
{
	HUMAN = 0,
	TREE = 1, 
	FOOD_BUSH = 2,
	WOLF = 3
};

struct Unit
{
	StaticMesh* mesh;
	UNIT_TYPE type;
	bool male;
	int age;
	int resources;
};

class GameEngine
{
private:
	MaloW::Array<Unit*> units;
	GraphicsEngine* eng;
	StaticMesh* arrow;

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

	void DeleteUnitClosestToArrow();

	void CreateHuman(bool male, int age);
	void CreateWolf(bool male, int age);
	void CreateTree(int age, int wood);
	void CreateFoodBush(int food);

	void SaveToPath(char* path);
	void LoadFromPath(char* path);
	void ResetScene();

	char* ProcessText(char* msg);
};
#endif