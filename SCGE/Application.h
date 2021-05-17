#pragma once

#include "Core.h"

namespace scge {
	class SC_API Application
	{
	public:
		Application();
		virtual ~Application();

		void Run();
	};

	// To be defined in Client
	Application* CreateApplication();
}
