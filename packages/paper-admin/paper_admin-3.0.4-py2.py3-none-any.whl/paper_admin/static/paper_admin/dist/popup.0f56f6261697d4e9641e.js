/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["popup"],{

/***/ 2284:
/*!********************************************************!*\
  !*** ./paper_admin/static/paper_admin/src/js/popup.js ***!
  \********************************************************/
/***/ (function() {

eval("/* global gettext */\n// Autofocus for \"add\" page\nif (/add\\/?$/.test(window.location.pathname)) {\n  const form = document.querySelector(\".paper-form\");\n\n  if (form) {\n    const field = form.querySelector(\"input:not([type=hidden]), select, textarea\");\n    field && field.focus();\n  }\n} // Close popup on Esc\n\n\ndocument.addEventListener(\"keydown\", function (event) {\n  if (event.which === 27) {\n    window.close();\n  }\n}); // \"Close popup\" button\n\ndocument.addEventListener(\"click\", function (event) {\n  const link = event.target.closest(\".cancel-link\");\n\n  if (link) {\n    event.preventDefault();\n    window.close();\n  }\n});\n\n//# sourceURL=webpack://paper-admin/./paper_admin/static/paper_admin/src/js/popup.js?");

/***/ })

}]);