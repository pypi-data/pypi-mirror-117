"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.es-to-primitive"],{

/***/ 1503:
/*!************************************************!*\
  !*** ./node_modules/es-to-primitive/es2015.js ***!
  \************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar hasSymbols = typeof Symbol === 'function' && typeof Symbol.iterator === 'symbol';\n\nvar isPrimitive = __webpack_require__(/*! ./helpers/isPrimitive */ 4149);\nvar isCallable = __webpack_require__(/*! is-callable */ 5320);\nvar isDate = __webpack_require__(/*! is-date-object */ 8923);\nvar isSymbol = __webpack_require__(/*! is-symbol */ 2636);\n\nvar ordinaryToPrimitive = function OrdinaryToPrimitive(O, hint) {\n\tif (typeof O === 'undefined' || O === null) {\n\t\tthrow new TypeError('Cannot call method on ' + O);\n\t}\n\tif (typeof hint !== 'string' || (hint !== 'number' && hint !== 'string')) {\n\t\tthrow new TypeError('hint must be \"string\" or \"number\"');\n\t}\n\tvar methodNames = hint === 'string' ? ['toString', 'valueOf'] : ['valueOf', 'toString'];\n\tvar method, result, i;\n\tfor (i = 0; i < methodNames.length; ++i) {\n\t\tmethod = O[methodNames[i]];\n\t\tif (isCallable(method)) {\n\t\t\tresult = method.call(O);\n\t\t\tif (isPrimitive(result)) {\n\t\t\t\treturn result;\n\t\t\t}\n\t\t}\n\t}\n\tthrow new TypeError('No default value');\n};\n\nvar GetMethod = function GetMethod(O, P) {\n\tvar func = O[P];\n\tif (func !== null && typeof func !== 'undefined') {\n\t\tif (!isCallable(func)) {\n\t\t\tthrow new TypeError(func + ' returned for property ' + P + ' of object ' + O + ' is not a function');\n\t\t}\n\t\treturn func;\n\t}\n\treturn void 0;\n};\n\n// http://www.ecma-international.org/ecma-262/6.0/#sec-toprimitive\nmodule.exports = function ToPrimitive(input) {\n\tif (isPrimitive(input)) {\n\t\treturn input;\n\t}\n\tvar hint = 'default';\n\tif (arguments.length > 1) {\n\t\tif (arguments[1] === String) {\n\t\t\thint = 'string';\n\t\t} else if (arguments[1] === Number) {\n\t\t\thint = 'number';\n\t\t}\n\t}\n\n\tvar exoticToPrim;\n\tif (hasSymbols) {\n\t\tif (Symbol.toPrimitive) {\n\t\t\texoticToPrim = GetMethod(input, Symbol.toPrimitive);\n\t\t} else if (isSymbol(input)) {\n\t\t\texoticToPrim = Symbol.prototype.valueOf;\n\t\t}\n\t}\n\tif (typeof exoticToPrim !== 'undefined') {\n\t\tvar result = exoticToPrim.call(input, hint);\n\t\tif (isPrimitive(result)) {\n\t\t\treturn result;\n\t\t}\n\t\tthrow new TypeError('unable to convert exotic object to primitive');\n\t}\n\tif (hint === 'default' && (isDate(input) || isSymbol(input))) {\n\t\thint = 'string';\n\t}\n\treturn ordinaryToPrimitive(input, hint === 'default' ? 'number' : hint);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-to-primitive/es2015.js?");

/***/ }),

/***/ 4149:
/*!*************************************************************!*\
  !*** ./node_modules/es-to-primitive/helpers/isPrimitive.js ***!
  \*************************************************************/
/***/ (function(module) {

eval("\n\nmodule.exports = function isPrimitive(value) {\n\treturn value === null || (typeof value !== 'function' && typeof value !== 'object');\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-to-primitive/helpers/isPrimitive.js?");

/***/ })

}]);