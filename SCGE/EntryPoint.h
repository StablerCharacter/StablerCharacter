#pragma once

#ifdef SC_PLATFORM_WINDOWS

extern scge::Application* scge::CreateApplication();

int main(int argc, char** argv)
{
	std::cout << "StablerCharacter Beta 1.0.0\n";
	scge::Log::Init();
	SC_CORE_INFO("Log Initialized!");

	auto app = scge::CreateApplication();
	app->Run();
	delete app;

	return 0;
}

#endif