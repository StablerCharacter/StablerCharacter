#pragma once

#include <memory>
#include "Core.h"

#pragma warning(push, 0)
#include <spdlog/spdlog.h>
#include <spdlog/fmt/ostr.h>
#pragma warning(pop)

namespace scge
{
	class SC_API Log
	{
	public:
		static void Init();

		static std::shared_ptr<spdlog::logger>& GetCoreLogger() { return s_CoreLogger; }
		static std::shared_ptr<spdlog::logger>& GetClientLogger() { return s_ClientLogger; }
	private:
		static std::shared_ptr<spdlog::logger> s_CoreLogger;
		static std::shared_ptr<spdlog::logger> s_ClientLogger;
	};
}

//Core log macros
#define SC_CORE_ERROR(...) 	::scge::Log::GetCoreLogger()->error(__VA_ARGS__)
#define SC_CORE_WARN(...) 	::scge::Log::GetCoreLogger()->warn(__VA_ARGS__)
#define SC_CORE_INFO(...) 	::scge::Log::GetCoreLogger()->info(__VA_ARGS__)
#define SC_CORE_TRACE(...) 	::scge::Log::GetCoreLogger()->trace(__VA_ARGS__)
#define SC_CORE_CRITICAL(...) 	::scge::Log::GetCoreLogger()->critical(__VA_ARGS__)

//Client log macros
#define SC_ERROR(...) 	::scge::Log::GetClientLogger()->error(__VA_ARGS__)
#define SC_WARN(...) 	::scge::Log::GetClientLogger()->warn(__VA_ARGS__)
#define SC_INFO(...) 	::scge::Log::GetClientLogger()->info(__VA_ARGS__)
#define SC_TRACE(...) 	::scge::Log::GetClientLogger()->trace(__VA_ARGS__)
#define SC_CRITICAL(...) 	::scge::Log::GetClientLogger()->critical(__VA_ARGS__)