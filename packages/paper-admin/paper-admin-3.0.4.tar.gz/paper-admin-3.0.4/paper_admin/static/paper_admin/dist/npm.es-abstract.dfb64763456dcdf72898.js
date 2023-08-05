"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkpaper_admin"] = self["webpackChunkpaper_admin"] || []).push([["npm.es-abstract"],{

/***/ 7593:
/*!*************************************************************!*\
  !*** ./node_modules/es-abstract/2020/ArraySpeciesCreate.js ***!
  \*************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $Array = GetIntrinsic('%Array%');\nvar $species = GetIntrinsic('%Symbol.species%', true);\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar Get = __webpack_require__(/*! ./Get */ 4573);\nvar IsArray = __webpack_require__(/*! ./IsArray */ 7912);\nvar IsConstructor = __webpack_require__(/*! ./IsConstructor */ 5497);\nvar IsInteger = __webpack_require__(/*! ./IsInteger */ 1377);\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-arrayspeciescreate\n\nmodule.exports = function ArraySpeciesCreate(originalArray, length) {\n\tif (!IsInteger(length) || length < 0) {\n\t\tthrow new $TypeError('Assertion failed: length must be an integer >= 0');\n\t}\n\tvar len = length === 0 ? 0 : length;\n\tvar C;\n\tvar isArray = IsArray(originalArray);\n\tif (isArray) {\n\t\tC = Get(originalArray, 'constructor');\n\t\t// TODO: figure out how to make a cross-realm normal Array, a same-realm Array\n\t\t// if (IsConstructor(C)) {\n\t\t// \tif C is another realm's Array, C = undefined\n\t\t// \tObject.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(Array))) === null ?\n\t\t// }\n\t\tif ($species && Type(C) === 'Object') {\n\t\t\tC = Get(C, $species);\n\t\t\tif (C === null) {\n\t\t\t\tC = void 0;\n\t\t\t}\n\t\t}\n\t}\n\tif (typeof C === 'undefined') {\n\t\treturn $Array(len);\n\t}\n\tif (!IsConstructor(C)) {\n\t\tthrow new $TypeError('C must be a constructor');\n\t}\n\treturn new C(len); // Construct(C, len);\n};\n\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ArraySpeciesCreate.js?");

/***/ }),

/***/ 1341:
/*!***********************************************!*\
  !*** ./node_modules/es-abstract/2020/Call.js ***!
  \***********************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\nvar callBound = __webpack_require__(/*! call-bind/callBound */ 1924);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar IsArray = __webpack_require__(/*! ./IsArray */ 7912);\n\nvar $apply = GetIntrinsic('%Reflect.apply%', true) || callBound('%Function.prototype.apply%');\n\n// https://ecma-international.org/ecma-262/6.0/#sec-call\n\nmodule.exports = function Call(F, V) {\n\tvar argumentsList = arguments.length > 2 ? arguments[2] : [];\n\tif (!IsArray(argumentsList)) {\n\t\tthrow new $TypeError('Assertion failed: optional `argumentsList`, if provided, must be a List');\n\t}\n\treturn $apply(F, V, argumentsList);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/Call.js?");

/***/ }),

/***/ 5427:
/*!*************************************************************!*\
  !*** ./node_modules/es-abstract/2020/CreateDataProperty.js ***!
  \*************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar DefineOwnProperty = __webpack_require__(/*! ../helpers/DefineOwnProperty */ 3682);\n\nvar FromPropertyDescriptor = __webpack_require__(/*! ./FromPropertyDescriptor */ 1323);\nvar OrdinaryGetOwnProperty = __webpack_require__(/*! ./OrdinaryGetOwnProperty */ 7695);\nvar IsDataDescriptor = __webpack_require__(/*! ./IsDataDescriptor */ 2846);\nvar IsExtensible = __webpack_require__(/*! ./IsExtensible */ 9405);\nvar IsPropertyKey = __webpack_require__(/*! ./IsPropertyKey */ 3086);\nvar SameValue = __webpack_require__(/*! ./SameValue */ 9640);\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-createdataproperty\n\nmodule.exports = function CreateDataProperty(O, P, V) {\n\tif (Type(O) !== 'Object') {\n\t\tthrow new $TypeError('Assertion failed: Type(O) is not Object');\n\t}\n\tif (!IsPropertyKey(P)) {\n\t\tthrow new $TypeError('Assertion failed: IsPropertyKey(P) is not true');\n\t}\n\tvar oldDesc = OrdinaryGetOwnProperty(O, P);\n\tvar extensible = !oldDesc || IsExtensible(O);\n\tvar immutable = oldDesc && (!oldDesc['[[Writable]]'] || !oldDesc['[[Configurable]]']);\n\tif (immutable || !extensible) {\n\t\treturn false;\n\t}\n\treturn DefineOwnProperty(\n\t\tIsDataDescriptor,\n\t\tSameValue,\n\t\tFromPropertyDescriptor,\n\t\tO,\n\t\tP,\n\t\t{\n\t\t\t'[[Configurable]]': true,\n\t\t\t'[[Enumerable]]': true,\n\t\t\t'[[Value]]': V,\n\t\t\t'[[Writable]]': true\n\t\t}\n\t);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/CreateDataProperty.js?");

/***/ }),

