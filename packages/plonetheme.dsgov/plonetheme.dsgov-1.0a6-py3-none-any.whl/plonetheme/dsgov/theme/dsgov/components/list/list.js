/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 203);
/******/ })
/************************************************************************/
/******/ ({

/***/ 203:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(3);
__webpack_require__(61);
__webpack_require__(62);
__webpack_require__(204);
__webpack_require__(205);
__webpack_require__(206);
__webpack_require__(207);
__webpack_require__(208);
__webpack_require__(209);
__webpack_require__(210);
__webpack_require__(211);
__webpack_require__(212);
module.exports = __webpack_require__(213);


/***/ }),

/***/ 204:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-dense-high.html");

/***/ }),

/***/ 205:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-dense-medium.html");

/***/ }),

/***/ 206:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-dense-small.html");

/***/ }),

/***/ 207:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-group-divider.html");

/***/ }),

/***/ 208:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-group-expansion.html");

/***/ }),

/***/ 209:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-group-tag.html");

/***/ }),

/***/ 210:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-horizontal-divider.html");

/***/ }),

/***/ 211:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-horizontal-expansion.html");

/***/ }),

/***/ 212:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-simples-selecionaveis.html");

/***/ }),

/***/ 213:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples/list-vertical-simples.html");

/***/ }),

/***/ 3:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRList {
  constructor(name, component) {
    this.name = name
    this.component = component
    this.collapsible = this.name === 'br-list-collapsible'
    this.checkable = this.name === 'br-list-checkable'
    this.unique = component.hasAttribute('data-unique')
    this.cols = this.horizontal ? component.querySelectorAll('.col') : []
    this.itens = component.querySelectorAll(':scope > .br-item')
    // suporte a colunas do bootstrap dentro da lista
    if (this.itens.length === 0)
      this.itens = component.querySelectorAll('div > .br-item')
    this._setBehavior()
  }

  _setBehavior() {
    if (this.collapsible) {
      this._closeAllItens()
      this.itens.forEach((item) => {
        item.addEventListener('click', (event) => {
          this._toggle(event, item)
        })
      })
    }
    if (this.checkable) {
      this.itens.forEach((item) => {
        this._setSelected(item)
        if (!item.classList.contains('disabled')) {
          item
            .querySelector('.br-checkbox > input')
            .addEventListener('click', (event) => {
              if (event.target.getAttribute('type') === 'checkbox') {
                this._check(event, item)
              }
            })
        }
      })
    }
    if (this.cols.length > 0) {
      const n = this.cols.length
      const pos = n > 6 && n % 2 === 1 ? n + 1 : n
      const resto = pos / Math.ceil(pos / 6)
      const equal = 100 / resto
      this.cols.forEach((col) => {
        col.style.flexBasis = `${equal}%`
      })
    }
  }

  _toggle(event, item) {
    if (!item.classList.contains('open')) {
      if (this.unique) this._closeAllItens()
    }
    if (item.classList.contains('open')) {
      item.classList.remove('open')
    } else {
      item.classList.add('open')
    }
    const icon = item.querySelector('.fa-angle-down')
      ? item.querySelector('.fa-angle-down')
      : item.querySelector('.fa-angle-up')
    if (icon) {
      icon.classList.toggle('fa-angle-down')
      icon.classList.toggle('fa-angle-up')
    }
  }

  _closeAllItens() {
    this.itens.forEach((item) => {
      item.classList.remove('open')
      const icon = item.querySelector('.fa-angle-down')
        ? item.querySelector('.fa-angle-down')
        : item.querySelector('.fa-angle-up')
      if (icon) {
        icon.classList.add('fa-angle-down')
        icon.classList.remove('fa-angle-up')
      }
    })
  }

  _check(event, item) {
    item.classList.toggle('selected')
    this._setSelected(item)
  }

  _setSelected(item) {
    const brCheckbox = item.querySelector('.br-checkbox')
    const brCheckboxInput = brCheckbox.querySelector('input')
    const selected = item.classList.contains('selected')
    if (brCheckbox) {
      if (selected) {
        brCheckbox.classList.add('is-inverted')
        brCheckboxInput.setAttribute('checked', '')
        brCheckboxInput.checked = true
      } else {
        brCheckbox.classList.remove('is-inverted')
        brCheckboxInput.removeAttribute('checked')
        brCheckboxInput.checked = false
      }
    }
  }
}

const listList = []
for (const brList of window.document.querySelectorAll(
  '.br-list[data-toggle]'
)) {
  listList.push(new BRList('br-list-collapsible', brList))
}
for (const brList of window.document.querySelectorAll(
  '.br-list[data-checkable]'
)) {
  listList.push(new BRList('br-list-checkable', brList))
}
/* harmony default export */ __webpack_exports__["default"] = (BRList);


/***/ }),

/***/ 61:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 62:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/list/examples.html");

/***/ })

/******/ });
//# sourceMappingURL=list.js.map