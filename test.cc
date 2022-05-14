#include "monster_generated.h"
#include "monster_data.h"
#include <iostream>


using namespace MyGame::Sample; // Specified in the schema.

int main(int argc, char* argv[]){
  
    auto monster = GetMonster(g_monster_data);
  
    auto hp = monster->hp();
    auto mana = monster->mana();
    auto name = monster->name()->c_str();
    
    std::cout << "name: " << name << "\n";
    std::cout << "hp:  " << hp << "\n";

    return 0;
}