/***/ 5797:
/*!********************************************************************!*\
  !*** ./node_modules/es-abstract/2020/CreateDataPropertyOrThrow.js ***!
  \********************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar CreateDataProperty = __webpack_require__(/*! ./CreateDataProperty */ 5427);\nvar IsPropertyKey = __webpack_require__(/*! ./IsPropertyKey */ 3086);\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// // https://ecma-international.org/ecma-262/6.0/#sec-createdatapropertyorthrow\n\nmodule.exports = function CreateDataPropertyOrThrow(O, P, V) {\n\tif (Type(O) !== 'Object') {\n\t\tthrow new $TypeError('Assertion failed: Type(O) is not Object');\n\t}\n\tif (!IsPropertyKey(P)) {\n\t\tthrow new $TypeError('Assertion failed: IsPropertyKey(P) is not true');\n\t}\n\tvar success = CreateDataProperty(O, P, V);\n\tif (!success) {\n\t\tthrow new $TypeError('unable to create data property');\n\t}\n\treturn success;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/CreateDataPropertyOrThrow.js?");

/***/ }),

/***/ 5289:
/*!****************************************************************!*\
  !*** ./node_modules/es-abstract/2020/DefinePropertyOrThrow.js ***!
  \****************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar isPropertyDescriptor = __webpack_require__(/*! ../helpers/isPropertyDescriptor */ 2435);\nvar DefineOwnProperty = __webpack_require__(/*! ../helpers/DefineOwnProperty */ 3682);\n\nvar FromPropertyDescriptor = __webpack_require__(/*! ./FromPropertyDescriptor */ 1323);\nvar IsAccessorDescriptor = __webpack_require__(/*! ./IsAccessorDescriptor */ 4275);\nvar IsDataDescriptor = __webpack_require__(/*! ./IsDataDescriptor */ 2846);\nvar IsPropertyKey = __webpack_require__(/*! ./IsPropertyKey */ 3086);\nvar SameValue = __webpack_require__(/*! ./SameValue */ 9640);\nvar ToPropertyDescriptor = __webpack_require__(/*! ./ToPropertyDescriptor */ 5627);\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-definepropertyorthrow\n\nmodule.exports = function DefinePropertyOrThrow(O, P, desc) {\n\tif (Type(O) !== 'Object') {\n\t\tthrow new $TypeError('Assertion failed: Type(O) is not Object');\n\t}\n\n\tif (!IsPropertyKey(P)) {\n\t\tthrow new $TypeError('Assertion failed: IsPropertyKey(P) is not true');\n\t}\n\n\tvar Desc = isPropertyDescriptor({\n\t\tType: Type,\n\t\tIsDataDescriptor: IsDataDescriptor,\n\t\tIsAccessorDescriptor: IsAccessorDescriptor\n\t}, desc) ? desc : ToPropertyDescriptor(desc);\n\tif (!isPropertyDescriptor({\n\t\tType: Type,\n\t\tIsDataDescriptor: IsDataDescriptor,\n\t\tIsAccessorDescriptor: IsAccessorDescriptor\n\t}, Desc)) {\n\t\tthrow new $TypeError('Assertion failed: Desc is not a valid Property Descriptor');\n\t}\n\n\treturn DefineOwnProperty(\n\t\tIsDataDescriptor,\n\t\tSameValue,\n\t\tFromPropertyDescriptor,\n\t\tO,\n\t\tP,\n\t\tDesc\n\t);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/DefinePropertyOrThrow.js?");

/***/ }),

/***/ 1323:
/*!*****************************************************************!*\
  !*** ./node_modules/es-abstract/2020/FromPropertyDescriptor.js ***!
  \*****************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar assertRecord = __webpack_require__(/*! ../helpers/assertRecord */ 2188);\n\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-frompropertydescriptor\n\nmodule.exports = function FromPropertyDescriptor(Desc) {\n\tif (typeof Desc === 'undefined') {\n\t\treturn Desc;\n\t}\n\n\tassertRecord(Type, 'Property Descriptor', 'Desc', Desc);\n\n\tvar obj = {};\n\tif ('[[Value]]' in Desc) {\n\t\tobj.value = Desc['[[Value]]'];\n\t}\n\tif ('[[Writable]]' in Desc) {\n\t\tobj.writable = Desc['[[Writable]]'];\n\t}\n\tif ('[[Get]]' in Desc) {\n\t\tobj.get = Desc['[[Get]]'];\n\t}\n\tif ('[[Set]]' in Desc) {\n\t\tobj.set = Desc['[[Set]]'];\n\t}\n\tif ('[[Enumerable]]' in Desc) {\n\t\tobj.enumerable = Desc['[[Enumerable]]'];\n\t}\n\tif ('[[Configurable]]' in Desc) {\n\t\tobj.configurable = Desc['[[Configurable]]'];\n\t}\n\treturn obj;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/FromPropertyDescriptor.js?");

/***/ }),

