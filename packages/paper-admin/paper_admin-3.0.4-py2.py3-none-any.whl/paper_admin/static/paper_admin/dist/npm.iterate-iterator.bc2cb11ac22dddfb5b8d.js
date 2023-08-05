"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.iterate-iterator"],{

/***/ 2252:
/*!************************************************!*\
  !*** ./node_modules/iterate-iterator/index.js ***!
  \************************************************/
/***/ (function(module) {

eval("\n\nvar $TypeError = TypeError;\n\n// eslint-disable-next-line consistent-return\nmodule.exports = function iterateIterator(iterator) {\n\tif (!iterator || typeof iterator.next !== 'function') {\n\t\tthrow new $TypeError('iterator must be an object with a `next` method');\n\t}\n\tif (arguments.length > 1) {\n\t\tvar callback = arguments[1];\n\t\tif (typeof callback !== 'function') {\n\t\t\tthrow new $TypeError('`callback`, if provided, must be a function');\n\t\t}\n\t}\n\tvar values = callback || [];\n\tvar result;\n\twhile ((result = iterator.next()) && !result.done) {\n\t\tif (callback) {\n\t\t\tcallback(result.value); // eslint-disable-line callback-return\n\t\t} else {\n\t\t\tvalues.push(result.value);\n\t\t}\n\t}\n\tif (!callback) {\n\t\treturn values;\n\t}\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/iterate-iterator/index.js?");

/***/ })

}]);