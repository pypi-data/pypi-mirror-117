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
/******/ 	return __webpack_require__(__webpack_require__.s = 120);
/******/ })
/************************************************************************/
/******/ ({

/***/ 120:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(8);
__webpack_require__(39);
__webpack_require__(40);
module.exports = __webpack_require__(121);


/***/ }),

/***/ 121:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/breadcrumb/examples/breadcrumb-default.html");

/***/ }),

/***/ 39:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 40:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/breadcrumb/examples.html");

/***/ }),

/***/ 8:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRBreadcrumb {
  constructor(name, component) {
    this.name = name
    this.component = component
    this._setBehavior()
  }

  _setBehavior() {
    this._setView()
    window.addEventListener('resize', () => {
      this._setView()
    })
    window.document.addEventListener('click', (event) => {
      if (
        !this.component.contains(event.target) &&
        this.component.querySelector('.br-card')
      ) {
        this.component.querySelector('.br-card').remove()
      }
    })
  }

  _setView() {
    this._reset()
    for (const crumbList of this.component.querySelectorAll('.crumb-list')) {
      const crumbs = crumbList.querySelectorAll('.crumb:not([data-active])')
      if (window.innerWidth < 575) {
        crumbs.forEach((crumb) => {
          crumb.classList.add('d-none')
        })
        this._insertExpandButton()
      } else {
        if (
          crumbList.scrollWidth > crumbList.offsetWidth ||
          crumbs.length > 5
        ) {
          crumbs.forEach((crumb, index) => {
            if (index > 0 && index < crumbs.length - 1) {
              crumb.classList.add('d-none')
            }
          })
          this._insertExpandButton()
        }
      }
    }
  }

  _insertExpandButton() {
    const crumb = this._createCrumb()
    const crumbList = this.component.querySelector('.crumb-list')
    const crumbs = crumbList.querySelectorAll('.crumb')
    crumbList.insertBefore(crumb, crumbs[1])
  }

  _reset() {
    this.component.querySelectorAll('.crumb-list .crumb').forEach((crumb) => {
      if (crumb.classList.contains('menu-mobil')) {
        crumb.remove()
      } else {
        crumb.classList.remove('d-none')
      }
    })
  }

  _createCrumb() {
    const crumb = document.createElement('li')
    crumb.classList.add('crumb', 'menu-mobil')
    crumb.setAttribute('data-toggle', 'dropdown')

    const button = document.createElement('button')
    button.classList.add('br-button', 'circle')

    const span = document.createElement('span')
    span.classList.add('sr-only')
    span.innerHTML = 'Botão Menu'

    const folderIcon = document.createElement('i')
    folderIcon.classList.add('icon', 'fas', 'fa-folder-plus')

    const chevronIcon = document.createElement('i')
    chevronIcon.classList.add('icon', 'fas', 'fa-chevron-right')

    crumb.appendChild(chevronIcon)
    crumb.appendChild(button)
    button.appendChild(span)
    button.appendChild(folderIcon)

    crumb.addEventListener('click', () => {
      let card = this.component.querySelector('.br-card')
      if (card) {
        card.remove()
      } else {
        card = this._createList()
        this.component.appendChild(card)
      }
    })

    return crumb
  }

  _createList() {
    const card = document.createElement('div')
    card.classList.add('br-card')

    const front = document.createElement('div')
    front.classList.add('front')

    const content = document.createElement('div')
    content.classList.add('content')

    const list = document.createElement('div')
    list.classList.add('br-list')

    card.appendChild(front)
    front.appendChild(content)
    content.appendChild(list)

    this.component.querySelectorAll('.crumb-list .crumb').forEach((crumb) => {
      if (crumb.classList.contains('d-none')) {
        const item = document.createElement('div')
        item.classList.add('br-item', 'py-3')

        const row = document.createElement('div')
        row.classList.add('row', 'align-items-center')

        const col = document.createElement('div')
        col.classList.add('col')
        if (!crumb.classList.contains('home')) {
          col.appendChild(crumb.querySelector('a').cloneNode(true))
          row.appendChild(col)
          item.appendChild(row)
          list.appendChild(item)
        }
      }
    })

    return card
  }
}

const breadcrumbList = []
for (const brBreadcrumb of window.document.querySelectorAll('.br-breadcrumb')) {
  breadcrumbList.push(new BRBreadcrumb('br-breadcrumb', brBreadcrumb))
}
/* harmony default export */ __webpack_exports__["default"] = (BRBreadcrumb);


/***/ })

/******/ });
//# sourceMappingURL=breadcrumb.js.map