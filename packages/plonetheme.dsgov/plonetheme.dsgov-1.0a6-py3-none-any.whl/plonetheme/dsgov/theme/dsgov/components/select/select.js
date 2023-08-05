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
/******/ 	return __webpack_require__(__webpack_require__.s = 281);
/******/ })
/************************************************************************/
/******/ ({

/***/ 1:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRItem {
  constructor(name, component) {
    this.name = name
    this.component = component
    this._setBehavior()
  }

  _setBehavior() {
    this._setCheckboxSelection()
    this._setRadioSelection()
  }

  _setCheckboxSelection() {
    for (const checkbox of this.component.querySelectorAll(
      '.br-checkbox input[type="checkbox"]'
    )) {
      if (checkbox.checked) {
        checkbox.setAttribute('checked', '')
        this.component.classList.add('selected')
      }
      checkbox.addEventListener('click', (event) => {
        if (event.currentTarget.checked) {
          event.currentTarget.setAttribute('checked', '')
          this.component.classList.add('selected')
        } else {
          event.currentTarget.removeAttribute('checked')
          this.component.classList.remove('selected')
        }
      })
    }
  }

  _setRadioSelection() {
    for (const radio of this.component.querySelectorAll(
      '.br-radio input[type="radio"]'
    )) {
      if (radio.checked) {
        radio.setAttribute('checked', '')
        this.component.classList.add('selected')
      }
      radio.addEventListener('click', (event) => {
        for (const item of this.component.parentElement.querySelectorAll(
          '.br-item'
        )) {
          for (const radioItem of item.querySelectorAll(
            '.br-radio input[type="radio"]'
          )) {
            if (radioItem === event.currentTarget) {
              radioItem.setAttribute('checked', '')
              item.classList.add('selected')
            } else {
              radioItem.removeAttribute('checked')
              item.classList.remove('selected')
            }
          }
        }
      })
    }
  }
}

const itemList = []
for (const brItem of window.document.querySelectorAll('.br-item')) {
  itemList.push(new BRItem('br-item', brItem))
}
/* harmony default export */ __webpack_exports__["default"] = (BRItem);


/***/ }),

/***/ 18:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _item_item__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(1);


class BRSelect {
  constructor(name, component) {
    this.name = name
    this.component = component
    this.multiple = component.hasAttribute('multiple')
    this.optionsList = this._setOptionsList()
    this._setBehavior()
  }

  get selected() {
    let selected = []
    for (const [index, option] of this.optionsList.entries()) {
      if (!this.multiple) {
        if (option.selected) {
          selected = option.value
          break
        }
      } else {
        if (index > 0 && option.selected) {
          selected.push(option.value)
        }
      }
    }
    return selected
  }
  _setOptionsList() {
    const optionsList = []
    for (const item of this.component.querySelectorAll('.br-list .br-item')) {
      for (const label of item.querySelectorAll(
        '.br-radio label, .br-checkbox label'
      )) {
        const option = {
          focus: false,
          selected: false,
          value: label.innerText,
          visible: true,
        }
        optionsList.push(option)
      }
    }
    return optionsList
  }

  _setBehavior() {
    this._setDropdownBehavior()
    this._setKeyboardBehavior()
    this._setSelectionBehavior()
    this._setFilterBehavior()
  }

  _setDropdownBehavior() {
    for (const input of this.component.querySelectorAll(
      '.br-input input[type="text"]'
    )) {
      input.addEventListener('focus', () => {
        this._openSelect()
        this._resetFocus()
      })
    }
    for (const trigger of this.component.querySelectorAll(
      '.br-input .br-button[data-trigger]'
    )) {
      trigger.addEventListener('click', () => {
        for (const list of this.component.querySelectorAll('.br-list')) {
          if (list.hasAttribute('expanded')) {
            this._closeSelect()
          } else {
            this._openSelect()
          }
        }
      })
    }
    window.document.addEventListener('click', (event) => {
      if (!this.component.contains(event.target)) {
        this._closeSelect()
      }
    })
  }

