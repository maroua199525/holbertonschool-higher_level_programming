#!/usr/bin/node
function factoriel (n) {
  if (n < 2 && n > 0) {
    return (1);
  } else if (n > 1) {
    return (n * factoriel(n - 1));
  } else {
    return (1);
  }
}
console.log(factoriel(parseInt(process.argv[2])));
