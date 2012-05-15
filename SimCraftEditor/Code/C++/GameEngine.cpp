//File: GameEngine.h

#include "GameEngine.h"
#include <fstream>

GameEngine::GameEngine()
{
	MaloW::ClearDebug();
	this->eng = NULL;
	this->arrow = NULL;

	this->m_ScreenWidth = 0;
	this->m_ScreenHeight = 0;
}
GameEngine::~GameEngine()
{
	while(this->units.size() > 0)
		delete this->units.getAndRemove(0);
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
	eng->SetSleepInRenderingThread(10);

	gfxeng::eng = eng; // Set the global eng to our engine so that GetGraphicsEngine(); can work.
	eng->GetCamera()->setPosition(D3DXVECTOR3(100, 40, 100));
	eng->CreateSkyBox("Media/skymap.dds");
	Terrain* terrain = this->eng->CreateTerrain(D3DXVECTOR3(0, -1, 0), D3DXVECTOR3(200, 1, 200), "Media/TerrainTexture.png", "", 256);
	Light* light = eng->CreateLight(D3DXVECTOR3(50, 50, 50));
	Light* light2 = eng->CreateLight(D3DXVECTOR3(150, 50, 50));
	Light* light3 = eng->CreateLight(D3DXVECTOR3(50, 50, 150));
	Light* light4 = eng->CreateLight(D3DXVECTOR3(150, 50, 150));
	float inte = 100.0f;
	light->SetIntensity(inte);
	light2->SetIntensity(inte);
	light3->SetIntensity(inte);
	light4->SetIntensity(inte);

	this->arrow = eng->CreateStaticMesh("Media/RedArrow.obj", D3DXVECTOR3(100, 0, 130));

	return S_OK;
}
HRESULT GameEngine::Shutdown()
{
	return S_OK;
}