/***/ 4573:
/*!**********************************************!*\
  !*** ./node_modules/es-abstract/2020/Get.js ***!
  \**********************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar inspect = __webpack_require__(/*! object-inspect */ 631);\n\nvar IsPropertyKey = __webpack_require__(/*! ./IsPropertyKey */ 3086);\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n/**\n * 7.3.1 Get (O, P) - https://ecma-international.org/ecma-262/6.0/#sec-get-o-p\n * 1. Assert: Type(O) is Object.\n * 2. Assert: IsPropertyKey(P) is true.\n * 3. Return O.[[Get]](P, O).\n */\n\nmodule.exports = function Get(O, P) {\n\t// 7.3.1.1\n\tif (Type(O) !== 'Object') {\n\t\tthrow new $TypeError('Assertion failed: Type(O) is not Object');\n\t}\n\t// 7.3.1.2\n\tif (!IsPropertyKey(P)) {\n\t\tthrow new $TypeError('Assertion failed: IsPropertyKey(P) is not true, got ' + inspect(P));\n\t}\n\t// 7.3.1.3\n\treturn O[P];\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/Get.js?");

/***/ }),

/***/ 5994:
/*!******************************************************!*\
  !*** ./node_modules/es-abstract/2020/HasProperty.js ***!
  \******************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar IsPropertyKey = __webpack_require__(/*! ./IsPropertyKey */ 3086);\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-hasproperty\n\nmodule.exports = function HasProperty(O, P) {\n\tif (Type(O) !== 'Object') {\n\t\tthrow new $TypeError('Assertion failed: `O` must be an Object');\n\t}\n\tif (!IsPropertyKey(P)) {\n\t\tthrow new $TypeError('Assertion failed: `P` must be a Property Key');\n\t}\n\treturn P in O;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/HasProperty.js?");

/***/ }),

/***/ 4275:
/*!***************************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsAccessorDescriptor.js ***!
  \***************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar has = __webpack_require__(/*! has */ 7642);\n\nvar assertRecord = __webpack_require__(/*! ../helpers/assertRecord */ 2188);\n\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-isaccessordescriptor\n\nmodule.exports = function IsAccessorDescriptor(Desc) {\n\tif (typeof Desc === 'undefined') {\n\t\treturn false;\n\t}\n\n\tassertRecord(Type, 'Property Descriptor', 'Desc', Desc);\n\n\tif (!has(Desc, '[[Get]]') && !has(Desc, '[[Set]]')) {\n\t\treturn false;\n\t}\n\n\treturn true;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsAccessorDescriptor.js?");

/***/ }),

/***/ 7912:
/*!**************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsArray.js ***!
  \**************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $Array = GetIntrinsic('%Array%');\n\n// eslint-disable-next-line global-require\nvar toStr = !$Array.isArray && __webpack_require__(/*! call-bind/callBound */ 1924)('Object.prototype.toString');\n\n// https://ecma-international.org/ecma-262/6.0/#sec-isarray\n\nmodule.exports = $Array.isArray || function IsArray(argument) {\n\treturn toStr(argument) === '[object Array]';\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsArray.js?");

/***/ }),

/***/ 5233:
/*!*****************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsCallable.js ***!
  \*****************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\n// http://262.ecma-international.org/5.1/#sec-9.11\n\nmodule.exports = __webpack_require__(/*! is-callable */ 5320);\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsCallable.js?");

/***/ }),

/***/ 5497:
/*!********************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsConstructor.js ***!
  \********************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! ../GetIntrinsic.js */ 4445);\n\nvar $construct = GetIntrinsic('%Reflect.construct%', true);\n\nvar DefinePropertyOrThrow = __webpack_require__(/*! ./DefinePropertyOrThrow */ 5289);\ntry {\n\tDefinePropertyOrThrow({}, '', { '[[Get]]': function () {} });\n} catch (e) {\n\t// Accessor properties aren't supported\n\tDefinePropertyOrThrow = null;\n}\n\n// https://ecma-international.org/ecma-262/6.0/#sec-isconstructor\n\nif (DefinePropertyOrThrow && $construct) {\n\tvar isConstructorMarker = {};\n\tvar badArrayLike = {};\n\tDefinePropertyOrThrow(badArrayLike, 'length', {\n\t\t'[[Get]]': function () {\n\t\t\tthrow isConstructorMarker;\n\t\t},\n\t\t'[[Enumerable]]': true\n\t});\n\n\tmodule.exports = function IsConstructor(argument) {\n\t\ttry {\n\t\t\t// `Reflect.construct` invokes `IsConstructor(target)` before `Get(args, 'length')`:\n\t\t\t$construct(argument, badArrayLike);\n\t\t} catch (err) {\n\t\t\treturn err === isConstructorMarker;\n\t\t}\n\t};\n} else {\n\tmodule.exports = function IsConstructor(argument) {\n\t\t// unfortunately there's no way to truly check this without try/catch `new argument` in old environments\n\t\treturn typeof argument === 'function' && !!argument.prototype;\n\t};\n}\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsConstructor.js?");

/***/ }),

