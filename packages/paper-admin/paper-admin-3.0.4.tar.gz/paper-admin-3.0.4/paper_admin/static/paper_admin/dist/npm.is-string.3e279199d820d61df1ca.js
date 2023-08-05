"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.is-string"],{

/***/ 9981:
/*!*****************************************!*\
  !*** ./node_modules/is-string/index.js ***!
  \*****************************************/
/***/ (function(module) {

eval("\n\nvar strValue = String.prototype.valueOf;\nvar tryStringObject = function tryStringObject(value) {\n\ttry {\n\t\tstrValue.call(value);\n\t\treturn true;\n\t} catch (e) {\n\t\treturn false;\n\t}\n};\nvar toStr = Object.prototype.toString;\nvar strClass = '[object String]';\nvar hasToStringTag = typeof Symbol === 'function' && !!Symbol.toStringTag;\n\nmodule.exports = function isString(value) {\n\tif (typeof value === 'string') {\n\t\treturn true;\n\t}\n\tif (typeof value !== 'object') {\n\t\treturn false;\n\t}\n\treturn hasToStringTag ? tryStringObject(value) : toStr.call(value) === strClass;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/is-string/index.js?");

/***/ })

}]);