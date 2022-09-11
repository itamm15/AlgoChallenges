#include <iostream>
#include <string>
#include <cmath>

class Rectangle{
    int width, height;
    public: 
    void set_values(int, int);
    int area(){
        return width*height;
    };
};

void Rectangle::set_values(int x, int y){
    width = x;
    height = y;
}

class Square{
    int width, height;
    public: 
        Square(int, int);
        int area(){
            return width*height;
        }
};

Square::Square(int _width, int _height){
    width = _width;
    height = _height;
}

class Triangle{
    public:
    int width, height;
    Triangle(int x){
        this->height = x;
    }
    Triangle(int x, int y) : width(x), height(y) {}
    int area(){
        return width*height/2;
    }
    int permiter();
    ~Triangle(){
        std::cout << "~Triangle instances have been deleted" << std::endl;
    }
};

int Triangle::permiter(){
    return width + 2*sqrt(width*width + height*height);
}

class Point{
    public: 
    //Points in 2-dimensional space
    int x, y;
    Point(){};
    Point(int x, int y){
        this->x = x;
        this->y = y;
    }
    Point operator+(Point &obj){
        Point result;
        result.x = x + obj.x;
        result.y = y + obj.y;
        return result; 
    }

};

class Animal{
    public:
        void publicFunction(){
            std::cout << "Let's assume I am dog!" << std::endl;
        }
    protected:
        void protectedFunction(){
            std::cout << "Let's assume I am cat!" << std::endl;
        }
    private:
        void privateFunction(){
            std::cout << "Let's assume I am lion!" << std::endl;
        }

};
  
class Cat : public Animal{
    public:
    void useFunction(){
        publicFunction();
        protectedFunction();
        privateFunction();
    }
};

struct plane{
    std::string name;
    int maxVelocity;
};
int main(){
    plane Firstplane = {"F35", 2600};
    std::cout << Firstplane.name << std::endl;

    //Rectangle

    Rectangle rect;
    rect.set_values(3,4);

    std::cout << "area: " << rect.area() << std::endl;

    //Square

    Square square(3,5);
    std::cout << "area: " << square.area() << std::endl;

    //Square pointers

    Square *sqr = new Square(5,7);
    std::cout << "sqr: " << sqr << "\n&sqr: " << &sqr << std::endl; 
    std::cout << "sqr area: " << sqr->area() << std::endl;
    sqr = &square;
    std::cout << "sqr: " << sqr << "\n&sqr: " << &sqr << std::endl; 
    std::cout << "sqr area: " << sqr->area() << std::endl;

    //Triangle pointers

    Triangle *triangle = new Triangle(3,4);
    std::cout << "Triangle area: " << triangle->area() << std::endl;

    Triangle *triangleArr;
    triangleArr = new Triangle[2] { {1,2}, {6,8}};


    std::cout << "area: " << triangleArr[0].area() << std::endl;
    std::cout << "area: " << triangleArr[1].area() << std::endl;
    std::cout << "Permiter: " << triangleArr[0].permiter() << std::endl;
    std::cout << "Permiter: " << triangleArr[1].permiter() << std::endl;
    std::cout << "before delete: " << triangleArr[0].width << std::endl;

    // delete triangleArr;

    std::cout << "after delete: " << triangleArr[0].width << std::endl;

    std::cout << "reference: " << &triangleArr[0].width << std::endl;

    triangleArr->~Triangle();

    // Points in space

    Point x(2,5);
    Point y(3,6);

    std::cout << "x.x: " << x.x << ", x.y: " << x.y  << std::endl;
    std::cout << "y.x: " << y.x << ", y.y: " << y.y << std::endl;   

    Point z = x + y;

    std::cout << "z.x: " << z.x << ", z.y: " << z.y << std::endl;

    // ---------------- ANIMAL --------------

    Cat cat;
    cat.useFunction();

    Animal a;
    a.publicFunction();

}