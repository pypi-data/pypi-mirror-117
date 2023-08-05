"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.promise.allsettled"],{

/***/ 138:
/*!***********************************************************!*\
  !*** ./node_modules/promise.allsettled/implementation.js ***!
  \***********************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar requirePromise = __webpack_require__(/*! ./requirePromise */ 8118);\n\nrequirePromise();\n\nvar PromiseResolve = __webpack_require__(/*! es-abstract/2020/PromiseResolve */ 2407);\nvar Type = __webpack_require__(/*! es-abstract/2020/Type */ 1501);\nvar iterate = __webpack_require__(/*! iterate-value */ 8330);\nvar map = __webpack_require__(/*! array.prototype.map */ 4770);\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\nvar callBind = __webpack_require__(/*! call-bind */ 5559);\n\nvar all = callBind(GetIntrinsic('%Promise.all%'));\nvar reject = callBind(GetIntrinsic('%Promise.reject%'));\n\nmodule.exports = function allSettled(iterable) {\n\tvar C = this;\n\tif (Type(C) !== 'Object') {\n\t\tthrow new TypeError('`this` value must be an object');\n\t}\n\tvar values = iterate(iterable);\n\treturn all(C, map(values, function (item) {\n\t\tvar onFulfill = function (value) {\n\t\t\treturn { status: 'fulfilled', value: value };\n\t\t};\n\t\tvar onReject = function (reason) {\n\t\t\treturn { status: 'rejected', reason: reason };\n\t\t};\n\t\tvar itemPromise = PromiseResolve(C, item);\n\t\ttry {\n\t\t\treturn itemPromise.then(onFulfill, onReject);\n\t\t} catch (e) {\n\t\t\treturn reject(C, e);\n\t\t}\n\t}));\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/promise.allsettled/implementation.js?");

/***/ }),

/***/ 9392:
/*!**************************************************!*\
  !*** ./node_modules/promise.allsettled/index.js ***!
  \**************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar callBind = __webpack_require__(/*! call-bind */ 5559);\nvar define = __webpack_require__(/*! define-properties */ 4289);\n\nvar requirePromise = __webpack_require__(/*! ./requirePromise */ 8118);\nvar implementation = __webpack_require__(/*! ./implementation */ 138);\nvar getPolyfill = __webpack_require__(/*! ./polyfill */ 2295);\nvar shim = __webpack_require__(/*! ./shim */ 1105);\n\nrequirePromise();\nvar bound = callBind(getPolyfill());\n\nvar rebindable = function allSettled(iterable) {\n\t// eslint-disable-next-line no-invalid-this\n\treturn bound(typeof this === 'undefined' ? Promise : this, iterable);\n};\n\ndefine(rebindable, {\n\tgetPolyfill: getPolyfill,\n\timplementation: implementation,\n\tshim: shim\n});\n\nmodule.exports = rebindable;\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/promise.allsettled/index.js?");

/***/ }),

/***/ 2295:
/*!*****************************************************!*\
  !*** ./node_modules/promise.allsettled/polyfill.js ***!
  \*****************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar requirePromise = __webpack_require__(/*! ./requirePromise */ 8118);\n\nvar implementation = __webpack_require__(/*! ./implementation */ 138);\n\nmodule.exports = function getPolyfill() {\n\trequirePromise();\n\treturn typeof Promise.allSettled === 'function' ? Promise.allSettled : implementation;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/promise.allsettled/polyfill.js?");

/***/ }),

/***/ 8118:
/*!***********************************************************!*\
  !*** ./node_modules/promise.allsettled/requirePromise.js ***!
  \***********************************************************/
/***/ (function(module) {

eval("\n\nmodule.exports = function requirePromise() {\n\tif (typeof Promise !== 'function') {\n\t\tthrow new TypeError('`Promise.allSettled` requires a global `Promise` be available.');\n\t}\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/promise.allsettled/requirePromise.js?");

/***/ }),

/***/ 1105:
/*!*************************************************!*\
  !*** ./node_modules/promise.allsettled/shim.js ***!
  \*************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar requirePromise = __webpack_require__(/*! ./requirePromise */ 8118);\n\nvar getPolyfill = __webpack_require__(/*! ./polyfill */ 2295);\nvar define = __webpack_require__(/*! define-properties */ 4289);\n\nmodule.exports = function shimAllSettled() {\n\trequirePromise();\n\n\tvar polyfill = getPolyfill();\n\tdefine(Promise, { allSettled: polyfill }, {\n\t\tallSettled: function testAllSettled() {\n\t\t\treturn Promise.allSettled !== polyfill;\n\t\t}\n\t});\n\treturn polyfill;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/promise.allsettled/shim.js?");

/***/ })

}]);