/***/ 2846:
/*!***********************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsDataDescriptor.js ***!
  \***********************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar has = __webpack_require__(/*! has */ 7642);\n\nvar assertRecord = __webpack_require__(/*! ../helpers/assertRecord */ 2188);\n\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-isdatadescriptor\n\nmodule.exports = function IsDataDescriptor(Desc) {\n\tif (typeof Desc === 'undefined') {\n\t\treturn false;\n\t}\n\n\tassertRecord(Type, 'Property Descriptor', 'Desc', Desc);\n\n\tif (!has(Desc, '[[Value]]') && !has(Desc, '[[Writable]]')) {\n\t\treturn false;\n\t}\n\n\treturn true;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsDataDescriptor.js?");

/***/ }),

/***/ 9405:
/*!*******************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsExtensible.js ***!
  \*******************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $Object = GetIntrinsic('%Object%');\n\nvar isPrimitive = __webpack_require__(/*! ../helpers/isPrimitive */ 4790);\n\nvar $preventExtensions = $Object.preventExtensions;\nvar $isExtensible = $Object.isExtensible;\n\n// https://ecma-international.org/ecma-262/6.0/#sec-isextensible-o\n\nmodule.exports = $preventExtensions\n\t? function IsExtensible(obj) {\n\t\treturn !isPrimitive(obj) && $isExtensible(obj);\n\t}\n\t: function IsExtensible(obj) {\n\t\treturn !isPrimitive(obj);\n\t};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsExtensible.js?");

/***/ }),

/***/ 1377:
/*!****************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsInteger.js ***!
  \****************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar abs = __webpack_require__(/*! ./abs */ 1737);\nvar floor = __webpack_require__(/*! ./floor */ 6183);\n\nvar $isNaN = __webpack_require__(/*! ../helpers/isNaN */ 4619);\nvar $isFinite = __webpack_require__(/*! ../helpers/isFinite */ 2633);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-isinteger\n\nmodule.exports = function IsInteger(argument) {\n\tif (typeof argument !== 'number' || $isNaN(argument) || !$isFinite(argument)) {\n\t\treturn false;\n\t}\n\tvar absValue = abs(argument);\n\treturn floor(absValue) === absValue;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsInteger.js?");

/***/ }),

/***/ 3086:
/*!********************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsPropertyKey.js ***!
  \********************************************************/
/***/ (function(module) {

eval("\n\n// https://ecma-international.org/ecma-262/6.0/#sec-ispropertykey\n\nmodule.exports = function IsPropertyKey(argument) {\n\treturn typeof argument === 'string' || typeof argument === 'symbol';\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsPropertyKey.js?");

/***/ }),

/***/ 1780:
/*!***************************************************!*\
  !*** ./node_modules/es-abstract/2020/IsRegExp.js ***!
  \***************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $match = GetIntrinsic('%Symbol.match%', true);\n\nvar hasRegExpMatcher = __webpack_require__(/*! is-regex */ 8420);\n\nvar ToBoolean = __webpack_require__(/*! ./ToBoolean */ 2970);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-isregexp\n\nmodule.exports = function IsRegExp(argument) {\n\tif (!argument || typeof argument !== 'object') {\n\t\treturn false;\n\t}\n\tif ($match) {\n\t\tvar isRegExp = argument[$match];\n\t\tif (typeof isRegExp !== 'undefined') {\n\t\t\treturn ToBoolean(isRegExp);\n\t\t}\n\t}\n\treturn hasRegExpMatcher(argument);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/IsRegExp.js?");

/***/ }),

/***/ 7695:
/*!*****************************************************************!*\
  !*** ./node_modules/es-abstract/2020/OrdinaryGetOwnProperty.js ***!
  \*****************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $gOPD = __webpack_require__(/*! ../helpers/getOwnPropertyDescriptor */ 882);\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar callBound = __webpack_require__(/*! call-bind/callBound */ 1924);\n\nvar $isEnumerable = callBound('Object.prototype.propertyIsEnumerable');\n\nvar has = __webpack_require__(/*! has */ 7642);\n\nvar IsArray = __webpack_require__(/*! ./IsArray */ 7912);\nvar IsPropertyKey = __webpack_require__(/*! ./IsPropertyKey */ 3086);\nvar IsRegExp = __webpack_require__(/*! ./IsRegExp */ 1780);\nvar ToPropertyDescriptor = __webpack_require__(/*! ./ToPropertyDescriptor */ 5627);\nvar Type = __webpack_require__(/*! ./Type */ 1501);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-ordinarygetownproperty\n\nmodule.exports = function OrdinaryGetOwnProperty(O, P) {\n\tif (Type(O) !== 'Object') {\n\t\tthrow new $TypeError('Assertion failed: O must be an Object');\n\t}\n\tif (!IsPropertyKey(P)) {\n\t\tthrow new $TypeError('Assertion failed: P must be a Property Key');\n\t}\n\tif (!has(O, P)) {\n\t\treturn void 0;\n\t}\n\tif (!$gOPD) {\n\t\t// ES3 / IE 8 fallback\n\t\tvar arrayLength = IsArray(O) && P === 'length';\n\t\tvar regexLastIndex = IsRegExp(O) && P === 'lastIndex';\n\t\treturn {\n\t\t\t'[[Configurable]]': !(arrayLength || regexLastIndex),\n\t\t\t'[[Enumerable]]': $isEnumerable(O, P),\n\t\t\t'[[Value]]': O[P],\n\t\t\t'[[Writable]]': true\n\t\t};\n\t}\n\treturn ToPropertyDescriptor($gOPD(O, P));\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/OrdinaryGetOwnProperty.js?");

/***/ }),

