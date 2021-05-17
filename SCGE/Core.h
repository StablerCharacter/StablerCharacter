#pragma once

#ifdef SC_PLATFORM_WINDOWS
	#ifdef SC_BUILD_DLL
		#define SC_API __declspec(dllexport)
	#else
		#define SC_API __declspec(dllimport)
	#endif
#else
	#error StablerCharacter only support Windows!
#endif