#include <SCGE.h>

class Sandbox : public scge::Application
{
public:
	Sandbox()
	{

	}

	~Sandbox()
	{

	}
};

scge::Application* scge::CreateApplication()
{
	return new Sandbox();
}