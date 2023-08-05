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
/******/ 	return __webpack_require__(__webpack_require__.s = 220);
/******/ })
/************************************************************************/
/******/ ({

/***/ 13:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRMenu {
  constructor(name, component) {
    this.name = name
    this.component = component
    this.trigger = this.component.querySelector('[data-toggle="menu"]')
    this.scrim = this.component.querySelector('.menu-scrim')
    this.dismiss = this.component.querySelectorAll('[data-dismiss="menu"]')
    this.componentFolders = this.component.querySelectorAll('.menu-folder')
    this.componentItems = this.component.querySelectorAll('.menu-item')
    this._setBehavior()
  }

  _setBehavior() {
    this._toggleMenu()
    this._closeMenu()
    this._setDropMenu()
    this._setSideMenu()
    this._setKeyboardBehaviors()
    this._initType2Menu()
  }

  _setKeyboardBehaviors() {
    // Fechar com tecla ESC
    this.component.addEventListener('keyup', (event) => {
      switch (event.keyCode) {
        case 27:
          this._closeMenu()
          break
        default:
          break
      }
    })
    // Fechar com Tab fora do menu
    if (this.scrim) {
      this.scrim.addEventListener('keyup', () => {
        return this._closeMenu()
      })
    }
  }

  _toggleMenu() {
    // Clicar no trigger
    if (this.trigger) {
      this.trigger.addEventListener('click', () => {
        // Fechar Menu caso esteja aberto
        if (this.component.classList.contains('active')) {
          this._closeMenu()
          return
        }
        // Abre Menu
        this._openMenu()
      })
    }
    // Clicar no dismiss
    for (const close of this.dismiss) {
      close.addEventListener('click', () => {
        return this._closeMenu()
      })
    }
  }

  _openMenu() {
    return this.component.classList.add('active')
  }

  _closeMenu() {
    return this.component.classList.remove('active')
  }

  _setDropMenu() {
    // Configura Drop Menu para filho imediato de ".menu-folder"
    for (const item of this.component.querySelectorAll(
      '.menu-folder > a.menu-item'
    )) {
      // Inclui ícone de Drop Menu
      this._createIcon(item, 'fa-angle-down')
      // Configura como Drop Menu
      item.parentNode.classList.add('drop-menu')
      // Inicializa Drop Menu
      this._toggleDropMenu(item)
    }
  }

  _setSideMenu() {
    // Configura Side Menu para quem não for filho imediato de ".menu-folder"
    for (const ul of this.component.querySelectorAll('a.menu-item + ul')) {
      if (!ul.parentNode.classList.contains('menu-folder')) {
        // Inclui ícone de Side Menu
        this._createIcon(ul.previousElementSibling, 'fa-angle-right')
        // Configura como Side Menu
        ul.parentNode.classList.add('side-menu')
        // Inicializa Side Menu
        this._toggleSideMenu(ul.previousElementSibling)
      }
    }
  }

  _toggleDropMenu(element) {
    element.addEventListener('click', () => {
      // Fecha Drop Menu caso esteja aberto
      if (element.parentNode.classList.contains('active')) {
        element.parentNode.classList.remove('active')
        return
      }

      // Abre Drop Menu
      element.parentNode.classList.add('active')
    })
  }

  _toggleSideMenu(element) {
    element.addEventListener('click', () => {
      // Esconde todos os itens
      this._hideItems(element)

      // Mostra itens do Side Menu ativo
      this._showItems(element.parentNode)

      // Fecha Side Menu caso esteja aberto
      if (element.parentNode.classList.contains('active')) {
        this._closeSideMenu(element)
        element.focus()
        return
      }

      // Abre Side Menu
      element.parentNode.classList.add('active')
      element.focus()
    })
  }

  _closeSideMenu(element) {
    element.parentNode.classList.remove('active')
    // Verifica se existe Side Menu anterior, caso contrário mostra todos os itens de volta
    const parentFolder = element.parentNode.closest('.side-menu.active')
      ? element.parentNode.closest('.side-menu.active')
      : element.closest('.menu-body')
    this._showItems(parentFolder)
  }

  _hideItems(element) {
    for (const item of element
      .closest('.menu-body')
      .querySelectorAll('.menu-item')) {
      item.setAttribute('hidden', '')
    }
  }

  _showItems(element) {
    for (const item of element.querySelectorAll('.menu-item')) {
      item.removeAttribute('hidden')
    }
  }

  _createIcon(element, icon) {
    const menuIconContainer = document.createElement('span')
    menuIconContainer.classList.add('support')

    const menuIcon = document.createElement('i')
    menuIcon.classList.add('fas')
    menuIcon.classList.add(icon)
    menuIcon.setAttribute('aria-hidden', 'true')

    menuIconContainer.appendChild(menuIcon)
    element.appendChild(menuIconContainer)
  }

  _initType2Menu() {
    const ativadorMenu = document.querySelector(
      '[data-toggle="menu"][data-target="#navigation"]'
    )
    if (ativadorMenu) {
      ativadorMenu.addEventListener('click', () => {
        document
          .querySelector(ativadorMenu.dataset.target)
          .classList.toggle('active')
      })
    }
  }
}

const menuList = []
for (const brMenu of window.document.querySelectorAll('.br-menu:not(.dsgov)')) {
  menuList.push(new BRMenu('br-menu', brMenu))
}

/* harmony default export */ __webpack_exports__["default"] = (BRMenu);


/***/ }),

/***/ 220:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(13);
__webpack_require__(65);
__webpack_require__(66);
__webpack_require__(221);
__webpack_require__(222);
__webpack_require__(223);
__webpack_require__(224);
__webpack_require__(225);
__webpack_require__(226);
__webpack_require__(227);
__webpack_require__(228);
__webpack_require__(229);
module.exports = __webpack_require__(230);


/***/ }),

/***/ 221:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-auxiliary-simple.html");

/***/ }),

/***/ 222:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-auxiliary.html");

/***/ }),

/***/ 223:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-groupedby-divider.html");

/***/ }),

/***/ 224:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-groupedby-dropdown.html");

/***/ }),

/***/ 225:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-groupedby-label.html");

/***/ }),

/***/ 226:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-large.html");

/***/ }),

/***/ 227:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-medium.html");

/***/ }),

/***/ 228:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-principal-1.html");

/***/ }),

/***/ 229:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-principal-2.html");

/***/ }),

/***/ 230:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples/menu-small.html");

/***/ }),

/***/ 65:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 66:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/menu/examples.html");

/***/ })

/******/ });
//# sourceMappingURL=menu.js.map