typedef struct {
    // User defined data may be declared here.
    int lock;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    
    // Initialize user defined data here.
    obj->lock = 1;
    return obj;
}

void first(Foo* obj) {
    
    while (obj->lock != 1) {}
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    obj->lock++;
}

void second(Foo* obj) {
    
    while (obj->lock != 2) {}
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    obj->lock++;
}

void third(Foo* obj) {
    
    while (obj->lock != 3) {}
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
    obj->lock++;
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    
}