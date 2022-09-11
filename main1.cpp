#include <iostream>
#include <string>

class Animal{
    public:
    Animal(){
        std::cout << "Animal class here!" << std::endl;
    }
    Animal(std::string name) : name(name) {
        std::cout << "Animal class here = " <<  name << std::endl;
    }
    std::string getName(){
        return this->name;
    }
    private:
    std::string name;
};

class Cat : public Animal{
    public:
    Cat(){
        std::cout << "Cat class here!" << std::endl;
    }
    Cat(std::string name){
        std::cout << "Cat class here = " << name << std::endl;
    }
};

int main(){
    Cat cat;
    Animal animal("some animal");
    std::cout << animal.getName() << std::endl;;
}