  _setKeyboardBehavior() {
    for (const input of this.component.querySelectorAll(
      '.br-input input[type="text"]'
    )) {
      input.addEventListener('keydown', (event) => {
        //Close Select
        if (event.shiftKey && event.key === 'Tab') {
          this._closeSelect()
          this._resetFocus()
        }
        if (event.keyCode === 40) {
          event.preventDefault()
          for (const list of this.component.querySelectorAll('.br-list')) {
            list.focus()
            if (list === document.activeElement) {
              this._getNextItem().focus()
            }
          }
        }
      })
    }
    for (const list of this.component.querySelectorAll('.br-list')) {
      // eslint-disable-next-line complexity
      list.addEventListener('keydown', (event) => {
        event.preventDefault()
        switch (event.keyCode) {
          case 9:
            this._closeSelect()
            this._resetFocus()
            break
          case 27:
            this._closeSelect()
            break
          case 32:
            this._setKeyClickOnOption(list)
            break
          case 38:
            this._getPreviousItem().focus()
            break
          case 40:
            this._getNextItem().focus()
            break
          default:
            break
        }
      })
    }
  }

  _setKeyClickOnOption(list) {
    for (const [index, item] of list.querySelectorAll('.br-item').entries()) {
      if (this.optionsList[index].focus) {
        for (const check of item.querySelectorAll(
          '.br-radio input[type="radio"], .br-checkbox input[type="checkbox"]'
        )) {
          check.click()
        }
      }
    }
  }

  _setDefaultSelected() {
    const selectedItems = this.component.querySelectorAll('.br-list .selected')

    const iterable = typeof selectedItems[Symbol.iterator]
    if (selectedItems !== null && iterable === 'function') {
      for (const item of selectedItems) {
        this._setSelected(this._positionSelected(item), item)
      }
    }
  }

  _positionSelected(component) {
    for (const [index, componente] of this.component
      .querySelectorAll('.br-list .br-item')
      .entries()) {
      if (componente === component) {
        return index
      }
    }
    return 0
  }

  _setSelectionBehavior() {
    this._setDefaultSelected()
    const itemList = []
    for (const [index, item] of this.component
      .querySelectorAll('.br-list .br-item')
      .entries()) {
      for (const check of item.querySelectorAll(
        '.br-radio input[type="radio"], .br-checkbox input[type="checkbox"]'
      )) {
        itemList.push(new _item_item__WEBPACK_IMPORTED_MODULE_0__["default"]('br-item', item))
        check.addEventListener('click', (event) => {
          if (!this.multiple) {
            for (const [index2, item2] of this.component
              .querySelectorAll('.br-list .br-item')
              .entries()) {
              this._removeSelected(index2, item2)
            }
            this._setSelected(index, item)
            this._closeSelect()
          } else if (!event.currentTarget.hasAttribute('checked')) {
            this._removeSelected(index, item)
          } else {
            this._setSelected(index, item)
          }
          if (item.hasAttribute('data-all')) {
            for (const check of item.querySelectorAll(
              '.br-checkbox input[type="checkbox"]'
            )) {
              if (!check.hasAttribute('checked')) {
                this._setAttribute()
                item.querySelectorAll('label')[0].innerText = 'Selecionar Todos'
              } else {
                for (const item2 of this.component.querySelectorAll(
                  '.br-list .br-item'
                )) {
                  for (const check2 of item2.querySelectorAll(
                    '.br-checkbox input[type="checkbox"]'
                  )) {
                    if (!check2.hasAttribute('checked')) {
                      check2.click()
                    }
                  }
                }
                item.querySelectorAll('label')[0].innerText =
                  'Desselecionar Todos'
              }
            }
          }
        })
      }
    }
  }

  _setFilterBehavior() {
    for (const input of this.component.querySelectorAll(
      '.br-input input[type="text"]'
    )) {
      input.addEventListener('input', (event) => {
        let allHidden = true
        this._filter(event.currentTarget.value)
        for (const option of this.optionsList) {
          if (option.visible) {
            allHidden = false
          }
        }
        if (allHidden) {
          event.currentTarget.value = event.currentTarget.value.slice(0, -1)
          this._filter(event.currentTarget.value)
        }
      })
    }
  }

  _filter(value) {
    for (const [index, item] of this.component
      .querySelectorAll('.br-list .br-item')
      .entries()) {
      if (
        this.optionsList[index].value
          .toUpperCase()
          .indexOf(value.toUpperCase()) === -1
      ) {
        item.classList.add('d-none')
        this.optionsList[index].visible = false
      } else {
        item.classList.remove('d-none')
        this.optionsList[index].visible = true
      }
    }
  }

  _setAttribute() {
    for (const item2 of this.component.querySelectorAll('.br-list .br-item')) {
      for (const check2 of item2.querySelectorAll(
        '.br-checkbox input[type="checkbox"]'
      )) {
        if (check2.hasAttribute('checked')) {
          check2.click()
        }
      }
    }
  }
  _setSelected(index, item) {
    item.classList.add('selected')
    for (const check of item.querySelectorAll('.br-radio, .br-checkbox')) {
      for (const input of check.querySelectorAll(
        'input[type="radio"], input[type="checkbox"]'
      )) {
        input.setAttribute('checked', '')
      }
    }
    this.optionsList[index].selected = true
    this._setInput()
  }