/***/ 2407:
/*!*********************************************************!*\
  !*** ./node_modules/es-abstract/2020/PromiseResolve.js ***!
  \*********************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\nvar callBind = __webpack_require__(/*! call-bind */ 5559);\n\nvar $resolve = GetIntrinsic('%Promise.resolve%', true);\nvar $PromiseResolve = $resolve && callBind($resolve);\n\n// https://262.ecma-international.org/9.0/#sec-promise-resolve\n\nmodule.exports = function PromiseResolve(C, x) {\n\tif (!$PromiseResolve) {\n\t\tthrow new SyntaxError('This environment does not support Promises.');\n\t}\n\treturn $PromiseResolve(C, x);\n};\n\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/PromiseResolve.js?");

/***/ }),

/***/ 6237:
/*!*****************************************************************!*\
  !*** ./node_modules/es-abstract/2020/RequireObjectCoercible.js ***!
  \*****************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nmodule.exports = __webpack_require__(/*! ../5/CheckObjectCoercible */ 4559);\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/RequireObjectCoercible.js?");

/***/ }),

/***/ 9640:
/*!****************************************************!*\
  !*** ./node_modules/es-abstract/2020/SameValue.js ***!
  \****************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar $isNaN = __webpack_require__(/*! ../helpers/isNaN */ 4619);\n\n// http://262.ecma-international.org/5.1/#sec-9.12\n\nmodule.exports = function SameValue(x, y) {\n\tif (x === y) { // 0 === -0, but they are not identical.\n\t\tif (x === 0) { return 1 / x === 1 / y; }\n\t\treturn true;\n\t}\n\treturn $isNaN(x) && $isNaN(y);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/SameValue.js?");

/***/ }),

/***/ 2970:
/*!****************************************************!*\
  !*** ./node_modules/es-abstract/2020/ToBoolean.js ***!
  \****************************************************/
/***/ (function(module) {

eval("\n\n// http://262.ecma-international.org/5.1/#sec-9.2\n\nmodule.exports = function ToBoolean(value) { return !!value; };\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ToBoolean.js?");

/***/ }),

/***/ 5959:
/*!***************************************************!*\
  !*** ./node_modules/es-abstract/2020/ToNumber.js ***!
  \***************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\nvar $Number = GetIntrinsic('%Number%');\nvar $RegExp = GetIntrinsic('%RegExp%');\nvar $parseInteger = GetIntrinsic('%parseInt%');\n\nvar callBound = __webpack_require__(/*! call-bind/callBound */ 1924);\nvar regexTester = __webpack_require__(/*! ../helpers/regexTester */ 823);\nvar isPrimitive = __webpack_require__(/*! ../helpers/isPrimitive */ 4790);\n\nvar $strSlice = callBound('String.prototype.slice');\nvar isBinary = regexTester(/^0b[01]+$/i);\nvar isOctal = regexTester(/^0o[0-7]+$/i);\nvar isInvalidHexLiteral = regexTester(/^[-+]0x[0-9a-f]+$/i);\nvar nonWS = ['\\u0085', '\\u200b', '\\ufffe'].join('');\nvar nonWSregex = new $RegExp('[' + nonWS + ']', 'g');\nvar hasNonWS = regexTester(nonWSregex);\n\n// whitespace from: https://es5.github.io/#x15.5.4.20\n// implementation from https://github.com/es-shims/es5-shim/blob/v3.4.0/es5-shim.js#L1304-L1324\nvar ws = [\n\t'\\x09\\x0A\\x0B\\x0C\\x0D\\x20\\xA0\\u1680\\u180E\\u2000\\u2001\\u2002\\u2003',\n\t'\\u2004\\u2005\\u2006\\u2007\\u2008\\u2009\\u200A\\u202F\\u205F\\u3000\\u2028',\n\t'\\u2029\\uFEFF'\n].join('');\nvar trimRegex = new RegExp('(^[' + ws + ']+)|([' + ws + ']+$)', 'g');\nvar $replace = callBound('String.prototype.replace');\nvar $trim = function (value) {\n\treturn $replace(value, trimRegex, '');\n};\n\nvar ToPrimitive = __webpack_require__(/*! ./ToPrimitive */ 8840);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-tonumber\n\nmodule.exports = function ToNumber(argument) {\n\tvar value = isPrimitive(argument) ? argument : ToPrimitive(argument, $Number);\n\tif (typeof value === 'symbol') {\n\t\tthrow new $TypeError('Cannot convert a Symbol value to a number');\n\t}\n\tif (typeof value === 'bigint') {\n\t\tthrow new $TypeError('Conversion from \\'BigInt\\' to \\'number\\' is not allowed.');\n\t}\n\tif (typeof value === 'string') {\n\t\tif (isBinary(value)) {\n\t\t\treturn ToNumber($parseInteger($strSlice(value, 2), 2));\n\t\t} else if (isOctal(value)) {\n\t\t\treturn ToNumber($parseInteger($strSlice(value, 2), 8));\n\t\t} else if (hasNonWS(value) || isInvalidHexLiteral(value)) {\n\t\t\treturn NaN;\n\t\t} else {\n\t\t\tvar trimmed = $trim(value);\n\t\t\tif (trimmed !== value) {\n\t\t\t\treturn ToNumber(trimmed);\n\t\t\t}\n\t\t}\n\t}\n\treturn $Number(value);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ToNumber.js?");

