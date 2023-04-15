#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
  sf::Window window(sf::VideoMode(800, 600), "My Window");

  while(window.isOpen()) {
    sf::Event event;
    while(window.pollEvent(event)) {
      switch(event.type) {
        case sf::Event::Closed:
          window.close();
          break;
        case sf::Event::KeyPressed:
          std::cout << "The key has been pressed!";
          break;
        default:
          break;
        }
    }
  }
}
