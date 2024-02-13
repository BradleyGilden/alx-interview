#!/usr/bin/node
const request = require('request');

/**
 * Write a script that prints all characters of a Star Wars movie using
 * Star Wars API
 * Author: Bradley Dillion Gilden
 * Date: 13-02-2024
 */

const index = Number(process.argv[2]);
const queryStr = `https://swapi-api.alx-tools.com/api/films/${index}/`;

request(queryStr, function (error, response, body) {
  if (response.statusCode < 400 && !error) {
    const res = JSON.parse(body);
    const characters = res.characters;
    const printRoles = (idx) => {
      if (idx < characters.length) {
        request(characters[idx], function (error, response, body) {
          if (response.statusCode < 400 && !error) {
            const character = JSON.parse(body);
            console.log(character.name);
            printRoles(idx + 1);
          }
        });
      }
    };
    printRoles(0);
  }
});
