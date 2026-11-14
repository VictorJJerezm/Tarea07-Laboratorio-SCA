'use strict';
const _ = require('lodash');

/**
 * Ejercicio académico: procesa únicamente datos internos, sin servicios expuestos.
 * El escenario inicial contiene una versión vulnerable de lodash.
 */
function totalUnits(items) {
  if (!Array.isArray(items)) throw new TypeError('Se requiere un arreglo');
  for (const item of items) {
    if (!item || !Number.isSafeInteger(item.units) || item.units < 0) {
      throw new TypeError('Las unidades deben ser enteros no negativos');
    }
  }
  return _.sumBy(items, 'units');
}

if (require.main === module) {
  console.log('Unidades disponibles:', totalUnits([{ units: 2 }, { units: 3 }]));
}

module.exports = { totalUnits };
