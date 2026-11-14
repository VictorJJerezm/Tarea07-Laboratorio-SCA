'use strict';
const assert = require('node:assert/strict');
const test = require('node:test');
const { totalUnits } = require('../src/app');

test('suma correctamente los elementos', () => {
  assert.equal(totalUnits([{ units: 2 }, { units: 3 }]), 5);
});

test('rechaza cantidades invalidas', () => {
  assert.throws(() => totalUnits([{ units: -1 }]), /enteros no negativos/);
});
