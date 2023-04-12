#include <iostream>

class HelloClass {
    public:
        void show_hello();
        int add_numbers(
            int x,
            int y
        );
        int add_numbers(
            int x, 
            int y,
            int z
        );
};

int HelloClass::add_numbers(int x, int y) {
    std::cout << "Func1  called" << std::endl;
    return x + y;
}

int HelloClass::add_numbers(int x, int y, int z) {
    std::cout << "Func2 called" << std::endl;
    return x + y + z;
}

void HelloClass::show_hello() {
    std::cout << "Hello from class!" << std::endl;
    return;
}

int main() {
    HelloClass *hello_instance = new HelloClass();
    hello_instance->show_hello();
    int resp1 = hello_instance->add_numbers(1, 2, 3);
    int resp2 = hello_instance->add_numbers(1, 3);
    std::cout << "Output : " << resp1 << ", " << resp2 << std::endl;
    return 0;
}