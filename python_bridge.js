'use strict';

let assert = require('assert');
let pythonBridge = require('python-bridge');

let python3 = pythonBridge();

python3.ex`import math`;
python3`math.sqrt(9)`.then((x) => assert.equal(x, 3));

let list = [3, 4, 2, 1];
python3`sorted(${list})`.then((x) => assert.deepEqual(x, list.sort()));

python3.end();
