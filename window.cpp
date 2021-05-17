#include "window.h"
#include <iostream>

namespace stablerCharacter
{
	namespace graphics {
		Window::Window(const char* nTitle, int nWidth, int nHeight)
		{
			title = nTitle;
			width = nWidth;
			height = nHeight;
			if(init())
		}

		Window::~Window()
		{
			glfwTerminate();
		}

		bool Window::init()
		{
			if (!glfwInit())
			{
				std::cout << "GLFW cannot initialize properly.";
				return false;
			}
			else std::cout << "Successfully initialized GLFW.\n";
			window = glfwCreateWindow(width, height, title, NULL, NULL);
			if (!window)
			{
				glfwTerminate();
				std::cout << "Cannot create GLFW window properly.\n";
				return false;
			}
			else std::cout << "Successfully created OpenGL window.\n";
			glfwMakeContextCurrent(window);
			glfwSetWindowSizeCallback(window, windowResize);

			if (glewInit() != GLEW_OK)
			{
				std::cout << "Unable to Initialize GLEW\n";
				return false;
			}
			else std::cout << "Successfully initialized GLEW\n";

			std::cout << "OpenGL Version " << glGetString(GL_VERSION) << std::endl;
			return true;
		}

		bool Window::closed() const
		{
			return glfwWindowShouldClose(window) == 1;
		}

		void Window::clear() const
		{
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		}

		void Window::update()
		{
			glfwPollEvents();
			glfwGetFramebufferSize(window, &width, &height);
			glfwSwapBuffers(window);
		}

		void windowResize(GLFWwindow *window, int width, int height)
		{
			glViewport(0, 0, width, height);
		}
	}
}