  _removeSelected(index, item) {
    item.classList.remove('selected')
    for (const check of item.querySelectorAll('.br-radio, .br-checkbox')) {
      for (const input of check.querySelectorAll(
        'input[type="radio"], input[type="checkbox"'
      )) {
        input.removeAttribute('checked')
      }
      this.optionsList[index].selected = false
      this._setInput()
    }
  }

  _setInput() {
    for (const input of this.component.querySelectorAll(
      '.br-input input[type="text"]'
    )) {
      if (!this.multiple) {
        input.value = this.selected
      } else if (this.selected.length === 0) {
        input.value = ''
      } else if (this.selected.length === 1) {
        input.value = this.selected
      } else {
        input.value = `${this.selected[0]} + (${this.selected.length - 1})`
      }
    }
  }

  // eslint-disable-next-line complexity
  _getNextItem() {
    const list = this.component.querySelectorAll('.br-list .br-item')
    let iFocused
    let iVisible
    for (iFocused = 0; iFocused < this.optionsList.length; iFocused++) {
      if (this.optionsList[iFocused].focus) {
        for (
          iVisible = iFocused + 1;
          iVisible < this.optionsList.length;
          iVisible++
        ) {
          if (this.optionsList[iVisible].visible) {
            break
          }
        }
        break
      }
    }
    if (iFocused === this.optionsList.length) {
      for (const [index, option] of this.optionsList.entries()) {
        if (option.visible) {
          option.focus = true
          return list[index]
        }
      }
    } else if (iVisible < this.optionsList.length) {
      this.optionsList[iFocused].focus = false
      this.optionsList[iVisible].focus = true
      return list[iVisible]
    } else {
      return list[iFocused]
    }
    return ''
  }

  _getPreviousItem() {
    const list = this.component.querySelectorAll('.br-list .br-item')
    let iFocused
    let iVisible
    for (iFocused = 0; iFocused < this.optionsList.length; iFocused++) {
      if (this.optionsList[iFocused].focus) {
        for (iVisible = iFocused - 1; iVisible > 0; iVisible--) {
          if (this.optionsList[iVisible].visible) {
            break
          }
        }
        break
      }
    }
    if (iFocused === 0) {
      return list[iFocused]
    } else {
      this.optionsList[iFocused].focus = false
      this.optionsList[iVisible].focus = true
      return list[iVisible]
    }
  }

  _resetInput() {
    for (const input of this.component.querySelectorAll(
      '.br-input input[type="text"]'
    )) {
      input.value = ''
    }
  }

  _resetFocus() {
    for (const option of this.optionsList) {
      option.focus = false
    }
  }

  _resetVisible() {
    const list = this.component.querySelectorAll('.br-list .br-item')
    for (const [index, option] of this.optionsList.entries()) {
      option.visible = true
      list[index].classList.remove('d-none')
    }
  }

  _openSelect() {
    for (const list of this.component.querySelectorAll('.br-list')) {
      list.setAttribute('expanded', '')
    }
    for (const icon of this.component.querySelectorAll(
      '.br-input .br-button i'
    )) {
      icon.classList.remove('fa-angle-down')
      icon.classList.add('fa-angle-up')
    }
    this._resetInput()
  }

  _closeSelect() {
    for (const list of this.component.querySelectorAll('.br-list')) {
      list.removeAttribute('expanded')
    }
    for (const icon of this.component.querySelectorAll(
      '.br-input .br-button i'
    )) {
      icon.classList.remove('fa-angle-up')
      icon.classList.add('fa-angle-down')
    }
    this._setInput()
    this._resetFocus()
    this._resetVisible()
  }
}

const selectList = []
for (const brSelect of window.document.querySelectorAll('.br-select')) {
  selectList.push(new BRSelect('br-select', brSelect))
}

/* harmony default export */ __webpack_exports__["default"] = (BRSelect);


/***/ }),

/***/ 281:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(18);
__webpack_require__(79);
__webpack_require__(80);
__webpack_require__(282);
module.exports = __webpack_require__(283);


/***/ }),

/***/ 282:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/select/examples/select-multiplo.html");

/***/ }),

/***/ 283:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/select/examples/select-simples.html");

/***/ }),

/***/ 79:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 80:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/select/examples.html");

/***/ })

/******/ });
//# sourceMappingURL=select.js.map