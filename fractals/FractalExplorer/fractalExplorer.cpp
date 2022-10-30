#include <SFML/Graphics.hpp>
#include <iostream>
#include <math.h>
#include <complex>

static const int WINDOW_H_INIT = 700;
static const int WINDOW_W_INIT = 1200;
static const char WINDOW_NAME[] = "Fractal Explorer";

int main()
{
    sf::RenderWindow window(sf::VideoMode(WINDOW_W_INIT, WINDOW_H_INIT), "SFML works!");
    sf::CircleShape shape(100.f);
    shape.setFillColor(sf::Color::Green);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(shape);
        window.display();
    }

    return 0;
}