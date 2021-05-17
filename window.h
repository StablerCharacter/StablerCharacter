#pragma once

#include <GLFW/glfw3.h>

namespace stablerCharacter
{
	namespace graphics {
		class Window
		{
		private:
			const char* title;
			int width, height;
			GLFWwindow* window;
			bool closed;
		public:
			Window(const char *nTitle, int nWidth, int nHeight);
			~Window();
			bool closed() const;
			void clear() const;
			void update();

			inline int getWidth() const { return width; }
			inline int getHeight() const { return height; }
		private:
			bool init();
		};
	}
}