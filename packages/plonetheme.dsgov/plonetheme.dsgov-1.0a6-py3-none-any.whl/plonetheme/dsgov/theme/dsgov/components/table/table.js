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
/******/ 	return __webpack_require__(__webpack_require__.s = 317);
/******/ })
/************************************************************************/
/******/ ({

/***/ 20:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* eslint-disable complexity */
class BRTable {
  constructor(name, component, sequence) {
    this.name = name
    this.component = component
    this._header = this.component.querySelector('.header, .table-header')
    this._table = this.component.querySelector('table')
    this._sequence = sequence
    this._setBehaviors()
  }

  _setBehaviors() {
    this._makeResponsiveTable()
    this._headerBehavior()
    this._setHeaderWidth()
    this._searchBehavior()
    this._dropdownBehavior()
    this._densityBehavior()
    this._setClickActions()
  }

  _makeResponsiveTable() {
    const responsiveClass = 'responsive'
    if (!this.component.querySelector(`.${responsiveClass}`)) {
      const responsiveElement = document.createElement('div')
      responsiveElement.classList.add(responsiveClass)
      responsiveElement.appendChild(this._table)
      this._header.after(responsiveElement)
    }
  }

  _headerBehavior() {
    // this._hideThead()

    window.addEventListener('resize', () => {
      // this._hideThead()
    })

    for (const responsive of this.component.querySelectorAll('.responsive')) {
      if (window.innerWidth > 575) {
        // this._setSyncScroll(responsive)
      }
    }

    // this._cloneHeaders()
  }

  _makeScroller() {
    const scrollerTag = document.createElement('div')
    // this._setSyncScroll(scrollerTag)
    scrollerTag.classList.add('scroller')
    for (const header of this._table.querySelectorAll('thead tr th')) {
      const clonedHeader = document.createElement('div')
      clonedHeader.classList.add('item')
      clonedHeader.innerHTML = header.innerHTML
      if (header.offsetWidth) {
        clonedHeader.style.flex = `1 0 ${header.offsetWidth}px`
      }
      scrollerTag.appendChild(clonedHeader)
      const checkbox = clonedHeader.querySelector('.br-checkbox')
      if (checkbox) {
        const input = checkbox.querySelector('input')
        const label = checkbox.querySelector('label')
        input.id = `${input.id}-clone`
        label.setAttribute('for', input.id)
      }
    }
    return scrollerTag
  }

  _cloneHeaders() {
    const headersTag = document.createElement('div')
    headersTag.classList.add('headers')
    headersTag.style.top = `${this._header.offsetHeight}px`
    headersTag.appendChild(this._makeScroller())
    this._header.after(headersTag)
  }

  _hideThead() {
    this._table.style.marginTop = `-${
      this._table.querySelector('thead').offsetHeight
    }px`
  }

  _setSyncScroll(element) {
    element.classList.add('syncscroll')
    element.setAttribute('name', `table-${this._sequence}`)
    element.setAttribute('style', 'overflow-y: hidden')
    // element.setAttribute('tabindex', 0)
  }

  _setHeaderWidth() {
    for (const clonedHeader of this.component.querySelectorAll(
      '.headers > div'
    )) {
      for (const [index, header] of this.component
        .querySelectorAll('table thead tr th')
        .entries()) {
        clonedHeader.children[index].style.flex = `1 0 ${header.offsetWidth}px`
      }
    }
  }

  _dropdownBehavior() {
    for (const dropdown of this.component.querySelectorAll(
      '[data-toggle="dropdown"]'
    )) {
      this._dropdownInit(dropdown)
      this._dropdownToggle(dropdown)
    }
  }

  _dropdownToggle(element) {
    element.addEventListener('click', () => {
      if (element.getAttribute('aria-expanded') === 'false') {
        this._dropdownOpen(element)
        return
      }
      this._dropdownClose(element)
    })
    window.document.addEventListener('click', (event) => {
      if (!this.component.contains(event.target)) {
        this._dropdownClose(element)
      }
    })
  }

  _dropdownInit(element) {
    element.parentElement.classList.add('dropdown')
    element.nextElementSibling.setAttribute('role', 'menu')
    element.setAttribute('aria-haspopup', 'true')
    this._dropdownClose(element)
  }

  _dropdownOpen(element) {
    element.setAttribute('aria-expanded', 'true')
    element.nextElementSibling.classList.add('show')
  }

  _dropdownClose(element) {
    element.setAttribute('aria-expanded', 'false')
    element.nextElementSibling.classList.remove('show')
  }

  _searchBehavior() {
    if (this.component.dataset.search) {
      const trigger = this.component.querySelector('[data-toggle="search"]')
      const target = this.component.querySelector('.search-bar')
      const dismiss = this.component.querySelector('[data-dismiss="search"]')

      // Inicializar
      this._searchInit(trigger)

      // Abre busca
      trigger.addEventListener('click', () => {
        return this._searchOpen(trigger, target)
      })

      // Fecha busca
      dismiss.addEventListener('click', () => {
        return this._searchClose(trigger, target)
      })
      target.querySelector('input').addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
          this._searchClose(trigger, target)
        }
      })
    }
  }

  _searchInit(trigger) {
    trigger.setAttribute('aria-expanded', 'false')
  }

  _searchOpen(trigger, target) {
    trigger.setAttribute('aria-expanded', 'true')
    target.classList.add('show')
    target.querySelector('input').focus()
  }

  _searchClose(trigger, target) {
    target.querySelector('input').value = ''
    target.classList.remove('show')
    trigger.focus()
    trigger.setAttribute('aria-expanded', 'false')
  }

  _densityBehavior() {
    const desityTriggers = this.component.querySelectorAll('[data-density]')
    for (const desityTrigger of desityTriggers) {
      desityTrigger.addEventListener('click', () => {
        this.component.classList.remove('small', 'medium', 'large')
        this.component.classList.add(desityTrigger.dataset.density)
        this._hideThead()
        this._dropdownClose(
          desityTrigger
            .closest('.dropdown')
            .querySelector('[data-toggle="dropdown"]')
        )
      })
    }
  }

  _setClickActions() {
    const headerCheckbox = this.component.querySelector(
      '.headers [type="checkbox"]'
    )
    const tableCheckboxes = this.component.querySelectorAll(
      'tbody [type="checkbox"]'
    )
    const selectedBar = this.component.querySelector('.selected-bar')
    const checkAlls = this.component.querySelectorAll(
      '[data-toggle="check-all"]'
    )
    for (const checkAll of checkAlls) {
      checkAll.addEventListener('click', () => {
        this._checkAllTable(selectedBar, tableCheckboxes, headerCheckbox)
        if (checkAll.parentElement.classList.contains('br-list')) {
          this._dropdownClose(
            checkAll
              .closest('.dropdown')
              .querySelector('[data-toggle="dropdown"]')
          )
        }
      })
    }
    if (tableCheckboxes) {
      for (const checkbox of tableCheckboxes) {
        checkbox.addEventListener('click', () => {
          this._checkRow(checkbox, selectedBar, tableCheckboxes, headerCheckbox)
        })
      }
    }
  }

  _setRow(checkbox, check) {
    const tr = checkbox.parentNode.parentNode.parentNode
    if (check) {
      tr.classList.add('is-selected')
      checkbox.parentNode.classList.add('is-inverted')
      checkbox.checked = true
    } else {
      tr.classList.remove('is-selected')
      checkbox.parentNode.classList.remove('is-inverted')
      checkbox.checked = false
    }
  }

  _checkRow(checkbox, selectedBar, tableCheckboxes, headerCheckbox) {
    const check = checkbox.checked
    this._setRow(checkbox, check)
    this._setSelectedBar(
      check ? 1 : -1,
      selectedBar,
      tableCheckboxes,
      headerCheckbox
    )
  }

  _checkAllRows(tableCheckboxes) {
    for (const checkbox of tableCheckboxes) {
      this._setRow(checkbox, true)
    }
  }

  _uncheckAllRows(tableCheckboxes) {
    for (const checkbox of tableCheckboxes) {
      this._setRow(checkbox, false)
    }
  }

  _checkAllTable(selectedBar, tableCheckboxes, headerCheckbox) {
    let count = tableCheckboxes.length
    const infoCount = selectedBar.querySelector('.info .count')
    const total = parseInt(infoCount.innerHTML, 10)
    if (total === count) {
      this._uncheckAllRows(tableCheckboxes)
      count = -1 * count
    } else {
      this._checkAllRows(tableCheckboxes)
    }
    this._setSelectedBar(count, selectedBar, tableCheckboxes, headerCheckbox)
  }

  _setSelectedBar(count, selectedBar, tableCheckboxes, headerCheckbox) {
    const infoCount = selectedBar.querySelector('.info .count')
    const infoText = selectedBar.querySelector('.info .text')
    const total = count < 2 ? parseInt(infoCount.innerHTML, 10) + count : count
    if (total > 0) {
      selectedBar.classList.add('show')
      infoCount.innerHTML = total
      infoText.innerHTML = total > 1 ? 'itens selecionados' : 'item selecionado'
      if (headerCheckbox) headerCheckbox.parentNode.classList.add('is-checking')
      if (total === tableCheckboxes.length) {
        if (headerCheckbox) {
          headerCheckbox.checked = true
          headerCheckbox.parentNode.classList.remove('is-checking')
        }
      }
    } else {
      infoCount.innerHTML = 0
      if (headerCheckbox) {
        headerCheckbox.checked = false
        headerCheckbox.parentNode.classList.remove('is-checking')
      }
      selectedBar.classList.remove('show')
    }
  }

  /**
   * @fileoverview syncscroll - scroll several areas simultaniously
   * @version 0.0.3
   *
   * @license MIT, see http://github.com/asvd/intence
   * @copyright 2015 asvd <heliosframework@gmail.com>
   */
  // static _syncscroll() {
  //   const scroll = 'scroll'
  //   const elems = document.getElementsByClassName(`sync${scroll}`)
  //   const EventListener = 'EventListener'
  //   const length = 'length'
  //   const names = {}
  //   // clearing existing listeners
  //   let i, j, el, found, name
  //   for (name in names) {
  //     if (Object.prototype.hasOwnProperty.call(names, name)) {
  //       for (i = 0; i < names[name][length]; i++) {
  //         names[name][i][`remove${EventListener}`](
  //           scroll,
  //           names[name][i].syn,
  //           0
  //         )
  //       }
  //     }
  //   }
  //   // setting-up the new listeners
  //   for (i = 0; i < elems[length]; i++) {
  //     found = j = 0
  //     el = elems[i]
  //     if (!(name = el.getAttribute('name'))) {
  //       // name attribute is not set
  //       continue
  //     }
  //     el = el[`${scroll}er`] || el // needed for intence
  //     // searching for existing entry in array of names;
  //     // searching for the element in that entry
  //     for (; j < (names[name] = names[name] || [])[length]; j++) {
  //       found |= names[name][j] === el
  //     }
  //     if (!found) {
  //       names[name].push(el)
  //     }
  //     el.eX = el.eY = 0
  //     this._elSyn(el, name, scroll, elems, EventListener, length, names)
  //   }
  // }

  static _elSyn(el, name, scroll, elems, EventListener, length, names) {
    const addEventListener = `add${EventListener}`
    const client = 'client'
    const Height = 'Height'
    const Left = 'Left'
    const mathRound = Math.round
    const Top = 'Top'
    const Width = 'Width'
    el[addEventListener](
      scroll,
      () => {
        const otherElems = names[name]
        let scrollX = el[scroll + Left]
        let scrollY = el[scroll + Top]
        const xRate = scrollX / (el[scroll + Width] - el[client + Width])
        const yRate = scrollY / (el[scroll + Height] - el[client + Height])
        const updateX = scrollX !== el.eX
        const updateY = scrollY !== el.eY
        el.eX = scrollX
        el.eY = scrollY
        otherElems.forEach((element) => {
          if (element !== el) {
            if (
              updateX &&
              mathRound(
                element[scroll + Left] -
                  (scrollX = element.eX = mathRound(
                    xRate * (element[scroll + Width] - element[client + Width])
                  ))
              )
            ) {
              element[scroll + Left] = scrollX
            }
            if (
              updateY &&
              mathRound(
                element[scroll + Top] -
                  (scrollY = element.eY = mathRound(
                    yRate *
                      (element[scroll + Height] - element[client + Height])
                  ))
              )
            ) {
              element[scroll + Top] = scrollY
            }
          }
        })
      },
      0
    )
  }
}
const tableList = []
for (const [index, brTable] of window.document
  .querySelectorAll('.br-table')
  .entries()) {
  tableList.push(new BRTable('br-table', brTable, index))
}
// BRTable._syncscroll()
/* harmony default export */ __webpack_exports__["default"] = (BRTable);


/***/ }),

/***/ 317:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(20);
__webpack_require__(89);
__webpack_require__(90);
module.exports = __webpack_require__(318);


/***/ }),

/***/ 318:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/table/examples/table.html");

/***/ }),

/***/ 89:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 90:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/table/examples.html");

/***/ })

/******/ });
//# sourceMappingURL=table.js.map