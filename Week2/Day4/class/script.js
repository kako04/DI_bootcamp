const colors = ['blue', 'lightgreen', 'green', 'yellow']

for (let i = 0; i  < colors.length; i++) {
    console.log('||||||||||')
    for (let j = 0; j < colors[i].length; j++) {
        const letter = colors[i][j];
        console.log(letter);
    }
    console.log('||||||||||')
}