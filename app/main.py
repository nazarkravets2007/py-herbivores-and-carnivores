class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def _die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Herbivore):
            return

        if animal.hidden:
            return

        animal.health -= 50
        if animal.health <= 0:
            animal.health = 0
            animal._die()


# ===== Example usage =====
if __name__ == "__main__":
    Animal.alive.clear()

    lion = Carnivore("Simba")
    assert len(Animal.alive) == 1
    assert isinstance(Animal.alive[0], Carnivore)

    rabbit = Herbivore("Susan")
    rabbit.hide()
    assert rabbit.hidden is True

    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 50

    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 50

    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 0
    assert rabbit not in Animal.alive

    Animal.alive.clear()
    pantera = Carnivore("Bagira")
    snake = Carnivore("Kaa")
    print(Animal.alive)
    # [{Name: Bagira, Health: 100, Hidden: False}, {Name: Kaa, Health: 100, Hidden: False}]
