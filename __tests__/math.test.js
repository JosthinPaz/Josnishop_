const suma = require('./math.js'); // <-- Se cambia la ruta

test('la función suma 1 + 2 y el resultado es 3', function() {
  expect(suma(1, 2)).toBe(3);
});