/***/ }),

/***/ 2747:
/*!***************************************************!*\
  !*** ./node_modules/es-abstract/2020/ToObject.js ***!
  \***************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $Object = GetIntrinsic('%Object%');\n\nvar RequireObjectCoercible = __webpack_require__(/*! ./RequireObjectCoercible */ 6237);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-toobject\n\nmodule.exports = function ToObject(value) {\n\tRequireObjectCoercible(value);\n\treturn $Object(value);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ToObject.js?");

/***/ }),

/***/ 8840:
/*!******************************************************!*\
  !*** ./node_modules/es-abstract/2020/ToPrimitive.js ***!
  \******************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar toPrimitive = __webpack_require__(/*! es-to-primitive/es2015 */ 1503);\n\n// https://ecma-international.org/ecma-262/6.0/#sec-toprimitive\n\nmodule.exports = function ToPrimitive(input) {\n\tif (arguments.length > 1) {\n\t\treturn toPrimitive(input, arguments[1]);\n\t}\n\treturn toPrimitive(input);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ToPrimitive.js?");

/***/ }),

/***/ 5627:
/*!***************************************************************!*\
  !*** ./node_modules/es-abstract/2020/ToPropertyDescriptor.js ***!
  \***************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar has = __webpack_require__(/*! has */ 7642);\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nvar Type = __webpack_require__(/*! ./Type */ 1501);\nvar ToBoolean = __webpack_require__(/*! ./ToBoolean */ 2970);\nvar IsCallable = __webpack_require__(/*! ./IsCallable */ 5233);\n\n// https://262.ecma-international.org/5.1/#sec-8.10.5\n\nmodule.exports = function ToPropertyDescriptor(Obj) {\n\tif (Type(Obj) !== 'Object') {\n\t\tthrow new $TypeError('ToPropertyDescriptor requires an object');\n\t}\n\n\tvar desc = {};\n\tif (has(Obj, 'enumerable')) {\n\t\tdesc['[[Enumerable]]'] = ToBoolean(Obj.enumerable);\n\t}\n\tif (has(Obj, 'configurable')) {\n\t\tdesc['[[Configurable]]'] = ToBoolean(Obj.configurable);\n\t}\n\tif (has(Obj, 'value')) {\n\t\tdesc['[[Value]]'] = Obj.value;\n\t}\n\tif (has(Obj, 'writable')) {\n\t\tdesc['[[Writable]]'] = ToBoolean(Obj.writable);\n\t}\n\tif (has(Obj, 'get')) {\n\t\tvar getter = Obj.get;\n\t\tif (typeof getter !== 'undefined' && !IsCallable(getter)) {\n\t\t\tthrow new $TypeError('getter must be a function');\n\t\t}\n\t\tdesc['[[Get]]'] = getter;\n\t}\n\tif (has(Obj, 'set')) {\n\t\tvar setter = Obj.set;\n\t\tif (typeof setter !== 'undefined' && !IsCallable(setter)) {\n\t\t\tthrow new $TypeError('setter must be a function');\n\t\t}\n\t\tdesc['[[Set]]'] = setter;\n\t}\n\n\tif ((has(desc, '[[Get]]') || has(desc, '[[Set]]')) && (has(desc, '[[Value]]') || has(desc, '[[Writable]]'))) {\n\t\tthrow new $TypeError('Invalid property descriptor. Cannot both specify accessors and a value or writable attribute');\n\t}\n\treturn desc;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ToPropertyDescriptor.js?");

/***/ }),

/***/ 2167:
/*!***************************************************!*\
  !*** ./node_modules/es-abstract/2020/ToString.js ***!
  \***************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $String = GetIntrinsic('%String%');\nvar $TypeError = GetIntrinsic('%TypeError%');\n\n// https://ecma-international.org/ecma-262/6.0/#sec-tostring\n\nmodule.exports = function ToString(argument) {\n\tif (typeof argument === 'symbol') {\n\t\tthrow new $TypeError('Cannot convert a Symbol value to a string');\n\t}\n\treturn $String(argument);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ToString.js?");

/***/ }),

/***/ 1514:
/*!***************************************************!*\
  !*** ./node_modules/es-abstract/2020/ToUint32.js ***!
  \***************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar ToNumber = __webpack_require__(/*! ./ToNumber */ 5959);\n\n// http://262.ecma-international.org/5.1/#sec-9.6\n\nmodule.exports = function ToUint32(x) {\n\treturn ToNumber(x) >>> 0;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/ToUint32.js?");

/***/ }),

/***/ 1501:
/*!***********************************************!*\
  !*** ./node_modules/es-abstract/2020/Type.js ***!
  \***********************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar ES5Type = __webpack_require__(/*! ../5/Type */ 3951);\n\n// https://262.ecma-international.org/11.0/#sec-ecmascript-data-types-and-values\n\nmodule.exports = function Type(x) {\n\tif (typeof x === 'symbol') {\n\t\treturn 'Symbol';\n\t}\n\tif (typeof x === 'bigint') {\n\t\treturn 'BigInt';\n\t}\n\treturn ES5Type(x);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/Type.js?");

