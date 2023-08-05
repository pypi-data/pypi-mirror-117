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
/******/ 	return __webpack_require__(__webpack_require__.s = 313);
/******/ })
/************************************************************************/
/******/ ({

/***/ 19:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRTab {
  constructor(name, component) {
    this.name = name
    this.component = component
    this._setBehavior()
  }

  _setBehavior() {
    for (const ancor of this.component.querySelectorAll('.tab-nav')) {
      this.height = ancor.clientHeight
      this.scollsizes = ancor.scrollHeight - ancor.clientHeight

      this.scrollHeight = Math.max(
        this.component.scrollWidth,
        document.documentElement.scrollWidth,
        this.component.offsetWidth,
        document.documentElement.offsetWidth,
        this.component.clientWidth,
        document.documentElement.clientWidth
      )
      this.leftPosition = this.component.offsetWidth - 1
      // debugger
      ancor.style.setProperty('--height-nav', `${this.height}px`)
      ancor.style.setProperty('--right-gradient-nav', `${this.leftPosition}px`)

      this.positionScroll(ancor, this.component)

      this.navigationRight = this.navigationRight + 4

      if (this.navigationRight <= this.lastItempos - 5) {
        ancor.classList.add('tab-nav-right')
      }

      ancor.onscroll = (event) => {
        this.positionScroll(ancor, this.component)

        if (this.navigationLeft <= 0) {
          ancor.classList.add('tab-nav-left')
        } else {
          ancor.classList.remove('tab-nav-left')
        }

        if (this.navigationRight <= this.lastItempos - 5) {
          ancor.classList.add('tab-nav-right')
        } else {
          ancor.classList.remove('tab-nav-right')
        }
      }
    }

    for (const ancor of this.component.querySelectorAll(
      '.tab-nav .tab-item:not([not-tab="true"]) button'
    )) {
      ancor.addEventListener(
        'click',
        (event) => {
          this._switchTab(event.currentTarget.parentElement)
          this._switchContent(event.currentTarget.parentElement)
        },
        false
      )
      ancor.addEventListener('keyup', (e) => {
        this.positionKeyboard(e, this)
      })
    }
    this.tabitems = this.component.querySelectorAll('tab-item')
  }

  positionKeyboard(event, componentTab) {
    event.preventDefault()
    const keys = {
      end: 35,
      home: 36,
      left: 37,
      right: 39,
    }
    const key = event.keyCode

    this.tabitems = this.component.querySelectorAll('.tab-item')

    this.buttons = this.component.querySelectorAll('button')

    switch (key) {
      case keys.end:
        event.preventDefault()
        // Activate last tab
        this.clean()
        this._switchTab(this.tabitems[this.tabitems.length - 1])
        this._switchContent(this.tabitems[this.tabitems.length - 1])
        this.tabitems[this.tabitems.length - 1].focus()

        break
      case keys.home:
        event.preventDefault()
        this.clean()

        this._switchTab(this.tabitems[0])
        this._switchContent(this.tabitems[0])
        this.tabitems[0].focus()
        event.stopPropagation()
        break

      // Up and down are in keydown
      // because we need to prevent page scroll >:)
      case keys.left:
        event.preventDefault()
        const contComponent = 0
        const contComponentActive = 0
        this.position(event.target, -1)
        event.stopPropagation()
        break
      case keys.right:
        event.preventDefault()
        this.position(event.target, 1)
        event.stopPropagation()
        break
      default:
        break
    }
  }

  position(target, direction) {
    let contComponent = 0
    let contComponentActive = 0

    const tabItems2 = target.parentElement.parentElement.querySelectorAll(
      '.tab-item'
    )
    for (const component of tabItems2) {
      if (component.classList.contains('is-active')) {
        contComponentActive = contComponent
      }
      contComponent += 1
    }
    if (
      tabItems2.length > contComponentActive + direction &&
      contComponentActive + direction >= 0
    ) {
      this.clean()
      this._switchTab(tabItems2[contComponentActive + direction])
      this._switchContent(tabItems2[contComponentActive + direction])
      tabItems2[contComponentActive + direction].focus()

      let x = ''

      if (tabItems2[contComponentActive + direction].querySelector('button')) {
        x = tabItems2[contComponentActive + direction].querySelector('button')
        x.focus()
      }

      // x[0].focus()
    }
  }
  clean() {
    for (const ancor of event.currentTarget.parentElement.querySelectorAll(
      'button'
    )) {
      ancor.classList.remove('focus-visible')
      ancor.classList.remove('is-active')
    }
    for (const ancor of event.currentTarget.parentElement.querySelectorAll(
      'tab-item'
    )) {
      ancor.classList.remove('is-active')
    }
  }

  positionScroll(ancor, component) {
    this.navItems = ancor.querySelectorAll('.tab-item')
    this.lastItempos = Math.ceil(
      this.navItems[this.navItems.length - 1].getBoundingClientRect().right
    )
    this.navigationLeft = Math.floor(
      this.navItems[0].getBoundingClientRect().left
    )
    this.navigationRight = Math.floor(ancor.getBoundingClientRect().right)
  }
  _switchTab(currentTab) {
    for (const tabItem of this.component.querySelectorAll(
      '.tab-nav .tab-item:not([not-tab="true"])'
    )) {
      if (tabItem === currentTab) {
        tabItem.classList.add('is-active')
      } else {
        tabItem.classList.remove('is-active')
      }
    }
  }

  _switchContent(currentTab) {
    for (const button of currentTab.querySelectorAll('button')) {
      for (const tabPanel of this.component.querySelectorAll(
        '.tab-content .tab-panel'
      )) {
        if (button.getAttribute('data-panel') === tabPanel.getAttribute('id')) {
          tabPanel.classList.add('is-active')
        } else {
          tabPanel.classList.remove('is-active')
        }
      }
    }
  }
}
const abasList = []
for (const brTab of window.document.querySelectorAll('.br-tab')) {
  abasList.push(new BRTab('br-tab', brTab))
}
/* harmony default export */ __webpack_exports__["default"] = (BRTab);


/***/ }),

/***/ 313:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(19);
__webpack_require__(87);
__webpack_require__(88);
__webpack_require__(314);
module.exports = __webpack_require__(315);


/***/ }),

/***/ 314:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/tab/examples/tab-contadores.html");

/***/ }),

/***/ 315:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/tab/examples/tab-padrao.html");

/***/ }),

/***/ 87:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 88:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/tab/examples.html");

/***/ })

/******/ });
//# sourceMappingURL=tab.js.map