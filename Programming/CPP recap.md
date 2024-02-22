automatic storage 
bit fields

## Threading
std::memory_order
std::atomic
std::mutex
semaphore
coroutine

## Value Categories
glvalue

## Keywords
good keywords list - [here](https://en.cppreference.com/w/cpp/keyword)

**Volatile** -- hint to compiler to not optimize away
**mutable** --- pierce the const viel you drape over objects 
**explicit** --- make constructions of object explicit without implicit conversions that compiler can support

**asm** -- inline assembly block
**export**
**consteval vs constexpr** -- both are evaluated at compiletime but consteval **should** return a returntype
**consteval if** --- let's us call consteval functions from constexpr (because constexpr can run both at compile time or runtime based on the data)
**constinit** - avoids static initialization problem

## Casting
dynamic_cast


## Templates
concept


## Unknown
lambdas 
lambdas with templates
lambda declarators


## Coroutines
co_return
co_yield
co_await 

## Modules

https://blog.feabhas.com/2021/08/c20-modules-with-gcc11/

## Ranges and Views
https://hannes.hauswedell.net/post/2019/11/30/range_intro/


## Concepts
requires --- list of nested requirements on the type

## Info 
Static initialization problem - if two static objects are dependent on one another [here](https://isocpp.org/wiki/faq/ctors#static-init-order)

std::invoke