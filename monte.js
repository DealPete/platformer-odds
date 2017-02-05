const TRIALS = 1000000;

const a = { attack: 3,
						defense: 5,
						health: 50,
						ability: ""
					};

const b = { attack: 3,
						defense: 5,
						health: 100,
						ability: ""
					};

let aWins = 0,
		bWins = 0,
		both_alive = true;

function rolld6(n) {
	dice = [];
	for (let i = 0; i < n; i++)
		dice.push(Math.floor(Math.random() * 6) + 1);
	return dice;
}

function attack(attacker, defender) {
	let hits = 0;
	let numDice = attacker.attack;
	if (attacker.ability == "Link" && attacker.health == attacker.hp)
		numDice += 2;
	let dice = rolld6(numDice);
	dice.map( die => {
		if (die > defender.defense)
			hits += 1;
	});
	return hits;
}

for (let i = 0; i < TRIALS; i++) {
	a.hp = a.health;
	b.hp = b.health;
	both_alive = true;

	while (both_alive) {
		b.hp -= attack(a, b);
		if (b.hp <= 0) {
			both_alive = false;
			aWins += 1;
		} else {
			a.hp -= attack(b, a);
			if (a.hp <= 0) {
				both_alive = false;
				bWins += 1;
			}
		}
	}
}
		
console.log("Link wins", aWins, "fights.\n");
console.log("Mutant wins", bWins, "fights.\n");

