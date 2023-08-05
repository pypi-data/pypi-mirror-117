"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.multi.js"],{

/***/ 4356:
/*!*********************************************!*\
  !*** ./node_modules/multi.js/src/multi.css ***!
  \*********************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/multi.js/src/multi.css?");

/***/ }),

/***/ 8880:
/*!*****************************************************!*\
  !*** ./node_modules/multi.js/dist/multi-es6.min.js ***!
  \*****************************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/*! multi.js 20-08-2021 */\n\nvar multi=function(){var e=!1,t=function(t,n){var a,l,r=n.limit;if(r>-1){var i=0;for(a=0;a<t.options.length;a++)t.options[a].selected&&i++;if(i===r)for(e=!0,\"function\"==typeof n.limit_reached&&n.limit_reached(),a=0;a<t.options.length;a++)(l=t.options[a]).selected||l.setAttribute(\"disabled\",!0);else if(e){for(a=0;a<t.options.length;a++)\"false\"===(l=t.options[a]).getAttribute(\"data-origin-disabled\")&&l.removeAttribute(\"disabled\");e=!1}}},n=function(e,n,a){var l,r,i,d=e.options[n.target.getAttribute(\"multi-index\")];d.disabled||(d.selected=!d.selected,t(e,a),l=\"change\",r=e,(i=document.createEvent(\"HTMLEvents\")).initEvent(l,!1,!0),r.dispatchEvent(i))},a=function(e){var t=document.createElement(\"div\");if(t.className=\"item-group\",e.label){var n=document.createElement(\"span\");n.innerHTML=e.label,n.className=\"group-label\",t.appendChild(n)}return t},l=function(e,t){var n;if(e.wrapper.selected.innerHTML=\"\",e.wrapper.non_selected.innerHTML=\"\",t.non_selected_header&&t.selected_header){var l=document.createElement(\"div\"),r=document.createElement(\"div\");l.className=\"header\",r.className=\"header\",l.innerText=t.non_selected_header,r.innerText=t.selected_header,e.wrapper.non_selected.appendChild(l),e.wrapper.selected.appendChild(r)}if(e.wrapper.search)var i=e.wrapper.search.value;var d=null,s=null,o=null,c=null;for(n=0;n<e.options.length;n++){var p=e.options[n],u=p.value,m=p.textContent||p.innerText,h=document.createElement(\"a\");if(h.tabIndex=0,h.className=\"item\",h.innerText=m,h.setAttribute(\"role\",\"button\"),h.setAttribute(\"data-value\",u),h.setAttribute(\"multi-index\",n),p.disabled&&(h.className+=\" disabled\"),p.parentNode===e&&(d=null,s=null),\"OPTGROUP\"===p.parentNode.nodeName&&p.parentNode!==s&&(s=p.parentNode,d=a(s),e.wrapper.non_selected.appendChild(d)),p.selected){h.className+=\" selected\";var v=h.cloneNode(!0);d?d!==c&&(c=d,o=a(s),e.wrapper.selected.appendChild(o)):(c=null,o=null),o?o.appendChild(v):e.wrapper.selected.appendChild(v)}p.parentNode===e&&(d=null,s=null),(!i||i&&m.toLowerCase().indexOf(i.toLowerCase())>-1)&&(null!=d?d.appendChild(h):e.wrapper.non_selected.appendChild(h))}if(t.hide_empty_groups){var f=document.getElementsByClassName(\"item-group\");for(n=0;n<f.length;n++)f[n].childElementCount<2&&(f[n].style.display=\"none\")}};return function(e,a){if((a=void 0!==a?a:{}).enable_search=void 0===a.enable_search||a.enable_search,a.search_placeholder=void 0!==a.search_placeholder?a.search_placeholder:\"Search...\",a.non_selected_header=void 0!==a.non_selected_header?a.non_selected_header:null,a.selected_header=void 0!==a.selected_header?a.selected_header:null,a.limit=void 0!==a.limit?parseInt(a.limit):-1,isNaN(a.limit)&&(a.limit=-1),a.hide_empty_groups=void 0!==a.hide_empty_groups&&a.hide_empty_groups,null==e.dataset.multijs&&\"SELECT\"===e.nodeName&&e.multiple){e.style.display=\"none\",e.setAttribute(\"data-multijs\",!0);var r=document.createElement(\"div\");if(r.className=\"multi-wrapper\",a.enable_search){var i=document.createElement(\"input\");i.className=\"search-input\",i.type=\"text\",i.setAttribute(\"placeholder\",a.search_placeholder),i.setAttribute(\"title\",a.search_placeholder),i.addEventListener(\"input\",function(){l(e,a)}),r.appendChild(i),r.search=i}var d=document.createElement(\"div\");d.className=\"non-selected-wrapper\";var s=document.createElement(\"div\");s.className=\"selected-wrapper\",r.addEventListener(\"click\",function(t){t.target.getAttribute(\"multi-index\")&&n(e,t,a)}),r.addEventListener(\"keypress\",function(t){var l=32===t.keyCode||13===t.keyCode;t.target.getAttribute(\"multi-index\")&&l&&(t.preventDefault(),n(e,t,a))}),r.appendChild(d),r.appendChild(s),r.non_selected=d,r.selected=s,e.wrapper=r,e.parentNode.insertBefore(r,e.nextSibling);for(var o=0;o<e.options.length;o++){var c=e.options[o];c.setAttribute(\"data-origin-disabled\",c.disabled)}t(e,a),l(e,a),e.addEventListener(\"change\",function(){l(e,a)})}}}();\"undefined\"!=typeof jQuery&&function(e){e.fn.multi=function(t){return t=void 0!==t?t:{},this.each(function(){var n=e(this);multi(n.get(0),t)})}}(jQuery);/* harmony default export */ __webpack_exports__[\"default\"] = (multi);\n\n//# sourceURL=webpack://paper-admin/./node_modules/multi.js/dist/multi-es6.min.js?");

/***/ })

}]);