#include <SFML/Graphics.hpp>
#include <iostream>
#include <math.h>
#include <complex>
#include <functional>

// Constants
static const int WINDOW_H_INIT = 720;
static const int WINDOW_W_INIT = 1280;
static const char WINDOW_NAME[] = "Fractal Explorer";


static double camZoom = 280.0;
static double xOffset = -2.5;
static double yOffset = -1.25;
static int currFractal = 0;


sf::Color palette[255];

/* Translates window position to actual position */
double getXPos(double x) {
    return x / camZoom + xOffset;
}

double getYPos(double y) {
    return y / camZoom + yOffset;
}
/************************************************/

/* Fractals */
void mandelbrot(std::complex<double>& z, std::complex<double> c) {
    // z = z^2 + c

    //std::cout << z.real() << " + " << z.imag() << "i" << std::endl;
    z = z*z + c;
    //std::cout << z.real() << " + " << z.imag() << "i" << std::endl;

}

void burningShip(std::complex<double>& z, std::complex<double> c) {
    // z_n+1 = (abs(Re(z_n)) + i * abs(Im(z_n))^2 + c
    // Re(z_n+1) = Re(z_n)^2 - Im(z)^2 + Re(c)
    // Im(z_n+1) = abs(2 * Re(z) * Im(z)) + Im(c)
    std::complex<double> new_z(z.real() * z.real() - z.imag() * z.imag() + c.real(), std::abs(2 * z.real() * z.imag()) + c.imag());

    //std::cout << z.real() << " + " << z.imag() << "i" << std::endl;
    z = new_z;
    //std::cout << z.real() << " + " << z.imag() << "i" << std::endl;
}
/***********/

std::function<void(std::complex<double>&, std::complex<double>)> fractals[2] = {&mandelbrot, &burningShip};

sf::VertexArray drawSet(int maxIter, double escapeRadius) {
    sf::VertexArray plot;

    for (int px = 0; px < WINDOW_W_INIT; px++) {
        for (int py = 0; py < WINDOW_H_INIT; py++) {
            std::complex<double> z(getXPos(px), getYPos(py));
            std::complex<double>c = z;
            int i = 0; 

            while (std::norm(z) <= escapeRadius && i < maxIter) {

                fractals[currFractal](z, c);
                i++;
            }
            sf::Color color = palette[i];

            sf::Vertex point(sf::Vector2f(px, py), color);
            plot.append(point);
        }

    }
    return plot;
    
}

void updateFractal(sf::VertexArray& fractalVertexArray) 

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    sf::RenderWindow window(sf::VideoMode(WINDOW_W_INIT, WINDOW_H_INIT), WINDOW_NAME);
    
    for (int i = 0; i < 255; i++) {
        palette[i] = sf::Color(i*30, i*10, i*15, 255);
    }
    
    int x;
    std::cout << "Pick 1 for the mandelbrot set, and 2 for the burning ship fractal" << std::endl;
    std::cin >> x;
    currFractal = x-1;
    sf::VertexArray set_points = drawSet(255, 4.0);

    while (window.isOpen())
    {
        //std::cout << cam_zoom << std::endl;
        sf::Event event;
        double zoom = 1;
        while (window.pollEvent(event))
        {
            switch (event.type) {
            case sf::Event::Closed:
                window.close();
                break;

            case sf::Event::MouseWheelScrolled:

                if (event.mouseWheelScroll.delta <= -1) {
                    zoom += 0.1;
                    cam_zoom += 100;
                }
                else if (event.mouseWheelScroll.delta >= 1) {
                    zoom -= 0.1;
                    cam_zoom += 100;
                }
                set_points = draw_set(255, 4.0);
                break;

            case sf::Event::KeyPressed:
                if (event.key.code == sf::Keyboard::Left) {
                    x_offset -= 1;
                } else if (event.key.code == sf::Keyboard::Right) {
                    x_offset += 1;
                }
                else if (event.key.code == sf::Keyboard::Up) {
                    y_offset -= 1;
                }
                else if (event.key.code == sf::Keyboard::Down) {
                    y_offset += 1;
                }
                else if (event.key.code == sf::Keyboard::Num1) {
                    current_fractal = 0;
                }
                else if (event.key.code == sf::Keyboard::Num2) {
                    current_fractal = 1;
                }

                set_points = draw_set(255, 4.0);
                break;
            }
        }

        window.clear();
        window.draw(set_points);
        window.display();
    }

    return 0;
}