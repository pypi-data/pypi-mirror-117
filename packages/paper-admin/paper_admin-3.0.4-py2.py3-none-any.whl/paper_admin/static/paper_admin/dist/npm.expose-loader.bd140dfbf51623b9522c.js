"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.expose-loader"],{

/***/ 7672:
/*!******************************************************************!*\
  !*** ./node_modules/expose-loader/dist/runtime/getGlobalThis.js ***!
  \******************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\n// eslint-disable-next-line func-names\nmodule.exports = function () {\n  if (typeof globalThis === \"object\") {\n    return globalThis;\n  }\n\n  var g;\n\n  try {\n    // This works if eval is allowed (see CSP)\n    // eslint-disable-next-line no-new-func\n    g = this || new Function(\"return this\")();\n  } catch (e) {\n    // This works if the window reference is available\n    if (typeof window === \"object\") {\n      return window;\n    } // This works if the self reference is available\n\n\n    if (typeof self === \"object\") {\n      return self;\n    } // This works if the global reference is available\n\n\n    if (typeof __webpack_require__.g !== \"undefined\") {\n      return __webpack_require__.g;\n    }\n  }\n\n  return g;\n}();\n\n//# sourceURL=webpack://paper-admin/./node_modules/expose-loader/dist/runtime/getGlobalThis.js?");

/***/ })

}]);