HRESULT GameEngine::Update()
{
	
	if(this->eng->isRunning())
	{
		float diff = eng->Update();

		// Key inputs
		if(eng->GetKeyListener()->IsPressed('W'))
			eng->GetCamera()->moveForward(diff);
		if(eng->GetKeyListener()->IsPressed('A'))
			eng->GetCamera()->moveLeft(diff);
		if(eng->GetKeyListener()->IsPressed('S'))	
			eng->GetCamera()->moveBackward(diff);
		if(eng->GetKeyListener()->IsPressed('D'))	
			eng->GetCamera()->moveRight(diff);
		if(eng->GetKeyListener()->IsClicked(1))
			eng->GetCamera()->setPosition(eng->GetCamera()->getPosition() - D3DXVECTOR3(0, 0.01f, 0) * diff);
		if(eng->GetKeyListener()->IsClicked(2))
			eng->GetCamera()->setPosition(eng->GetCamera()->getPosition() + D3DXVECTOR3(0, 0.01f, 0) * diff);

		if(eng->GetKeyListener()->IsPressed(VK_UP))
			this->arrow->MoveBy(D3DXVECTOR3(0, 0, diff) * 0.03f);
		if(eng->GetKeyListener()->IsPressed(VK_LEFT))
			this->arrow->MoveBy(D3DXVECTOR3(-diff, 0, 0) * 0.03f);
		if(eng->GetKeyListener()->IsPressed(VK_DOWN))
			this->arrow->MoveBy(D3DXVECTOR3(0, 0, -diff) * 0.03f);
		if(eng->GetKeyListener()->IsPressed(VK_RIGHT))
			this->arrow->MoveBy(D3DXVECTOR3(diff, 0, 0) * 0.03f);
	}
	
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

char* GameEngine::ProcessText(char* msg)
{
	return msg;
}

float GetDistance(D3DXVECTOR3 a, D3DXVECTOR3 b)
{
	D3DXVECTOR3 c = a - b;
	return D3DXVec3Length(&c);
}

void GameEngine::DeleteUnitClosestToArrow()
{
	Unit* closest = NULL;
	float distance = 100.0f;	// Max range for delete
	int slot = 0;
	for(int i = 0; i < this->units.size(); i++)
	{
		if(float dist = GetDistance(this->arrow->GetPosition(), this->units.get(i)->mesh->GetPosition()) < distance)
		{
			closest = this->units.get(i);
			distance = dist;
			slot = i;
		}
	}

	if(closest)
	{
		this->eng->DeleteStaticMesh(this->units.getAndRemove(slot)->mesh);
		delete closest;
	}
}

void GameEngine::CreateHuman(bool male, int age)
{
	Unit* unit = new Unit();
	unit->type = HUMAN;
	unit->male = male;
	unit->mesh = this->eng->CreateStaticMesh("Media/Human.obj", this->arrow->GetPosition());
	unit->age = age;
	unit->resources = 0;
	this->units.add(unit);
}

void GameEngine::CreateTree(int age, int wood)
{
	Unit* unit = new Unit();
	unit->type = TREE;
	unit->mesh = this->eng->CreateStaticMesh("Media/Tree.obj", this->arrow->GetPosition());
	unit->age = age;
	unit->resources = wood;
	this->units.add(unit);
}

void GameEngine::CreateFoodBush(int food)
{
	Unit* unit = new Unit();
	unit->type = FOOD_BUSH;
	unit->mesh = this->eng->CreateStaticMesh("Media/FoodBush.obj", this->arrow->GetPosition());
	unit->age = 0;
	unit->resources = food;
	this->units.add(unit);
}

void GameEngine::SaveToPath(char* path)
{
	ofstream out;
	out.open(path);

	out << this->units.size() << endl;
	out << endl;

	for(int i = 0; i < this->units.size(); i++)
	{
		Unit* unit = this->units.get(i);
		if(unit->type == HUMAN)
		{
			out << "Human" << endl;
			out << unit->male << endl;
			out << unit->age << endl;
			
		}
		else if(unit->type == TREE)
		{
			out << "Tree" << endl;
			out << unit->age << endl;
			out << unit->resources << endl;
		}
		else if(unit->type == FOOD_BUSH)
		{
			out << "Food Bush" << endl;
			out << unit->resources << endl;
		}

		out << unit->mesh->GetPosition().x << endl;
		out << unit->mesh->GetPosition().y << endl;
		out << unit->mesh->GetPosition().z << endl;

		out << endl;
	}

	out.close();
}

void GameEngine::LoadFromPath(char* path)
{
	this->ResetScene();

	ifstream in;
	in.open(path);
	int nrOfUnits = 0;
	string line = "";

	getline(in, line);
	nrOfUnits = atoi(line.c_str());

	getline(in, line);

	for(int i = 0; i < nrOfUnits; i++)
	{
		getline(in, line);
		if(line == "Human")
		{
			getline(in, line);
			bool male = atoi(line.c_str());
			getline(in, line);
			int age = atoi(line.c_str());

			getline(in, line);
			float x = atof(line.c_str());
			getline(in, line);
			float y = atof(line.c_str());
			getline(in, line);
			float z = atof(line.c_str());
			this->arrow->SetPosition(D3DXVECTOR3(x, y, z));

			this->CreateHuman(male, age);
		}
		else if(line == "Tree")
		{
			getline(in, line);
			int age = atoi(line.c_str());
			getline(in, line);
			int wood = atoi(line.c_str());

			getline(in, line);
			float x = atof(line.c_str());
			getline(in, line);
			float y = atof(line.c_str());
			getline(in, line);
			float z = atof(line.c_str());
			this->arrow->SetPosition(D3DXVECTOR3(x, y, z));

			this->CreateTree(age, wood);
		}
		else if(line == "Food Bush")
		{
			getline(in, line);
			int food = atoi(line.c_str());

			getline(in, line);
			float x = atof(line.c_str());
			getline(in, line);
			float y = atof(line.c_str());
			getline(in, line);
			float z = atof(line.c_str());
			this->arrow->SetPosition(D3DXVECTOR3(x, y, z));

			this->CreateFoodBush(food);
		}

		getline(in, line);
	}

	in.close();


	this->arrow->SetPosition(D3DXVECTOR3(100, 0, 130));
}

void GameEngine::ResetScene()
{
	eng->GetCamera()->setPosition(D3DXVECTOR3(100, 40, 100));
	this->arrow->SetPosition(D3DXVECTOR3(100, 0, 130));

	while(this->units.size() > 0)
	{
		this->eng->DeleteStaticMesh(this->units.get(0)->mesh);
		delete this->units.getAndRemove(0);
	}
}