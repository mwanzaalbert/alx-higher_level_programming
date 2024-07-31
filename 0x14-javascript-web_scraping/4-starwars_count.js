#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(characterId)) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