/***/ }),

/***/ 1737:
/*!**********************************************!*\
  !*** ./node_modules/es-abstract/2020/abs.js ***!
  \**********************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $abs = GetIntrinsic('%Math.abs%');\n\n// http://262.ecma-international.org/5.1/#sec-5.2\n\nmodule.exports = function abs(x) {\n\treturn $abs(x);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/abs.js?");

/***/ }),

/***/ 6183:
/*!************************************************!*\
  !*** ./node_modules/es-abstract/2020/floor.js ***!
  \************************************************/
/***/ (function(module) {

eval("\n\n// var modulo = require('./modulo');\nvar $floor = Math.floor;\n\n// http://262.ecma-international.org/5.1/#sec-5.2\n\nmodule.exports = function floor(x) {\n\t// return x - modulo(x, 1);\n\treturn $floor(x);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/2020/floor.js?");

/***/ }),

/***/ 4559:
/*!************************************************************!*\
  !*** ./node_modules/es-abstract/5/CheckObjectCoercible.js ***!
  \************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\n\n// http://262.ecma-international.org/5.1/#sec-9.10\n\nmodule.exports = function CheckObjectCoercible(value, optMessage) {\n\tif (value == null) {\n\t\tthrow new $TypeError(optMessage || ('Cannot call method on ' + value));\n\t}\n\treturn value;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/5/CheckObjectCoercible.js?");

/***/ }),

/***/ 3951:
/*!********************************************!*\
  !*** ./node_modules/es-abstract/5/Type.js ***!
  \********************************************/
/***/ (function(module) {

eval("\n\n// https://262.ecma-international.org/5.1/#sec-8\n\nmodule.exports = function Type(x) {\n\tif (x === null) {\n\t\treturn 'Null';\n\t}\n\tif (typeof x === 'undefined') {\n\t\treturn 'Undefined';\n\t}\n\tif (typeof x === 'function' || typeof x === 'object') {\n\t\treturn 'Object';\n\t}\n\tif (typeof x === 'number') {\n\t\treturn 'Number';\n\t}\n\tif (typeof x === 'boolean') {\n\t\treturn 'Boolean';\n\t}\n\tif (typeof x === 'string') {\n\t\treturn 'String';\n\t}\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/5/Type.js?");

/***/ }),

/***/ 4445:
/*!**************************************************!*\
  !*** ./node_modules/es-abstract/GetIntrinsic.js ***!
  \**************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\n// TODO: remove, semver-major\n\nmodule.exports = __webpack_require__(/*! get-intrinsic */ 210);\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/GetIntrinsic.js?");

/***/ }),

/***/ 3682:
/*!***************************************************************!*\
  !*** ./node_modules/es-abstract/helpers/DefineOwnProperty.js ***!
  \***************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $defineProperty = GetIntrinsic('%Object.defineProperty%', true);\n\nif ($defineProperty) {\n\ttry {\n\t\t$defineProperty({}, 'a', { value: 1 });\n\t} catch (e) {\n\t\t// IE 8 has a broken defineProperty\n\t\t$defineProperty = null;\n\t}\n}\n\nvar callBound = __webpack_require__(/*! call-bind/callBound */ 1924);\n\nvar $isEnumerable = callBound('Object.prototype.propertyIsEnumerable');\n\n// eslint-disable-next-line max-params\nmodule.exports = function DefineOwnProperty(IsDataDescriptor, SameValue, FromPropertyDescriptor, O, P, desc) {\n\tif (!$defineProperty) {\n\t\tif (!IsDataDescriptor(desc)) {\n\t\t\t// ES3 does not support getters/setters\n\t\t\treturn false;\n\t\t}\n\t\tif (!desc['[[Configurable]]'] || !desc['[[Writable]]']) {\n\t\t\treturn false;\n\t\t}\n\n\t\t// fallback for ES3\n\t\tif (P in O && $isEnumerable(O, P) !== !!desc['[[Enumerable]]']) {\n\t\t\t// a non-enumerable existing property\n\t\t\treturn false;\n\t\t}\n\n\t\t// property does not exist at all, or exists but is enumerable\n\t\tvar V = desc['[[Value]]'];\n\t\t// eslint-disable-next-line no-param-reassign\n\t\tO[P] = V; // will use [[Define]]\n\t\treturn SameValue(O[P], V);\n\t}\n\t$defineProperty(O, P, FromPropertyDescriptor(desc));\n\treturn true;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/DefineOwnProperty.js?");

/***/ }),

