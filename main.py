
from entity.superHero import superHero

if __name__ == '__main__':
    # The client code.
    s1 = superHero()
    s2 = superHero()

    if id(s1) == id(s2):
        print(f'Singleton works, both variables contain the same superhero "{s1.name}".')
    else:
        print(f'Singleton failed, variables contain different superheroes, only one "{s1.name}" can exist.')


