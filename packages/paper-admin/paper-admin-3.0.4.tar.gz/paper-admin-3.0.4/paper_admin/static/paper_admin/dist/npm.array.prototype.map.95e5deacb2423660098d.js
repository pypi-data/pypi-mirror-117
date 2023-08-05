"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.array.prototype.map"],{

/***/ 7453:
/*!************************************************************!*\
  !*** ./node_modules/array.prototype.map/implementation.js ***!
  \************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar ArraySpeciesCreate = __webpack_require__(/*! es-abstract/2020/ArraySpeciesCreate */ 7593);\nvar Call = __webpack_require__(/*! es-abstract/2020/Call */ 1341);\nvar CreateDataPropertyOrThrow = __webpack_require__(/*! es-abstract/2020/CreateDataPropertyOrThrow */ 5797);\nvar Get = __webpack_require__(/*! es-abstract/2020/Get */ 4573);\nvar HasProperty = __webpack_require__(/*! es-abstract/2020/HasProperty */ 5994);\nvar IsCallable = __webpack_require__(/*! es-abstract/2020/IsCallable */ 5233);\nvar ToUint32 = __webpack_require__(/*! es-abstract/2020/ToUint32 */ 1514);\nvar ToObject = __webpack_require__(/*! es-abstract/2020/ToObject */ 2747);\nvar ToString = __webpack_require__(/*! es-abstract/2020/ToString */ 2167);\nvar callBound = __webpack_require__(/*! call-bind/callBound */ 1924);\nvar isString = __webpack_require__(/*! is-string */ 9981);\n\n// Check failure of by-index access of string characters (IE < 9) and failure of `0 in boxedString` (Rhino)\nvar boxedString = Object('a');\nvar splitString = boxedString[0] !== 'a' || !(0 in boxedString);\n\nvar strSplit = callBound('String.prototype.split');\n\nmodule.exports = function map(callbackfn) {\n\tvar O = ToObject(this);\n\tvar self = splitString && isString(O) ? strSplit(O, '') : O;\n\tvar len = ToUint32(self.length);\n\n\t// If no callback function or if callback is not a callable function\n\tif (!IsCallable(callbackfn)) {\n\t\tthrow new TypeError('Array.prototype.map callback must be a function');\n\t}\n\n\tvar T;\n\tif (arguments.length > 1) {\n\t\tT = arguments[1];\n\t}\n\n\tvar A = ArraySpeciesCreate(O, len);\n\tvar k = 0;\n\twhile (k < len) {\n\t\tvar Pk = ToString(k);\n\t\tvar kPresent = HasProperty(O, Pk);\n\t\tif (kPresent) {\n\t\t\tvar kValue = Get(O, Pk);\n\t\t\tvar mappedValue = Call(callbackfn, T, [kValue, k, O]);\n\t\t\tCreateDataPropertyOrThrow(A, Pk, mappedValue);\n\t\t}\n\t\tk += 1;\n\t}\n\n\treturn A;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/array.prototype.map/implementation.js?");

/***/ }),

/***/ 4770:
/*!***************************************************!*\
  !*** ./node_modules/array.prototype.map/index.js ***!
  \***************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar define = __webpack_require__(/*! define-properties */ 4289);\nvar RequireObjectCoercible = __webpack_require__(/*! es-abstract/2020/RequireObjectCoercible */ 6237);\nvar callBound = __webpack_require__(/*! call-bind/callBound */ 1924);\n\nvar implementation = __webpack_require__(/*! ./implementation */ 7453);\nvar getPolyfill = __webpack_require__(/*! ./polyfill */ 7373);\nvar polyfill = getPolyfill();\nvar shim = __webpack_require__(/*! ./shim */ 2717);\n\nvar $slice = callBound('Array.prototype.slice');\n\n// eslint-disable-next-line no-unused-vars\nvar boundMapShim = function map(array, callbackfn) {\n\tRequireObjectCoercible(array);\n\treturn polyfill.apply(array, $slice(arguments, 1));\n};\ndefine(boundMapShim, {\n\tgetPolyfill: getPolyfill,\n\timplementation: implementation,\n\tshim: shim\n});\n\nmodule.exports = boundMapShim;\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/array.prototype.map/index.js?");

/***/ }),

/***/ 7373:
/*!******************************************************!*\
  !*** ./node_modules/array.prototype.map/polyfill.js ***!
  \******************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar arrayMethodBoxesProperly = __webpack_require__(/*! es-array-method-boxes-properly */ 2868);\n\nvar implementation = __webpack_require__(/*! ./implementation */ 7453);\n\nmodule.exports = function getPolyfill() {\n\tvar method = Array.prototype.map;\n\treturn arrayMethodBoxesProperly(method) ? method : implementation;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/array.prototype.map/polyfill.js?");

/***/ }),

/***/ 2717:
/*!**************************************************!*\
  !*** ./node_modules/array.prototype.map/shim.js ***!
  \**************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar define = __webpack_require__(/*! define-properties */ 4289);\nvar getPolyfill = __webpack_require__(/*! ./polyfill */ 7373);\n\nmodule.exports = function shimArrayPrototypeMap() {\n\tvar polyfill = getPolyfill();\n\tdefine(\n\t\tArray.prototype,\n\t\t{ map: polyfill },\n\t\t{ map: function () { return Array.prototype.map !== polyfill; } }\n\t);\n\treturn polyfill;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/array.prototype.map/shim.js?");

/***/ })

}]);