/***/ 2188:
/*!**********************************************************!*\
  !*** ./node_modules/es-abstract/helpers/assertRecord.js ***!
  \**********************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $TypeError = GetIntrinsic('%TypeError%');\nvar $SyntaxError = GetIntrinsic('%SyntaxError%');\n\nvar has = __webpack_require__(/*! has */ 7642);\n\nvar predicates = {\n\t// https://262.ecma-international.org/6.0/#sec-property-descriptor-specification-type\n\t'Property Descriptor': function isPropertyDescriptor(Type, Desc) {\n\t\tif (Type(Desc) !== 'Object') {\n\t\t\treturn false;\n\t\t}\n\t\tvar allowed = {\n\t\t\t'[[Configurable]]': true,\n\t\t\t'[[Enumerable]]': true,\n\t\t\t'[[Get]]': true,\n\t\t\t'[[Set]]': true,\n\t\t\t'[[Value]]': true,\n\t\t\t'[[Writable]]': true\n\t\t};\n\n\t\tfor (var key in Desc) { // eslint-disable-line\n\t\t\tif (has(Desc, key) && !allowed[key]) {\n\t\t\t\treturn false;\n\t\t\t}\n\t\t}\n\n\t\tvar isData = has(Desc, '[[Value]]');\n\t\tvar IsAccessor = has(Desc, '[[Get]]') || has(Desc, '[[Set]]');\n\t\tif (isData && IsAccessor) {\n\t\t\tthrow new $TypeError('Property Descriptors may not be both accessor and data descriptors');\n\t\t}\n\t\treturn true;\n\t}\n};\n\nmodule.exports = function assertRecord(Type, recordType, argumentName, value) {\n\tvar predicate = predicates[recordType];\n\tif (typeof predicate !== 'function') {\n\t\tthrow new $SyntaxError('unknown record type: ' + recordType);\n\t}\n\tif (!predicate(Type, value)) {\n\t\tthrow new $TypeError(argumentName + ' must be a ' + recordType);\n\t}\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/assertRecord.js?");

/***/ }),

/***/ 882:
/*!**********************************************************************!*\
  !*** ./node_modules/es-abstract/helpers/getOwnPropertyDescriptor.js ***!
  \**********************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $gOPD = GetIntrinsic('%Object.getOwnPropertyDescriptor%');\nif ($gOPD) {\n\ttry {\n\t\t$gOPD([], 'length');\n\t} catch (e) {\n\t\t// IE 8 has a broken gOPD\n\t\t$gOPD = null;\n\t}\n}\n\nmodule.exports = $gOPD;\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/getOwnPropertyDescriptor.js?");

/***/ }),

/***/ 2633:
/*!******************************************************!*\
  !*** ./node_modules/es-abstract/helpers/isFinite.js ***!
  \******************************************************/
/***/ (function(module) {

eval("\n\nvar $isNaN = Number.isNaN || function (a) { return a !== a; };\n\nmodule.exports = Number.isFinite || function (x) { return typeof x === 'number' && !$isNaN(x) && x !== Infinity && x !== -Infinity; };\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/isFinite.js?");

/***/ }),

/***/ 4619:
/*!***************************************************!*\
  !*** ./node_modules/es-abstract/helpers/isNaN.js ***!
  \***************************************************/
/***/ (function(module) {

eval("\n\nmodule.exports = Number.isNaN || function isNaN(a) {\n\treturn a !== a;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/isNaN.js?");

/***/ }),

/***/ 4790:
/*!*********************************************************!*\
  !*** ./node_modules/es-abstract/helpers/isPrimitive.js ***!
  \*********************************************************/
/***/ (function(module) {

eval("\n\nmodule.exports = function isPrimitive(value) {\n\treturn value === null || (typeof value !== 'function' && typeof value !== 'object');\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/isPrimitive.js?");

/***/ }),

/***/ 2435:
/*!******************************************************************!*\
  !*** ./node_modules/es-abstract/helpers/isPropertyDescriptor.js ***!
  \******************************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar has = __webpack_require__(/*! has */ 7642);\nvar $TypeError = GetIntrinsic('%TypeError%');\n\nmodule.exports = function IsPropertyDescriptor(ES, Desc) {\n\tif (ES.Type(Desc) !== 'Object') {\n\t\treturn false;\n\t}\n\tvar allowed = {\n\t\t'[[Configurable]]': true,\n\t\t'[[Enumerable]]': true,\n\t\t'[[Get]]': true,\n\t\t'[[Set]]': true,\n\t\t'[[Value]]': true,\n\t\t'[[Writable]]': true\n\t};\n\n\tfor (var key in Desc) { // eslint-disable-line no-restricted-syntax\n\t\tif (has(Desc, key) && !allowed[key]) {\n\t\t\treturn false;\n\t\t}\n\t}\n\n\tif (ES.IsDataDescriptor(Desc) && ES.IsAccessorDescriptor(Desc)) {\n\t\tthrow new $TypeError('Property Descriptors may not be both accessor and data descriptors');\n\t}\n\treturn true;\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/isPropertyDescriptor.js?");

/***/ }),

/***/ 823:
/*!*********************************************************!*\
  !*** ./node_modules/es-abstract/helpers/regexTester.js ***!
  \*********************************************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

eval("\n\nvar GetIntrinsic = __webpack_require__(/*! get-intrinsic */ 210);\n\nvar $test = GetIntrinsic('RegExp.prototype.test');\n\nvar callBind = __webpack_require__(/*! call-bind */ 5559);\n\nmodule.exports = function regexTester(regex) {\n\treturn callBind($test, regex);\n};\n\n\n//# sourceURL=webpack://paper-admin/./node_modules/es-abstract/helpers/regexTester.js?");

/***/ })

}]);